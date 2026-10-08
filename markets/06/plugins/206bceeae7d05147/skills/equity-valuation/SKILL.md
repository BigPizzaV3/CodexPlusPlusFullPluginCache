---
name: equity-valuation
description: Use when valuing public-equity candidates, testing market-implied expectations, or modeling long-term shareholder return scenarios and probability-sensitive rankings.
---

# Valuation and probability analyst

Read the [operating contract](../../references/operating-contract.md), [ranking method](../../references/ranking-method.md) and relevant [sector lens](../../references/sector-lenses.md). Work from reconciled financials, a verified entry price and a dated assumptions ledger. Explain value per share, not merely growth in the enterprise.

## Procedure

1. Build the valuation bridge: enterprise value to common equity to diluted per-share value; include net debt, leases where appropriate, noncontrolling interests, nonoperating assets, convertibles and dilution. Avoid double-counting assets or liabilities already reflected in cash flows. Banks/insurers need equity/distributable-capital approaches rather than industrial templates.
2. Reverse the current valuation: solve the growth/margin/reinvestment combinations consistent with price. Hold other variables explicit; price implies a family of assumptions, not one unique forecast. Compare with capacity, competitive behavior and relevant historical reference classes.
3. Forecast driver-linked cash flows. Match FCFF with WACC and FCFE/distributions with cost of equity; use compatible currencies and nominal/real assumptions. Link reinvestment to growth and competitive fade. Explain maintenance vs growth capital and financing needs. Model buybacks and SBC coherently in per-share outcomes.
4. Use an economic cross-check: cash-flow valuation plus comparable through-cycle multiples or asset/distributable-capital value where appropriate. Two multiples sharing the same optimistic earnings forecast are not independent confirmation. State terminal-value dependence and require discount rate above perpetual growth in a perpetuity model.
5. Construct central and plausible adverse probability/driver sets. Document base rates, source populations, adjustment rationale, dependencies and what is unknown. Include financing failure and recovery when material. Use unweighted ranges if probabilities lack support; never derive probabilities from a research-quality score.
6. Rebuild five-, seven- and ten-year forecasts, including horizon-specific reinvestment, dilution, distributions and valuation. Do not change only the CAGR denominator. Find assumptions and entry prices that reverse the leading pair's ranking.
7. Populate the [calculator input contract](../../references/calculator-input.md) and run `../../scripts/scenario_rank.py` when its return conventions fit. Inspect output against original inputs. Otherwise write a transparent alternative model with meaningful mathematical checks.

## Deliver

Return valuation methods and reconciliation; source-linked drivers; price-implied expectations; scenario tables and probability rationale; benchmark states; expected total return, annualized expected wealth and weighted scenario CAGR with distinct labels; terminal loss/severe-loss exposure; sensitivity/rank-reversal tests; entry-value ranges; unresolved model risks. Pass canonical inputs to the director and neutral recalculation questions to the auditor.

Never treat scenario weights as measured odds, terminal downside as path drawdown, or a high valuation estimate as evidence that the market must converge to it. If current price is unavailable, report conditional value and entry sensitivity without a current investment rank.
