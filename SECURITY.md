<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Security policy

This policy covers the crypto-service.co website built from this
repository. Vulnerabilities in the Crypto Service packages themselves are
handled under the
[crypto-service security policy](https://github.com/sebastienrousseau/crypto-service/security/policy).

## Supported versions

Only the current deployment of <https://crypto-service.co> and the latest
source on `main` receive security fixes.

## Reporting

Report privately through GitHub's private vulnerability reporting:

- for this website: the **Report a vulnerability** button on this
  repository's Security tab;
- for the packages:
  <https://github.com/sebastienrousseau/crypto-service/security/advisories/new>.

Do not open a public issue. Include the impact, reproduction steps, the
affected URLs and a safe proof of concept. The same contact is published in
[`/.well-known/security.txt`](https://crypto-service.co/.well-known/security.txt)
(RFC 9116).

You should receive an acknowledgement within seven days. Please allow
reasonable time for investigation and coordinated remediation before
disclosure.

## How a report is handled

1. **Acknowledge** the report within seven days, privately.
2. **Assess** it: reproduce the issue, decide whether it is a vulnerability,
   and rate its severity with CVSS. The reporter hears the outcome.
3. **Fix** it on a private branch or a GitHub security advisory draft, with
   a check that fails without the fix.
4. **Release** the fix by deploying the site from `main`.
5. **Disclose** it through a GitHub security advisory once the fix is live.

## Credit

Reporters are credited by name in the advisory unless they ask to remain
anonymous.

## What the site does

The site is static HTML built by CI. It runs no server-side code, loads no
third-party scripts, fonts or analytics, and sets a same-origin Content
Security Policy; the only cross-origin form target is the GitHub issue form
on the contact page.
