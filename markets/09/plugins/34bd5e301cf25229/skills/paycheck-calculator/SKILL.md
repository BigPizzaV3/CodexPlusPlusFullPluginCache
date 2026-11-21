---
name: paycheck-calculator
description: Estimate 2026 US take-home pay (paycheck after federal withholding, Social Security, Medicare, state income tax and state payroll taxes) per check and per year, compare two paycheck scenarios, or solve for the salary that gives a take-home target.
---

# Netwise Paycheck Calculator

Tools:
- `calculate_paycheck`: one job. "How much is my paycheck after taxes", "85k after taxes in California", "$22 an hour 40 hours".
- `compare_paychecks`: two scenarios. Job offers in two states, a raise, or "how much more per paycheck if I raise my 401k to 10%". Pass `a` in full and `b` with only the fields that change.
- `calculate_gross_up`: "what salary do I need to take home $X".

How to call:
1. Pay: `annual_salary`, or `hourly_rate` + `hours_per_week` (+ `overtime_hours_per_week`), or `gross_per_paycheck`. Pay frequency defaults to biweekly; filing status defaults to single. If the user gave the pay and the state, call right away; do not ask about W-4 details first.
2. State: a code or name (`CA`, `New Jersey`). For New York City pass `state: "NY", locality: "nyc"`. If the result says the state is not supported, tell the user the state tax is not included.
3. W-4: `filing_status`, `w4_step2_checked`, `children_under_17`/`other_dependents` or `w4_step3_amount`, and Step 4(a)-(c) only when the user mentions them.
4. Pre-tax: `k401_percent`, `hsa_per_paycheck`, `health_insurance_per_paycheck`. Roth: `roth_401k_percent`.
5. Reply with net pay per check and per year, the main tax lines, any notes about unsupported states or caps, and the PDF/CSV links. Say it is an estimate.

Do not use for making pay stubs or proof of income, running payroll for employees, filing tax returns, or self-employment tax.
