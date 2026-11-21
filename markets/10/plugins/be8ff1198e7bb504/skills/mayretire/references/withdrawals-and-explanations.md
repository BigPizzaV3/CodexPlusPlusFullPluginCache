# Withdrawals and explanations

Inspect the active strategy, its schedule, registered balances, and enabled
overrides before attributing a withdrawal. Use bounded `withdrawals` and
`balances` views from `calculate_plan_payload`, then
`explain_plan_payload` for a specific age or year. Explain only recorded
decision-trace evidence. Intermediate trace values can precede final tax,
contribution, or account-splitting adjustments; dividend, tax-solver, and OAS
details are not fully traced. If evidence is absent, describe the observed
annual result without inventing a cause.

`withdrawalStrategySchedule.entries` is authoritative when present. Entries
start in one-based planning years; each lasts until the next entry, and the
last lasts through plan end. The top-level RRSP and TFSA strategy fields are
year-one compatibility mirrors. JSON merge patches replace arrays, so an
edit to one range must preserve all other intended entries in the replacement
array. Show the resulting diff and validate before calculation.

For custom registered-withdrawal tax limits, inspect `activeRRSPTaxConstraint`:

| Mode | Active limit | Meaning |
| --- | --- | --- |
| Effective tax | `maxEffectiveTax` | Average rate across taxable income |
| Marginal tax | `maxMarginalTax` | Rate on the next dollar |
| Combined | Both above | Whichever binds first |
| RRSP withdrawal tax cost | `maxAvgRRSPTax` | Added tax as a fraction of that withdrawal |
| No tax limit | None | No tax-rate constraint |

`maxAvgRRSPTax` is not the average rate across all income. A predefined RRSP
strategy makes stored custom tax settings inactive. Change mode and the
matching active value together. A fixed withdrawal amount can bypass tax-limit
tuning. Compare income, depletion, lifetime tax, OAS clawback, and estate
before claiming a strategy improves the plan.

Prefer strategy changes over new account overrides. Preserve existing enabled
overrides unless the user allows changes. For a requested override, use
`describe` for its schema and `edit_plan_payload` item operations. `starts`
is a one-based planning year; `madeFor: 0` continues through plan end. An
override requests or limits withdrawals but does not guarantee a realized
amount: balances, spending needs, and mandatory RRIF/LIF minimums still apply.
Verify realized withdrawals in the calculated scenario. Avoid fixed lifetime
overrides for a broad optimization unless the user explicitly wants them.
