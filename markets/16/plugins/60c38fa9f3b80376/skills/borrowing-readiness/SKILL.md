---
name: borrowing-readiness
description: Assess whether someone is ready to take a loan and how lenders will see them — reading their credit report, overall financial health, irregular freelance or gig income, and what-if scenarios like taking a new loan or closing one. Use for "why was my loan rejected", "explain my CIBIL report", "am I ready for a loan", "I'm a freelancer, how much can I borrow", "what happens if I take a ₹5L personal loan".
---

# Borrowing readiness

Explicit instructions from the user override this workflow.

## Credit report
If the user shares a CIBIL / bureau report, read the score, total card limits and balances, hard enquiries in the last 6 months, 30+ day late payments in 24 months, any settled / written-off / SMA status, oldest account age, and active secured vs unsecured loans. Call `explain_credit_report`. Explain each factor plainly and give the time-based habits from the result. Be explicit that accurate entries cannot be removed; for inaccurate ones, explain the free bureau dispute route from `disputeRights`. Never suggest paid "credit repair".

## Financial health and what-ifs
Collect take-home income, fixed monthly expenses, each existing loan (outstanding, EMI, rate, months left), emergency savings and other savings. Call `check_financial_health`. For a "what if" question, call it once with `whatIf` and present before → after.

## Irregular income
For freelancers, gig workers and business owners, get 6–12 months of income (or total the credits in a bank statement the user shares, excluding own-account transfers, refunds and loan disbursals). Call `assess_variable_income`. Explain that banks average two years of ITR income and plan EMIs around the lowest months.

## Answer format
Start with a one-line readiness verdict, then the 2–3 factors that matter most, then concrete next steps with timeframes. Don't repeat account numbers or personal identifiers from documents.
