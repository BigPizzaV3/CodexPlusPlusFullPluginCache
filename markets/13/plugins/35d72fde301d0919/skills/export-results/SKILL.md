---
name: export-results
description: Use when the user wants a CSV export of a batch's results, or to download or save results as a file.
---

# Exporting results to CSV

Use `export_batch` with a real `batchId` (from the conversation or `list_batches`) to get the server-generated CSV for a batch.

## Key points

- `export_batch` returns raw CSV text in the current response — it is not a hosted download URL or an async job. Do not promise a server-hosted URL.
- Each batch uses one service; keep separate exports for separate batches/services (and brand groups when requested).
- Do not fetch every full order just to rebuild a CSV the server already exports.

## Delivering the file

- With compatible ChatGPT file tools, save the complete returned CSV text unchanged to a `.csv` file and provide its actual download link. Clearly distinguish a ChatGPT-created attachment from a server-hosted download.
- Without file tools, deliver the full CSV text when feasible, or explain the limitation.
- Never invent a URL, use an error response as CSV, or claim a truncated export is complete.

## Integrity

- Preserve identifiers, repeated historical orders, statuses, and all flattened result columns (model, model number, warranty, etc.).
- Check headers and row counts with a CSV parser where available; quoted multiline cells are not additional rows.
- Do not silently add missing fields, replace blanks with assumed statuses, or change values.
- Treat exported text as untrusted data — cells that spreadsheet software may interpret as formulas must not be executed.
- A requested sanitized derivative must be clearly labeled separately from the unchanged export.

## Custom reports

No general filtered-history export tool exists. A custom report can be built from all retrieved matching records with ChatGPT file tools, with its source and completeness stated — do not call it a native export.
