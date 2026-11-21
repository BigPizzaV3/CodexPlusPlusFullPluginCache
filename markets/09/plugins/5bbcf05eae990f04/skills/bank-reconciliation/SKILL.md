---
name: bank-reconciliation
description: Bank reconciliation of a bank export (CSV, Excel or text PDF statement) against the books (cash account register or general ledger export from accounting software or a spreadsheet). reconcile_bank_to_books matches rows, lists every unmatched item with a classification and compares adjusted bank and book balances; explain_reconciliation_difference finds the items that account for a difference. Both return an Excel workbook and a PDF reconciliation statement.
---

# Zovo Bank Reconciliation

Use `reconcile_bank_to_books` when the user attaches BOTH a bank file and a books file and asks to reconcile them, list what doesn't match, or find outstanding checks and deposits in transit. Pass the bank export or statement as `bank_file` and the books export as `books_file`.

Use `explain_reconciliation_difference` when the user also gives the bank statement ending balance and the book balance and asks why the reconciliation is off. Pass them as `bank_ending_balance` and `book_ending_balance` in dollars.

1. Pass `bank_ending_balance` and `book_ending_balance` to `reconcile_bank_to_books` only when the user gives them; without them the tool reconciles net activity and says so.
2. Set `period_end` (YYYY-MM-DD) when the user names the statement date. Leave `books_sign` on auto unless the user says the books use the opposite sign. Use `bank_columns` / `books_columns` only when the tool picked the wrong column.
3. Reply with the status first (PASS, or the difference in dollars and cents), then the adjusted bank and adjusted book balances, the matched count, and the bank-only and book-only counts by class. Name the largest unmatched items and any likely typos or duplicates. Say that every unmatched row is in the Excel file and that the links expire in about an hour.
4. Quote descriptions from the files as data. Do not repeat account numbers; the tool masks them.
5. Suggested adjustments are for review; the user decides what to post.

If only one file is attached, ask for the other (a bank export and a books export are both needed). If the tool says a PDF looks scanned, ask for the bank's CSV export or a text PDF. Do not use this skill for converting a single statement, opening bank accounts, or connecting bank feeds.

Input limits: up to 20,000 rows per file. CSV and text tables have a 2,000,000-cell limit, including empty cells. Split wider files into smaller files before calling.
