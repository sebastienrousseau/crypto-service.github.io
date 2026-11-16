#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0 OR MIT
set -euo pipefail

# Build crypto-service.co with the Static Site Generator (ssg) into site/,
# the directory CI uploads as the GitHub Pages artifact. Nothing built is
# committed.
#
#   1. content/ is staged to .build/content with the suite version from
#      VERSION filled in (scripts/render_version.py).
#   2. ssg compiles the staged pages and _layouts/ into .build/public.
#   3. static/ (PRISM CSS and JS, fonts, images, robots.txt,
#      security.txt, llms.txt) is copied over the output root, and
#      security.txt is also published at /.well-known/ (RFC 9116).
#   4. The result replaces site/.
#
# Usage: ./build.sh          (build into site/)
#        ./build.sh --audit  (build, then run the ssg audit gates)

cd "$(git rev-parse --show-toplevel)"

AUDIT=0
[[ "${1:-}" == "--audit" ]] && AUDIT=1

STAGE=.build
rm -rf "$STAGE"
mkdir -p "$STAGE"

python3 scripts/render_version.py content "$STAGE/content"
ssg build -f ssg.toml --quiet

# GitHub Pages: the custom domain, and no Jekyll pass (it would drop the
# underscore-prefixed /_csp/ assets ssg writes).
printf 'crypto-service.co\n' > "$STAGE/public/CNAME"
touch "$STAGE/public/.nojekyll"

rsync -a static/ "$STAGE/public/"
mkdir -p "$STAGE/public/.well-known"
cp "$STAGE/public/security.txt" "$STAGE/public/.well-known/security.txt"

# Build-only files ssg leaves in its output.
rm -rf "$STAGE/public/.meta" "$STAGE/public/.ssg" "$STAGE/public/.ssg-cache" "$STAGE/public/.ssg-plugin-cache.json"

mkdir -p site
rsync -a --delete "$STAGE/public/" site/
rm -rf "$STAGE"

if [[ "$AUDIT" == "1" ]]; then
  ssg audit -f ssg.toml -o site --severity warn
fi

echo "Build published to site/."
