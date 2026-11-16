<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# crypto-service.github.io

Source for <https://crypto-service.co>, the website of
[Crypto Service Suite](https://github.com/sebastienrousseau/crypto-service):
an open-source, self-hosted post-quantum cryptography toolkit published as
18 TypeScript npm packages at one shared version, with six thin language
SDKs (Java, Rust, Go, C++, .NET, Python) for its REST service.

[![CI](https://img.shields.io/github/actions/workflow/status/sebastienrousseau/crypto-service.github.io/ci.yml?branch=main&style=for-the-badge&logo=github&label=CI)](https://github.com/sebastienrousseau/crypto-service.github.io/actions/workflows/ci.yml)
[![License: Apache-2.0 OR MIT](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg?style=for-the-badge)](LICENSE-APACHE)

## Requirements

- [ssg](https://crates.io/crates/ssg) 0.0.76, pinned in `mise.toml`
  (`mise install`) and in the CI workflows. Without mise:
  `cargo install ssg --locked --version 0.0.76`.
- Python 3 (build and gate scripts use the standard library only).
- `rsync` and GNU Make.

## Build and check

```bash
make build   # ./build.sh: stage content/, run ssg, publish to site/
make audit   # build, then ssg's audit gates
make check   # build, then every CI gate
make serve   # build, then serve site/ on http://127.0.0.1:8099
make clean   # remove .build/ and site/
```

`site/` is never committed. CI (`.github/workflows/ci.yml`) builds it on
every push and pull request, runs the gates, and on `main` deploys it to
GitHub Pages as an artifact.

## How the build works

`build.sh`:

1. copies `content/` to `.build/content`, adding the suite version from
   `VERSION` to each page's front matter and replacing `{{version}}` in page
   bodies (`scripts/render_version.py`);
2. runs `ssg build -f ssg.toml`, which reads `.build/content` and the
   templates in `_layouts/`;
3. copies `static/` (PRISM CSS and JS, fonts, images, `robots.txt`,
   `security.txt`, `llms.txt`) over the output root, and publishes
   `security.txt` at `/.well-known/` as well;
4. replaces `site/` with the result.

## Layout

| Path | Contents |
| :--- | :--- |
| `content/` | One Markdown file per page (bodies are HTML). URLs follow the paths. |
| `_layouts/` | `base`, `header`, `footer`, `page`, `index` and `404` templates. |
| `static/` | Files copied to the site root as they are. |
| `scripts/` | `render_version.py`, `check_links.py`, `check_versions.py`. |
| `VERSION` | The suite version every page renders. |
| `ssg.toml` | ssg configuration (below). |

The design is the PRISM theme used by
[pain001.com](https://github.com/sebastienrousseau/pain001.github.io):
`static/css/prism.css` and `static/js/prism*.js` are copied unmodified, and
`static/css/crypto-service-prism.css` holds this site's additions. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Configuration

`ssg.toml`:

```toml
site_name = "crypto-service"
site_title = "Crypto Service Suite: Post-Quantum Cryptography Toolkit"
base_url = "https://crypto-service.co"
language = "en-GB"
content_dir = ".build/content"   # staged by build.sh
template_dir = "_layouts"
output_dir = ".build/public"     # published to site/ by build.sh

[agents]
agents_txt = true
ai_plugin = false

[audit.disabled]
gates = ["markdownlint"]
```

## Versions

Pages never spell out the current suite version: they use `{{version}}`,
rendered from `VERSION`. `scripts/check_versions.py` fails CI if a page,
layout or published text file names another `0.0.x` outside a marked
history section (`<!-- history:start -->` … `<!-- history:end -->`, or a
line containing `onward`, `since`, `first released` or
`<!-- history -->`).

When crypto-service releases, its release workflow can send a
`crypto-service-release` repository dispatch; `regenerate.yml` (also
runnable by hand) stamps the new `VERSION`, rebuilds, runs the gates and
exports a patch to apply on the `feat/v<version>` branch, together with a
news entry written from the code repository's CHANGELOG.

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities through GitHub
private advisories, never in a public issue.

## License

Copyright © 2022–2026 [Sebastien Rousseau](https://sebastienrousseau.com/).
Dual-licensed under [Apache-2.0](LICENSE-APACHE) or [MIT](LICENSE-MIT).
Fonts are under the SIL Open Font License 1.1
([LICENSES/OFL-1.1.txt](LICENSES/OFL-1.1.txt)).
