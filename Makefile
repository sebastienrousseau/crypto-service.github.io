# SPDX-License-Identifier: Apache-2.0 OR MIT
# Semantic Version: v0.0.1
.PHONY: all build clean help

all: build

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using local SSG and sync to docs/"
	@echo "  make clean      - Remove build artifacts and temporary files"

build:
	@ssg build -f ssg.toml
	@python3 scripts/post-build.py

clean:
	@rm -rf public docs dist .cache coverage *.log
	@echo "Workspace cleaned."
