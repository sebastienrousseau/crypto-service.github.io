# SPDX-License-Identifier: Apache-2.0 OR MIT
.PHONY: all build audit check serve clean help

all: build

help:
	@echo "Available Makefile targets:"
	@echo "  make build   - Build the site into site/ (./build.sh)"
	@echo "  make audit   - Build, then run the ssg audit gates"
	@echo "  make check   - Build, then run every CI gate"
	@echo "  make serve   - Build, then serve site/ on http://127.0.0.1:8099"
	@echo "  make clean   - Remove build output"

build:
	./build.sh

audit: build
	ssg audit -f ssg.toml -o site --severity warn

check: build
	ssg audit -f ssg.toml -o site --severity warn --fail-on warn
	python3 scripts/check_links.py site
	python3 scripts/check_versions.py site

serve: build
	cd site && python3 -m http.server 8099 --bind 127.0.0.1

clean:
	rm -rf .build site public
