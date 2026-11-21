---
name: web-traffic-analysis
description: Use when the user asks about a brand's website traffic in Google Analytics: views, users, most viewed pages or daily trend, overall or for a specific section.
---

Analyze a brand's website traffic with Google Analytics 4. Read-only flow. Reply in the user's language.

1. Call `list_brands`, confirm the brand and the period (`start_date` and `end_date` as `YYYY-MM-DD`).
2. Call `ga4_report` depending on the question:
   - Period totals: `dimensions = []`.
   - Most viewed pages: `dimensions = ["page"]`.
   - Daily trend: `dimensions = ["date"]`.
   - A specific section: add `page_filter` with a fragment of the path (e.g. `/blog/`).
   - If there are more results, page through them with the `next_offset` the tool returns.
3. To compare, repeat the query for the previous period of the same length.
4. If organic traffic sources matter, add `gsc_search_analytics` (`dimensions = ["page"]` or `["query"]`).
5. Write the analysis:
   - Key figures (views and users) and their change.
   - Pages that grow and drop the most, with their share of the total.
   - Spikes or drops in the daily trend and their likely cause.
   - Concrete recommendations.

Rules:
- Users cannot be added up across rows (pages or days): use the total the tool returns.
- If the brand has no Google Analytics connected, say so and suggest connecting it in Abency.
