#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Stage content/ for ssg with the suite version filled in.

The suite version lives in one place, the VERSION file. ssg substitutes
front-matter keys in layouts but not in Markdown bodies, so this script
copies content/ to a staging directory and, in every page:

  * adds ``version: "<VERSION>"`` to the front matter, which the layouts
    read as ``{{version}}``;
  * replaces the literal ``{{version}}`` token in the body.

Pages therefore never spell the current version out, and a release only
changes VERSION.

Usage: python3 scripts/render_version.py <source-dir> <staging-dir>
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = "{{version}}"
VERSION_RE = re.compile(r"^0\.0\.\d{1,3}$")


def read_version() -> str:
    """Return the suite version from VERSION, refusing a malformed one."""
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not VERSION_RE.match(version):
        raise SystemExit(f"VERSION is not a 0.0.x version: {version!r}")
    return version


def render(text: str, version: str) -> str:
    """Stamp one page: front-matter key plus body tokens."""
    if text.startswith("---\n"):
        text = f'---\nversion: "{version}"\n' + text[len("---\n"):]
    return text.replace(TOKEN, version)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    source, staging = Path(argv[1]), Path(argv[2])
    version = read_version()
    if staging.exists():
        shutil.rmtree(staging)
    shutil.copytree(source, staging)
    pages = 0
    for page in sorted(staging.rglob("*.md")):
        page.write_text(render(page.read_text(encoding="utf-8"), version), encoding="utf-8")
        pages += 1
    print(f"render_version: {pages} page(s) staged at {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
