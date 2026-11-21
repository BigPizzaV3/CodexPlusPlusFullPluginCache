---
name: pdf-to-excel
description: Convert one or more PDFs the user attaches (bank statement, invoice, receipt, report, price list, any table) into Excel .xlsx workbooks with Better Analyst, one workbook per PDF. Use whenever the user asks to turn PDFs into Excel, a spreadsheet, rows, or a table they can download.
---

# PDF to Excel with Better Analyst

1. Make sure at least one PDF is attached. If none is, ask the user to attach one.
2. Work out what the user wants extracted:
   - If they named columns ("date, description, amount"), pass them as `extractFields` in that order.
   - Put any other guidance ("one row per line item", "skip subtotals", "only the second table") in `instructions`.
   - If they only want some pages, pass `pageRange` such as `"2-5"`. It applies to every file.
   - Otherwise omit these; AI Extract picks sensible columns.
   - `extractFields` and `instructions` also apply to every file. If different PDFs need different columns, call `convert_pdf_to_excel` once per group of PDFs that share the same settings.
3. Call `convert_pdf_to_excel` once with every attached PDF in `files`. Do not make one call per file. If the plan's per-request limit is too low, the result says so; then convert the PDFs in smaller groups.
4. While any file is `processing`, tell the user which are still running, then call `get_conversion_status` with the `jobIds` the result names, until each is `completed` or `failed`. Each status call waits up to about 15 seconds; large PDFs can take a few minutes.
5. For each completed file, give its download as a markdown link and say how many rows were extracted. Show the preview rows as a short markdown table: at most 10 rows for a single file, at most 5 rows per file when there are several. Download links last up to an hour; call `get_conversion_status` again for fresh ones.
6. Tell the user about any file that failed or was skipped, and why.
7. If the user runs out of AI Actions, say how many the conversion needs and how many they have, and give the subscribe, upgrade, or contact link from the tool result as a markdown link. Suggest a smaller `pageRange` when that would fit their balance. Do not retry until they have more AI Actions.

Do not invent rows or values from the PDF yourself. The workbooks from the tool are the source of truth and the finished deliverables: do not download, rebuild, reformat, merge, or re-verify them with code, spreadsheet skills, or other tools. Share the links and previews, and stop.
