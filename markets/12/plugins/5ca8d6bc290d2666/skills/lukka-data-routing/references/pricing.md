# Lukka-Pricing - 20 Production Tools

All tools exposed as `pricing___<tool>`.

> **Analytics tools** (implied rates, volatility surface, OTC FX) are on a separate server: `Lukka-Analytics`. See [analytics.md](analytics.md).

## Sources (5 tools)

| Tool | Use when |
|------|----------|
| `pricing___list_pricing_sources` | Discover exchange IDs. Call first when unsure of sourceId |
| `pricing___get_source_details` | Pairs / details for a specific source |
| `pricing___list_sources_by_product` | Sources by product. Param is `productType` (string enum): `prices`, `trades`, `candles`, `mvwaps`, `market-caps`, `variances`. NOT `product`, and NOT values like `derivatives`/`indices`. |
| `pricing___get_source_details_by_product` | Source details filtered by product + optional asset filter |
| `pricing___get_derivative_source_details` | Derivative exchange details (futures, options, perpetuals). Use for derivative identifier matching (client-side string match against the source details) |

## Prices (7 tools)

| Tool | Use when | Key params |
|------|----------|-----------|
| `pricing___get_latest_prices` | Current price | `sourceId` (REQUIRED integer: 1000=EOD, 2000=Realtime, 4xxx=exchange), `pairCodes`. Use integer sourceId (1000/2000/4xxx) directly. |
| `pricing___get_latest_index_prices` | Reference rate - **available with Lukka Reference Rate access; standard path: sourceId 1000 (EOD) / 2000 (Intraday)** | `sourceId`, `pairCodes` |
| `pricing___get_historical_prices` | Price over time range | `pairCode`, `from`, `to`, `interval` (ms) |
| `pricing___get_historical_index_prices` | Index prices over time | `sourceId`, `pairCode`, `from`, `to` |
| `pricing___get_candles` | OHLCV candles (supports hourly) | `sourceId` (REQUIRED integer, default 4002 Coinbase Pro), `pairCode` (required), `from`, `to`, `interval` |
| `pricing___get_market_variances` | Per-exchange variance | `pairCode`, `sourceId` |
| `pricing___get_vwap` | Volume-weighted price | `pairCode`, `sourceIds`, `from`, `to` (max 7 days) |

### Intervals (ms)

Both `get_historical_prices` and `get_candles` accept the **full interval set in MILLISECONDS**: `1000`, `5000`, `30000`, `60000`, `300000`, `1800000`, `3600000`, `86400000` (1s .. 1day). Default `60000` (1min).

- **Hourly (`3600000`) works directly on `get_historical_prices`** - no need to switch to `get_candles`.
- Reference Rate sources (`5001` / `5002`) support only `3600000` and `86400000`.

## Market Cap (2 tools)

| Tool | Use when | Notes |
|------|----------|-------|
| `pricing___get_market_capitalization` | Market cap (history/snapshot) for ONE pair | Param is `pairCode` (BASE-USD), NOT `assetCodes`. `from`/`to`/`limit`/`order`. **Data is minute-by-minute (Lukka Prime methodology) - there is NO daily-aggregation param, so `limit:7` returns 7 MINUTES, not 7 days.** For N daily points, page over a wider `from`/`to` window and subsample one row per day. For top-N multi-asset snapshot use `get_latest_market_caps`. |
| `pricing___get_latest_market_caps` | Top N market caps | Pass `order:"DESC"` explicitly for "top N" queries (highest cap first). **Returns ONLY `pairCode`, `marketCap`, `circulatingSupply`, `totalSupply`, `rank`, `ts` - NO `assetLid` / `assetCode`.** To enrich rows with LID / sector / LCAS / flags, resolve each separately: the pair BASE is the Lukka asset code (`USDSKY-USD` -> `lukkaAssetCode:"USDSKY"`), so call `get_asset_mappings(lukkaAssetCode: "{base}", mappingStatus:"Active", limit:1)` -> `lukkaAssetId`, then `get_asset_by_id` / `get_sectors` / `get_core_asset_scores`. |

## Market / Depth / Trades (4 tools)

| Tool | Use when | Notes |
|------|----------|-------|
| `pricing___get_latest_markets` | Market rollup for spot/derivatives | `marketType` (SPOT/DERIVATIVE), `sourceIds` |
| `pricing___get_market_depth` | Order-book depth | **Accepts comma-separated `sourceIds` (e.g. `"4001,4002"`) - returns one record per source.** Always pass `baseAssetCodes` + `counterAssetCodes` to filter - omitting returns a 6.8 MB exchange dump. |
| `pricing___get_order_book_snapshot` | Best bid/ask point-in-time | `sourceIds`, `pairCodes`, `asOf` |
| `pricing___get_spot_trades` | Raw trade prints | `sourceId`, `pairCode`, `from`, `to` (max 3600 records) |

## Derivatives (2 tools)

| Tool | Use when | Notes |
|------|----------|-------|
| `pricing___get_latest_derivative_trades` | Latest futures/options/perp trades | `lookback` is in **MINUTES** (default 1440 = 24h), NOT milliseconds |
| `pricing___get_historical_derivative_trades` | Historical derivative trades | |

## Source ID catalog

### Fixed high-level sources

| sourceId | Name | Notes |
|---|---|---|
| 1000 | Lukka Prime EOD | Canonical end-of-day benchmark (also market cap) |
| 2000 | Intraday | Realtime current-price workflow |
| 2100 | Prime Global Intraday | Newer intraday coverage |
| 3000 | Hourly | Hourly aggregate prices |
| 5001 | Reference Rate | **Available with Lukka Reference Rate access - request at https://lukka.tech/plugin. Standard path: sourceId 1000 (EOD) / 2000 (Intraday).** |
| 5002 | Median Reference Rate | **Available with Lukka Reference Rate access - request at https://lukka.tech/plugin. Standard path: sourceId 1000 (EOD) / 2000 (Intraday).** |
| 5004 | Staking Rates | |
| 5005 | MVWAP | Multi-source VWAP |

### Client-assigned sources

Assigned per client - **do NOT guess these, discover via `list_pricing_sources`**:

| Range | Type | Notes |
|---|---|---|
| 4001-4999 | Exchanges | Per-exchange prices/candles/trades/depth (e.g. Kraken 4001, Coinbase Pro 4002, Binance 4005) |
| 6xxx | Index | Digital asset index prices - use with `get_latest_index_prices` / `get_historical_index_prices` |
| 10xxx | Custom | Client-specific custom pricing sources |

### Reference rates vs implied rates (IMPORTANT)

Lukka-Pricing exposes **reference rates** (sourceIds 5001, 5002) via `get_latest_index_prices` / `get_historical_index_prices`. These are **not the same** as implied forward rates. In the current hosted deployment:

- `get_latest_index_prices(sourceId: 5001)` requires Lukka Reference Rate access - request at https://lukka.tech/plugin. Standard path: `get_latest_prices(sourceId: 2000)` (Intraday) or `sourceId: 1000` (EOD).
- **Implied forward rates**, **volatility surface**, **OTC FX** are on the **Lukka-Analytics** server (`analytics___*`). See [analytics.md](analytics.md).

## Default Source IDs

| Tool | Default | Required? |
|------|---------|----------|
| `get_candles` | 4002 (Coinbase Pro) | yes |
| `get_latest_index_prices` | 3000 | yes (sourceId) |
| `get_market_variances` | 1000 | yes |
| `get_market_depth` | **no default - explicit sourceId required** | yes |

## Cursor Pagination

`get_historical_prices`, `get_candles`, `get_vwap`, `get_spot_trades`, `get_market_capitalization`, `get_latest_market_caps`, `get_latest_derivative_trades` return `nextCursor` + `hasMore`. Pass `cursor` to continue.

## Quick Examples

```
# Current BTC price (sourceId required - 2000 = Lukka Prime Intraday)
pricing___get_latest_prices({
  sourceId: 2000,
  pairCodes: "XBT-USD"
})

# Top 20 by market cap
pricing___get_latest_market_caps({
  limit: 20,
  order: "DESC"
})

# ETH daily candles (sourceId required - 4002 = Coinbase Pro)
pricing___get_candles({
  sourceId: 4002,
  pairCode: "ETH-USD",
  from: "2026-04-01T00:00:00Z",
  to: "2026-04-30T23:59:59Z",
  interval: 86400000
})

# Filtered order-book depth (avoid 6.8 MB dump)
pricing___get_market_depth({
  sourceIds: "4001",
  baseAssetCodes: "SOLN",
  counterAssetCodes: "USD"
})
```
