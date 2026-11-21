# MCP Tool Reference for Asset Resolution

All tools use the hosted Lukka production wire format: `<group>___<tool>`. Name lookups resolve through RefData mappings: alias map + `get_asset_mappings(entityAssetCode)` + `get_asset_by_id` (see parent SKILL.md).

## Primary Lookup: Lukka-RefData

### get_asset_mappings - search by street ticker

The input is a **street ticker**, not a `lukkaAssetCode`. On collisions Lukka keeps the bare code on the oldest (often inactive) asset and suffixes the rest, so `lukkaAssetCode:"TKN"` returns the older migrated asset, never the current one. Search by `entityAssetCode` (the exchange/blockchain-side ticker):

```
refdata___get_asset_mappings({
  entityAssetCode: "TKN",
  mappingStatus: "Active",
  limit: 200
})
```

Collect the **distinct `lukkaAssetId` values** - one real asset spans many mapping rows (a multi-chain fund can have 10+ chain mappings).

For an aliased major (BTC->XBT, GALA->GALAT3) the canonical code is unique, so `lukkaAssetCode:"{alias}"` is safe and skips the ticker search.

Caveats:
- `whitepaperCode` / `commonStreetCode` are **not filterable** here - confirm via `get_asset_by_id` -> `nameDetails[]` after you have the LID
- `mappingStatus:"Active"` does NOT drop inactive assets - the mapping is active even when the asset is `Contract Migrated`

### list_assets

`list_assets` filters by `lukkaAssetIds` (comma-separated LIDs) / `assetGroupId` / `expandDetails` / `limit`/`offset`. Code resolution goes through `get_asset_mappings(entityAssetCode)` then `get_asset_by_id`. All list values MUST be wrapped in square brackets (`[LA1,LA2]`, `[ALL]`) or the API returns 500; with brackets, multi-id + `expandDetails:[ALL]` works correctly.

### get_asset_by_id - validate each distinct candidate

```
refdata___get_asset_by_id({ assetLid: "LA0EXAMPLE0" })
```

Key fields:
- `statusDetails[].assetStatus` - must be `Active` (reject `Inactive`)
- `statusDetails[].assetSubstatus` - reject `Contract Migrated` (removes inactive legacy holders of a bare ticker)
- `assetGroupDetails[].assetGroupList` - if present, collapse to the `isPrimaryAsset: true` LID
- `successorDetails[].successorLukkaId` - replacement LID if migrated
- `nameDetails[].whitepaperCode` / `commonStreetCode` - confirms the original ticker matches user input

### get_sectors

LDACS 5-tier classification.

```
refdata___get_sectors({ assetLid: "LA8OQ23Y4U4" })
```

Returns: Category > Super Sector > Macro Sector > Mid Sector > Sub Sector.

## Pricing Tools: Lukka-Pricing

### get_latest_prices

```
pricing___get_latest_prices({
  sourceId: 1000,
  pairCodes: "GALAT3-USD"
})
```

Source IDs:
- `1000` - Lukka Prime End of Day (preferred)
- `2000` - Lukka Prime Intraday (fallback)

If pair returns empty with `sourceId: 1000`, try `sourceId: 2000` before declaring UNRESOLVED. Use integer sourceId (1000/2000/4xxx) directly.

### get_historical_prices

```
pricing___get_historical_prices({
  sourceId: 1000,
  pairCode: "GALAT3-USD",
  from: "2025-01-15T00:00:00Z",
  to: "2025-01-15T23:59:59Z",
  interval: 86400000
})
```

**CRITICAL**: Interval in MILLISECONDS. 1 day = `86400000` (NOT `86400`).

## Ticker Collision Resolution Flow

When a street ticker maps to multiple assets (the common, dangerous case):

```
1. Not in alias map -> treat input as raw street ticker.
2. get_asset_mappings({ entityAssetCode: "TKN", mappingStatus: "Active", limit: 200 })
3. Collect distinct lukkaAssetId values from the rows.
4. get_asset_by_id on each:
   - drop Inactive / Contract Migrated  (the older inactive asset is filtered out here)
   - collapse chain-variants to the group isPrimaryAsset:true LID
5. One active group survives -> resolve it.
   More than one -> PROMPT for disambiguation (large fund vs same-ticker token on another chain vs an unrelated same-ticker token). Never auto-pick.
6. If the resolved asset is itself Contract Migrated, follow successorDetails and repeat.
```

Aliased-major flow (no collision): `GALA -> GALAT3`, query `lukkaAssetCode:"GALAT3"` directly, single active candidate, done.

## Verified Mappings

| White Paper | Lukka Code | Asset LID | Pair Code | Mappings | Trap |
|---|---|---|---|---|---|
| BTC | XBT | LA6EV2NKQ95 | XBT-USD | 100+ | ISO 4217 |
| ETH | ETH | LA8VRAGEMT1 | ETH-USD | 23,895 | Straightforward |
| SOL | SOLN | LA1DB6PX4M7 | SOLN-USD | 295 | NOT "SOL", name lookups return unrelated same-ticker ERC-20 tokens |
| GALA | GALAT3 | LA8OQ23Y4U4 | GALAT3-USD | 103 | Contract migrated from GALAG |
| ADA | ADA | LA7SQV7F4A4 | ADA-USD | - | Straightforward |
| USDT | USDT | - | USDT-USD | - | Multiple chains |
| USDC | USDC | - | USDC-USD | - | Multiple chains |

## Anti-Patterns

1. **Do NOT** resolve a raw street ticker via `lukkaAssetCode` - on collisions the bare code is the oldest (often inactive) asset. Use `entityAssetCode`.
2. **Do NOT** call `list_assets({ assetCode: ... })` - `list_assets` filters by `lukkaAssetIds` / `assetGroupId`; code resolution goes through `get_asset_mappings`.
3. **Do NOT** auto-pick the highest-mapping candidate on a collided ticker - prompt for disambiguation.
4. **Do NOT** trust `mappingStatus:"Active"` to drop inactive assets - validate `assetStatus`/`assetSubstatus` at the asset level.
5. **Do NOT** hardcode asset codes - tokens migrate, always verify via the workflow.
6. **Do NOT** pass intervals in seconds - always milliseconds.
7. **Name lookups** resolve through RefData mappings: alias map + `entityAssetCode` lookup.
8. **Do NOT** filter mappings by `whitepaperCode`/`commonStreetCode` - not supported; confirm via `get_asset_by_id` -> `nameDetails[]`.
