# Lukka-RefData - 20 Production Tools

All tools exposed as `refdata___<tool>`. Global MCP does not advertise the legacy `detailed` argument; use its advertised pagination parameters. Pagination: `offset`/`limit` (default 100).

## Assets (6 tools)

| Tool | Notes |
|------|-------|
| `refdata___list_assets` | **No `assetCode` filter.** Supported filters: `lukkaAssetIds` (comma-separated LIDs), `assetGroupId`, `expandDetails`, `limit`/`offset`. To resolve a street ticker -> LID, use `get_asset_mappings(entityAssetCode)` first (NOT `lukkaAssetCode` - see Ticker resolution below). All list values MUST be wrapped in square brackets (`[LA1,LA2]`, `[ALL]`) or the API returns 500; multi-id + `expandDetails:[ALL]` together works fine with brackets. |
| `refdata___get_asset_by_id` | Single asset by Lukka ID |
| `refdata___get_asset_exposure` | Asset exposure data. Filter: `assetCode` |
| `refdata___get_asset_crypto_actions` | Per-asset crypto actions. Params: `assetLid` (LA-code, NOT `assetCode`) + `domain` required (assets/derivatives/assetMappings/pairMappings) |
| `refdata___get_crypto_actions` | Global crypto actions feed |
| `refdata___get_reference_assets` | Reference asset list |

## Classifications (4 tools)

| Tool | Notes |
|------|-------|
| `refdata___get_sectors` | Sector taxonomy (super/macro/mid/sub) |
| `refdata___get_core_asset_scores` | LCAS scores. **Requires both `fromDate` + `toDate`** - returns empty without them |
| `refdata___get_market_scores` | Market quality scores |
| `refdata___get_enums` | Valid enum values by name |

## Entities (2 tools)

| Tool | Notes |
|------|-------|
| `refdata___list_entities` | 3000+ entities - paginate. **Field naming (per API spec, NOT a bug):** `entityTypeCode` holds the human-readable label (e.g. `"Exchange"`, `"Prime Broker"`, `"OTC Desk"`), `entityType` holds the short code (e.g. `"XCHNG"`, `"PBKR"`, `"OTC"`). Read them by name, do not assume Code=short/Type=label |
| `refdata___get_entity_by_code` | **`COINBASE` is not a canonical code** and does not resolve to the exchange. Use `CPRO` (Coinbase Pro), `CBSE`, `CPRM` (Coinbase Prime) instead |

### Known exchange codes (canonical)

| Venue | Code |
|-------|------|
| Coinbase Pro (retail exchange) | `CPRO` |
| Coinbase (parent entity) | `CBSE` |
| Coinbase Prime (institutional) | `CPRM` |
| Kraken | `KRAK` |
| Binance (Cayman) | `BINA` |
| Binance US | `BIUS` |
| Gemini | `GMNI` |
| Bitstamp | `BSTP` |
| OKX | `OKX` |

## Mappings (2 tools)

| Tool | Notes |
|------|-------|
| `refdata___get_asset_mappings` | How assets are named across exchanges. Filters: `entityCode`, `entityAssetCode` (street ticker), `lukkaAssetCode`, `lukkaAssetId`, `mappingStatus`. `whitepaperCode`/`commonStreetCode` are NOT filterable. **Resolve a street ticker via `entityAssetCode`, not `lukkaAssetCode`** - see below. |
| `refdata___get_legal_entity_mappings` | Legal entity mappings |

### Street ticker resolution (collision-safe)

User input is a **street ticker**, NOT a `lukkaAssetCode`. On collisions Lukka keeps the bare code on the oldest asset and suffixes the rest, so `lukkaAssetCode:"TKN"` returns the older migrated asset (status Inactive / Contract Migrated), never the current one (`TKN01`/`TKNA1C`). Resolve like this:

1. `get_asset_mappings({ entityAssetCode: "{ticker}", mappingStatus: "Active", limit: 200 })` -> distinct `lukkaAssetId` values
2. `get_asset_by_id` per LID -> drop `Inactive`/`Contract Migrated`; collapse chain-variants to the group `isPrimaryAsset: true` LID
3. One active group -> resolve. More than one -> prompt for disambiguation (never auto-pick)

Aliased majors (BTC->XBT, GALA->GALAT3) are unique - query `lukkaAssetCode` directly. See the **asset-resolver** skill for the full workflow.

## Markets (1 tool)

| Tool | Notes |
|------|-------|
| `refdata___list_vasps` | Virtual Asset Service Providers. **VASPs are NOT filterable by `entityCode`** - entityCode only bridges to asset/pair mappings, not VASPs (not in the schema). Query `limit`/`offset`/`vasp_id`/`vaspLids`; the response carries `lukkaEntityCode` per row, so filter client-side on that if you need a specific exchange. |

## Pairs (2 tools)

| Tool | Notes |
|------|-------|
| `refdata___get_reference_pairs` | Reference trading pairs |
| `refdata___get_pair_mappings` | Pair naming across exchanges. Filter: `lukkaPairCode`, `entityCode`, `entityPairCode`, `mappingStatus`. **To check whether a SPECIFIC exchange maps a pair, always add `entityCode` - never conclude "not mapped" from a `lukkaPairCode`-only page** (a popular pair returns many exchanges across pages; a default `limit:100` can omit the one you want). E.g. BINA XBT-USD IS mapped (entityPairCode `BTCUSD`), but a `lukkaPairCode:XBT-USD` page without `entityCode` may not surface it. |

### get_pair_mappings use cases

- Exchange pair -> Lukka: `entityPairCode: "BTC/USD", entityCode: "KRAK"`
- All exchange names for Lukka pair: `lukkaPairCode: "XBT-USD", mappingStatus: "Active", limit: 1000` (a flagship pair has 80+ venues - page fully or you will miss exchanges)
- **Does exchange X map this pair?** ALWAYS pin both: `lukkaPairCode: "XBT-USD", entityCode: "BINA", mappingStatus: "Active"`. Do NOT infer absence from an unfiltered page - an unfiltered page may omit the exchange you are looking for.
- All pairs for exchange: `entityCode: "BINA", mappingStatus: "Active", limit: 1000`

## Derivatives (3 tools)

| Tool | Notes |
|------|-------|
| `refdata___list_derivatives` | List. Filter: `status` (active/inactive/expired) |
| `refdata___get_derivative_by_id` | Single derivative |
| `refdata___get_reference_derivatives` | Reference derivatives |

## Quick Examples

```
# Find Bitcoin - XBT is an aliased major (unique canonical code), so lukkaAssetCode is safe here.
# For a RAW street ticker (e.g. a collided ticker) use entityAssetCode instead - see "Street ticker resolution".
refdata___get_asset_mappings({
  lukkaAssetCode: "XBT",
  mappingStatus: "Active",
  limit: 5
})
refdata___get_asset_by_id({
  assetLid: "LA6EV2NKQ95"
})

# Coinbase Pro entity details (NOT "COINBASE")
refdata___get_entity_by_code({ code: "CPRO" })

# Asset mappings for an exchange
refdata___get_asset_mappings({
  entityCode: "KRAK",
})

# LCAS score for XBT
refdata___get_core_asset_scores({
  assetLid: "LA6EV2NKQ95",
  fromDate: "2026-04-01T00:00:00Z",
  toDate: "2026-05-05T00:00:00Z"
})

# Pair mappings for XBT-USD
refdata___get_pair_mappings({
  lukkaPairCode: "XBT-USD",
  mappingStatus: "Active",
  limit: 100
})
```
