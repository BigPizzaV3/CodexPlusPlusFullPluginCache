---
name: sheet-validate
description: Check a spreadsheet (CSV, TSV, .xlsx or a pasted table) for data errors before import or sending, with check_spreadsheet and list_spreadsheet_columns. Finds impossible and mixed-format dates, invalid emails, phone digit counts, duplicate IDs and rows, blanks, numbers stored as text, mixed decimal marks, extra spaces, lost leading zeros, 1.2E+15 IDs, formula errors and totals that do not add up.
---

# Zovo Spreadsheet Checker

Use `check_spreadsheet` when the user wants a file checked for errors, validated before an import, or searched for duplicates. Pass the attached file as `file`, or the pasted rows as `table` (CSV text, a Markdown table or a list of rows). Call it right away; no rules are needed because column types are detected from the values.

Add rules only when the user states them:
- `required_columns`: columns that must not be blank, e.g. "Email, Order ID".
- `unique_columns`: columns whose values must not repeat.
- `allowed_values`: e.g. {"Status": ["Open", "Closed"]} or "Status: Open, Closed".
- `ranges`: e.g. {"Age": "0-120"} or "Qty: >= 1".
- `total_rules`: e.g. "Total = Q1 + Q2 + Q3" or "Amount = Qty * Price".
- `date_order`: DMY when the user says dates are day/month; otherwise leave it out.
- `sheet` and `header_row` only when the user names a sheet or the header was detected wrongly.

Use `list_spreadsheet_columns` when the user asks what a file contains, which column is the ID, or wants rule suggestions before checking.

After the tool returns, give the issue count and health score, the counts per check, the first issues with row, column and the exact cell value, any notes (assumed date order, skipped title rows), then both download links (highlighted Excel and issues CSV, valid for about an hour). Say that no value was changed. Do not invent issues that are not in the result and do not claim an email or phone number exists.

Do not use this skill to compare two versions of a file, to merge files, to write Excel formulas, or to build a new spreadsheet.
