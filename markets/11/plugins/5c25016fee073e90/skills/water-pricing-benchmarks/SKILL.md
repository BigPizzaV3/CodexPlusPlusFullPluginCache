---
name: water-pricing-benchmarks
description: Answer unit-cost questions for water and wastewater construction and supply — "what does 12-inch PVC water main cost per foot", "is this bid price high", "typical price for a 36-inch gravity sewer" — from awarded and bid unit prices, using the Water Investment Navigator MCP pricing tools.
---

# Water pricing benchmarks

Use the `water-investment-navigator` MCP tools `pricing_benchmarks` and `pricing_observations`.

## Workflow

1. `pricing_benchmarks(q=...)`: search by item words (size, material, item type),
   e.g. `q="12 in PVC"`. Each row is one canonical item **per unit** (`LF`, `EA`,
   `CY`, `TON`, ...) with `observations`, `n_utilities`, `p25_unit_price`,
   `median_unit_price`, `p75_unit_price` and `quality_tier`. Match the unit the
   user asked about; the same item can appear once per unit.
2. Check `quality_tier`:
   - `benchmark`: enough observations across utilities to quote a range.
   - `indicative`: quote it, but say it is indicative and give the count.
   - `insufficient`: prices are null **by design**. Don't make up a number.
     Say there isn't enough data, and optionally list the individual observations.
3. `pricing_observations(canonical_item_id, unit=...)` shows the individual
   prices behind a benchmark: utility, date, bidder, `price_kind`
   (`awarded` vs bid/quoted), `is_winner`, quantity, and the `decision_id` to cite.
   Use it to explain spread (small quantities cost more per unit; older
   observations predate recent inflation) and to find comparable local prices.

## Answering

- Quote the median with the p25–p75 range, the unit, the observation count and
  the date range (`first_observed`–`last_observed`).
- Prefer awarded (winning) prices when the user asks what work "costs"; losing
  bids are useful for spread, not for what utilities actually pay.
- Prices are nominal and not adjusted for inflation or region. Say so when the
  observation window spans several years.
- Cite at least one source decision (`get_decision_source_text`) when a user
  will act on the number.
- To see the bid tabulation or schedule of values itself,
  `get_decision(decision_id, include=["documents"])` gives the `resource_id` and
  pages, and `get_document_text(resource_id, start_page, end_page)` returns the
  page text. `search_documents(q="<item words>", utility_id=...)` finds priced
  pages that no benchmark covers yet.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
