# Lukka Pricing & Market Data MCP — hosted workflows

Adapted from the publisher-provided `lukka-mcp-hosted` product reference. Old deployment observations must be checked against current discovery and returned data.

## Resolve sources before requesting prices

Use `pricing___list_pricing_sources` or `pricing___list_sources_by_product` to discover an entitled source for the requested product. Pass a numeric `sourceId` where required; do not reuse the internal server's `source` alias. Source availability is account-specific.

Use canonical pair codes such as `XBT-USD`, `ETH-USD` and `SOLN-USD` only where supported. Preserve the distinction between spot prices, reference rates and separately entitled index sources. A source returning 403 is not a reason to silently substitute a different price basis.

## Choose the observation

- Current prices: `pricing___get_latest_prices`.
- OHLCV: `pricing___get_candles`; historical prices: `pricing___get_historical_prices`.
- Top market capitalization: `pricing___get_latest_market_caps`. The supplied hosted skill observed largest-first ordering when `order` was omitted. Leave it unspecified for that workflow and check returned ranks and values before describing a top-N result.
- Liquidity: `pricing___get_vwap`, `pricing___get_market_depth` or `pricing___get_order_book_snapshot` according to the request.
- Derivatives: the derivative source and trade tools in this connection; implied curves and volatility surfaces require a separate Analytics connection.

Intervals are milliseconds: `3600000` is one hour and `86400000` one day. Set explicit UTC windows and bounded result sizes. Narrow order-book requests by asset/pair and source before calling; a broad request can return megabytes. Source notes about defaults and coverage are historical observations, not guarantees of today's response.

For market-cap enrichment, a returned pair's base code is not an asset LID. Reference-data enrichment requires a separately available connection. Report price basis, venue/source, units and actual observation times; keep missing coverage distinct from a zero value.
