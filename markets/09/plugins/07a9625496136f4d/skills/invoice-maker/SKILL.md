---
name: invoice-maker
description: Create invoices, quotes, estimates, receipts, and credit notes with exact tax and currency totals and a downloadable PDF and CSV, using the generate_invoice tool.
---

# Billwise Invoice Maker

Use `generate_invoice` whenever the user wants an invoice, invoice template, bill, quote, estimate, receipt, or credit note.

1. Collect what the document needs: who it is from (seller), who it is for (client), and line items (description, quantity, unit price). If the seller or client is unknown, create the document anyway and mention the warning; ask at most one short question.
2. Pass amounts as numbers in the document currency. Put tax rates on each line (`tax_rate`, percent) and set `tax_label` to VAT, GST, or Sales tax when the user uses that word. Never invent tax rates; use 0 if the user gives none and say so.
3. For "due in 14 days" or "Net 30" use `payment_terms_days`; for a fixed date use `due_date` (YYYY-MM-DD). Use `discount_percent` or `discount_amount` for a whole-document discount (applied before tax).
4. Use `document_type: receipt` only for a payment that actually happened, and `credit_note` with `reference` set to the original invoice number for refunds.
5. After the tool returns, state the total and due date, repeat any warnings verbatim, and give the PDF and CSV links. To change quantities or prices, call the tool again with the full corrected arguments (the widget's Edit button does this too).

Do not collect or print payment card numbers; `payment_instructions` is free text such as bank details or a payment link. This tool does not email invoices, chase payments, process payments, or give tax advice.
