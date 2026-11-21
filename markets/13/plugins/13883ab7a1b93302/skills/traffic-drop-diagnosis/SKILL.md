---
name: traffic-drop-diagnosis
description: Diagnose a drop in Google organic traffic by comparing Search Console periods and auditing the pages that lost the most clicks. Use when the user says traffic fell, clicks dropped, a page stopped ranking, or asks what happened to their SEO. Requires the DidYouSEO MCP connector with Search Console connected.
---

# Traffic drop diagnosis

Work out whether a drop is technical, a ranking loss, a demand change or a result-page change, and say which with evidence.

## Tools

- `get_search_console_changes` (website, days) - biggest click losers and gainers against the previous period, with position changes.
- `run_seo_audit` (url) - audit the pages that lost the most.
- `check_robots_txt` (url) - rule out a crawl block.
- `get_ga4_organic_traffic` (website, days) - confirm the drop in real visits, if Google Analytics is connected.

## Steps

1. Ask when the drop started if the user didn't say. Use a window that covers it: `days: 28` for a recent drop, `days: 90` for a slow decline.
2. Call `get_search_console_changes`. If Google Analytics is connected, also call `get_ga4_organic_traffic` for the same window: if Search Console clicks held but GA4 organic sessions fell, suspect tracking (a removed or broken GA4 tag), not SEO.
3. Classify the pattern from the losers:
   - **Position fell, impressions held** - ranking loss. Likely content or competition.
   - **Impressions fell, position held** - demand or seasonality. Fewer people searching.
   - **Impressions held, position held, clicks fell** - the result page changed (AI Overview, new features). CTR problem, not a ranking problem.
   - **Many pages fell at once, sitewide** - technical issue or a Google update.
4. For a sitewide drop, run `check_robots_txt` on the homepage and `run_seo_audit` on the homepage and the top 2 losing pages. Look for noindex, canonical, robots or server errors first.
5. For page-level drops, run `run_seo_audit` on the top 3 losing pages.
6. Only call something a Google update if the timing matches and nothing technical explains it. Say it's a hypothesis.

## Output format

```
What happened: <one sentence with the numbers>
Most likely cause: <category> - <evidence>
Ruled out: <what you checked and found fine>

Fix
1. <action>
2. <action>

Watch: <what to re-check and when>
```

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
