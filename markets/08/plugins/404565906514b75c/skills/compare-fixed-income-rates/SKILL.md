---
name: compare-fixed-income-rates
description: Compare multiple current public CD, money-market, Treasury, or municipal options when the user explicitly asks for a bounded comparison.
---

# Compare fixed-income rates

Use this workflow only for an explicit descriptive comparison across one or more supported instrument types. For a simple find, search, list, browse, or lookup request, use `search` instead.

1. Preserve the user's requested instrument types, minimum maturity, maximum maturity, and result limit; ask only when a missing bound materially changes the comparison.
2. Call `compare_rates` once with those explicit filters.
3. Organize the returned options by instrument and maturity. Include each canonical BrinkerAdvisor row link and the common as-of date.
4. Explain that APY, seven-day SEC yield, Treasury par yield, and not-yet-priced offerings are not interchangeable conventions.
5. If the user needs complete provenance for one option, call `fetch` with that option's stable ID.

Do not label a winner or turn the ordering into suitability, tax, return, or allocation advice. An empty result is evidence that no current row passed the filters, not evidence that the market has no such product.
