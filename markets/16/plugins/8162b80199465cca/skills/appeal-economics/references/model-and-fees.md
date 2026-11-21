# Financial model and fee scope

## Equations and interpretation

`P` = demand principal; `r` = annual interest as a decimal; `m` = planning months; `p` = assumed full-relief probability; `F` = fixed appeal fee. Same currency throughout.

```text
I = P × r × m / 12
B = P + I
Full-win cost = F
Full-loss cost = F + B
Expected appeal cost E = F + (1 − p) × B
Savings versus repayment now = P − E
Break-even fee ceiling versus repayment now = P − (1 − p) × B
Break-even full-relief probability = 1 − (P − F) / B
```

For an alternative fixed fee `F0` and assumed probability `p0`, using the same balance:

```text
E0 = F0 + (1 − p0) × B
Proposed appeal advantage = E0 − E
Fee ceiling versus alternative = F0 + (p − p0) × B
Probability needed to match alternative = p0 + (F − F0) / B
Relevant fee ceiling = lower of the two comparison ceilings
```

Positive savings/advantage favors the proposed appeal **under the assumptions**; zero is equality; negative favors the comparator. A negative ceiling means even a zero fee cannot beat that comparator at the assumed probabilities. A threshold above 100% cannot be reached in this model; one below 0% means the proposed fee already has lower expected cost throughout the allowed range. Keep equality distinct from strict advantage.

Unknown probability is not a barrier: show hypothetical sensitivity and required threshold. Do not choose the threshold as the case's actual probability. Do not relabel full-or-partial favorability rates as full-relief probabilities. Do not aggregate stage-specific conditional outcomes without a compatible joint model.

## Assumptions that matter

The model preserves the website calculator's simple-interest, full-relief/full-loss, fixed-fee mathematics. Input interest is a planning assumption; this is not a determination of an applicable Medicare rate or balance. Repayment-now cost is principal only; if accrued interest, payments, offsets, or other demand components already exist, this baseline is incomplete. Do not silently substitute a current balance as principal and charge interest on it again.

Fees are paid in either outcome, with no discounting. Both quotes use the same rate and timeline. No partial relief, interest-only relief, recoupment cash-flow path, hearing expenses outside the stated fee, fee refunds, fee contingency, interest accrual exceptions, investment return, or liquidity constraints are modeled. Estimated future interest is applied only to the full-loss branch. Explain material departures before interpreting a result.

## Evaluating a service fee

A financial ceiling answers what fee would preserve value relative to a comparator at assumed odds. It does not answer what the work should cost. Compare:

- appeal levels included, preparation versus representation, and number of hearings;
- claim/beneficiary counts expressed as aggregate counts, distinct fact patterns, record pages, and reconciliation burden;
- clinical declarations, product literature, expert review, and counsel scope;
- urgency, revisions, additional-evidence handling, exclusions, travel, and third-party expenses;
- payment/refund/contingency terms and when another fee becomes due.

For a concrete budget, use supplied rates, quotes, and estimated effort. If absent, make a transparent **proposed workload budget**, with hours and rates explicitly assumed; do not claim it is an ArcLight quote or prevailing market price. Documentation quality changes review burden; it is not a win-rate multiplier. Avoid recommending a fee solely as a percentage of hypothetical savings.

## Checked synthetic examples

P = $100,000; rate = 10%; months = 8; fee = $7,500; projected balance = $106,666.67.

| Assumed full relief | Expected cost | Savings vs repayment | Fee ceiling vs repayment |
|---|---:|---:|---:|
| 10% | $103,500.00 | −$3,500.00 | $4,000.00 |
| 25% | $87,500.00 | $12,500.00 | $20,000.00 |
| 50% | $60,833.33 | $39,166.67 | $46,666.67 |
| 80% | $28,833.33 | $71,166.67 | $78,666.67 |
| 90% | $18,166.67 | $81,833.33 | $89,333.33 |

Full loss costs $114,166.67; full win costs $7,500.00. Break-even probability is 13.28125%. None of these percentages estimates real odds.

At proposed 50% versus alternative fee $3,500 and assumed 66.6%, alternative expected cost is $39,126.67; proposed advantage is **−$21,706.67** and alternative fee ceiling **−$14,206.67**. Positive savings versus repayment does not establish superiority to the other quote. These inputs are illustrative, not evidence that either representative attains these rates.

## Execution

Pass a minimal JSON object to the helper on standard input using the host's Python runtime. Decimal inputs have website-compatible bounds: principal $1–$100m (2 decimal places); fee $0–$100m (2); rate 0–100 percent (4); months 0–1200 (2); probability 0–100 percent (4). Sensitivity contains 1–25 percentages. Unknown fields, booleans, NaN, Infinity, and partial alternative objects are rejected. Values are never echoed on input errors. Currency outputs round half away from zero to cents only at display; percentages display up to six decimal places, so equality decisions use the unrounded values.
