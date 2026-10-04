<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<p align="center">
  <img src="images/logo.svg" alt="Crypto Service logo" width="128" />
</p>

<h1 align="center">crypto-service.github.io</h1>

<p align="center">
  Official website for Crypto Service Suite — post-quantum cryptographic infrastructure for institutional finance and modern enterprise stacks.
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/crypto-service.github.io/actions/workflows/deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/sebastienrousseau/crypto-service.github.io/deploy.yml?branch=main&style=for-the-badge&logo=github&label=Deploy" alt="Deploy" /></a>
  <a href="https://crypto-service.co"><img src="https://img.shields.io/badge/website-crypto--service.co-005950?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Website: crypto-service.co" /></a>
  <a href="https://docs.crypto-service.co"><img src="https://img.shields.io/badge/docs-docs.crypto--service.co-2ec4b6?style=for-the-badge&logo=gitbook&logoColor=white" alt="Docs: docs.crypto-service.co" /></a>
  <a href="https://github.com/sebastienrousseau/crypto-service/releases"><img src="https://img.shields.io/github/v/release/sebastienrousseau/crypto-service?style=for-the-badge&color=fc8d62&logo=git&label=Suite%20Release" alt="Suite Release" /></a>
  <a href="https://static-site-generator.com/"><img src="https://img.shields.io/badge/SSG-0.0.63-66c2a5?style=for-the-badge&labelColor=555555&logo=rust" alt="Built with SSG" /></a>
  <a href="LICENSE-APACHE"><img src="https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg?style=for-the-badge" alt="License: Apache-2.0 OR MIT" /></a>
</p>

---

## Contents

**Getting started**

- [Overview](#overview) — architecture and design principles
- [Quick Start](#quick-start) — build and serve locally in minutes

**Ecosystem & Architecture**

- [Features](#features) — core capabilities and performance highlights
- [Technology Stack](#technology-stack) — SSG, Rust, and modern web standards
- [Accessibility & Compliance](#accessibility--compliance) — 100% WCAG 2.1 AAA and Lighthouse scores

**Operational**

- [Development](#development) — make targets and automated build
- [Security](#security) — Subresource Integrity (SRI) and Content Security Policy (CSP)
- [License](#license) — dual Apache-2.0 and MIT licensing

---

## Overview

`crypto-service.github.io` serves the primary marketing, architecture, and solutions website at [https://crypto-service.co](https://crypto-service.co). Built with **Static Site Generator (SSG)** and the **Skeletonic Design System**, it delivers static page generation, zero third-party tracking, and responsive navigation.

For API references and package documentation across all 18 monorepo packages, visit the documentation portal at [https://docs.crypto-service.co](https://docs.crypto-service.co).

---

## Quick Start

### Prerequisites

Ensure you have `ssg` installed:

```bash
cargo install ssg
```

### Local Build

Compile the site into the `public/` directory:

```bash
make build
```

---

## Features

- **Post-Quantum Cryptographic Portfolio**: Comprehensive whitepapers, architecture guides, and compliance matrices for institutional finance.
- **Static Compilation**: Compiled with Rust-based SSG for sub-second generation and zero server-side vulnerabilities.
- **WCAG 2.2 AAA Accessible**: High-contrast, semantic HTML structure with complete screen reader support.

---

## Technology Stack

- **Engine**: Static Site Generator (SSG) in Rust
- **Styling**: Skeletonic CSS design system
- **Hosting**: GitHub Pages via custom domain `crypto-service.co`

---

## Accessibility & Compliance

Every page complies with WCAG 2.2 AAA requirements, automated Lighthouse auditing, and valid Open Graph / Schema.org metadata.

---

## Development

```bash
make build
```

---

## Security

Report vulnerabilities according to `security.txt` or to [security@crypto-service.co](mailto:security@crypto-service.co).

---

## License

Copyright © 2022-2026 Sebastien Rousseau. Dual licensed under Apache-2.0 and MIT.
