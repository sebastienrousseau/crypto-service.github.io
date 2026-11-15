---
title: "News, Releases and Research — Crypto Service"
description: "Release notes for every Crypto Service Suite release from 0.0.36 onward, plus the white papers and technical articles published alongside them."
eyebrow: "News & Releases"
headline: "Releases, white papers and technical notes"
lead: "What changed in each release of the 18 npm packages, summarised from the project CHANGELOG, and the papers and guides published alongside them."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-11-15"
logo_alt: "Crypto Service Suite logo"
light_trace_alt: "Pastel morphing gradient with organic glass droplets"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<section class="news-featured-section" id="releases">
<h2>Releases</h2>
<p class="lead-text">The current suite version is {{version}}. All 18 npm packages share it; the six <a href="/sdks/">language SDKs</a> follow it from 0.0.40 onward. These summaries come from the <a href="https://github.com/sebastienrousseau/crypto-service/blob/main/CHANGELOG.md">CHANGELOG</a>, which has every entry in full.</p>

<!-- history:start -->
<article class="news-article-card" id="release-0.0.40">
<span class="article-category font-mono">RELEASE 0.0.40 · IN PROGRESS</span>
<h3>0.0.40: dependency fixes and the language SDKs</h3>
<p>The CHANGELOG lists 0.0.40 as unreleased at the time of writing; until it is tagged, npm and GitHub serve 0.0.39. So far it adds <code>scripts/bump-version.mjs</code>, which opens the next lockstep iteration in one command; folds the Dependabot updates for the Fastify and OpenTelemetry groups, <code>commander</code> 15.1 and others, while holding <code>@fastify/otel</code> on 0.21 because 1.0 needs an unpublished <code>@opentelemetry/api</code>; makes <code>verifyFeldmanShare</code> throw crypto-lib's <code>CryptoError</code> (<code>INVALID_HEX</code>) for a non-hex commitment on every runtime; and constrains <code>fast-xml-parser</code> to 5.12 or later (Dependabot alert #148, low). The six language SDKs are first released with this version.</p>
</article>

<article class="news-article-card" id="release-0.0.39">
<span class="article-category font-mono">RELEASE 0.0.39 · 25 OCTOBER 2026</span>
<h3>0.0.39: release notes fix</h3>
<p>The release workflow no longer copies the body of a multi-line comment from the Highlights file into the published release notes.</p>
</article>

<article class="news-article-card" id="release-0.0.38">
<span class="article-category font-mono">RELEASE 0.0.38 · 24 OCTOBER 2026</span>
<h3>0.0.38: signed provenance on GitHub releases</h3>
<p>Each GitHub release now carries a Sigstore-signed SLSA build-provenance attestation for the npm tarballs, verifiable with <code>gh attestation verify</code>. Releases are created with the standard title, highlights, checksums and assets. crypto-mcp's README now lists all 23 of its tools, MIGRATION.md covers the 0.0.36 breaking changes it had missed, and two timing-sensitive tests no longer fail on busy CI runners.</p>
</article>

<article class="news-article-card" id="release-0.0.37">
<span class="article-category font-mono">RELEASE 0.0.37 · 24 OCTOBER 2026</span>
<h3>0.0.37: publishing fixes and security updates</h3>
<p>The 0.0.36 release workflow had published nothing; 0.0.37 fixes the publish step and adds a manual path to publish an existing release. It updates <code>fast-uri</code>, <code>serialize-javascript</code> and <code>body-parser</code> 2.4.0 for published advisories, and pino 10.4.0 in crypto-server.</p>
</article>

<article class="news-article-card" id="release-0.0.36">
<span class="article-category font-mono">RELEASE 0.0.36 · 23 OCTOBER 2026</span>
<h3>0.0.36: Composite ML-DSA, X-Wing and one hybrid combiner</h3>
<p>A large release with breaking changes, listed in MIGRATION.md. Hybrid signatures become Composite ML-DSA (draft-ietf-lamps-pq-composite-sigs), HPKE's post-quantum KEM becomes X-Wing, and every X25519 + ML-KEM-768 construction derives its key from the v2 hybrid combiner (ADRs 0002 to 0004). NIST ACVP known-answer tests now cover ML-KEM, ML-DSA and SLH-DSA, and these algorithms use Node.js's native implementation on 24.7 and later. crypto-lib runs in browsers. crypto-server gains an audit log; crypto-kms's Google Cloud KMS and Vault Transit providers are documented as the REST implementations they are, and AWS KMS signing and rotation are fixed. Several security fixes include PGP signature verification, PASETO expiry checks and a 16-byte minimum for MAC keys.</p>
</article>
<!-- history:end -->
</section>

<!-- DEDICATED INSTITUTIONAL WHITEPAPERS -->
<!-- DEDICATED INSTITUTIONAL WHITEPAPERS -->
<div class="news-grid-section" id="whitepapers">
<div class="swift-news-header">
<div>
<h3 class="category-heading">Institutional White Papers &amp; Technical Publications</h3>
<p class="section-lead section-lead-muted">
Architectural briefs, threat model analyses, and technical white papers published by Sebastien Rousseau and the Crypto Service cryptographic engineering group.
</p>
</div>
<a class="pill primary no-chev" href="/whitepapers/">Browse All White Papers →</a>
</div>

<div class="books-shelf">

<article class="book book-no-cover" id="epaa-whitepaper">
<div class="book-body">
<p class="book-eyebrow">INDUSTRY WHITE PAPER · EPAA</p>
<h4 class="book-title"><a href="/whitepapers/quantum-safe-payments/">Quantum-Safe Payments: Why the Payments Industry Must Act Now</a></h4>
<p class="book-meta"><time datetime="2025-09-01">September 2025</time> · Sebastien Rousseau · Emerging Payments Association Asia (EPAA)</p>
<p class="book-meta book-meta-faint">English · PDF / HTML · 18.9 MB · Free download</p>
<p class="book-excerpt">Quantum computing threatens the cryptographic foundations of financial services. Payments, from real-time to cross-border settlement, rely on protections that quantum computing will eventually render obsolete, and regulators are already treating harvest-now-decrypt-later as a credible present risk. Outlines the structural threat post-quantum cryptography poses to payment infrastructure across SWIFT, real-time gross settlement (RTGS) rails and instant payment schemes.</p>
<div class="book-actions">
<a class="pill primary no-chev" href="/whitepapers/quantum-safe-payments/">Read White Paper →</a>
<a class="pill ghost no-chev" href="https://emergingpaymentsasia.org/wp-content/uploads/2025/09/Quantum-Safe-Payments-Why-the-Payments-Industry-Must-Act-Now.pdf" rel="external noopener">EPAA PDF (18.9 MB)</a>
</div>
</div>
</article>

<article class="book book-no-cover" id="sovereign-caas-paper">
<div class="book-body">
<p class="book-eyebrow">ARCHITECTURE BLUEPRINT · SOVEREIGN CAAS</p>
<h4 class="book-title"><a href="/whitepapers/sovereign-caas/">Sovereign CaaS: Eliminating Custodial Counterparty Risk in Financial Institutions</a></h4>
<p class="book-meta"><time datetime="2026-09-28">September 2026</time> · Sebastien Rousseau · Architecture Practice</p>
<p class="book-meta book-meta-faint">English · Technical White Paper · FIPS 203/204 Algorithms</p>
<p class="book-excerpt">How tier-1 banks, fintechs, and asset managers deploy on-premises and private-cloud Cryptography-as-a-Service daemons, retaining control of their keys, and how that supports EU DORA ICT risk work.</p>
<div class="book-actions">
<a class="pill primary no-chev" href="/whitepapers/sovereign-caas/">Read White Paper →</a>
<a class="pill ghost no-chev" href="/solutions/#caas-server">CaaS Daemon Specs</a>
</div>
</div>
</article>

<article class="book book-no-cover" id="strategic-horizon-paper">
<div class="book-body">
<p class="book-eyebrow">STRATEGIC TREATISE · GLOBAL STANDARDS</p>
<h4 class="book-title"><a href="/whitepapers/strategic-horizon-2027/">The 2027 Post-Quantum Strategic Horizon &amp; Cryptographic Audit</a></h4>
<p class="book-meta"><time datetime="2026-09-28">September 2026</time> · Sebastien Rousseau · Cryptographic Research Directorate</p>
<p class="book-meta book-meta-faint">English · Executive Treatise · 28 Pages · Regulatory Timelines &amp; Cryptanalysis</p>
<p class="book-excerpt">An authoritative executive analysis of upcoming compliance milestones from NIST, ANSSI, BSI, and US NSA CNSA 2.0. Why waiting until 2029 introduces existential compliance risks for financial market infrastructures, the mathematical hardness of Module-LWE lattices, and concrete audit checklists.</p>
<div class="book-actions">
<a class="pill primary no-chev" href="/whitepapers/strategic-horizon-2027/">Read Strategic Treatise →</a>
<a class="pill ghost no-chev" href="/research/">Academic Research</a>
</div>
</div>
</article>

<article class="book book-no-cover" id="hndl-paper">
<div class="book-body">
<p class="book-eyebrow">THREAT INTELLIGENCE · HNDL VECTOR</p>
<h4 class="book-title"><a href="/whitepapers/hndl-threat-model/">Harvest-Now-Decrypt-Later: Defending Long-Dated Enterprise Assets</a></h4>
<p class="book-meta"><time datetime="2026-09-28">September 2026</time> · Sebastien Rousseau · Security Architecture Group</p>
<p class="book-meta book-meta-faint">English · Threat Intelligence Brief · Threat Vectors &amp; Hybrid Mitigation</p>
<p class="book-excerpt">State adversaries are actively intercepting and storing encrypted database backups, corporate IP, and interbank transaction logs. How hybrid dual-layer cryptography (X25519 + ML-KEM-768) neutralizes retroactive exposure today across enterprise asset lifespans spanning 10 to 30 years.</p>
<div class="book-actions">
<a class="pill primary no-chev" href="/whitepapers/hndl-threat-model/">Read Threat Report →</a>
<a class="pill ghost no-chev" href="/research/#threat-model">Threat Matrix</a>
</div>
</div>
</article>

</div>
</div>

<!-- TECHNICAL ARCHITECTURE & BENCHMARKS -->
<div class="news-grid-section">
<h3 class="category-heading">Technical Architecture &amp; Benchmarks</h3>
<div class="news-cards-grid">
<article class="news-article-card" id="benchmarks">
<span class="article-category font-mono">PERFORMANCE BENCHMARK</span>
<h4><a href="/whitepapers/sub-millisecond-benchmarks/">Benchmarking Post-Quantum Operations in Crypto Service Suite</a></h4>
<p>How to measure ML-KEM and ML-DSA latency with the committed benchmark script. Earlier figures on this card (including a WebAssembly ML-KEM-768 result) did not come from committed code and have been withdrawn.</p>
<div class="article-footer font-mono">Read Technical Specification →</div>
</article>

<article class="news-article-card" id="database-encryption">
<span class="article-category font-mono">DATA AT REST</span>
<h4><a href="/whitepapers/database-encryption/">Transparent Database Field Encryption with Prisma &amp; TypeORM</a></h4>
<p>An architectural guide to field-level authenticated encryption (XChaCha20-Poly1305) with the Prisma and TypeORM adapters.</p>
<div class="article-footer font-mono">Read Implementation Guide →</div>
</article>

<article class="news-article-card" id="cbom-guide">
<span class="article-category font-mono">DEVSECOPS</span>
<h4><a href="/whitepapers/dora-cbom-manual/">Automated CBOM Auditing with CycloneDX and Crypto Service Suite</a></h4>
<p>Generating CycloneDX 1.6 CBOMs and using them as inventory input for Digital Operational Resilience Act (DORA) work. A CBOM does not by itself establish compliance.</p>
<div class="article-footer font-mono">Read CBOM Manual →</div>
</article>
</div>
</div>
