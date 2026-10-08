---
name: dns-tls-origin-security
description: Review Cloudflare DNS, DNSSEC, TLS, certificates, origin exposure, and tunnel configuration.
---

# DNS, TLS, and Origin Security

Review authoritative DNS and record exposure, DNSSEC status and registrar DS coordination, TLS mode, certificate validity/hostname coverage, HTTPS redirects, origin TLS, Authenticated Origin Pulls where relevant, and whether direct origin access can bypass Cloudflare controls. Recommend Full (strict) only after confirming the origin certificate and HTTPS path are valid; warn about 526/outage risks and test before enforcing. Check for leaked historical origin addresses and non-proxied records only as evidence permits.

Consider Cloudflare Tunnel for suitable origins to avoid public inbound origin reachability, paired with restrictive egress/firewall policy and protected tunnel credentials. Tunnel does not replace application authentication or Access policy. Never change nameservers, DNSSEC, DNS records, TLS mode, or firewall state during audit. Require an explicit, specific approval and staged rollback plan before any such mutation.
