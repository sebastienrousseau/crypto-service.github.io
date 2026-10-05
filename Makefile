# SPDX-License-Identifier: Apache-2.0 OR MIT
# Semantic Version: v0.0.21
.PHONY: all build clean demo help

all: build

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using local SSG and sync to docs/"
	@echo "  make clean      - Remove build artifacts and temporary files"
	@echo "  make demo       - Render terminal animation demo with VHS"

build:
	@ssg build -f ssg.toml
	@python3 scripts/post-build.py

clean:
	@rm -rf public docs dist .cache coverage *.log
	@echo "Workspace cleaned."

demo:
	@export PATH="/Applications/Google Chrome.app/Contents/MacOS:$$PATH"; vhs .github/demo.tape

