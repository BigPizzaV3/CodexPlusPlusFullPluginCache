---
name: google-trends-research
description: Compare Google Trends search interest over time or by region, or find related queries and topics with HasData. Use for relative interest, not absolute keyword volume, sales or organic rankings.
---

# Compare search interest

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_google_trends_search_getTrendsData` with q. Choose dataType from the task: timeseries, geoMap, relatedTopics or relatedQueries. Inspect the live schema for how multiple terms are encoded; use a single shared request for comparisons when supported, not separately normalized queries treated as equivalent scales.

Preserve supplied geo and date. Use a supported date string such as today 12-m for an explicitly requested past year. region applies to geoMap, not timeseries. relatedTopics and relatedQueries accept one query; do not pass an unsupported multi-term comparison.

Keep query, date range, geography, data type and returned time granularity with the output. Explain relative interest and missing periods. A 0-100 interest index is not absolute search volume, revenue or a demand forecast. Cite returned source context/snapshots and avoid converting separately normalized scores into a cross-query ranking.
