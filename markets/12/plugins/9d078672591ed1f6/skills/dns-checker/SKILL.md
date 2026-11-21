---
name: dns-checker
description: Check a domain's live DNS records and email authentication (MX, SPF with the 10-lookup count, DMARC, DKIM) and look up raw A, AAAA, MX, NS, TXT, CNAME, CAA, and SOA records, each with a CSV report.
---

# Zovo DNS Checker

Use these tools when the user asks for a DNS lookup, an MX lookup, an SPF record checker, a DMARC check, or a DKIM checker for a domain. The tools read live public DNS through DNS-over-HTTPS; the assistant cannot query DNS on its own.

1. `check_email_dns` — email authentication for one domain.
   - Pass `domain` (for example `example.com`). Add `dkim_selectors` (up to 5) only when the user names them, for example `["mail", "selector1"]`.
   - Returns MX hosts, the SPF record and its DNS-lookup count against the limit of 10, the DMARC policy and reporting, DKIM keys, and a pass/warn/fail findings list with a one-line fix, plus a CSV report.
   - Summarise the verdicts and the non-pass findings with their fixes. Quote the SPF lookup count when it is near 10.
2. `lookup_dns_records` — raw records.
   - Pass `domain` and, when the user asks for specific types, `types` as a subset of `A, AAAA, MX, NS, TXT, CNAME, CAA, SOA`; omit `types` for the default set.
   - Returns the records with TTLs and a CSV report. Show the first rows and link the CSV for long lists.

Always state in the reply that the result is public DNS as seen by public resolvers at that moment, and give the source and the check time. Ask for the selector only if the user asks about DKIM and has not given one; otherwise skip DKIM.

Unicode domains are converted to punycode. Non-public addresses in returned records produce warnings and do not block a check. The tools query only public resolvers.

Do not use these tools for internal DNS server visibility, for WHOIS or domain-registrar data, or as a full deliverability test.
