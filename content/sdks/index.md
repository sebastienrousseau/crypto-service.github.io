---
title: "Language SDKs for crypto-server — Crypto Service Suite"
description: "Six thin async-first client SDKs for the crypto-server REST API: Java, Rust, Go, C++, .NET and Python, first released at suite version 0.0.40."
eyebrow: "Language SDKs"
headline: "Six language SDKs for crypto-server"
lead: "Thin async-first clients for the crypto-server REST API in Java, Rust, Go, C++, .NET and Python. They call a crypto-server you run; they do no cryptography themselves."
layout: page
author: "Sebastien Rousseau"
name: "Crypto Service"
language: en-GB
date: "2026-11-15"
---

<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<p>Crypto Service ships two kinds of package. The <a href="/ecosystem/">18 npm packages</a> are the TypeScript suite itself: crypto-lib, crypto-server, the CLI, the TypeScript SDK and the rest, all at one version. The 6 language SDKs below are separate, thin clients for crypto-server's REST API, first released with suite version 0.0.40 and versioned with the suite. The current suite version is {{version}}.</p>

<div class="table-responsive">
<table>
<thead><tr><th scope="col">Language</th><th scope="col">Package</th><th scope="col">Published on</th></tr></thead>
<tbody>
<tr><th scope="row"><a href="/sdks/java/">Java</a></th><td><code>co.cryptoservice:crypto-service-sdk</code></td><td>Maven Central</td></tr>
<tr><th scope="row"><a href="/sdks/rust/">Rust</a></th><td><code>crypto-service-sdk</code></td><td>crates.io</td></tr>
<tr><th scope="row"><a href="/sdks/go/">Go</a></th><td><code>github.com/sebastienrousseau/crypto-service-sdk-go</code></td><td>Go module proxy</td></tr>
<tr><th scope="row"><a href="/sdks/cpp/">C++</a></th><td><code>crypto_service_sdk</code></td><td>GitHub release (CMake package)</td></tr>
<tr><th scope="row"><a href="/sdks/dotnet/">.NET</a></th><td><code>CryptoService.Sdk</code></td><td>NuGet</td></tr>
<tr><th scope="row"><a href="/sdks/python/">Python</a></th><td><code>crypto-service-sdk</code></td><td>PyPI</td></tr>
</tbody>
</table>
</div>

<h2 id="what-they-do">What they do, and what they do not</h2>
<ul>
<li>Each SDK sends HTTP requests to a crypto-server instance and returns its responses. Keys and cryptographic operations stay on that server.</li>
<li>They are async-first: calls return the language's future, promise or async type.</li>
<li>They implement no cryptographic algorithm and are not validated cryptographic modules; neither is crypto-server.</li>
<li>Usage examples live in each SDK's README, linked from its page. This site lists install commands only.</li>
</ul>
