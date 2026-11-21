---
name: price-history-research
description: Research how one exact trading-card printing or sealed product's observed price changed over a date range, with marketplace, finish, currency and missing-day coverage kept explicit.
---

Use `search_card_prices` or `search_sealed_prices` to establish identity, then
`summarize_price_history` for a bounded statistical summary. This is historical
research, not a numerical forecast or an instruction to trade.

- Cards require the exact game, history set code, TCGplayer product ID and
  `sub_type_name` such as Normal or Foil. Keep collector number, frame/treatment
  and finish distinct. Sealed products require the exact game, base set, model
  and TCGplayer product ID. Do not choose a similarly named printing or deck.
- Honor the user's range, marketplace and price basis. If no range is given,
  use the last 30 calendar days through today and state those explicit dates.
  Choose a single supported marketplace/basis; label any assumption. One call
  covers 1 to 366 inclusive days. Broader research needs explicit windows; do
  not average window medians or percentage changes into a false overall result.
- Cardmarket card history supports the `price` basis in EUR. Other supported
  combinations use `low` or `market`; preserve the returned currency. Never
  substitute a market quote for a missing low quote or convert currencies
  without a separately sourced rate and user request.
- Report the actual first and last usable observation dates and values,
  absolute/percentage change, minimum, maximum, median, and observed/requested
  days. Distinguish the requested date range from observed endpoints. A single
  observation cannot establish change, and a zero starting price has no finite
  percentage change.
- Check `coverage.complete` before calling the summary complete. If false,
  narrow the range or report the limit. Missing days are not filled; conflicting
  same-day observations are excluded and counted. Sparse coverage is part of
  the result, not a claim of price stability.

Use `card_price_history` or `sealed_price_history` for the underlying dated rows
when the user wants details or a chart; follow pagination and do not invent
intermediate points. Cite the source returned by the tools and identify the exact
product. Keep current price research separate from historical observations.
