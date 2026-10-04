#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
import os, glob, re, shutil

def post_build():
    output_dir = "public"
    docs_dir = "docs"
    base_url = "https://crypto-service.co"

    # Copy static images and assets into public/
    for folder in ["images", "assets"]:
        if os.path.isdir(folder):
            dest = os.path.join(output_dir, folder)
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(folder, dest)

    for single_file in ["favicon.ico", "robots.txt", "security.txt"]:
        if os.path.isfile(single_file):
            shutil.copy2(single_file, os.path.join(output_dir, single_file))

    # Sync public/ into docs/
    os.makedirs(docs_dir, exist_ok=True)
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(docs_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    all_pages = set()
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, f), output_dir)
                if rel_path == "index.html":
                    all_pages.add(f"{base_url}/")
                else:
                    all_pages.add(f"{base_url}/{rel_path}")

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in sorted(all_pages):
        sitemap_xml += f'  <url>\n    <loc>{p}</loc>\n    <lastmod>2026-10-04</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_xml += '</urlset>\n'

    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap_xml)
        with open(os.path.join(d, "CNAME"), "w", encoding="utf-8") as f:
            f.write("crypto-service.co\n")

    llms_txt = f"""# Crypto Service Suite
> Open-source, self-hosted post-quantum cryptography toolkit for banks, custodians and fintechs: FIPS 203 ML-KEM and FIPS 204 ML-DSA algorithms, KMS provider interface, database field encryption, and CycloneDX CBOM generation across 18 lockstep packages.

## Documentation Hub
- Ecosystem Documentation Portal: https://docs.crypto-service.co/
- Package Documentation: https://docs.crypto-service.co/packages/crypto-lib/index.html

## Core Website Pages
- Homepage: {base_url}/
- Ecosystem Overview: {base_url}/ecosystem.html
- Solutions: {base_url}/solutions.html
- Cryptographic Standards: {base_url}/standards.html
- Whitepapers: {base_url}/whitepapers/index.html
- Competitive Comparisons: {base_url}/compare/index.html
- Research: {base_url}/research.html
- About: {base_url}/about.html
- Contact: {base_url}/contact.html
"""
    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "llms.txt"), "w", encoding="utf-8") as f:
            f.write(llms_txt)

    for base_path in [output_dir, docs_dir]:
        for html_file in glob.glob(f"{base_path}/**/*.html", recursive=True):
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("http://127.0.0.1:8000", base_url)
            content = content.replace("http://localhost:8000", base_url)

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"Post-build optimization complete ({len(all_pages)} URLs sync'd to docs/ and public/, images and assets mirrored).")

if __name__ == "__main__":
    post_build()
