---
name: installment-plan
description: Split an amount into a payment plan or installment schedule (count or fixed amount, weekly to quarterly, optional deposit and flat simple interest) with the generate_installment_plan tool, returning exact amounts, due dates, a printable PDF schedule, Excel, CSV and calendar reminders.
---

# Zovo Installment Planner

Use `generate_installment_plan` when the user wants to split an amount into installments, a payment plan, or a payment schedule with a deposit.

1. Required: `total_amount`, `first_due_date` (YYYY-MM-DD), and either `installments` (a count, 1 to 360) or `installment_amount` (a fixed amount; the last one is the smaller rest). If the first due date is missing, ask one short question. Do not assume today.
2. `frequency`: weekly, biweekly (every 2 weeks), semimonthly (twice a month), monthly (default) or quarterly. "Bimonthly" is ambiguous: ask whether it means twice a month or every 2 months (every 2 months is not offered).
3. Optional: `deposit` as an amount or a percent ("20%") and `deposit_date`; `annual_interest_rate` only when the parties agreed interest (flat simple interest on the amount paid in installments, not an APR); `rounding_rule` (remainder_last default, remainder_first, even_up) and `round_to` (e.g. 5 for whole fives); `weekend_rule`; `payer_name`, `payee_name`, `plan_title`, `reference` for the PDF.
4. After the tool returns, give the installment amount (and the one that differs, if any), the first and last due dates, the total to pay, any notes verbatim, and the PDF, Excel, calendar and CSV links.

Do not use this skill for amortizing loan or mortgage payments, APR, credit decisions, collecting payments, or legal advice about a payment agreement.
