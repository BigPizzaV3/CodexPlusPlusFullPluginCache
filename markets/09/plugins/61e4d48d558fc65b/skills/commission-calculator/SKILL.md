---
name: commission-calculator
description: Calculate sales commission from a comp plan (flat, tiered marginal or retroactive, quota accelerators, caps, draws, splits, SPIFFs, clawbacks, gross margin, OTE), build per-rep commission statements from a deals CSV/XLSX, and compare two comp plans.
---

# Quotaline Commissions

Tools:
- `calculate_commission`: one rep. Pass the plan and either `sales_total` or `deals`.
- `generate_commission_statements`: several reps, or an attached deals export (CSV or .xlsx). Pass the file as `file`; columns are matched automatically. Use `rep_overrides` for per-rep quota, draw or prior balance.
- `compare_comp_plans`: two plans side by side at several sales levels.

How to fill the plan:
1. "5% up to 50k then 8% above" = `tiers: [{"up_to":50000,"rate":5},{"up_to":null,"rate":8}]`.
2. Tiers by quota attainment: `tier_unit: "quota_percent"` plus `quota`. Accelerators and decelerators can be rates or `multiplier`s of the base rate (`rate`, or `target_variable` / `quota`, or `ote` minus `base_salary`).
3. Set `tier_method` only when the user says whether tiers are retroactive or marginal (stepped). Otherwise leave it out: both results are returned. Tell the user both numbers and ask which one their plan uses.
4. Split deals: `split_percent` on the deal (one rep) or `splits` (several reps). Refunds and cancellations: `status` plus `cancel_date`; for a deal paid in an earlier period also `commission_paid`.
5. Draw: `draw_amount` and `draw_type` (recoverable carries the shortfall forward; non_recoverable forgives it).

After the call, report the payable amount, total earned, attainment, any clawbacks, and both tier readings when the plan was ambiguous. Share the PDF statement and Excel links; they expire after about an hour.

Real estate commission splits (agent/broker shares) work as split_percent. Do not use for payroll tax, withholding or take-home pay, commission-free trading, or commissioning artwork.
