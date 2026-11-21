---
name: investigate-price
description: "Deep price investigation at specific timestamp with exchange breakdown"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `UDA___get_block`, `pricing___get_candles`, `pricing___get_historical_prices`, `pricing___get_latest_prices`, `pricing___get_market_depth`, `pricing___get_market_variances`, `pricing___get_order_book_snapshot`, `pricing___list_pricing_sources`.

# investigate-price workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

investigate-price workflow <user input>

Parse <user input> for pair code and optional timestamp (default: latest).

## Flow

1. **Discover sources**: `pricing___list_pricing_sources({})` 
2. **Price at time**: `pricing___get_latest_prices({ sourceId: 1000, pairCodes: "{pair}", asOf: "{timestamp}" })` or `pricing___get_historical_prices({ pairCode: "{pair}", from, to, interval: 60000 })`  (sourceId 1000 = Lukka Prime EOD)
   - Note: price returned is the latest available *on or before* `asOf`. For exact minute-precision use `get_historical_prices({ interval: 60000 })`.
3. **Exchange variance**: `pricing___get_market_variances({ pairCode: "{pair}", from: "{ts-1h}", to: "{ts}" })` 
   - Provides per-exchange deviation from composite
4. **Candles per exchange**: For top exchanges, `pricing___get_candles({ pairCode: "{pair}", sourceId: {id}, from: "{ts-2h}", to: "{ts}", interval: 3600000 })` 
   - Provides per-exchange volume
   - **Merge step 3 + step 4** on `pairCode + sourceId`: variance fills Deviation column, candle fills Volume column
5. **Order book snapshot**: `pricing___get_order_book_snapshot({ sourceIds: "{single_sourceId}", pairCodes: "{pair}", asOf: "{timestamp}" })` 
   - Top exchange sourceId (e.g. 4002 Coinbase Pro or 4005 Binance), one at a time
6. **Market depth per top exchange**: `pricing___get_market_depth({ sourceIds: "{single_sourceId}", baseAssetCodes: "{base}", counterAssetCodes: "USD" })` 
   - **CRITICAL**: one sourceId per call + base/counter filters (avoids 6.8 MB full exchange dump)

## Output

### Price Investigation: {pair} at {timestamp}

**Lukka Prime Price**: ${price}

**Exchange Contributions**
| Exchange | Price | Share % | Volume | Deviation |
|----------|-------|---------|--------|-----------|

- Share % = `volume_exchange / total_volume_across_exchanges * 100` (computed from candles volume)

**Hourly Candles (leading 2h)**
| Time | Exchange | Open | High | Low | Close | Volume |
|------|----------|------|------|-----|-------|--------|

**Order Book Snapshot**
- Best Bid: ${bid} ({bid_size})
- Best Ask: ${ask} ({ask_size})
- Spread: ${spread} ({spread_bps} bps)

**Analysis**: {Describe deviation pattern, liquidity concentration, any outliers across exchanges}

> **Block-level analysis**: if the user wants on-chain context around the timestamp, use `UDA___get_block` and the `large-data-processing` skill's `process_block.py`.
