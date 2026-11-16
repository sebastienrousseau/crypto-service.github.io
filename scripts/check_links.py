#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Check every link in the built site.

Internal links (same-origin paths and https://crypto-service.co/ URLs)
must resolve to a built file, and a ``#fragment`` must name an ``id`` on
the target page. Any failure exits 1.

With ``--external``, http(s) links to other hosts are also requested and
failures are reported; they never change the exit status, because a
third-party outage must not block a deploy.

Usage: python3 scripts/check_links.py site [--external]
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag, urlparse

ORIGIN = "crypto-service.co"
SKIP_SCHEMES = ("mailto:", "tel:", "data:", "javascript:")


class Collector(HTMLParser):
    """Collect link targets and element ids from one page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("name"):
            self.ids.add(values["name"] or "")
        for key in ("href", "src"):
            target = values.get(key)
            if target and not (tag == "link" and values.get("rel") in ("canonical", "alternate")):
                self.links.append(target)


def parse(page: Path) -> Collector:
    collector = Collector()
    collector.feed(page.read_text(encoding="utf-8", errors="replace"))
    return collector


def resolve(site: Path, page: Path, path: str) -> Path | None:
    """Map a URL path to the built file that serves it, or None."""
    base = site if path.startswith("/") else page.parent
    candidate = (base / unquote(path).lstrip("/")).resolve()
    for option in (candidate, candidate / "index.html", candidate.with_suffix(".html")):
        if option.is_file() and site.resolve() in option.parents:
            return option
    return None


def internal_path(link: str) -> str | None:
    """Return the path of a same-site link, or None for an external one."""
    parsed = urlparse(link)
    if parsed.scheme in ("http", "https"):
        return (parsed.path or "/") if parsed.netloc == ORIGIN else None
    if parsed.scheme:
        return None
    return parsed.path


def check_internal(site: Path) -> tuple[list[str], set[str]]:
    pages = sorted(site.rglob("*.html"))
    parsed = {page.resolve(): parse(page) for page in pages}
    errors: list[str] = []
    external: set[str] = set()
    for page in pages:
        for link in parsed[page.resolve()].links:
            if link.startswith(SKIP_SCHEMES):
                continue
            url, fragment = urldefrag(link)
            path = internal_path(url)
            if path is None:
                external.add(link)
                continue
            target = page.resolve() if path == "" else resolve(site, page, path)
            where = page.relative_to(site)
            if target is None:
                errors.append(f"{where}: broken link {link}")
                continue
            if fragment and target.suffix == ".html":
                ids = parsed.get(target) or parse(target)
                if unquote(fragment) not in ids.ids:
                    errors.append(f"{where}: missing anchor {link}")
    return errors, external


def check_external(links: set[str]) -> list[str]:
    failures = []
    for link in sorted({urldefrag(x)[0] for x in links}):
        request = urllib.request.Request(link, method="GET", headers={"User-Agent": "link-check"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:  # nosec B310
                status = response.status
        except urllib.error.HTTPError as error:
            status = error.code
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            failures.append(f"{link}: {error}")
            continue
        if status >= 400:
            failures.append(f"{link}: HTTP {status}")
    return failures


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    site = Path(argv[1])
    errors, external = check_internal(site)
    for error in errors:
        print(f"ERROR {error}")
    if "--external" in argv:
        for failure in check_external(external):
            print(f"WARN external {failure}")
    pages = len(list(site.rglob("*.html")))
    print(f"check_links: {pages} page(s), {len(errors)} internal error(s), {len(external)} external link(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
