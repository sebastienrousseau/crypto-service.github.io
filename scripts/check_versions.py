#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Fail when a page names a suite version other than the one in VERSION.

Pages render the current version from VERSION through the
``{{version}}`` token (scripts/render_version.py), so a spelled-out
``0.0.N`` is either history or drift. A literal is allowed only where it
records history:

  * between ``<!-- history:start -->`` and ``<!-- history:end -->``
    (the release notes on /news/);
  * on a line that says ``onward``, ``since`` or ``first released``;
  * on a line ending in ``<!-- history -->``.

With a built site directory as the argument, also fail on any
``{{version}}`` token left unrendered in the output.

Usage: python3 scripts/check_versions.py [site]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Not inside a dotted quad, and not an increment such as "+0.0.1".
VERSION = re.compile(r"(?<![\d.+])v?0\.0\.(\d{1,3})(?![.\d])")
HISTORY = re.compile(r"\bonward\b|\bsince\b|first released|<!-- history -->")
START, END = "<!-- history:start -->", "<!-- history:end -->"
SOURCES = ("content/**/*.md", "_layouts/*.html", "static/*.txt")


def stale_lines(current: str) -> list[str]:
    found: list[str] = []
    for pattern in SOURCES:
        for path in sorted(ROOT.glob(pattern)):
            in_history = False
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if START in line:
                    in_history = True
                if END in line:
                    in_history = False
                    continue
                if in_history or HISTORY.search(line):
                    continue
                for match in VERSION.finditer(line):
                    if match.group(0).lstrip("v") != current:
                        found.append(f"{path.relative_to(ROOT)}:{number}: {match.group(0)}")
    return found


def unrendered(site: Path) -> list[str]:
    return [str(p.relative_to(site)) for p in sorted(site.rglob("*.html"))
            if "{{version}}" in p.read_text(encoding="utf-8", errors="replace")]


def main(argv: list[str]) -> int:
    current = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    problems = [f"stale version {line} (VERSION is {current})" for line in stale_lines(current)]
    if len(argv) > 1:
        problems += [f"unrendered {{{{version}}}} in {page}" for page in unrendered(Path(argv[1]))]
    for problem in problems:
        print(f"ERROR {problem}")
    print(f"check_versions: {len(problems)} problem(s) against {current}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
