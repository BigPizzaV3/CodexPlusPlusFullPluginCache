---
name: altodocs-spreadsheets
description: Create and edit saved native AltoDocs spreadsheet workbooks, tabs, cell values, formulas and supported styles from conversation data. Use when the requested result is a standalone spreadsheet, rather than a MathCanvas sheet or report table.
---

# Native spreadsheet files

Use the available spreadsheet tools for the requested standalone workbook.
`create_spreadsheet` creates named tabs; `list_spreadsheet_sheets` returns their
real IDs; `read_spreadsheet` and `edit_spreadsheet` operate on saved cells. Do not
substitute a report table or MathCanvas sheet without the user's agreement.
If these tools are absent in the host/grant, state the missing capability.

Use conversation data or values the host has actually extracted from an
authorised attachment. Keep unknown cells unknown and source/formula assumptions
explicit. This tool surface does not import an XLSX binary or fetch an external
workbook. Resolve the destination with project/file discovery; use the workspace
workflow when project/folder creation or a file lifecycle operation is requested.

For a new file, use new request/document UUIDs, a meaningful title and unique tab
names. After creation, obtain tab IDs with `list_spreadsheet_sheets`. For an
existing file, read its saved content version and target range first. Omit
`sheetId` only if there is exactly one tab.

Cell/range coordinates are zero-based. Use ascending bounded ranges, not an
entire million-row sheet; `read_spreadsheet` and clear ranges are limited to
20,000 cells. A `set_cells` batch has at most 2,000 cells, and an edit batch at
most 100 operations. Write either a value or a formula for a cell, never both;
formulas start with `=`. Apply only supported schema styles. Preserve untouched
cells and tabs. Use add/rename/duplicate/delete tab operations only as requested.

**Formula source is saved, not recalculated by these connector tools.** A cached
display value is not proof of a new result. Read back the exact cell values,
formula strings and styles and state when recalculation has not been verified.
Do not claim arbitrary Excel compatibility, charts, merged-cell authoring,
pivots or filters. If separate calculation is useful, label it as a separate
evaluation rather than a recalculated workbook result.

Use the latest `expectedVersion` for writes. Retry a lost response with identical
UUID and payload; re-read after conflicts. After saving, verify the affected
range and tab list. Return the actual spreadsheet URL and a short description
of the saved source changes. Retain the same workbook on follow-up edits unless
the user requests a copy.
