---
name: loan-planner
description: Mortgage calculator, loan calculator and amortization calculator. Use calculate_loan for one loan's exact payment, amortization schedule, extra-payment savings, PITI with PMI and CSV; use compare_loans to compare 2 to 4 loans such as 15-year vs 30-year or paying points.
---

# Amortiza Loan Planner

Use `calculate_loan` when the user asks for a mortgage or loan payment, an amortization schedule or table, total interest, a payoff date, savings from extra payments or paying off early, or a full monthly housing payment (PITI).

1. Pass `principal`, or `home_price` with `down_payment` or `down_payment_percent`. Pass `annual_rate` in percent and `term_years` or `term_months`. Ask one short question only if the rate or the term is missing.
2. Add `extra_payment` for a recurring extra amount per payment and `one_time_payments` for lump sums (date as YYYY-MM).
3. For a house purchase, add `property_tax_annual`, `home_insurance_annual`, `hoa_monthly`, and `pmi_rate` (needs `home_price`) when the user gives them. Never invent tax, insurance or PMI figures; say they are excluded instead.
4. Use `payment_frequency` biweekly or weekly when asked; set `accelerated: true` for "half the monthly payment every two weeks".

Use `compare_loans` when the user wants 2 to 4 options side by side. Put shared values (loan amount, start date) at the top level and what differs (rate, term, points, closing costs) in each scenario.

After a result, state the payment, total interest, payoff date and any savings in one or two sentences, then give the CSV link. Say the figures are informational, not financial advice, when the user is deciding on a loan.

Do not use these tools for current mortgage rates, rent-vs-buy advice, pre-approval or choosing a lender, and do not present results as a lender quote. Adjustable-rate, interest-only and balloon loans are not supported.
