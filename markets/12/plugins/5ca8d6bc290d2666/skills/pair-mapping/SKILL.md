---
name: pair-mapping
description: "Resolve exchange pair codes to Lukka canonical pairs, or find how a Lukka pair is named across exchanges"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `refdata___get_pair_mappings`, `refdata___list_entities`.

# pair-mapping workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

pair-mapping workflow <user input>

Parse <user input> - can be:
- A Lukka pair code: `XBT-USD`
- An exchange-specific pair code: `BTC/USDT`, `XBTUSD`
- An exchange name/code + pair: `KRAK XBT/USD`
- An exchange code only: `KRAK` (returns all pairs for that exchange)

Use canonical Lukka codes (`CPRO`, `KRAK`, `BINA`, ...) - never `COINBASE`.

## Personas

- **FX & Stablecoin Settlement**: Normalize obscure pairs (e.g. USDT/UAHG) for PnL and fiat on/off-ramp reconciliation
- **Regulatory & Tax Reporting**: Translate every exchange pair into standard base/quote for capital gains and jurisdictional reporting

## Flow

### Case A: Resolve exchange pair -> Lukka canonical

1. If a free-form exchange name is given, resolve to entityCode via `refdata___list_entities({ })` 
2. `refdata___get_pair_mappings({ entityPairCode: "{code}", entityCode: "{code}", mappingStatus: "Active", })` 
3. Returns: `lukkaPairCode`, `lukkaAssetOneCode` (base), `lukkaAssetTwoCode` (counter), direction

### Case B: All exchange names for a Lukka pair

1. `refdata___get_pair_mappings({ lukkaPairCode: "XBT-USD", mappingStatus: "Active", limit: 1000 })` 
2. Returns all entity-specific codes for that pair
   - **`lukkaPairCode` is the Lukka identifier; `entityPairCode` is the exchange-side code** (e.g. Lukka `XBT-USD` == Binance `BTCUSD`). To confirm a specific exchange, pin `entityCode` too - do NOT conclude "not mapped" from a partial `lukkaPairCode`-only page (80+ venues on a flagship pair; page until `next` is null).

### Case C: All pairs for an exchange

1. `refdata___get_pair_mappings({ entityCode: "{KRAK}", mappingStatus: "Active", limit: 1000 })` 

### Supplemental search

When the exact code is unknown, page through `get_pair_mappings({ entityCode: "{code}", mappingStatus: "Active", limit: 1000 })`  and filter client-side on the `entityPairCode` substring.

## Output

### Pair Mapping: {input}

**Canonical Lukka Pair**: {lukkaPairCode}
- Base asset: {lukkaAssetOneCode} ({assetName})
- Counter asset: {lukkaAssetTwoCode} ({assetName})

**Exchange Names** ({count} active mappings)
| Exchange | Pair Code | Direction | Status |
|----------|-----------|-----------|--------|
| Kraken | XBT/USD | Standard | Active |
| Binance | BTCUSDT | Reversed | Active |

- Direction vocabulary: "Standard" = exchange base/counter matches Lukka pair order. "Reversed" = exchange pair is inverted relative to Lukka canonical. "Ambiguous" = cannot determine (rare, flag for review).

**Notes**: {any reversed pairs, deprecated codes, or ambiguous mappings}
- "Ambiguous" heuristic: when `lukkaAssetOneCode` and `lukkaAssetTwoCode` are both digital assets (no fiat counter), direction is determined by `pairDirection` field. If absent, mark as "Ambiguous".
