---
name: ar-aging
description: Build an accounts receivable aging report, one-page customer statements and polite past-due reminder email drafts from open invoices (typed, pasted CSV/TSV, or a QuickBooks, Xero, FreshBooks or Wave CSV/XLSX export) with the generate_aging_report and generate_customer_statements tools.
---

# Zovo AR Aging Report

Use `generate_aging_report` when the user asks for an AR aging report, aged receivables, who owes them money, or how late customers are. Use `generate_customer_statements` when they want customer statements or statements of account.

1. Pass the invoices exactly as the user gave them. An attached export goes in `file`. Typed invoices go in `invoices` as objects (`customer`, `invoice_number`, `invoice_date`, `due_date` or `terms`, `amount`, `amount_paid`), or as the pasted text. Never invent invoices, amounts or dates.
2. Pass `as_of_date` when the user names a date ("as of October 31"). Without it the tool uses the date in the export's title line, else today in New York, and says which.
3. Pass `credit_sales` (and `sales_period_days` if not a year) only when the user gives sales and wants DSO.
4. After the tool returns, give the total receivable, the past-due amount, the five bucket totals, the customers most past due, any rows left out, and the download links (they expire in about an hour).
5. Reminder email drafts state only invoice facts. Share them as drafts; the user sends them. Offer `generate_customer_statements` after an aging report.

Do not use this skill for accounts payable (bills the user owes), for sending emails, or for connecting to QuickBooks or Xero.
