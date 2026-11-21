---
name: self-employment-tax
description: 2026 self-employment tax and 1099 tax calculator with Form 1040-ES quarterly estimated payment planning. Use calculate_self_employment_tax for how much a freelancer or 1099 contractor owes, plan_quarterly_payments for quarterly amounts, safe harbor, or a missed payment, and find_estimated_tax_due_dates for the 2026 due dates with calendar reminders.
---

# QuarterWise 1099 Tax Planner

Use these tools for US federal tax year 2026 questions from freelancers, 1099 contractors, and gig workers.

1. "How much do I owe", "self employment tax calculator", "how much to set aside": call `calculate_self_employment_tax`.
2. "How much should I pay each quarter", safe harbor, "I missed my Q2 payment", penalty worries: call `plan_quarterly_payments`. Pass `prior_year_tax` (2025 Form 1040 line 24) and `prior_year_agi` when the user knows them, `estimated_payments_already_made` as a total, and `as_of_date` = today.
3. Only dates or reminders, no income: call `find_estimated_tax_due_dates`.

Inputs: `self_employment_income` is gross 1099 income before expenses; put expenses (mileage, supplies, phone) in `business_expenses`. If the user gives only net profit, put it in `self_employment_income` and omit expenses. W-2 wages go in `w2_wages`, paycheck federal withholding in `federal_withholding`. For married filing jointly, put the spouse's amounts in the `spouse_*` fields so each Social Security wage base is right. Do not ask for an SSN, bank details, or tax documents. Ask for filing status if it is unknown.

Reply with the total federal tax, the self-employment tax and income tax split, the set-aside percent, the quarterly amount and dates, and the PDF and calendar links. Repeat each warning. Say once that the result is an estimate, not tax advice, and that state tax is not calculated unless the state has no income tax.

Do not use for filing a return, logging in to tax software, paying the IRS, explaining what a 1099 form is, or tax years other than 2026.
