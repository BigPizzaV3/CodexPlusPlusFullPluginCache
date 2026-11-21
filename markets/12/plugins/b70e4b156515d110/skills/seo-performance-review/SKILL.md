---
name: seo-performance-review
description: Review organic search performance from Google Search Console, tracked keyword rankings, technical SEO audits and GA4 in CitationLab. Use for questions about clicks, impressions, rankings, lost traffic, cannibalization or index problems.
---

# SEO performance review

All tools need `projectId`.

1. **Search Console:**
   - `get_gsc_full_report` for totals, top queries and top pages over a period. Compare two equal periods (for example the last 28 days against the 28 before) by calling it twice with `startDate`/`endDate`.
   - `get_gsc_keywords` and `get_gsc_pages` to find which queries and URLs moved. Rank winners and losers by the change in clicks.
   - `get_gsc_cannibalization` when several pages compete for one query.
2. **Rankings:** `list_keywords` and `get_rank_tracking` for tracked positions; `get_ranking_history` for one keyword over time.
3. **Technical health:** `list_technical_seo_audits`, then `get_technical_seo_issues` or `get_technical_seo_full_report` for the latest audit; `get_index_checker_report` for pages that are not indexed.
4. **Traffic and conversions:** `get_ga4_summary`, `get_ga4_page_engagement` and `get_ga4_events` to confirm whether a drop in clicks shows up as lost sessions and conversions.

## How to report

- State the period compared, then the net change, then the top movers by name (query or URL) with before → after.
- Separate what the data shows from what you infer (seasonality, a ranking loss, an indexing problem).
- If Search Console or GA4 is not connected, say which and continue with what is available.
- Offer to record next steps as actions (see `actions-and-follow-up`).
