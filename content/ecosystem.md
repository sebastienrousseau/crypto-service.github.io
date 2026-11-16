---
title: "The Crypto Service Ecosystem — 18 npm Packages and 6 Language SDKs"
description: "The 18 npm packages of the Crypto Service monorepo, released in lockstep: post-quantum primitives, a REST service, a KMS interface, ORM encryption, edge adapters and developer tooling."
eyebrow: "Monorepo Architecture & Modules"
headline: "An Integrated Post-Quantum Ecosystem Built in Lockstep"
lead: "From cryptographic primitives to a KMS interface, AI agent tooling and a REST service: all 18 npm packages share one version and each enforces 100% statement, branch, function and line coverage in CI."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-11-15"
logo_alt: "Crypto Service Suite logo"
light_trace_alt: "Pastel morphing gradient with organic glass droplets"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<section class="ecosystem-intro">
<h2>The 18 npm packages</h2>
<p class="lead-text">
Crypto Service Suite is a TypeScript monorepo released in lockstep. CI builds, lints and tests every package, with a strict 100% statements, branches, functions, and lines coverage floor across all 18 packages. Property-based fuzz tests cover token, CBOM and input parsing. Every tagged release publishes all 18 packages to npm and GitHub Packages from automated CI. The six <a href="/sdks/">language SDKs</a> for Java, Rust, Go, C++, .NET and Python are separate repositories and registries, not part of these 18 packages.
</p>
</section>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="core-packages">Core Cryptographic Primitives &amp; Runtimes</h3>
<div class="packages-grid">
<div class="package-card" id="crypto-lib">
<div class="package-header">
<span class="package-badge font-mono">FIPS 203 / 204</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lib/index.html">@sebastienrousseau/crypto-lib</a></h4>
</div>
<p>Implements FIPS 203/204/205 algorithms (via <code>@noble/post-quantum</code>; not a validated cryptographic module): ML-KEM key encapsulation, ML-DSA and SLH-DSA signatures, X25519/P-256/X448 + ML-KEM hybrid KEMs through one v2 combiner, Composite ML-DSA hybrid signatures, and RFC 9180 HPKE with X-Wing as its post-quantum KEM, alongside classical algorithms from <code>@noble/*</code> and OpenPGP.js. Seven runtime dependencies.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-server">
<div class="package-header">
<span class="package-badge font-mono">CaaS Engine</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-server/index.html">@sebastienrousseau/crypto-server</a></h4>
</div>
<p>Self-hostable Fastify REST microservice exposing crypto-lib operations over HTTP, with OpenAPI documentation, multi-cloud KMS endpoints, OPAQUE authentication, rate limiting and OpenTelemetry instrumentation.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-cli">
<div class="package-header">
<span class="package-badge font-mono">DevOps &amp; Ops</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cli/index.html">@sebastienrousseau/crypto-cli</a></h4>
</div>
<p>Command-line tool with non-interactive subcommands for scripts and CI (<code>hash</code>, <code>keygen</code>, <code>encrypt</code>, <code>decrypt</code>, <code>sign</code>, <code>verify</code>, <code>password</code>, <code>cbom</code>, <code>stream</code>, <code>opaque</code>, <code>hpke</code>, <code>kms</code>) and an interactive menu when run without arguments in a terminal.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-sdk">
<div class="package-header">
<span class="package-badge font-mono">Client SDK</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-sdk/index.html">@sebastienrousseau/crypto-sdk</a></h4>
</div>
<p>Zero-dependency, fetch-based TypeScript client for the crypto-server REST API, with typed requests and responses and algorithm negotiation. For other languages, see the <a href="/sdks/">six language SDKs</a>.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="enterprise-frameworks">Enterprise Connectors &amp; Infrastructure</h3>
<div class="packages-grid">
<div class="package-card" id="crypto-kms">
<div class="package-header">
<span class="package-badge font-mono">Key Management</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-kms/index.html">@sebastienrousseau/crypto-kms</a></h4>
</div>
<p>One KMS interface for envelope encryption, signing and rotation. Implemented providers: AWS KMS (including ML-DSA signing keys, through the optional <code>@aws-sdk/client-kms</code> peer), Google Cloud KMS and HashiCorp Vault Transit (over their REST APIs with <code>fetch</code>), and an in-memory local store. The Azure Key Vault provider is a stub that rejects every call, and the PKCS#11 provider is a software simulation with no HSM.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-edge">
<div class="package-header">
<span class="package-badge font-mono">Edge Computing</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-edge/index.html">@sebastienrousseau/crypto-edge</a></h4>
</div>
<p>Web Crypto API adapter for edge runtimes (Cloudflare Workers, Vercel Edge, Deno, Bun, browsers), with runtime detection and text/base64 fallbacks.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-api">
<div class="package-header">
<span class="package-badge font-mono">API Contracts</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-api/index.html">@sebastienrousseau/crypto-api</a></h4>
</div>
<p>TypeScript types for Postman collections and a converter that turns a collection into Markdown API documentation. It is not the crypto-server request/response contract; that is the server's OpenAPI document.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-middleware">
<div class="package-header">
<span class="package-badge font-mono">Security Filter</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-middleware/index.html">@sebastienrousseau/crypto-middleware</a></h4>
</div>
<p>Express and Fastify middleware for request payload decryption, response encryption, HMAC signature verification and HS256 JWT verification.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="database-encryption">Database Envelope Encryption &amp; ORM Extensions</h3>
<div class="packages-grid">
<div class="package-card" id="crypto-prisma">
<div class="package-header">
<span class="package-badge font-mono">Prisma Extension</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-prisma/index.html">@sebastienrousseau/crypto-prisma</a></h4>
</div>
<p>Prisma Client extension for field-level encryption with XChaCha20-Poly1305; fields marked deterministic are stored as an HMAC-SHA-256 blind index for equality search.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-typeorm">
<div class="package-header">
<span class="package-badge font-mono">TypeORM Decorator</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-typeorm/index.html">@sebastienrousseau/crypto-typeorm</a></h4>
</div>
<p>A TypeORM <code>@EncryptedColumn()</code> decorator and transformer that encrypt entity columns with XChaCha20-Poly1305.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-wasm">
<div class="package-header">
<span class="package-badge font-mono">Placeholder</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-wasm/index.html">@sebastienrousseau/crypto-wasm</a></h4>
</div>
<p>Placeholder for a future WebAssembly accelerator. It ships runtime detection and a loader for a caller-supplied module only; no WebAssembly module ships, so every operation runs in JavaScript.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-cbom">
<div class="package-header">
<span class="package-badge font-mono">CBOM</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cbom/index.html">@sebastienrousseau/crypto-cbom</a></h4>
</div>
<p>CycloneDX 1.6 and SPDX 3.0 Cryptographic Bill of Materials generator that scans source code for algorithm usage and cryptographic inventory.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="developer-tools">AI Tooling, Developer Experience &amp; UI Libraries</h3>
<div class="packages-grid">
<div class="package-card" id="crypto-mcp">
<div class="package-header">
<span class="package-badge font-mono">AI Protocol</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-mcp/index.html">@sebastienrousseau/crypto-mcp</a></h4>
</div>
<p>Model Context Protocol server over stdio that gives AI assistants 23 cryptography tools: key generation, encryption, ML-KEM, ML-DSA signing, hashing, streaming encryption, KMS and CBOM. It opens no network port.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-lsp">
<div class="package-header">
<span class="package-badge font-mono">IDE Analysis</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lsp/index.html">@sebastienrousseau/crypto-lsp</a></h4>
</div>
<p>Language Server Protocol server that flags broken hashes, weak ciphers, short keys, quantum-vulnerable algorithms, hard-coded secrets and malformed PEM, with quick fixes.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-react">
<div class="package-header">
<span class="package-badge font-mono">React Hooks</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-react/index.html">@sebastienrousseau/crypto-react</a></h4>
</div>
<p>React hooks (<code>useEncrypt</code>, <code>useHash</code>, <code>useKeypair</code>, <code>useSignature</code>) and a provider for client-side cryptography.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-vue">
<div class="package-header">
<span class="package-badge font-mono">Vue Composables</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-vue/index.html">@sebastienrousseau/crypto-vue</a></h4>
</div>
<p>Vue 3 composables (<code>useEncrypt</code>, <code>useHash</code>, <code>useKeypair</code>, <code>useSignature</code>) and a plugin for client-side cryptography.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-testing">
<div class="package-header">
<span class="package-badge font-mono">Quality Assurance</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-testing/index.html">@sebastienrousseau/crypto-testing</a></h4>
</div>
<p>Synthetic test keys, fixtures, mocks and helpers for testing code that uses crypto-lib.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>

<div class="package-card" id="crypto-benchmarks">
<div class="package-header">
<span class="package-badge font-mono">Performance</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-benchmarks/index.html">@sebastienrousseau/crypto-benchmarks</a></h4>
</div>
<p>Micro-benchmark harness comparing classical and post-quantum operation latency and throughput across symmetric, asymmetric, and streaming ciphers.</p>
<div class="package-meta font-mono">Version: {{version}}</div>
</div>
</div>
</div>
