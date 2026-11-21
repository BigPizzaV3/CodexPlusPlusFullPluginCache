---
name: statista-data
description: Retrieves and answers with Statista figures from Market Insights, Consumer Insights and Statistics. Use for a single figure, a lookup, a trend, a quick comparison, or whether Statista covers a topic. Not for sizing, scoring, frameworks or decks.
---

# Statista Data

## Route

| Need | Bucket | Tools |
|---|---|---|
| Market size, revenue, forecast, CAGR, ARPU, share | Market Insights | `search-market-insights` → `fetch-market-insights` |
| Intent, WTP, brand, channel, buyer demographics | Consumer Insights | `search-consumer-insights` → `fetch-consumer-insights` |
| Counts, actual spend, adoption, single companies, niche series | Statistics | `search-statistics` → `get-chart-data-by-id` |

Out of scope: live prices, M&A, funding, valuations, ownership, regulation, company filings. Ecommerce connector tools (`search-ecommerce`, `ranked-ecommerce`, `metrics-ecommerce`, `profile-ecommerce`, `shopper-ecommerce`) are out of scope until documented. Say so and name the closest Statista coverage.

## Retrieve

- Run all searches in one parallel batch, then fetch in one batch. Searches are cheap, fetches are the budget.
- Search returns IDs and metadata, never values. Ignore numbers in search titles and descriptions. Every figure comes from a fetch.
- Market Insights `geo`: at most 5 codes per `fetch-market-insights` call; split into batches if more are needed.
- Nothing relevant found: stop, say what was searched, offer a narrower or adjacent angle.
- Statista only. No web, no model knowledge, no estimates.

## Gotchas

- Market Insights geography codes come from `covered_geos` in search results. Pass them exactly (`DEU`, not `Germany`). A missing country is not covered. Fetch several geos in one call.
- Regional codes are aggregates, never sums of countries.
- Market Insights growth rates are decimals (0.10 = 10%).
- Consumer Insights search is keyword-based: 2–3 words. Crosstabs need both variables from the same survey and country. Skip year-named variables (`..._2023`). Thin cells are not findings.
- `search-statistics` returns a `link`: keep it as the source URL. Never build a URL.
- Use the newest vintage per metric. Never mix vintages in one comparison; flag data older than two years.
- Reuse figures already fetched in this conversation.

## Cross-check

When two buckets cover the same quantity: spread = |A − B| / mean. ≤30% triangulated, 30–67% report both, >67% direction only. Never average. Single source = Low or Medium confidence.

## Answer

Answer first, with the number, year and confidence. Cite bucket and year per figure. Label calculated figures with their inputs. State currency, and actual vs forecast. Chart only when the reader needs a shape (trend of 3+ points, ranking of 4+); otherwise a sentence or table.
