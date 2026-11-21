---
name: striking-distance-keywords
description: Find queries ranking in positions 8-20 in Google Search Console and plan the on-page changes most likely to move them onto page one. Use when the user asks for quick SEO wins, keywords close to page one, low-hanging fruit, or what to optimize next. Requires the DidYouSEO MCP connector with Search Console connected.
---

# Striking distance keywords

Find the queries Google already considers relevant but ranks just off the top, and say exactly how to push each one.

## Tools

- `get_search_console_keywords` (website, days=90) - queries with clicks, impressions, CTR and average position.
- `analyze_meta_tags` (url) - current title, description and headings of the ranking page.
- `serp_preview` (url) - how the snippet looks now.

## Steps

1. Call `get_search_console_keywords` with `days: 90`.
2. Keep queries with average position between 8 and 20. Drop any with fewer than 100 impressions in the window; they won't bring meaningful traffic even at position 3.
3. Drop branded queries (containing the site's brand name). Those rank on their own.
4. Rank the rest by impressions, highest first. Take the top 10.
5. The keyword tool doesn't say which page ranks for each query. For each of the top 5, find the most likely page on the site (ask the user if it isn't obvious) and call `analyze_meta_tags` on it.
6. For each, recommend at most three changes from this list, in this order of preference:
   - put the exact query in the title, near the front
   - answer the query in the first 100 words
   - add the section that competing pages cover and this page doesn't
   - add 3-5 internal links to it with descriptive anchor text
   - refresh outdated facts, then the date
7. Never recommend creating a new page for a query an existing page already ranks for. That splits the signal.

## Output format

A table of the top 10: query, position, impressions, page. Then, for the top 5, the specific changes with a drafted title where relevant.

End with: "Re-check in 4 weeks. Compare the 4 weeks after the change with the 4 weeks before, for the same query."

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
