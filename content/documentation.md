---
title: "Crypto Service Suite Documentation — Developer & API Reference"
description: "Interactive TypeDoc API references, developer quick-start guides, and architectural blueprints across all 18 lockstep packages of the Crypto Service Suite."
eyebrow: "Developer Documentation & API Matrix"
headline: "Crypto Service Suite Technical Documentation"
lead: "Interactive TypeDoc API references, guides, and integration specifications across all 18 lockstep packages. Built for institutional finance, high-assurance custody, and modern cloud stacks."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-10-04"
logo_alt: "Crypto Service Suite logo"
light_trace_alt: "Pastel morphing gradient with organic glass droplets"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<div class="standards-bar standards-bar-spaced">
<span class="standard-pill"><span class="pill-dot"></span> 18 LOCKSTEP PACKAGES</span>
<span class="standard-pill"><span class="pill-dot"></span> 100% CI COVERAGE FLOOR</span>
<span class="standard-pill"><span class="pill-dot"></span> FIPS 203 (ML-KEM)</span>
<span class="standard-pill"><span class="pill-dot"></span> FIPS 204 (ML-DSA)</span>
<span class="standard-pill"><span class="pill-dot"></span> CYCLONEDX 1.6 CBOM</span>
<span class="standard-pill"><span class="pill-dot"></span> MULTI-CLOUD KMS</span>
</div>

<section class="ecosystem-intro">
<h2>Developer Quick Start</h2>
<p class="lead-text">
Install cryptographic primitives or full-stack CaaS components directly from npm. All 18 packages in the workspace move strictly in lockstep and are tested against a mandatory 100% coverage floor.
</p>

<div class="quickstart-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 2rem 0 3rem;">
  <div class="quickstart-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
    <h3 style="margin-top: 0; font-size: 1.15rem; color: #005950;">1. Post-Quantum Primitives</h3>
    <pre style="background: var(--bg-subtle); padding: 1rem; border-radius: 8px; font-family: var(--font-mono); font-size: 0.825rem; overflow-x: auto;"><code>pnpm add @sebastienrousseau/crypto-lib

import { mlKemGenerateKeyPair, mlKemEncapsulate } from "@sebastienrousseau/crypto-lib";
const keys = mlKemGenerateKeyPair();
const { ciphertext, sharedSecret } = mlKemEncapsulate(keys.publicKey);</code></pre>
    <a href="https://docs.crypto-service.co/packages/crypto-lib/index.html" target="_blank" rel="noopener" class="pill primary" style="display: inline-block; margin-top: 0.75rem; font-size: 0.85rem;">crypto-lib API Docs &rarr;</a>
  </div>

  <div class="quickstart-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
    <h3 style="margin-top: 0; font-size: 1.15rem; color: #005950;">2. Sovereign CaaS Daemon</h3>
    <pre style="background: var(--bg-subtle); padding: 1rem; border-radius: 8px; font-family: var(--font-mono); font-size: 0.825rem; overflow-x: auto;"><code>pnpm add @sebastienrousseau/crypto-server

import { createCryptoServer } from "@sebastienrousseau/crypto-server";
const server = await createCryptoServer({ port: 8080 });
await server.listen();</code></pre>
    <a href="https://docs.crypto-service.co/packages/crypto-server/index.html" target="_blank" rel="noopener" class="pill primary" style="display: inline-block; margin-top: 0.75rem; font-size: 0.85rem;">crypto-server API Docs &rarr;</a>
  </div>

  <div class="quickstart-card" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
    <h3 style="margin-top: 0; font-size: 1.15rem; color: #005950;">3. Database Field Encryption</h3>
    <pre style="background: var(--bg-subtle); padding: 1rem; border-radius: 8px; font-family: var(--font-mono); font-size: 0.825rem; overflow-x: auto;"><code>pnpm add @sebastienrousseau/crypto-prisma

import { fieldEncryptionExtension } from "@sebastienrousseau/crypto-prisma";
const prisma = new PrismaClient().$extends(fieldEncryptionExtension({ key: masterKey }));</code></pre>
    <a href="https://docs.crypto-service.co/packages/crypto-prisma/index.html" target="_blank" rel="noopener" class="pill primary" style="display: inline-block; margin-top: 0.75rem; font-size: 0.85rem;">crypto-prisma API Docs &rarr;</a>
  </div>
</div>
</section>

<!-- Section 1: Core Cryptographic Primitives -->
<div class="ecosystem-category-section" id="core-primitives">
<h3 class="category-heading">01. Core Cryptographic Primitives &amp; Runtimes</h3>
<p style="color: var(--fg-muted); margin-bottom: 1.5rem;">Low-level mathematical primitives, post-quantum key encapsulation, digital signatures, and WebAssembly acceleration.</p>
<div class="packages-grid">

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">FIPS 203 / 204</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lib/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-lib</a></h4>
</div>
<p>Implements FIPS 203 ML-KEM, FIPS 204 ML-DSA, SLH-DSA, hybrid HPKE (X25519 + ML-KEM), AES-GCM, and OpenPGP.js.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-lib</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-lib/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">WASM Engine</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-wasm/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-wasm</a></h4>
</div>
<p>WebAssembly acceleration module routing post-quantum lattice primitives through native WASM with pure-JS fallbacks.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-wasm</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-wasm/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">CaaS Engine</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-server/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-server</a></h4>
</div>
<p>Self-hostable Fastify REST microservice exposing crypto-lib operations over HTTP with rate limiting and OpenTelemetry.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-server</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-server/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">DevOps &amp; Ops</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cli/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-cli</a></h4>
</div>
<p>Interactive terminal CLI for key generation, HPKE encryption, KMS operations, signing, password hashing, and CBOM generation.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-cli</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-cli/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Client SDK</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-sdk/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-sdk</a></h4>
</div>
<p>Zero-dependency, fetch-based TypeScript client with typed bindings for all crypto-server REST API endpoints.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-sdk</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-sdk/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

</div>
</div>

<!-- Section 2: Enterprise Connectors & Infrastructure -->
<div class="ecosystem-category-section" id="enterprise-infra">
<h3 class="category-heading">02. Enterprise Connectors &amp; Infrastructure</h3>
<p style="color: var(--fg-muted); margin-bottom: 1.5rem;">KMS integration drivers, edge compute adapters, database column encryption, and compliance bill-of-materials.</p>
<div class="packages-grid">

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Key Management</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-kms/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-kms</a></h4>
</div>
<p>Unified KMS interface with native production providers for AWS KMS, Google Cloud KMS, Vault Transit, Azure Key Vault, and Local KMS.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-kms</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-kms/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Edge Computing</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-edge/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-edge</a></h4>
</div>
<p>Web Crypto API adapter for Cloudflare Workers, Vercel Edge, Deno, Bun, and browser environments.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-edge</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-edge/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Prisma Extension</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-prisma/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-prisma</a></h4>
</div>
<p>Transparent field-level encryption middleware for Prisma ORM with XChaCha20-Poly1305 and deterministic HMAC indexing.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-prisma</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-prisma/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">TypeORM Decorator</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-typeorm/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-typeorm</a></h4>
</div>
<p>Custom TypeORM column decorators (@EncryptedColumn()) and transformers for entity-level envelope encryption.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-typeorm</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-typeorm/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">CBOM / DORA</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-cbom/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-cbom</a></h4>
</div>
<p>CycloneDX 1.6 and SPDX 3.0 Cryptographic Bill of Materials generator scanning source code for algorithm inventory.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-cbom</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-cbom/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

</div>
</div>

<!-- Section 3: Developer Tools & AI Suite -->
<div class="ecosystem-category-section" id="developer-tooling">
<h3 class="category-heading">03. Developer Tools, AI Protocols &amp; UI Components</h3>
<p style="color: var(--fg-muted); margin-bottom: 1.5rem;">AI agent integration via Model Context Protocol, Language Server diagnostics, reactive UI hooks, and test vectors.</p>
<div class="packages-grid">

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">AI Protocol</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-mcp/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-mcp</a></h4>
</div>
<p>Model Context Protocol server exposing cryptographic tools, key generation, and CBOM generation to AI coding agents.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-mcp</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-mcp/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">IDE Analysis</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-lsp/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-lsp</a></h4>
</div>
<p>Language Server Protocol server detecting legacy and quantum-vulnerable ciphers with automated refactoring suggestions.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-lsp</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-lsp/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">React Hooks</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-react/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-react</a></h4>
</div>
<p>React hooks for client-side cryptographic operations, key derivation, and post-quantum digital signatures.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-react</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-react/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Vue Composables</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-vue/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-vue</a></h4>
</div>
<p>Vue 3 composables for reactive encryption, signing, and key exchange in modern web frontends.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-vue</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-vue/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Test Vectors</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-testing/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-testing</a></h4>
</div>
<p>RFC test vectors, synthetic key fixtures, KATs, and mock KMS providers for high-assurance cryptographic testing.</p>
<div class="package-meta font-mono"><code>pnpm add -D @sebastienrousseau/crypto-testing</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-testing/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Benchmarking</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-benchmarks/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-benchmarks</a></h4>
</div>
<p>Automated latency and throughput benchmark suite evaluating post-quantum primitives across runtime environments.</p>
<div class="package-meta font-mono"><code>pnpm add -D @sebastienrousseau/crypto-benchmarks</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-benchmarks/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">API Contracts</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-api/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-api</a></h4>
</div>
<p>Postman collections, OpenAPI specifications, and shared TypeScript type contracts for the crypto-server REST API.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-api</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-api/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

<div class="package-card">
<div class="package-header">
<span class="package-badge font-mono">Security Filter</span>
<h4><a href="https://docs.crypto-service.co/packages/crypto-middleware/index.html" target="_blank" rel="noopener">@sebastienrousseau/crypto-middleware</a></h4>
</div>
<p>Express and Fastify middleware for request payload decryption, response encryption, and HMAC signature verification.</p>
<div class="package-meta font-mono"><code>pnpm add @sebastienrousseau/crypto-middleware</code></div>
<div style="margin-top: 1rem;"><a href="https://docs.crypto-service.co/packages/crypto-middleware/index.html" target="_blank" rel="noopener" style="color: #005950; font-weight: 600;">View TypeDoc API Reference &rarr;</a></div>
</div>

</div>
</div>
