---
name: pre-launch-seo-check
description: Run a go/no-go SEO check before a site, redesign or migration goes live - indexing, robots.txt, canonicals, structured data, hreflang, speed and social tags. Use when the user is launching a site, migrating, redesigning, moving from staging to production, or asks if a site is ready to go live. Requires the DidYouSEO MCP connector; most checks are free.
---

# Pre-launch SEO check

Catch the mistakes that quietly wreck a launch: a leftover noindex, a staging robots.txt, canonicals pointing at the old domain.

## Tools

- `check_robots_txt` (url)
- `analyze_meta_tags` (url) - robots meta, canonical, title, description.
- `validate_schema` (url)
- `check_hreflang` (url) - only if the site has more than one language or region.
- `run_pagespeed_insights` (url, strategy) - Lighthouse scores, real-user Core Web Vitals and the biggest speed fixes.
- `check_open_graph` (url)
- `run_seo_audit` (url) - full audit of the most important page, if the user is signed in.

## Steps

1. Ask for the 3-5 most important URLs (homepage, a main product or service page, a blog post, a contact page) if the user only gave a domain.
2. Run `check_robots_txt` once on the domain. A `Disallow: /` for all user agents is an automatic no-go.
3. For each URL run `analyze_meta_tags`, `validate_schema`, `check_open_graph` and `run_pagespeed_insights` (mobile). Run `check_hreflang` if relevant. A performance score under 50 on the homepage is a fix-this-week item, not a blocker.
4. Check for launch-specific failures:
   - `noindex` on pages that should rank
   - canonicals pointing at a staging or old domain
   - titles or descriptions still showing placeholder text, or identical across pages
   - missing or broken structured data on key templates
5. If the user is signed in, run `run_seo_audit` on the homepage for the full picture.

## Output format

```
Verdict: GO | GO WITH FIXES | NO-GO

Blockers (fix before launch)
- <issue> on <url> - <exact fix>

Fix this week
- <issue> - <fix>

Checked and fine
- <list>
```

A single blocker makes the verdict NO-GO. Be explicit about which item caused it.

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
