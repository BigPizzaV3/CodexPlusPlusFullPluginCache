---
name: invoice-ledger
description: Turn several supplier invoices (rows, invoice PDFs with selectable text, or pasted invoice text) into one Excel and CSV ledger with tax by rate, totals per supplier, and duplicate-number and wrong-total checks, using the generate_invoice_ledger tool.
---

# Zovo Invoice Ledger

Use `generate_invoice_ledger` when the user wants a batch of invoices in one spreadsheet, a purchase ledger, a VAT/GST/sales-tax summary by rate, or a check for duplicate invoices and totals that do not add up.

1. Values in the chat or a screenshot: send one object per invoice in `invoices` (supplier, invoice_number, invoice_date, due_date, currency, net, tax or tax_rate, gross). Several rates on one invoice go in `tax_lines`. Rates are percents (20, not 0.2).
2. Attached invoice PDFs: pass them in `files` (up to 20). Scanned PDFs have no text and are skipped; ask the user to type those values.
3. Pasted invoice text: one string per invoice in `invoice_texts`. Use `text` only when you cannot split it.
4. Pass `currency` when the invoices show only "$" or no currency. Pass `date_order` (DMY or MDY) if the user says which.
5. After the tool returns, give the totals per currency, the tax by rate, every flagged invoice verbatim, and the Excel and CSV links (they expire in about an hour).

Amounts in different currencies are never added together. Do not use this skill to create or send an invoice, to convert currencies, to read line items, or to decide whether tax can be reclaimed.
