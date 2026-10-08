---
title: "The Crypto Service Ecosystem — 18 Workspace Packages & Enterprise Modules"
description: "Explore the comprehensive Crypto Service monorepo architecture: 18 lockstep packages spanning post-quantum cryptographic primitives, CaaS servers, KMS brokers, edge runtimes, and developer tooling."
eyebrow: "Monorepo Architecture & Modules"
headline: "An Integrated Post-Quantum Ecosystem Built in Lockstep"
lead: "From cryptographic primitives to a multi-cloud KMS interface, AI agent protocols and a REST service: all 18 packages move together in lockstep, with 100% CI coverage floor across every package."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-10-04"
logo_alt: "Crypto Service Suite logo"
light_trace_alt: "Pastel morphing gradient with organic glass droplets"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<section class="ecosystem-intro">
<h2>The 18 Monorepo Workspace Modules</h2>
<p class="lead-text">
Crypto Service Suite is a TypeScript monorepo released in lockstep. CI builds, lints and tests every package, with a strict 100% statements, branches, functions, and lines coverage floor across all 18 packages. Property-based fuzz tests cover token, CBOM and input parsing. Every tagged release publishes all 18 packages to npm and GitHub Packages from automated CI.
</p>
</section>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="core-packages">Core Cryptographic Primitives &amp; Runtimes</h3>
<div class="packages-grid">
<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">FIPS 203 / 204</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lib/index.html">@sebastienrousseau/crypto-lib</a></h4>
</div>
<p>Implements FIPS 203/204/205 algorithms (via <code>@noble/post-quantum</code>; not a validated cryptographic module): ML-KEM key encapsulation, ML-DSA and SLH-DSA signatures, and X25519/P-256/X448 + ML-KEM hybrid KEMs and RFC 9180 HPKE, alongside classical algorithms from <code>@noble/*</code> and OpenPGP.js.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">CaaS Engine</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-server/index.html">@sebastienrousseau/crypto-server</a></h4>
</div>
<p>Self-hostable Fastify REST microservice exposing crypto-lib operations over HTTP, with OpenAPI documentation, multi-cloud KMS endpoints, OPAQUE authentication, rate limiting and OpenTelemetry instrumentation.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">DevOps &amp; Ops</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cli/index.html">@sebastienrousseau/crypto-cli</a></h4>
</div>
<p>Interactive command-line tool for OpenPGP, modern and post-quantum key generation, HPKE encryption, KMS operations, signing, hashing, password hashing (Argon2id) and CBOM generation.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Client SDK</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-sdk/index.html">@sebastienrousseau/crypto-sdk</a></h4>
</div>
<p>Zero-dependency, fetch-based TypeScript client with typed bindings for all crypto-server REST API endpoints including KMS, HPKE, OPAQUE, and algorithm negotiation.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="enterprise-frameworks">Enterprise Connectors &amp; Infrastructure</h3>
<div class="packages-grid">
<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Key Management</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-kms/index.html">@sebastienrousseau/crypto-kms</a></h4>
</div>
<p>Unified KMS interface with native production providers for AWS KMS, Google Cloud KMS (REST v1), HashiCorp Vault Transit, Azure Key Vault, and Local KMS with zero external SDK dependencies.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Edge Computing</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-edge/index.html">@sebastienrousseau/crypto-edge</a></h4>
</div>
<p>Web Crypto API adapter for edge runtimes (Cloudflare Workers, Vercel Edge, Deno, Bun, browsers), with runtime detection and text/base64 fallbacks.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">API Contracts</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-api/index.html">@sebastienrousseau/crypto-api</a></h4>
</div>
<p>Postman collections and environments for the crypto-server REST API, plus shared TypeScript types and schemas.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Security Filter</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-middleware/index.html">@sebastienrousseau/crypto-middleware</a></h4>
</div>
<p>Express and Fastify middleware for request payload decryption, response encryption, HMAC signature verification and HS256 JWT verification.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="database-encryption">Database Envelope Encryption &amp; ORM Extensions</h3>
<div class="packages-grid">
<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Prisma Extension</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-prisma/index.html">@sebastienrousseau/crypto-prisma</a></h4>
</div>
<p>Transparent field-level encryption for Prisma ORM (XChaCha20-Poly1305, with optional HMAC for searchable fields).</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">TypeORM Decorator</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-typeorm/index.html">@sebastienrousseau/crypto-typeorm</a></h4>
</div>
<p>Custom TypeORM column decorators (<code>@EncryptedColumn()</code>) and transformers for transparent entity-level envelope encryption.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Acceleration</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-wasm/index.html">@sebastienrousseau/crypto-wasm</a></h4>
</div>
<p>WebAssembly acceleration module routing heavy cryptographic and post-quantum operations (ML-KEM, ML-DSA, BLAKE3, ChaCha20) through native WASM with transparent pure-JS fallback.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">CBOM</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cbom/index.html">@sebastienrousseau/crypto-cbom</a></h4>
</div>
<p>CycloneDX 1.6 and SPDX 3.0 Cryptographic Bill of Materials generator that scans source code for algorithm usage and cryptographic inventory.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>
</div>
</div>

<div class="ecosystem-category-section">
<h3 class="category-heading" id="developer-tools">AI Tooling, Developer Experience &amp; UI Libraries</h3>
<div class="packages-grid">
<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">AI Protocol</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-mcp/index.html">@sebastienrousseau/crypto-mcp</a></h4>
</div>
<p>Model Context Protocol server exposing crypto-lib operations and key management tools to AI assistants.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">IDE Analysis</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lsp/index.html">@sebastienrousseau/crypto-lsp</a></h4>
</div>
<p>Language Server Protocol implementation that flags weak or quantum-vulnerable algorithm names (MD5, SHA-1, DES, short RSA keys) with pattern rules.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">React Hooks</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-react/index.html">@sebastienrousseau/crypto-react</a></h4>
</div>
<p>React hooks (<code>useEncrypt</code>, <code>useHash</code>, <code>useKeypair</code>, <code>useSignature</code>) and a provider for client-side cryptography.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Vue Composables</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-vue/index.html">@sebastienrousseau/crypto-vue</a></h4>
</div>
<p>Vue 3 composables (<code>useEncrypt</code>, <code>useHash</code>, <code>useKeypair</code>, <code>useSignature</code>) and a plugin for client-side cryptography.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Quality Assurance</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-testing/index.html">@sebastienrousseau/crypto-testing</a></h4>
</div>
<p>Synthetic test keys, fixtures, mocks and helpers for testing code that uses crypto-lib.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Performance</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-benchmarks/index.html">@sebastienrousseau/crypto-benchmarks</a></h4>
</div>
<p>Micro-benchmark harness comparing classical and post-quantum operation latency and throughput across symmetric, asymmetric, and streaming ciphers.</p>
<div class="package-meta font-mono">Version: 0.0.24</div>
</div>
</div>
</div>
