---
name: get-started
description: Use this when the user asks "what status code does <url> return", "is this a 301 or 302", "redirect checker <url>", "check these for redirect chains", "check every row of our redirect map lands on the right page", or about a Search Console "redirect error". The tools make a live HTTP request and return each hop's exact status code and Location header, the final URL and the chain length. Do not use for general redirect theory such as "301 vs 308 for SEO".
---

Typical requests: "what status code does https://example.com/old return", "is this a 301 or 302: example.com/promo", "redirect checker http://example.com", "we moved to https, check these for redirect chains", "here is our redirect map, check every row lands on the right page". Each one needs a live request that answers with real status codes, not documented behaviour.


1. Ask only for what is missing: the URL(s), or the redirect map (old URL → expected new URL). Paths like `/old-page` need the site address: pass it as `siteUrl`.
2. One URL or a list without expected targets: call `check_redirects`. A map with expected targets (pasted CSV, an attached CSV file, a Shopify redirect export, `.htaccess` "Redirect 301" lines): call `check_redirect_map` with `csv` exactly as given, `rows`, or the attached `file`.
3. Lead with what to fix: failing rows first (wrong target, loop, 404/410 final page, blocked or unreachable), then warnings (chains, 302/307 that should be 301, http→https or www in separate hops, canonical pointing elsewhere, meta-refresh or JavaScript redirects). Quote the status chain, e.g. `301 → 302 → 200`.
4. A 403, 429 or no answer on the last page usually means the site blocks automated checkers. Say so; the redirects before it are real. Never call such a row broken.
5. If the result has `next.startRow`, call the tool again with the same input and that `startRow` until every row is checked, then summarise all parts together.
6. Offer to write the fix: one direct 301 per old URL to its final target, in the user's server format (.htaccess, nginx, Netlify `_redirects`, `vercel.json`, Shopify CSV). Ask which one if unknown. Do not write rules for sites the user does not control.
7. Localhost, intranet and private addresses, and pages behind a login, cannot be checked. Results reflect a request from Frankfurt (EU) without cookies; country, device or login redirects may differ.
