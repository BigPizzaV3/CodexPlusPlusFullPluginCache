---
name: statement-converter
description: Bank and credit card statement converter. Turns a statement PDF (or a bank CSV/Excel export) into clean transactions with convert_bank_statement, reconciles opening + transactions = closing to the cent, points to missing or duplicated rows, suggests categories, and returns Excel, CSV and QuickBooks CSV files. summarize_transactions does the same for pasted transactions.
---

# Tallyproof Statement Converter

Use `convert_bank_statement` when the user attaches a bank or credit card statement and wants it in Excel, CSV or QuickBooks: "convert bank statement to excel", "bank statement pdf to csv", "does my statement balance". Pass the attached file as `file`. Accepted: text PDFs, CSV and .xlsx exports.

Use `summarize_transactions` when the user types or pastes transactions instead of attaching a file, or wants money in and out by month or category. Put each row in `transactions` with a signed `amount` (money out negative; for credit cards, charges negative and payments positive) and an ISO or MM/DD/YYYY `date`. Pass `opening_balance` and `closing_balance` only when the user gives them.

1. Leave `account_type` on auto for files. Set `credit_card` for pasted card transactions or card CSV exports.
2. Set `statement_year` only if the dates have no year and the user says which year. Set `flip_signs` only for a card export that shows purchases as positive numbers.
3. Reply with the reconciliation first: PASS, or the difference in dollars and cents and the rows the tool flags (quote its reasons). Then give money in, money out and net, the main suggested categories, each warning, and the three download links. Say the links expire in about an hour and that categories are suggestions.
4. Never repeat full account numbers; the tool shows only the last 4 digits.

If the tool says the PDF is a scan or the file is an image, do not call convert_bank_statement again with the same file. Read the transaction rows from the pages yourself and call summarize_transactions with them (it reconciles to the cent, so a misread row shows up). Ask the user for the text PDF or CSV export only when you cannot read the rows. Do not use this skill for opening bank accounts, routing numbers, tax advice, or editing non-financial PDFs.
