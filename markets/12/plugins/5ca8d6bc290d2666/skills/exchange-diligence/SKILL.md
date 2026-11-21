---
name: exchange-diligence
description: "Exchange compliance profile with jurisdiction, VASP status, and services"
---

## OpenAI connection notes

Tool identifiers below are raw operation names. The host may add a namespace;
use the matching advertised Global MCP tool. Resolve `<resolved-package-root>`
to this plugin's installed directory before using paths. Workflow names identify
packaged skills; they are not literal Claude slash commands.

Original procedure tool scope: `refdata___get_asset_by_id`, `refdata___get_asset_mappings`, `refdata___get_entity_by_code`, `refdata___list_vasps`.

# exchange-diligence workflow

> See [CONNECTORS.md](../../CONNECTORS.md) for tool details.

## Usage

exchange-diligence workflow <user input>

### Canonical codes (IMPORTANT)

Do **not** pass free-form names. `COINBASE` is not a canonical code and does not resolve to the exchange. Use canonical Lukka codes:

| Venue | Code |
|-------|------|
| Coinbase Pro | `CPRO` |
| Coinbase (parent) | `CBSE` |
| Coinbase Prime | `CPRM` |
| Kraken | `KRAK` |
| Binance | `BINA` |
| Binance US | `BIUS` |
| Gemini | `GMNI` |
| Bitstamp | `BSTP` |
| OKX | `OKX` |

If the user types a free-form name, translate it to the code above before calling.

## Flow

> **NOTE:** This command builds the exchange profile from entity + VASP + asset-mapping data.

1. **Entity info**: `refdata___get_entity_by_code({ code: "<user input>" })` 
2. **VASP data**: `refdata___list_vasps({ limit: 100 })`  -> find the row where `lukkaEntityCode` == `<user input>`. VASPs are NOT filterable by `entityCode` (it only bridges to mappings, not VASPs) - filter client-side on `lukkaEntityCode`; paginate via `offset` if not on the first page.
3. **Asset listings + services**: `refdata___get_asset_mappings({ entityCode: "<user input>", mappingStatus: "Active", limit: 100 })` 
   - Count active listings
   - Aggregate `supportedFunctionList` across all mappings: for each flag (`tradingSupported`, `custodySupported`, `lendingSupported`, `savingsSupported`, `stakingSupported`), set to "yes" if *any* mapping has it `true`

### Optional: `--flag-risky` mode (expensive - user must explicitly request)

4. **Flag risky assets**: iterate mappings from step 3 and per row call `refdata___get_asset_by_id({ assetLid: "{lukkaAssetId}" })`  to inspect `assetDetails.potentiallySuspicious` / `potentiallyMemeCoin` flags.
   - Do NOT run by default (100+ calls for large exchanges)

## Output

### Exchange Due Diligence: {exchange_name}

**Entity Profile**
- Code: {entityCode}
- Type: {entityType}
- Country: {country}
- Status: {status}

**Regulatory**
- Jurisdiction: {jurisdiction} (primary; subsidiaries not enumerated)
- AML/KYC Process: {amlKycProcess}
- VASP Registration: {status from list_vasps} or "N/A" if no VASP registration found
- Note: Regulatory registrations per jurisdiction are provided via `list_vasps` (match `lukkaEntityCode` client-side).

**Services** (aggregated from `supportedFunctionList` across all active mappings)
- Spot trading: {yes/no}
- Derivatives: {yes/no}
- Lending: {yes/no}
- Staking: {yes/no}
- Custody: {yes/no}
- Savings: {yes/no}
- Note: based on supported asset function flags aggregated across listings

**Asset Coverage**
- Active listings: {count} (from step 3 `get_asset_mappings`)

> Suspicious/meme coin counts are not resolved by default (requires N individual asset lookups). Use `--flag-risky` to iterate all mappings and check `potentiallySuspicious` / `potentiallyMemeCoin` flags.

**Risk Flags**
- {flag descriptions from entity/VASP data}
