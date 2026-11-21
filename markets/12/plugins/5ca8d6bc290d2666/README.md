# Lukka Digital Assets Intel for ChatGPT and Codex

Access to Lukka's 7 products through the Global MCP server for digital asset professionals: pricing, reference data, analytics, AML/compliance, on-chain data, news intelligence, and prediction markets.

> The 13 commands and three agent procedures from the Claude edition are packaged as skills. Ask for the named workflow in ChatGPT or Codex.

## Who Is This For?

- **Traders**: Price investigation, liquidity analysis, new listing alerts, derivatives vs spot
- **Fund Managers**: Daily briefings, asset reports, market cap tracking
- **Compliance Officers**: AML reports (Scoring/Standard/Enhanced), exchange due diligence, wallet review
- **Research Analysts**: Asset deep dives, governance flags, activity trends
- **Data Ops / Middle Office**: Bulk asset resolution, exchange mapping, pair reconciliation

## Workflows (13)

| Command | Example | Description |
|---------|---------|-------------|
| `briefing workflow` | `briefing workflow` | Daily macro overview - top 20 market caps, realtime prices, 24h candles for top 5, prediction-market sentiment |
| `asset-report workflow` | `asset-report workflow XBT` | Asset deep dive: identity, LCAS, sectors, exchange coverage, Crypto Actions, price + cap |
| `asset-activity workflow` | `asset-activity workflow UNI` | Activity-focused: 30d price trend, 7d VWAP, market cap, liquidity snapshot, events |
| `new-listings workflow` | `new-listings workflow CPRO since:2026-04-01` | New exchange listings since a date (use canonical codes, not COINBASE) |
| `resolve-assets workflow` | `resolve-assets workflow BTC,ETH,SOL,GALA` | Bulk resolve white paper codes -> Lukka asset code (XBT, SOLN, GALAT3) + EOD price |
| `wallet-scan workflow` | `wallet-scan workflow 0xADDRESS eth` | Balance + tokens + 100-tx preview + AML Scoring report. Escalate to Standard / Enhanced with processor pipe. |
| `investigate-price workflow` | `investigate-price workflow XBT-USD 2026-05-01T12:00:00Z` | Price at timestamp: Lukka Prime, exchange contributions, hourly candles, order book snapshot, depth |
| `liquidity-scan workflow` | `liquidity-scan workflow SOLN-USD` | Cross-exchange liquidity: depth (base/counter filters; sourceIds comma-separated OK), spread, VWAP, 24h volume |
| `exchange-diligence workflow` | `exchange-diligence workflow CPRO` | Exchange profile: entity, licenses, VASP, listings, risk flags |
| `deriv-spot-compare workflow` | `deriv-spot-compare workflow XBT-USD` | Spot vs perpetual basis + 24h VWAP + implied forward curve + volatility surface (via Lukka-Analytics). |
| `pair-mapping workflow` | `pair-mapping workflow KRAK XBT/USD` | Resolve exchange pair codes to Lukka canonical pairs (Case A/B/C) |
| `news workflow` | `news workflow bitcoin --sentiment negative --days 3` | Digital asset news search with sentiment, category, and date filtering; daily summaries |
| `health workflow` | `health workflow` | Ping every hosted server + known-drift checks (COINBASE non-canonical, CPRO canonical, index-price availability). PASS / DEGRADED / FAIL verdict. |

## Skills

| Skill | Purpose |
|-------|---------|
| `lukka-data-routing` | Routes queries to correct MCP server/tool on first try (production wire names) |
| `asset-resolver` | White paper code -> Lukka asset code -> price |
| `digital-asset-market-knowledge` | Domain knowledge: pair formats, source IDs, intervals |
| `compliance-patterns` | AML workflow patterns for the hosted report surface |
| `large-data-processing` | Local Python processors for 300 KB - 6.8 MB MCP responses (including AML Standard/Enhanced reports) |

## Agent Procedures (Packaged as Skills)

| Agent | Purpose |
|-------|---------|
| `market-data-gatherer` | Parallel exchange data collection for liquidity/pricing |
| `compliance-scanner` | AML + VASP checks against the hosted report surface |
| `asset-discovery` | Cross-MCP asset resolution + enrichment |

## MCP Products (7)

| Server | Auth | Domain |
|--------|------|--------|
| Lukka-Pricing | OAuth 2.0 (Auth0) | Pricing, candles, VWAP, market cap, order book, derivative trades |
| Lukka-RefData | OAuth 2.0 (Auth0) | Assets, entities, mappings, sectors, VASPs |
| Lukka-AML | OAuth 2.0 (Auth0) | AML reports (scoring/standard/enhanced) |
| Lukka-UDA | OAuth 2.0 (Auth0) | On-chain balances, transactions, blocks |
| Lukka-Analytics | OAuth 2.0 (Auth0) | Implied rates, volatility surface, OTC FX |
| Lukka-News | OAuth 2.0 (Auth0) | Digital asset news search, daily summaries, sentiment, categories |
| Lukka-Predmar | OAuth 2.0 (Auth0) | Prediction markets (Polymarket, Kalshi, Gemini) |

**Credentials**: all 7 servers require Lukka credentials (OAuth 2.0 via Auth0) - full functionality needs a Lukka account. Connect `https://global.mcp.lukka.tech` through the host and sign in at `https://auth0.lukka.tech`. No Lukka account or keys yet? Request access at **https://lukka.tech/plugin**. For any setup or access problems, contact **plugin-support@lukka.global**.

See [CONNECTORS.md](CONNECTORS.md) for the full breakdown.

## Key Conventions

- **Pair format**: `XBT-USD` (not BTC-USD), `ETH-USD`, `SOLN-USD` (not SOL-USD)
- **Intervals**: Milliseconds. 1 day = `86400000`, 1 hour = `3600000`
- **Source IDs**: 1000=EOD, 2000=Realtime, 3000=Hourly, 5001/5002=Reference Rate (requires access), 4xxx=Exchanges
- **Blockchain case**: lowercase for Lukka-UDA (`eth`), UPPERCASE for Lukka-AML (`ETH`)
- **Exchange codes**: use canonical Lukka codes (`CPRO`, `CBSE`, `CPRM`, `KRAK`, `BINA`, `GMNI`). **Never** use `COINBASE` - it is not a canonical code and does not resolve to the exchange
- **Tool wire names**: `<group>___<tool>` (triple underscore before the tool name) - short names will not dispatch

## Legal and Compliance

- **[DISCLAIMER.md](DISCLAIMER.md)** -- Regulatory disclaimers, warranty, data accuracy
- **[TERMS.md](TERMS.md)** -- Acceptable use, restrictions, data flow, export control
- **[SECURITY.md](SECURITY.md)** -- Vulnerability disclosure, authentication (Auth0/CIMD), data handling

This plugin provides access to Lukka's market data and blockchain analytics
infrastructure. Output is for informational purposes only and does not
constitute financial, legal, or compliance advice. AML reports are not a
substitute for regulated sanctions screening, SAR filing, or KYC processes.

## Usage Notes (this surface)

| Topic | Guidance |
|-------|----------|
| Asset/pair search | Use `Lukka-RefData` direct filters: `list_assets`, `get_asset_mappings`, `get_pair_mappings` |
| Derivative matching | Use `get_derivative_source_details` + client-side string match |
| `generateAmlStandardReport` / `...Enhanced` | 300-500 KB+ responses - pipe through `process_aml_report.py` in `large-data-processing` |
| `get_address_transactions` with `limit:1000` | 150 KB+ - preview <= 100, bulk via `process_transactions.py` |
| `get_market_depth` | Filter with `sourceIds` (comma-separated OK, one record per source) + `baseAssetCodes` + `counterAssetCodes` |
| `get_latest_market_caps` ordering | Always pass `order:"DESC"` for top-N |
| `list_assets` multi-id + `expandDetails` | Use `expandDetails:"[ALL]"` (brackets required) |
| `get_latest_index_prices` / `get_historical_index_prices` | Available with Lukka Reference Rate access - request at https://lukka.tech/plugin. Standard path: `get_latest_prices({ sourceId: 2000 })` realtime or `{ sourceId: 1000 }` EOD |
| Lukka-News date params (`publishDateFrom`/`publishDateTo`) | Always full ISO 8601: `2026-04-01T00:00:00Z` |

## Wire Format Reference

All tool calls use the production wire format: `<group>___<tool>` (triple underscore before tool name).

**Lukka-AML** - Available tools: `generateAmlScoringReport` (light default), `generateAmlStandardReport` (full - mandatory processor pipe), `generateAmlEnhancedReport` (deepest - mandatory processor pipe). For counterparty exposure data, use the Standard/Enhanced reports.

**Lukka-UDA** - Wire names: `Get_newest_block_blockheight` (block height), `get_block` (block data), `Get_transaction_for_txhash` (decoded transaction), `get_address_balance`, `get_address_transactions`, `get_address_assets`.

**Lukka-Predmar** - Wire names: `GetPredictionMarkets` (search/details), `GetSimilarMarkets`, `GetPMCSstats`, `GetPredictionMarketsTaxonomy`, `GetMarketNews`, `GetMarketOverview`, `GetMarketRecap`, `GetOpenInterest`, `GetPredictionMarketTotalVolume`, `GetPriceHistory`, `GetExchanges`.

## Installation

See [INSTALL.md](INSTALL.md) for supported ChatGPT/Codex installation and a
Global MCP development connection. The public listing has not yet been completed.
Use a Lukka account with MCP access and the relevant product entitlements.

## Audit logging

The Claude lifecycle hook is omitted from this public OpenAI package.
It does not install the original local usage logger. Host and server logging
are separate from that plugin hook. See [SECURITY.md](SECURITY.md).

## Preferences

Optional user-local defaults live in `settings/preferences.local.md` (copy from `settings/preferences.local.md.example` and edit).

**Currently wired:** `Top N` is read by `briefing workflow` (default 20, max 50). The other keys in the example file (counter currency, AML depth, news lookback, output format) are **planned / not yet consumed by commands** - they are placeholders for future releases, not active settings.

## Validation

The OpenAI submission portal validates the package, skills and MCP tools.
See [submission preparation](docs/SUBMISSION.md). Successful local checks do
not establish a submitted or approved public listing.

## Troubleshooting

### Slash commands do not appear after install

Start a new conversation after installing the plugin and authenticate Global through the host's MCP connection settings.

### "ValidationException - Parameter validation failed"

Hosted MCP wrappers strictly validate parameter types. Most common drifts and fixes:

| Error says | Root cause | Fix |
|---|---|---|
| `Missing required field(s): 'sourceId'` | Call to `get_candles` / `get_latest_prices` / `get_order_book_snapshot` without `sourceId` | Add `sourceId: 1000` (EOD), `2000` (realtime), or `4002` (Coinbase Pro candles). Use `list_pricing_sources` to discover others. |
| `Field '/limit' has invalid type: string found, integer expected` | Pricing or refdata tool called with a quoted integer | Pass as native int literal: `limit: 20` not `"20"`. UDA transaction limits use integers; prediction-market input types follow the advertised schema. |
| `Missing required field(s): 'address_type'` | Legacy AML call with `blockchain: "ETH"` | Rename to `address_type: "ETH"`. |
| `Missing required field(s): 'primary_location', 'vasp_classification', 'vast_type'` | `GetExchanges` called with too few params | Pass all 5 required (empty strings OK): `{ limit: "5", offset: "0", primary_location: "", vasp_classification: "", vast_type: "" }`. |
| `Field '/sourceId' has invalid type: string found, integer expected` | Pricing integer fields passed as strings | Native int. `sourceId: 4022`, not `"4022"`. |

### "Address type 'external' is not supported yet"

`generateAmlScoringReport` rejects `address_type: "external"`. Use the blockchain code: `"ETH"`, `"BTC"`, `"SOL"`, `"TRX"`.

### `get_entity_by_code("COINBASE")` is not canonical

The literal code `COINBASE` is not a canonical Lukka code and does not resolve to the exchange (it returns an unrelated record). Always use canonical codes: `CPRO` (Coinbase Pro), `CBSE` (Coinbase parent), `CPRM` (Coinbase Prime).

### AML report response >300 KB / context overflow

`generateAmlStandardReport` and `generateAmlEnhancedReport` return 300-500+ KB. Pipe through the `large-data-processing` skill's `process_aml_report.py` - converts to ~1.5 KB summary with top risk factors + monitoring flags. `generateAmlScoringReport` is context-safe as-is.

### "Expecting property name enclosed in double quotes" when parsing a response

Hosted MCP servers use Lukka compact notation (unquoted keys + bare-string values), which `json.loads()` rejects. See [CONNECTORS.md](CONNECTORS.md) "Response format" for parser notes. The bundled `process_aml_report.py` handles both standard JSON and Lukka notation via its `_LukkaParser` recursive-descent parser.

### `get_latest_index_prices` / `get_historical_index_prices` (Reference Rate access)

Available with Lukka Reference Rate access - request at https://lukka.tech/plugin. Standard path: `get_latest_prices({ sourceId: 1000 })` for EOD or `{ sourceId: 2000 }` for Intraday.

### Analytics flow (implied rates, volatility surface, OTC FX, valuations)

Analytics tools are available via `Lukka-Analytics` server (`analytics___*`). Includes: `getImpliedRates`, `getImpliedRatesOtcFx`, `getImpliedVolatilitySurface`. See `skills/lukka-data-routing/references/analytics.md` for parameters and examples.

### News `getNews` date filter

The hosted `Lukka-News` server requires **full ISO 8601 timestamps** for `publishDateFrom` and `publishDateTo`. Always use `2026-04-01T00:00:00Z` (not a bare date).

### Daily summaries return empty

`getDailySummaries` data starts from **2026-04-08**. Earlier dates return empty results. Monday summaries cover Saturday + Sunday as a weekend digest.

## OpenAI package scope

This edition preserves the original business procedures. Its documented tool
list is the original Claude list with three unavailable operations removed:
**66 operations**. See [the operation list](docs/TOOLS.md).
The configuration uses Global MCP and public Auth0 DCR settings. It does not
modify the remote MCP server's tool catalog. No reviewer credentials are packaged.
