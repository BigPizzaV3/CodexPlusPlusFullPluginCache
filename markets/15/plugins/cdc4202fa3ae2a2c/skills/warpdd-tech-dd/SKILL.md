---
name: warpdd-tech-dd
description: How to use the WARP DD MCP tools for technology due diligence — choosing between the no-sign-in index tools and the signed-in theme search, and the two-step search flow (start, then poll results).
---

# WARP DD — technology due diligence

WARP DD discovers technology companies for a technology theme and scores them on four axes (technology, commercial maturity, theme fit, evidence) with traceable sources.

## Choose the right tool

- Quick lookup, no account needed: `warp_tech_index` (theme → market map: segments and real companies with verified websites) and `warp_list_companies` (company name → profile and evidence counts). `warp_get_evidence` with only a company name returns public evidence counts.
- Full search, account required: `warp_screen_theme` starts a WARP DD theme search. It needs the user's WARP DD account to be connected. If the tool replies that sign-in is required, tell the user to connect their WARP DD account from the plugin settings; do not retry the tool.

## Two-step search flow

1. Call `warp_screen_theme` with a one-line theme (Japanese or English). It returns a `search_id` immediately; the search itself takes about 35–60 seconds.
2. Wait about 30 seconds, then call `warp_dd_workspace` with that `search_id`. If `status` is `searching`, wait `retry_after_seconds` (20) and call it again. When `status` is `completed`, present the companies with their scores.
3. For one company, use `warp_company_score` (score breakdown) and `warp_get_evidence` (sources) with the same `search_id`.

## Presenting results

- Show total score, grade and the four axes; mention that scores are evidence-based technology assessments, not investment advice.
- Offer the `web_url` so the user can open the search, reports, comparison tables and exports on warpdd.com.
- A theme search uses one search from the user's plan allowance. If the tool reports that the monthly allowance is exhausted, say so and point to the informational page it returns; do not suggest purchases.
