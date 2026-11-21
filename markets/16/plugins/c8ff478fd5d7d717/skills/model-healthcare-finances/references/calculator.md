# Calculator specification

The offline helper models 12 months in USD. Inputs are planning estimates; fractional expected visits are allowed. Do not silently round fractional volumes up to scheduled encounters. No credentials, patient records, code identifiers, or code descriptions belong in its JSON.

## Input contract

All fields below are required except `notes`. A missing value is an error, not zero. Unknown keys are rejected to catch misspellings or unsupported assumptions. Percentages are decimals in [0,1]. All monetary inputs and minutes are finite nonnegative numbers. Per-visit minutes must be positive.

| Field | Meaning |
|---|---|
| scenario_name | Short, non-sensitive label |
| mode | `existing_practice` or `standalone`; labels context, does not invent different costs |
| currency | `USD` |
| monthly_capacity_minutes | Array of 12 workable shared-resource minutes, after nonclinical commitments |
| monthly_fixed_cash_cost | Array of 12 incremental fixed cash expenses, including salary if applicable |
| billing_fee_rate | Fee on expected collections for operating results; on received cash for cash flow |
| collection_lag_weights | 1–13 weights summing to 1, starting at same-month collection then 1 through 12 months later; distribution of already-adjusted collectible revenue |
| startup_capex | Cash paid at month 0 for capital assets |
| startup_expense | Prelaunch cash expense at month 0; also deducted in first-year result after startup expense |
| annual_depreciation | Noncash annual expense for the modeled assets; supplied, not inferred |
| opening_cash | Cash available at month 0 before startup spending |
| cash_reserve | Desired minimum cash cushion, separate from projected spending |
| services | 1–100 mutually exclusive encounter profiles described below |
| notes | Optional explanatory metadata; not used in calculations |

Each service has `label`, 12 `monthly_demand_visits`, `minutes_per_visit` including travel/documentation, `variable_cost_per_visit`, and a `payment` object. Monthly fixed costs and per-visit costs must not duplicate the same clinician or overhead costs. Add independent room/device constraints before converting to the one shared capacity pool, or use an expanded model.

Two payment bases are accepted:

```json
{"basis":"expected_collected","amount":100}
```

This is ultimate expected collected revenue per encounter BEFORE billing fees and direct costs. It already includes payment losses, adjustments, and patient collection assumptions; none are applied again.

```json
{"basis":"allowed","allowed_amount":150,"claim_paid_probability":0.9,"payer_share":0.8,"payer_collection_factor":0.98,"patient_collection_rate":0.7}
```

These numbers are synthetic. The allowed amount must already match the modeled provider and setting. Expected collection is:

`allowed × claim_paid_probability × [payer_share × payer_collection_factor + (1 − payer_share) × patient_collection_rate]`.

Here `patient_collection_rate` means collection of the non-payer share, including applicable secondary insurance. The simple waterfall assumes claim-payment probability applies to both shares. If this does not fit the contract, derive an appropriate expected-collected input transparently outside the helper. Neither 80% nor any other rate is a built-in policy default.

## Computation

For each month, requested minutes equal the sum of profile demand × per-visit minutes. Scale all profiles by `min(1, available minutes / requested minutes)` if demand is positive. This preserves the entered mix and makes no clinical prioritization recommendation. Unmet visits are not automatically backlogged to another month; enter a deliberate backlog scenario if warranted.

Expected earned collections = sum(completed visits × expected collection per visit). Contribution = earned collections − variable costs − accrual billing fee. Recurring operating result = contribution − fixed cash costs − depreciation/12. First-year result after startup expense also subtracts prelaunch expense once.

Cash received in month t is the sum of earlier/current earned collections multiplied by the corresponding lag weight. Monthly operating cash flow = received cash − same-month variable costs − cash billing fee − fixed cash costs. Start cumulative cash at negative startup capex and expense; opening cash is added only when assessing cash balances and additional funding. Receivables = earned less received within the horizon. No second loss factor is applied to those receivables.

Peak deficit is the largest negative cumulative cash position including month 0, before financing. Total initial liquidity required = peak deficit + reserve. Additional funding = max(0, total initial liquidity required − opening cash). This is a single up-front funding estimate; the helper does not optimize financing timing or compute borrowing costs.

Monthly break-even at current mix = (monthly fixed cost + depreciation/12) / weighted contribution per visit, only if there are completed visits and their contribution is positive. Otherwise return null. Check the corresponding minutes against current capacity. This excludes startup recovery, collection delays, and cost/capacity steps; it is not the launch-year cash break-even target. It also does not establish sufficient demand.

The model reports unrounded calculations; round display dollars appropriately without changing the underlying reconciliation. `summary.json`, `monthly.csv`, and `service-economics.csv` are created in a new directory. An existing output directory causes an error to avoid overwriting work.

## Limits and fallback

The helper does not model opening receivables, monthly inventory purchases/vendor terms, debt, taxes, grants, multi-year forecasts, downstream clinic revenue, or clinical outcomes. Shared collection timing and proportional capacity scaling are simplifications. If one of these omitted factors could reverse the recommendation, extend the analysis transparently with a separately verified model, or label the conclusion unresolved. Never hide it inside a misleading field.

If execution is unavailable, use these same formulas in an inspectable table or supported spreadsheet, show assumptions, and say the packaged script was not executed. Do not report generated file links unless those files exist.
