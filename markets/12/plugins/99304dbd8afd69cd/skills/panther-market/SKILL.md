---
name: panther-market
description: Use Panther to compare Egyptian property listings, historical prices and validated absorption, count listed units, or read the connected user's own saved Land Intelligence.
---

# Panther market evidence

Use the connected Panther tools for Panther market evidence. Access requires an
approved Panther account; sign-in takes place on Panther's authorization page.
Installing this package does not grant access to another person's account.

## Choose the evidence

- Resolve named projects and developers with `panther_market_filters` before
  querying. `dimension=month` discovers stored waves; a project absent from the
  newest wave can still have historical evidence.
- For prices, tickets or areas, use `panther_market_comparison`. For minimum,
  average and maximum together, use `panther_market_price_ranges`.
- For available/listed unit counts, use `panther_market_comparison` with
  `metric=listing_count`, grouping by project or unit type. Return the dated
  snapshot count. These are observed listing rows, not total planned homes.
- A single historical snapshot uses `snapshot_month`. Every stored wave uses
  `snapshot_scope=all_waves`, optionally bounded by month. Keep the monthly cuts
  separate and follow pagination. Never sum repeated monthly stock as unique
  units. Use `panther_price_history` for its matched-project price trends.
- Use `panther_absorption` for validated absorption, including absorbed units,
  units offered, rates and measured time on market. Listing disappearances alone
  are not sales. Broad regional questions start with `view=overview`, the region,
  and no date restriction or sampled projects. This reads all published months
  for the entire selected cohort. Use `view=unit_types` and `view=monthly` for
  product and monthly detail as relevant.
- For a named project's most absorbed product, resolve its ID and query
  absorption `view=project_types` with `sort_by=absorbed_units`. Highest sales
  volume, highest rate and shortest measured time on market are different
  questions; use the requested measure and explain the period and coverage.
- For saved deals, call `panther_my_deals`, then `panther_land_intelligence` with
  an owned deal ID. Inspect available sections and retrieve relevant pages.
  Follow pagination before claiming a whole-cohort ranking. For ambiguous
  "strongest competitors", clarify the criterion or state a proposed method
  grounded in the requested comparable evidence; proximity alone is not strength.

## Explain the result

Lead with the answer supported by the retrieved evidence. Include the relevant
chart or table when useful, followed by a concise interpretation. State the data
dates, selected geography/projects and material coverage limitations.

Prices are broker-listed asking prices, not confirmed transaction prices.
Absorption uses Panther's validated historical engine. Its primary dashboard
rate is absorbed units divided by all stock offered in the same window;
`opening_book_rate_pct` is a separate measure. Do not average project percentages.
Unknown/held-back evidence is not zero. Preserve provisional-month flags.

Use returned full-cohort totals/shares and follow continuation pages; do not
substitute a few projects or arbitrary months for a regional question. If a tool
fails, explain the actual failure. Preserve the requested cohort and dates when
splitting reads; label partial answers and do not silently substitute a narrower
scope.
Do not claim all data is unavailable because a price-only tool lacks sales data.

The integration exposes market evidence and the user's own Land Intelligence.
Product Mix, pricing recommendations, feasibility, master plans, IC memos and
reporting remain in the Panther website: https://panther.rcrut-ai.com/.
The connection is read-only. Raw unit records/codes, confidential internal peers
and other users' deals are not exposed. Sign-in credentials belong only on the
Panther authorization page, never in chat.
