---
name: search-console
description: Use Cituna's connected Google Search Console properties to analyze queries, pages, clicks, impressions, ranking opportunities, zero-click pages, intent, coverage and AI-style searches.
---

# Analyze Google Search Console with Cituna

Read [connection and evidence rules](../../references/connection-and-evidence.md).

## Connection and scope

Call `gsc_status` and resolve the requested property from all connected accounts.
If disconnected, guide the user to https://cituna.com/integrations to connect
Google and verify the property, then recheck. Do not ask for Google credentials
or claim this MCP can connect, disconnect or verify a Google property directly.

Select the report that directly answers the request:

| Request | Tool |
| --- | --- |
| Traffic summary, top queries/pages, country/device splits | `gsc_overview` |
| Specific dimensions, filters, dates or pagination | `gsc_query` |
| Queries near page one worth improving | `gsc_striking_distance` |
| Pages with impressions and few or no clicks | `gsc_zero_click_pages` |
| Brand, competitor, commercial and other query intent | `gsc_query_mix` |
| Sitemap pages without observed impressions | `gsc_coverage_gap` |
| Multiple owned pages competing for the same query | `gsc_cannibalisation` |
| Queries with conversational or AI-style wording | `gsc_ai_searches` |

## Query and interpret correctly

- Use a bare `domain`, or the exact accessible `siteUrl` where supported. Observe
  each tool's schema: overview supports 1–90 days; several analysis tools and
  raw queries support 1–480 days. Never assume the same bounds for every tool.
- For `gsc_query`, choose dimensions from `query`, `page`, `country`, `device`,
  `searchAppearance`, `date`. Pair explicit `startDate` and `endDate`, or use
  trailing `days`. Filters combine with AND. Paginate with `startRow` when a
  response reaches `rowLimit`; disclose sampling if not retrieving every row.
- State dates and GSC reporting lag. Inspect returned `history`, actual covered
  dates and `windowTruncated` before describing a period as a full month/quarter.
  Use comparable windows and property scopes for trends.
- Use returned site totals for site totals. Named-query rows omit anonymized
  queries, so summing them may undercount. Calculate aggregate CTR from total
  clicks divided by impressions; do not average row percentages. Do not average
  positions without the appropriate weighting and scope.
- Striking-distance `priority` is an ordering heuristic, not forecast traffic.
  For zero-click pages, preserve the tool's distinctions between brand searches,
  snippet issues, page-two position and deeper ranking. Phrase causes as the
  report's classifications rather than independently proven diagnoses.
- No impressions is not proof a page is unindexed. `gsc_coverage_gap` compares
  sitemap URLs with observed impressions and cannot separate indexing failures
  from low visibility. Recommend checking URL Inspection when needed.
- `gsc_ai_searches` identifies query wording; it does not measure Google's AI
  Overviews/AI Mode totals or prove where an individual query originated. Keep
  those heuristic results separate from Cituna's measured AI-engine answers.
- Join GSC demand to prompt tracking, citations or content opportunities only
  with explicit matching evidence. If the match is semantic, label it as such.
- Google access is read-only. This plugin cannot submit sitemaps, request
  indexing, change Google settings or mutate GSC data.

## Relevant tools

`gsc_status`, `gsc_overview`, `gsc_query`, `gsc_striking_distance`,
`gsc_zero_click_pages`, `gsc_query_mix`, `gsc_coverage_gap`,
`gsc_cannibalisation`, `gsc_ai_searches`.
