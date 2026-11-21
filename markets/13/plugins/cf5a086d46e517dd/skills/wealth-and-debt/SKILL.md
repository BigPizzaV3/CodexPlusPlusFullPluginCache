---
name: wealth-and-debt
description: Understand or update Fina debts, property and investment observations, compare supported debt-payment or fixed-income scenarios, or request a property valuation. Use for wealth and debt questions grounded in saved evidence; never execute trades, transfers or lending decisions.
---

# Wealth and debt

Read [Fina's shared workflow](references/fina-core.md) and [financial facts](references/financial-facts.md). Check setup and read `get_financial_context(detail=summary)` before a joint financial decision. Retrieve `get_account_details` only for the relevant account and sections, and follow its current domain guidance.

## Save facts with their meaning

Reuse existing accounts. For an explicitly requested new loan/property/investment/other asset, use `create_account`; wealth accounts do not require bank/card last digits. Use `update_account_details` with current version for supported conditions, ownership/liability shares or evidenced status changes. Use `record_account_observation` for dated amounts, holdings and extracted evidence.

Keep `amount_kind`, currency, observation date, `amount_scope`, quality and coverage accurate. A later-received old statement does not become today's balance or erase a newer correction. Supersede an observation only when the user/evidence actually corrects it. Partial holdings do not replace a complete portfolio: distinguish total-value coverage from `positions_coverage`. Account total plus positions would double count assets.

Debt total, outstanding principal, next installment and payoff quote differ. Property gross value is not net sale proceeds; portfolio market value is not equity after margin debt unless evidence establishes it. Preserve ownership and liability shares and avoid subtracting the same liability twice. Missing facts stay unknown. Documents may update the requested observations, but incidental transactions/subscriptions follow their separate consent workflows.

## Compare supported scenarios

Use the server's calculators and live schemas, not an invented spreadsheet model:

- `simulate_debt_scenario`: requires principal/currency, fixed periodic rate, principal-and-interest payment, horizon, proposed extra principal and known prepayment fee. Set `assumptions_confirmed=true` only with evidence of the fixed declining-principal model, period-end payments, payment composition and fee. An annual effective rate is not divided by 12. Unknown fees are not zero. Explain non-amortizing or exhausted-horizon results instead of inventing savings.
- `simulate_fixed_income`: requires known principal/currency, dated periods with explicit periodic rates and interest disposition, and principal disposition at maturity. Set confirmed assumptions only when known. Do not pass stored auxiliary fields such as `payout_account_id` into its strict schema. Keep principal return separate from income and distinguish expected gross flows from guaranteed returns or current cash.

Ask missing assumptions together. Give useful supported context while the scenario remains incomplete. A hypothetical comparison does not authorize updating records, buying a product or making a payment. Tie any proposed extra payment back to the user's cash needs and coverage, not wealth alone.

## Property research

Use `estimate_property_value` only for requested valuation/research needed for the user's decision. Inspect saved relevant property attributes first; ask missing coarse area/type/location details together without a precise private address or owner identifier. Research is a stateful external lookup, not a read-only calculation. Reuse a pending job and retrieve `get_property_valuation` rather than repeatedly starting research.

Report the actual dated range and returned source links; distinguish asking prices, weak comparables, failed research and absent attributes. Never fabricate a valuation or silently save an estimate as a confirmed observation. This operation is for property valuation, not general web browsing.

End with the evidence-supported answer, significant assumptions and a practical next step. Preserve Fina's approachable voice; avoid presenting a personalized investment guarantee, tax determination or automated trading action.
