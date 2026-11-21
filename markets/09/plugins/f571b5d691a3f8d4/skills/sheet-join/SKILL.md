---
name: sheet-join
description: Spreadsheet merge tools. join_spreadsheets joins two CSV/Excel files on an ID column (VLOOKUP job) with counted key clean-ups (spaces, case, leading zeros, Excel number formats), unmatched-row reasons and duplicate checks; combine_spreadsheets stacks up to 24 files with drifting column names into one sheet and lists every column decision.
---

# Zovo Spreadsheet Merge

Use `join_spreadsheets` when the user wants to VLOOKUP, match or merge two files side by side on an ID: "vlookup two spreadsheets", "merge orders with customers by customer ID", "why don't these IDs match". Pass the main file (rows to keep) as `left_file` and the lookup file as `right_file`. One workbook with both tables on two sheets can go alone in `left_file`. Without files, paste each table as CSV text in `left_table` / `right_table`, header row first.

1. Leave `left_key`/`right_key` out unless the user names the key; the tool explains the key it picked. Use a list for a two-column key.
2. `join_type` left (default) keeps every left row; inner = only matches; full = everything.
3. If the user says IDs are case-sensitive, or that 0123 and 123 are different codes, pass `skip_normalizations` (["case"], ["zeros"]).
4. Reply with the match rate first, then each clean-up with its row count (these are the rows a plain VLOOKUP misses), the unmatched reasons, duplicate-key warnings, and the two download links (they expire in about an hour). Quote keys exactly as the tool shows them.

Use `combine_spreadsheets` to stack or append files: "combine 12 monthly CSVs", "combine excel files with different column names", "combine all sheets into one". Pass all files in `files` (up to 24), or pasted tables in `tables`. Read back the column decisions, list every fuzzy match under "please confirm", and offer `column_map` (e.g. {"Amt":"Amount"}) to change any. Pass `date_order` only when the user states the date format.

Do not use these tools for mail merge (letters, labels, emails), for comparing two drafts of a document, or for explaining Excel formulas.
