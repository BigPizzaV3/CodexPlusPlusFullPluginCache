# Legal ID — find, validate & enrich

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this capability to resolve, validate, and enrich a company's registry identifier. The request
enum currently contains **17 registries across 16 countries**. France has SIRET and SIREN; the US
registry is CIK. **EIN is retired and is not available.** Two jobs in one:

- **Validation mode** — you already hold a `legal_id` and want to confirm it is real, normalized, and tied to the right company.
- **Search mode** — you have a `name` and/or `website` (plus a country signal) and want Delpha to find the identifier.

Either way the result carries an enriched `match` record you can write back to a CRM (see [Salesforce](salesforce.md)). To resolve a parent company instead, see [ultimate parent](ultimate-parent.md).

## Tools
- `findAndValidateLegalID(...)` — submits the job, returns a `job_id`.
- `getLegalIDResult(job_id)` — returns the result envelope.

The MCP `getLegalIDResult` holds the connection open and polls upstream internally, so a single call usually returns the final result. Typical latency is ~5–10s.

## Inputs & modes
The job MUST know which registry to target. **Provide AT LEAST ONE of:**

- `legal_id_type` — the registry directly, or
- `address.country` — the country, from which the registry is inferred.

Supplying neither (e.g. `{name, website}` alone) is rejected with `400 — "Either 'legal_id_type' or 'address.country' must be provided"`.

| Field | Type | Notes |
|---|---|---|
| `legal_id` | string | Existing identifier to validate, e.g. SIRET `88052440000012`. Format is registry-specific. |
| `legal_id_type` | enum | Registry directly. Closed enum of 17 registries. |
| `name` | string | Legal or trade name, e.g. `Delpha`. |
| `website` | uri | Domain is used as a country signal during registry resolution. |
| `address` | object | `{ street, city, state, postal_code, country }`. `country` is the registry signal. |

`legal_id_type` is a **closed enum**:

`"FRA - SIRET"`, `"FRA - SIREN"`, `"NZL - NZBN"`, `"AUS - ABN"`,
`"NOR - ORGANISASJONSNUMMER"`, `"CHE - UID"`, `"GBR - COMPANY REGISTRATION NUMBER"`,
`"BEL - ENTERPRISE NUMBER"`, `"DEU - HANDELSREGISTERNUMMER"`,
`"EST - COMMERCIAL REGISTER CODE"`, `"IRL - CRO NUMBER"`, `"ESP - NIF"`,
`"NLD - KVK-NUMMER"`, `"CAN - CORPORATION-NUMBER"`, `"FIN - Y-TUNNUS"`,
`"SWE - ORGANISATIONSNUMMER"`, `"USA - CIK"`.

Pass it whenever the numeric format is ambiguous; it overrides country inference.

## Reading the result
Every `getLegalIDResult` call returns the standard envelope:

```json
{ "message": "...", "status": "SUCCESS", "status_code": 200, "result": { ... }, "process_time": 6.4 }
```

- `status_code` 200 = done (`result` populated); 202 = still running (`result` null). Error outcomes
  include 400 bad input plus the common auth, credit, lookup and delivery failures in the
  [REST status table](rest-api.md#status-codes).
- `result` payload contains:
  - the **normalized** legal identifier,
  - the resolved `legal_id_type` (which registry it belongs to),
  - `scores` (discrete `validity`, continuous `accuracy`),
  - `match` — the enriched company record (account name, address, `financials`, employee count,
    industry, formation date, company type, website) when a confident match is found,
  - `suggestions` — an array of alternative company records, ranked by confidence.

If `match` is empty but `suggestions` is non-empty, the engine was not confident enough to auto-pick; surface the top suggestions for human selection.

## Scores & thresholds

For Legal ID, `validity` is the discrete integer `-1`/`0`/`1` and `accuracy` is continuous
`-1..1`. Treat `-1` as missing. Branch on `validity` exactly and apply the bands below only to
`accuracy` or `suggestions[].score`.

Suggested, tunable thresholds:
- `>= 0.8` — auto-accept.
- `0.5` ≤ score < `0.8` — route to human review (often: pick from `suggestions`).
- `< 0.5` — reject.

## Recipes

### MCP — validate a known SIRET (validation mode)
```json
{
  "legal_id": "88052440000012",
  "legal_id_type": "FRA - SIRET",
  "name": "Delpha",
  "website": "https://delpha.io/"
}
```
Then call `getLegalIDResult` with the returned `job_id`. Read `result.scores` and `result.match`.

### MCP — find an ID from name + country (search mode)
```json
{
  "name": "Delpha",
  "address": { "city": "Paris", "country": "France" }
}
```

### REST — async POST then GET
```bash
# 1. Submit the job -> HTTP 202 { job_id, ... }
JOB=$(curl -s -X POST https://api.delpha.io/v1/legal-id \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H "Content-Type: application/json" \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"legal_id":"88052440000012","legal_id_type":"FRA - SIRET"}' | jq -r .job_id)

# 2. Poll -> 202 while running, 200 when done
curl -s https://api.delpha.io/v1/legal-id/$JOB -H "Authorization: Bearer $DELPHA_API_KEY"
```

`match.financials` reports `revenue`, `operating_profit`, `net_income`, `equity`, `currency`,
`fiscal_period` and `revenue_range`. Amounts are exactly as filed by the national registry and are
not converted. See [Salesforce](salesforce.md) before mapping them into a CRM.

## Traps to avoid
- **Always provide a registry signal.** Sending `{name, website}` with no `legal_id_type` and no `address.country` fails with 400. The website domain alone is a *hint*, not a country.
- **Do not submit a retired registry such as `USA - EIN`.** Production refuses a positively
  identified unsupported registry with `422` before reserving credits and says that no credits were
  consumed. Development additionally exposes the typed error `code: "unsupported_registry"`; that
  typed field is not yet a production contract.
- **Do not treat `-1` as a low score.** It means the engine could not compute that dimension — handle it as missing, or it will skew your accept/reject logic.
- **Do not re-call `getLegalIDResult` while it is returning.** A single call usually yields the final result. Re-call only if `status_code` is still `202` after it returns, and wait 1–2s first — early re-calls render a duplicate result widget.
- **Set `legal_id_type` when formats collide.** SIREN vs SIRET, or any numeric code shared across registries, can resolve to the wrong registry if you rely on country inference alone.
- **Prefer `match` over `suggestions[0]` blindly.** An empty `match` with populated `suggestions` signals low confidence — gate on the score, do not auto-pick the first suggestion.
- **Never assume a re-run costs nothing.** Production `findAndValidateLegalID` mints a fresh,
  separately charged `job_id` for each accepted call; `getLegalIDResult` is read-only and never
  mutates or charges.
