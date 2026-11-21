---
name: imotesa-neighbourhood-comparison
description: Compare observed asking-price context across Bulgarian neighbourhoods or inspect one local market segment without giving forecasts or investment advice.
---

Use this skill when a user wants evidence-based asking-price context for one Bulgarian city or neighbourhood, or a comparison of two to five neighbourhoods in the same city. Do not use it for individual properties, forecasts, lifestyle comparisons, legal advice, mortgage guidance, or investment recommendations.

## Workflow

1. For one city or neighbourhood, call `get_market_stats`. For two to five neighbourhoods in the same city, call `compare_areas`.
2. Pass names directly when they are known. Call `list_locations` only when the user needs candidate places or a location needs disambiguation.
3. Use `search_properties` or `get_property` only if the user changes the request to a specific property or active offers.

## Reporting rules

- Describe every figure as an observed asking price in EUR, not a transaction price. Rent figures are monthly.
- Prefer median price per m² and include the sample size, availability, property type, sale or rent context, and any room-count filter.
- For comparisons, explain that rank 1 is the most expensive available area and that `pct_above_cheapest` is relative to the cheapest available area.
- `available=false` means the segment has too few listings for published statistics; it does not establish that demand, supply, or prices are absent.
- If the tool reports a matched location, name the matched city or neighbourhood. If history is unavailable, say so rather than extrapolating.
- Report facts and uncertainty without predicting price movements, asserting what buyers paid, or recommending where to buy.
- Link the returned `canonical_url` when it helps the user inspect the source context.
