---
name: on-page-seo-rewrite
description: Check a page's title, meta description, headings, structured data and social tags, then draft improved versions ready to paste. Use when the user asks to optimize a page, improve a title or meta description, fix how a page looks in Google or on social media, or add schema. Works with the free DidYouSEO MCP tools, no account needed.
---

# On-page SEO rewrite

Read what a page shows search engines and social networks today, then write better versions.

## Tools

All of these are free and work on any public URL:

- `analyze_meta_tags` (url) - title, description, robots, headings and more.
- `serp_preview` (url) - how the snippet renders in Google, with truncation.
- `validate_schema` (url) - structured data found and its errors.
- `check_open_graph` (url) - social share tags.

## Steps

1. Call all four tools on the URL.
2. Ask for the target query if the user didn't give one. Without it, infer it from the H1 and say what you assumed.
3. Draft:
   - **Title**: 50-60 characters, target query near the front, no keyword lists.
   - **Meta description**: 120-155 characters, answers why someone should click.
   - **H1**: if missing, duplicated or unrelated to the query.
   - **Structured data**: fix reported errors; suggest a type only if it fits the page (Article for posts, Product for products, Organization on the homepage). Don't add FAQ or Review markup to content that isn't really a FAQ or real reviews.
   - **Open Graph**: og:title, og:description and og:image if missing.
4. Show character counts for title and description.

## Output format

```
Target query: <query>

Title
Now:  <current> (<n> chars)
New:  <draft> (<n> chars)

Meta description
Now:  <current>
New:  <draft> (<n> chars)

Structured data: <issues and the corrected JSON-LD block>
Social tags: <missing tags with values>
```

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
