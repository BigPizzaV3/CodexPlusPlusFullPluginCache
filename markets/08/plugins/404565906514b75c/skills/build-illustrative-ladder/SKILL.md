---
name: build-illustrative-ladder
description: Build and explain an equal-weight illustrative fixed-income maturity ladder from current public BrinkerAdvisor records.
---

# Build an illustrative ladder

Use this workflow when the user explicitly asks for an educational maturity ladder using supported current public records.

1. Preserve the requested instrument types, rung count, maturity range, and optional hypothetical amount.
2. Call `build_ladder` once. Treat every uncovered rung as a real limitation; do not fill it with an invented option.
3. Explain the maturity spacing and equal target percentage. If an amount was supplied, reconcile the rung amounts to that hypothetical total.
4. Cite the canonical BrinkerAdvisor row URL for every covered rung and state the shared as-of date.
5. Surface reinvestment, liquidity, callability, insurance or credit, tax-treatment, and rate-change limitations that matter to interpretation.

The output is illustrative only. Never access an account, execute a trade, select a product for the user, or imply that equal weighting is suitable.
