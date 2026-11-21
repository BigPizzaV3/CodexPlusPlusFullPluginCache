---
name: domain-lookup
description: Look up who owns a domain and when it expires from live RDAP registry data with the lookup_domain tool, including the registrar, dates, status codes, nameservers, DNSSEC and a CSV of up to 20 domains.
---

# Zovo Domain Lookup

Use the `lookup_domain` tool when the user asks a whois lookup, a domain lookup, who owns a domain, when a domain expires, a domain registrar lookup, a domain age check, or a nameserver lookup.

1. Put one to 20 domains or URLs in `domains`. Separate bare domains with commas, semicolons or new lines. Put URLs on separate lines so commas and semicolons in their paths or queries stay inside the URL. The tool accepts a bare domain (`example.com`, up to 253 characters), a URL (`https://www.example.com/search?q=one,two`, up to 2,048 characters), and IDN names (`bücher.com`).
2. Call the tool right away when the request already names the domain. Ask a short question only when no domain is given.
3. The tool strips the scheme, path, port and a leading `www.`, lowercases the name and converts IDN to punycode. It looks up the registrable domain, so `www.example.com` gives the records for `example.com`.
4. After the tool returns, state the key facts in the reply: the registrar, the creation date, the expiry date with the days left (or "expired N days ago"), the status codes, the nameservers and the DNSSEC state, and give the CSV download link for a batch.
5. If the registry does not publish RDAP for the TLD, say so. If a domain is not found, say "not registered or not present in RDAP" and add that this does not mean the domain can be bought.

Do not use this skill for IP address lookups, DNS record resolution, website uptime checks, or SSL certificate checks.
