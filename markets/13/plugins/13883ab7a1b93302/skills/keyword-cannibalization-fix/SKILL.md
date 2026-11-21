---
name: keyword-cannibalization-fix
description: Detect keyword cannibalization from real Google Search Console data and decide, per conflict, whether to merge, redirect, re-target or leave the pages alone. Use when the user asks about cannibalization, pages competing with each other, duplicate rankings, or rankings that keep swapping between URLs. Requires the DidYouSEO MCP connector with Search Console connected.
---

# Keyword cannibalization fix plan

Find queries where two or more of the site's own pages compete, and give a decision for each conflict, not just a list.

## Tools

- `get_search_console_cannibalization` (website, days=90) - conflicts with competing pages, severity and the reason.
- `analyze_meta_tags` (url) - compare the competing pages' titles and headings.

## Steps

1. Call `get_search_console_cannibalization` with `days: 90`.
2. Skip low-severity conflicts unless there are no others. Two pages sharing a query is normal; it's only a problem when they split clicks or rankings swap.
3. For each remaining conflict, call `analyze_meta_tags` on the competing pages and decide:
   - **Merge and redirect** - both pages cover the same intent. Keep the one with more clicks, fold the other's unique content into it, 301 the weaker URL.
   - **Re-target** - different intents that look similar (for example a guide and a product page). Change the weaker page's title and H1 to its own intent and link it to the stronger page.
   - **Canonical** - near-duplicates that must both exist (filters, print versions). Canonical to the main one.
   - **Leave it** - Google shows both because they serve different searchers and both get clicks.
4. Give the reason for each decision in one line, based on the data returned.

## Output format

For each conflict:

```
Query: "<query>"
Pages: <url A> (<clicks>) vs <url B> (<clicks>)
Decision: <Merge and redirect | Re-target | Canonical | Leave it>
Why: <one line>
Steps: <2-4 concrete steps>
```

Finish with the order to do them in: highest-impression conflicts first.

## Limits

- Audits and single-URL checks (`run_seo_audit`, `run_pagespeed_insights`, `analyze_meta_tags`, `check_robots_txt`, `validate_schema`, `serp_preview`, `check_core_web_vitals`, `check_open_graph`, `check_hreflang`) count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop calling them, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- On the Free plan, the Search Console and Google Analytics tools return a short preview. Say the results may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
