---
name: website-launch-check
description: Scan a public website with Website Launch Check when the user wants to review launch readiness, technical SEO, social preview metadata, selected security headers, robots.txt, sitemap.xml, or basic technical setup.
---

Use the Website Launch Check MCP tool `scan_website` for the public website the user asks to check.

When presenting results:
- Lead with the overall score and grade.
- Prioritize failed checks before warnings.
- Group recommendations under technical SEO, social previews, security headers, and technical readiness when useful.
- Explain concrete fixes, but do not claim the scan proves a website is secure, accessible, legally compliant, or guaranteed to rank.
- Treat the scan as a read-only observation of the public response at scan time.
- If the scan fails because the URL is private, unresolved, too large, unsupported, or blocked by the target, explain the returned error and do not invent results.
- Do not ask for credentials, API keys, deployment tokens, passwords, or private URLs.
