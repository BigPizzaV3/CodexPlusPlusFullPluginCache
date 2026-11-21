# Connectors

The seven original product families use one Global MCP connection at `https://global.mcp.lukka.tech`.

| Category | Raw prefix | Server | Auth | Domain |
|----------|-------------|--------|------|--------|
| Pricing | `pricing___` | Lukka-Pricing | OAuth 2.0 (Auth0) | Prices, candles, VWAP, market cap, order book, derivative trades, reference rates |
| Reference Data | `refdata___` | Lukka-RefData | OAuth 2.0 (Auth0) | Assets, entities, mappings, classifications, sectors, pairs, VASPs |
| AML / Compliance | `AML___` | Lukka-AML | OAuth 2.0 (Auth0) | AML risk reports (scoring / standard / enhanced), 107+ blockchains |
| On-Chain | `UDA___` | Lukka-UDA | OAuth 2.0 (Auth0) | Balances, transactions, assets, blocks |
| Analytics | `analytics___` | Lukka-Analytics | OAuth 2.0 (Auth0) | Implied rates, volatility surface, OTC FX |
| News Intelligence | `news___` | Lukka-News | OAuth 2.0 (Auth0) | Digital asset news search, daily summaries, sentiment, categories |
| Prediction Markets | `prediction-markets___` | Lukka-Predmar | OAuth 2.0 (Auth0) | Market search, details, similarity, PMCS classification (Polymarket, Kalshi, Gemini) |

## Connection Requirements

Configure `https://global.mcp.lukka.tech` in [mcp.json](mcp.json) with Streamable
HTTP and OAuth. The authorization server is `https://auth0.lukka.tech`.
The package selects Dynamic Client Registration (DCR), with `mcp` as the
default scope and `openid`, `email`, `offline_access` as base scopes.
No client credentials or tokens are included. Sign in through the host's
connection settings. See [INSTALL.md](INSTALL.md) for the exact public endpoints.

## Resolution and matching approach

- **Asset/pair/market resolution**: use `Lukka-RefData.list_assets`, `get_asset_mappings`, `get_pair_mappings` with direct filters.
- **Derivative instrument matching**: use `Lukka-Pricing.get_derivative_source_details` + client-side string match.

## Products: 7, connection: 1 (Global, OAuth via Auth0)

## Response format: Lukka compact notation

Hosted Lukka MCP servers return responses in a compact object notation - unquoted keys, bare-string values (addresses, ISO timestamps, enum values), `_` for null. This is **not** RFC 8259 JSON.

Example:
`{report_info_section:{address:00000000000000000000000000000000000dead,report_time:2026-05-06T02:14:37.511Z,risk_level:LOW}}`

Any downstream parser must either:
- Use the recursive-descent parser in `skills/large-data-processing/references/process_aml_report.py` (class `_LukkaParser`) - handles both standard JSON and Lukka notation.
- Implement its own state-machine parser.
- NOT use `json.loads()` directly - it rejects unquoted keys.

Tables inside responses use a column-oriented shape: `{cols: [name, type, id], rows: [[...], [...]]}`. The processor's `_rows_to_dicts` helper converts these to list-of-dicts.
