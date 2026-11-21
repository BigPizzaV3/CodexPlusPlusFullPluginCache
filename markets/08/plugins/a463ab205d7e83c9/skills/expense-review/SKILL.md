---
name: expense-review
description: Check MinzSpend expenses and expense reports in Minz.ai, including what the user submitted, what is waiting for approval, and what was approved, rejected or reimbursed in a period, with totals by status, category or vendor. Use when the user asks about their expenses, claims, reimbursements, settlements or spending in a period.
---

# Expense review

Answer questions about the user's own spending records clearly and exactly.

## Data and its limits

- `finance_expenses_search` returns amount, currency, purpose, vendor, category, status, invoice date and creation date.
  - Filters: `status` (`draft`, `submitted`, `approved`, `rejected`, `reimbursed`), `category` (exact value), and `query` (matches purpose or vendor).
  - Dates: `from` and `to` are `YYYY-MM-DD`, inclusive, and must be sent together. They filter on invoice date, falling back to creation date.
  - Paging: at most 20 rows per call. Page with `offset` (use the `nextOffset` it returns) until you have them all or the total is clear.
- `finance_reports_search` returns settlement reports (which settle a cash advance) and reimbursement reports (which pay back personal spending), with title, kind, status, creation date and number of expenses. It does not return money totals, so compute amounts from expenses, not from reports.
- `scope` defaults to `mine`: the user's own records plus those of people they are an authorized proxy for. `all` works only for users with Spend team-view, control or admin access. Use it only when the user asks about the team; if access is refused, tell them.
- Receipts, attachments, invoice numbers and tax fields are never returned. These are expense records, not accounting statements or a P&L.

## What to report

Answer the question first, for example "You have 4 expenses waiting for approval, totalling 3,200,000 VND." Then give the breakdown the user asked for, by status, category, vendor or month. Add amounts only within one currency, and list each currency separately; never convert. Name anything unusual, such as rejected items or old drafts that were never submitted.

This is a read-only view. There is no tool to submit or approve expenses, so tell the user to do that in Minz.ai. Reply in the user's language.
