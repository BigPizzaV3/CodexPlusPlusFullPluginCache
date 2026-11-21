---
name: asset-activity
description: "Activity-focused asset report with trends, volume, and recent events"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `pricing___get_candles`, `pricing___get_latest_market_caps`, `pricing___get_market_capitalization`, `pricing___get_market_depth`, `pricing___get_vwap`, `refdata___get_asset_by_id`, `refdata___get_asset_crypto_actions`, `refdata___get_asset_mappings`.

# asset-activity workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

asset-activity workflow <user input>

## Flow

1. **Resolve code -> assetLid**: `refdata___get_asset_mappings({ lukkaAssetCode: "<user input>", mappingStatus: "Active", limit: 5 })`  -> take `lukkaAssetId` from first row
   - Name lookups resolve through RefData mappings; translate free-form names to canonical codes first; `list_assets` filters by `lukkaAssetIds` / `assetGroupId`, code resolution goes through `get_asset_mappings`
2. **Metadata**: `refdata___get_asset_by_id({ assetLid })` 
3. **Price trend**: `pricing___get_candles({ sourceId: 4002, pairCode: "{code}-USD", interval: 86400000, from: 30d_ago, to: now })`  (sourceId 4002 = Coinbase Pro, schema default)
   - 30d change % = `(last_close - first_open) / first_open * 100`
4. **VWAP (7d)**: `pricing___get_vwap({ pairCode: "{code}-USD", sourceIds: top_exchange_ids, from: 7d_ago, to: now })` 
   - max 7-day range per call
5. **Market cap + rank**:
   - `pricing___get_market_capitalization({ pairCode: "{code}-USD", limit: 1 })`  -> USD cap. Takes single `pairCode` (BASE-USD), NOT `assetCodes`.
   - `pricing___get_latest_market_caps({ limit: 100, order: "DESC" })`  -> find position of `{code}` in list; if not present, rank is "100+"
6. **Liquidity** (deterministic exchange selection: top 5 from `get_pair_mappings` where exchange is in {KRAK, CPRO, BINA, BFNX, GMNI}):
   Per exchange: `pricing___get_market_depth({ sourceIds: "{single}", baseAssetCodes: "{code}", counterAssetCodes: "USD" })` 
7. **Exchange coverage**: `refdata___get_asset_mappings({ lukkaAssetCode: "{code}", mappingStatus: "Active" })` 
8. **Recent events**: `refdata___get_asset_crypto_actions({ assetLid: "{LID}", domain: "assets" })`  - takes `assetLid` (LA-code), NOT `assetCode`; `domain` required.

## Output

### Activity Report: {asset_name} ({code})

**Price Trend (30d)**
- Current: ${price}
- 30d high: ${high}
- 30d low: ${low}
- 30d change: {pct}%

**Volume (7d)**
- 7d avg daily: ${vol}
- 7d VWAP: ${vwap}
- VWAP deviation: {bps} bps

**Market Cap**: ${cap} (rank #{rank})

**Liquidity Snapshot**
| Exchange | Bid Depth | Ask Depth | Spread |
|----------|-----------|-----------|--------|

**Exchange Coverage**: {count} active listings

**Recent Events**
| Date | Event | Description |
|------|-------|-------------|
