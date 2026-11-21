---
name: scan-now-tools
description: Use Scan.now when the user wants a passive security assessment of a website they are authorized to test, or wants to inspect a suspicious public link for phishing signals.
---

# Scan.now tools

Use `scan_website_security` only after the user states that they own the target website
or have explicit permission to assess it. If that authorization is absent, ask for it
before calling the tool. Set `authorized` to true only after that confirmation.

Choose the narrowest useful scope:

- `full` for a broad passive assessment.
- `tls` for certificates, protocol support, and HTTPS behavior.
- `headers` for HTTP security headers, cookies, CORS, and related page controls.
- `email` for SPF, DKIM, DMARC, DNSSEC, CAA, and email-domain posture.
- `js` for public JavaScript inventory and known vulnerable library versions.

Use `check_phishing_link` when the user wants to understand whether a public link looks
deceptive or where it redirects. Explain that a low score is not a guarantee: a new or
unreported phishing page may not yet appear on blocklists.

These tools are passive and read-only. They do not exploit findings, bypass access
controls, guess credentials, scan private networks, or prove that a target is secure.
Do not help use the results for unauthorized access. Prefer the finding's
`reference_url` when the user asks how to fix an issue.
