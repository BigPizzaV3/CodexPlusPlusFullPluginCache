---
name: allratestoday-fx
description: Use when a user asks for currency conversion, supported currencies, central-bank coverage, an institution's latest official exchange-rate table, or AllRatesToday's daily reference-rate snapshot.
---
# AllRatesToday exchange-rate guidance

Use the AllRatesToday MCP server for supported currency-rate questions. Do not guess rates or invent missing fields.

- For a single fiat-currency pair or amount conversion, call `get_exchange_rate`. Multiply the user's amount by the returned `rate` yourself.
- For supported currency codes, names, or symbols, call `list_currencies`.
- For covered institutions, or before selecting a bank code, call `list_central_banks` and use the returned `code`.
- For an institution's latest published table, call `get_official_rates`. Omit source/target to request the full table; provide both for one pair. Preserve any `derived` flag.
- For the once-daily reproducible reference snapshot, call `get_reference_rate`. This is the median of five samples around 16:00 London, not the WM/Refinitiv fix and not a registered benchmark.

Always name the source institution and report the returned `rate_date` for rate answers. Clearly distinguish official daily reference tables from live market/dealing quotes. If the returned rate is derived, say so. Do not claim a rate is current beyond its returned publication date. Rates are informational, not personalized financial advice; do not claim to execute transfers or guarantee future bank rates. If a tool errors or lacks a requested currency/source, explain the limitation instead of fabricating a result.
