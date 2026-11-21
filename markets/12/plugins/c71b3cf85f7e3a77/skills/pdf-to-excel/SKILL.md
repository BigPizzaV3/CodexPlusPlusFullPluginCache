---
name: pdf-to-excel
description: Read the tables in a text-based PDF with the convert_pdf_tables and list_pdf_tables tools, type the columns, and download an Excel workbook (one sheet per table) plus a ZIP of CSV files.
---

# Zovo PDF to Spreadsheet

Use `convert_pdf_tables` when a text-based PDF is attached and the user wants its tables as Excel or CSV. Use `list_pdf_tables` when the user only wants to see which tables the PDF holds before exporting.

1. Call the tool with the attached `file`. Add `pages` (e.g. `1-3,5`) only when the user names pages.
2. Leave `merge_tables` at its default (`true`) so a last table that continues as the first table on the next page with the same source header and column count is joined and the repeated header is removed. Pass `merge_tables: false` only when the user wants each page kept apart.
3. If the detected column type is wrong, call `convert_pdf_tables` again with `column_types`, e.g. `[{"table":1,"column":2,"type":"text"}]`. The widget's per-column type switches send this for you.
4. Report the number of tables, each table's row and column count with its column types, any warning (scanned page, merged or wrapped row, truncated pages), and the two download links. Say the links expire in about one hour.
5. Text PDFs only. Scanned or image-only pages are reported as "no text layer" and are not read (no OCR). The limit is 15 MB and 50 pages.

Do not use this skill to edit a PDF, to read an image-only PDF without OCR, or to make QR codes or barcodes.

High-precision numeric values remain original text with a warning. If a text cell exceeds 32,767 characters, split it into shorter source rows and upload again; conversion returns an actionable error without partial downloads.
