---
name: sheet-compare
description: Compare two versions of a spreadsheet (CSV, TSV or Excel) and list all added, removed and changed rows with old -> new values, as a summary plus Excel and CSV downloads.
---

# Zovo Spreadsheet Compare

Use this when the user has an OLD and a NEW version of the same table (price list, inventory, roster, budget, product
catalog, CRM export) and asks what changed.

1. `compare_spreadsheets`: the full change set. Pass the attached files as `old_file` and `new_file` (the older one is
   usually the earlier date or lower version). Small tables typed in chat go in `old_table` / `new_table` as CSV text
   with a header row.
2. `summarize_changes`: the same inputs, when the user wants counts and the biggest changes by column (how many prices
   went up, average change) rather than the row-by-row list.

Options: `key_columns` when the user names the ID column or the automatic key is wrong; `ignore_columns` for columns
like "Last updated"; `column_map` for renamed columns; `ignore_case`, `numeric_tolerance` (e.g. 0.01) for rounding;
`old_sheet` / `new_sheet` for a specific tab; `header_row_old` / `header_row_new` when title rows sit above the headings.

Report the counts and the key explanation, list the changes the result lists, and give both download links: the Excel
file holds all changes (Changed, Cell changes, Added, Removed, annotated new version). Mention excluded total rows and
any "renamed?" columns so the user can confirm them. Do not use it to join two different tables (customers + orders) or
to compare Word or PDF documents.
