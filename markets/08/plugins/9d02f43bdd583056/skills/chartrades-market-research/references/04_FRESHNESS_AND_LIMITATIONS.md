# Freshness And Limitations

Freshness matters. A correct historical read can still be unusable as a current market read.

Use freshness metadata whenever the live tool returns it.

Relevant freshness signals may include:

- latest update timestamp
- source freshness
- database freshness
- analyzer freshness
- rows returned
- capped rows
- stale flags
- missing-data warnings
- coverage warnings
- provider warnings

If freshness metadata is missing, say current reliability is unclear.

## Missing Or Partial Data

Missing data is not a market signal.

Examples:

- no wallet rows does not prove no wallet activity
- no on-chain rows does not prove no on-chain activity
- no anomaly rows does not prove the market is clean
- failed provider does not prove the asset is inactive

Say what is missing and how it affects confidence.

## Public Data Limits

Market data, public APIs, chain data, exchange data, wallet data, and provider feeds can have:

- symbol coverage gaps
- rate limits
- stale windows
- row caps
- lookback caps
- delayed refreshes
- parser gaps
- provider outages

Treat capped or partial results as scoped to the returned data unless the live response confirms full coverage.

## Status Cache Interpretation

When status-cache fields are returned:

- TTL staleness and lag behind the latest terminal worker generation are separate conditions.
- `refresh_in_progress` means stale-while-revalidate: the response can contain the previous value while a background refresh runs.
- Use the returned refresh outcome/reason and normalized cache health instead of treating the first stale response as proof that cache replacement failed.
- A cache-only warning with `execution_impact=none` is an observability limitation, not a market execution gate.

When effective derivative coverage is healthy through substitutes, a medium confidence basis may describe missing native-venue breadth rather than stale effective data. Do not call healthy substituted axes impaired unless the live response does.

## External Context

Use web/external context only when it materially affects interpretation, such as macro events, exchange incidents, regulatory news, protocol updates, exploits, unlocks, ETF flows, or broad risk regime.

Clearly separate:

- Internal data from Chartrades
- External context
- Interpretation

External news explains context. It does not validate a trade unless internal data confirms it.
