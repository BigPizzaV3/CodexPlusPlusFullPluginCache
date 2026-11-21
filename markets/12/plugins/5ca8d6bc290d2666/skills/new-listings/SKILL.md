---
name: new-listings
description: "Monitor new exchange listings since a given date"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `pricing___get_latest_prices`, `refdata___get_asset_by_id`, `refdata___get_asset_mappings`.

# new-listings workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

new-listings workflow <user input>

Parse <user input> for exchange code (use canonical Lukka codes: `CPRO`, `KRAK`, `BINA`, `GMNI`, etc. - never `COINBASE`) and optional `since` date (default: 7 days ago).

## Flow

1. **Recent mappings**: `refdata___get_asset_mappings({ entityCode: "{code}", mapProcessedStartTime: "{since}T00:00:00Z", mappingStatus: "Active", limit: 100 })` 
2. **Per new listing**: take `lukkaAssetId` from the mapping row, then `refdata___get_asset_by_id({ assetLid: "{lukkaAssetId}" })`  for metadata (`list_assets` filters by `lukkaAssetIds` / `assetGroupId`; code resolution goes through `get_asset_mappings`)
3. **Prices**: `pricing___get_latest_prices({ sourceId: 2000, pairCodes: "{code}-USD" })`  for each (sourceId 2000 = Lukka Prime Intraday)
   - If price returns empty/404 for a fresh listing, display "not yet indexed" instead of blank

## Output

### New Listings on {exchange} since {date}

Found **{count}** new listings.

| # | Asset Code | Asset Name | Blockchain | First Active | Price (USD) |
|---|-----------|------------|------------|--------------|-------------|

- First Active = `mapEffectiveStartTime` (when trading actually began); falls back to `mapProcessedStartTime` (when Lukka recorded) if effective is null
- Source shown in parentheses: "(effective)" or "(processed)"

**Summary**: {count} new assets listed. {highlights}.
