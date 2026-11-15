---
title: "C++ SDK for crypto-server — Crypto Service Suite"
description: "The Crypto Service C++ SDK: a thin async-first client for the crypto-server REST API, published as crypto_service_sdk (GitHub release (CMake package)). Install command and links."
eyebrow: "Language SDKs · C++"
headline: "The C++ SDK"
lead: "A thin async-first C++ client for the crypto-server REST API, published as crypto_service_sdk."
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
<p>Package: <code>crypto_service_sdk</code> on <a href="https://github.com/sebastienrousseau/crypto-service-sdk-cpp/releases">GitHub release (CMake package)</a>.</p>
<p>The C++ SDK is published only as a GitHub release, not to a package registry. Download the <code>v{{version}}</code> source archive from the <a href="https://github.com/sebastienrousseau/crypto-service-sdk-cpp/releases">releases page</a>, then build and install it with CMake:</p>
<pre><code>cmake -S crypto-service-sdk-cpp-{{version}} -B build
cmake --build build
cmake --install build</code></pre>
<p>Your project then finds it as the CMake package <code>crypto_service_sdk</code>:</p>
<pre><code>find_package(crypto_service_sdk {{version}} REQUIRED)</code></pre>

<h2 id="usage">Usage</h2>
<p>This site does not reproduce the SDK's API. For client construction, authentication and the available calls, <a href="https://github.com/sebastienrousseau/crypto-service-sdk-cpp#readme">see the SDK README</a>; for the endpoints themselves, see crypto-server's OpenAPI document, which the server publishes at <code>/docs</code> unless <code>DOCS_ENABLED=0</code>.</p>

<h2 id="links">Links</h2>
<ul>
<li>Source and README: <a href="https://github.com/sebastienrousseau/crypto-service-sdk-cpp">github.com/sebastienrousseau/crypto-service-sdk-cpp</a></li>
<li>Registry: <a href="https://github.com/sebastienrousseau/crypto-service-sdk-cpp/releases">GitHub release (CMake package)</a></li>
<li><a href="/sdks/">All language SDKs</a></li>
</ul>
