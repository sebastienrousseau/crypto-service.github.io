---
title: "Rust SDK for crypto-server — Crypto Service Suite"
description: "The Crypto Service Rust SDK: a thin async-first client for the crypto-server REST API, published as crypto-service-sdk (crates.io). Install command and links."
eyebrow: "Language SDKs · Rust"
headline: "The Rust SDK"
lead: "A thin async-first Rust client for the crypto-server REST API, published as crypto-service-sdk."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-11-15"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<h2 id="what-it-is">What it is</h2>
<p>A thin, async-first client for the <a href="/solutions/#caas-server">crypto-server</a> REST API. It does no cryptography of its own: every operation is an HTTP call to a crypto-server instance you run, and the server does the work with crypto-lib. You need a reachable crypto-server and its API key or JWT.</p>
<p>All six language SDKs were first released with suite version 0.0.40 and follow the suite version. They are separate from the 18 TypeScript npm packages; in TypeScript, use <a href="/ecosystem/#crypto-sdk">@sebastienrousseau/crypto-sdk</a> instead.</p>

<h2 id="install">Install</h2>
<p>Package: <code>crypto-service-sdk</code> on <a href="https://crates.io/crates/crypto-service-sdk">crates.io</a>.</p>
<pre><code>cargo add crypto-service-sdk@{{version}}</code></pre>

<h2 id="usage">Usage</h2>
<p>This site does not reproduce the SDK's API. For client construction, authentication and the available calls, <a href="https://github.com/sebastienrousseau/crypto-service-sdk-rust#readme">see the SDK README</a>; for the endpoints themselves, see crypto-server's OpenAPI document, which the server publishes at <code>/docs</code> unless <code>DOCS_ENABLED=0</code>.</p>

<h2 id="links">Links</h2>
<ul>
<li>Source and README: <a href="https://github.com/sebastienrousseau/crypto-service-sdk-rust">github.com/sebastienrousseau/crypto-service-sdk-rust</a></li>
<li>Registry: <a href="https://crates.io/crates/crypto-service-sdk">crates.io</a></li>
<li><a href="/sdks/">All language SDKs</a></li>
</ul>
