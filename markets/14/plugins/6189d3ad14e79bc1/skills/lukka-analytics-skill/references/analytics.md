# Lukka Quantitative Analytics MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Choose one of the three analytics tools

- Implied rate term structures: `analytics___getImpliedRates`.
- OTC FX observations: `analytics___getImpliedRatesOtcFx`.
- Options implied volatility surfaces: `analytics___getImpliedVolatilitySurface`.

DeFi and general liquidity tools mentioned in the old routing entrypoint are absent from the recorded product catalog; do not route to them without current discovery.

## Rates

For implied rates, inspect required `pairCode`, `lukkaEntityCode`, `curveType`, `source`, `rateType` and time arguments. Use documented canonical entity codes rather than exchange display names. When comparing `MC` and `NSS`, hold the instrument, entity, curve, source, rate type and UTC window constant.

Historical source tests found coverage for `INST_FWD` where some other curve values returned nothing. Treat that as a diagnostic starting point, not a promise of current coverage. A no-data error can arrive with HTTP 200 and a next-page link; stop paging when there are no actual data or no progress, and deduplicate cursors/windows.

## Volatility and OTC FX

For surfaces, select the supported entity, underlying code and `moneyness`; pass explicit `timeFrom` and `timeTo` where required. A shorthand `timeRange` still needs an anchor where specified. Preserve returned delta/strike grid labels and units instead of relabeling them.

The source observed ignored `grid_label` and `limit` filters on a surface endpoint. Narrow by tenor and time window first and bound the presentation locally if needed. Do not assume a small requested limit guarantees a small response. Start OTC FX with a bounded response and identify the returned pair, tenor, entity and timestamp.

Keep observed analytics separate from forecasts, execution prices and profit guarantees. This plugin does not access or rebalance an exchange account.
