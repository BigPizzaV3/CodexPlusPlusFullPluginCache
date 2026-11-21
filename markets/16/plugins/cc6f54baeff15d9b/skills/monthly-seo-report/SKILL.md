---
name: monthly-seo-report
description: Use when the user asks for a monthly SEO report, the evolution of keyword rankings, organic traffic or Search Console opportunities for a brand.
---

Produce a clear, actionable SEO report for a brand. The whole flow is read-only. Reply in the user's language.

1. Call `list_brands` and confirm the brand and the period (by default the last full month, dates as `YYYY-MM-DD`).
2. Call `gsc_search_analytics` for the period: clicks, impressions, CTR and average position. Repeat for the previous period of the same length to compute the change.
3. Call `gsc_top_queries` for the main queries with their position and impressions.
4. Call `keywords_tracked_list` and `keywords_snapshots` for the evolution of tracked keywords: what rises, what drops and what stalls.
5. Call `keywords_gsc_opportunities` for queries with impressions in improvable positions (11–30 by default).
6. If the brand has Google Analytics connected, call `ga4_report` with `dimensions = ["page"]` for the most viewed pages in the period.
7. Write the report:
   - Executive summary (2–3 sentences with the month's trend and key figures).
   - Search Console: clicks, impressions, CTR and position, with the change against the previous period.
   - Keyword movements: biggest gains and losses (previous position → current).
   - Most viewed pages (if Analytics data is available).
   - Opportunities: queries one push away from page one, with a concrete action for each (content, internal linking, search intent).
   - Prioritized next steps.

Rules:
- Make MCP calls one at a time.
- Use the numbers the tools return and never invent data; if a source is not connected or returns nothing, say so.
- Analytics users cannot be added up across rows: use the total the tool returns.
