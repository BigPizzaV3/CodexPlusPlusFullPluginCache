---
name: files-and-labels
description: Use when the user provides a CSV/PDF of identifiers to check, or asks for printable labels, barcode PDFs, or other file-based outputs.
---

# Files and printable labels

IMEILookup receives identifier strings, not files directly. File reading and PDF/barcode generation are ChatGPT-assisted tasks using compatible ChatGPT file tools.

## Reading identifiers from files

- With compatible file-reading tools, extract identifiers from the intended CSV column or a readable barcode PDF.
- Preserve leading zeros; avoid spreadsheet number conversion (numbers can lose precision).
- Reconcile extracted values with the source. If a PDF has conflicting printed vs barcode values, or a scan is unreadable, ask for clarification before ordering.
- Never invent a missing digit or assume a numeric cell can be restored after precision loss.
- Apply the same cleanup and service-compatibility rules as `run-device-checks`.
- If file tools are unavailable, explain the limitation and ask for identifiers as text. Do not claim the plugin parsed a file.

## Printable labels and barcodes

- Use exact device identifiers and actual returned result fields. Do not infer missing model, model number, warranty, MDM, or other values.
- For a final-stage MDM label, use only devices that reached the authorized MDM stage and their returned MDM results (including failures if requested).
- Use the user's label size/printer requirements when supplied; otherwise state the chosen size and provide a preview.
- Include human-readable identifiers, keep text within the label, and verify the encoded barcode value against its source.
- Render and inspect the PDF before delivery when rendering tools are available. If verification or rendering isn't possible, say so.
- Creating a printable PDF does not send it to a printer.
