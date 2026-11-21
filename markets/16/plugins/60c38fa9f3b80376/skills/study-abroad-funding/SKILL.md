---
name: study-abroad-funding
description: Plan how an Indian student funds a degree abroad (USA, UK, Canada, Australia, Germany) — loan amount at live exchange rates, interest during the moratorium, EMI after the course, visa proof-of-funds rules, lenders with and without collateral, documents and scams to avoid. Use for "education loan for MS in the US", "how much loan for UK masters", "GIC / blocked account / I-20 funds".
---

# Study-abroad funding

Explicit instructions from the user override this workflow.

## Collect
Country, course length, total tuition + living cost (in the country's currency — if the user only has tuition, ask for living cost or use the cost table from the result and say so), family contribution, scholarship, and whether property collateral is available.

## Steps
1. `plan_study_abroad_loan` with the figures.
2. `get_current_interest_rates` (loanType `education`) if the user wants lender rates beyond the country lender list.
3. If they ask about repayment after graduating, use the EMI from the result; if they have an expected salary, compare the EMI with 30–40% of take-home pay.
4. Use `find_government_schemes` (purpose Education) for interest subsidy schemes when family income is under ₹12L.

## Answer format
1. Loan needed and the EMI after the moratorium (one line each).
2. The visa funds rule for that country — what document, how much, by when.
3. Lenders: up to 4, split collateral / no collateral, with limits.
4. Moratorium tip: paying simple interest during the course reduces the EMI.
5. Country red flags from the result (max 3) and the documents checklist link.

Mention that exchange rates move and the result's rate is today's.
