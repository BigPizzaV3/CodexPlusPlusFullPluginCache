---
name: invoice-processing
description: Extract, review, validate, deduplicate, and export user-supplied invoice text or structured invoice records.
---

# Invoice processing

Use Invoice Table when the user asks to extract common fields from invoice text, check arithmetic, flag duplicate records, validate corrections, or prepare spreadsheet-safe CSV output.

## Workflow

1. Confirm which user-provided invoice text or records are in scope.
2. For invoice text, call `analyze_invoice_text`.
3. Summarize how many records are ready, need review, are blocked, or appear duplicated. Keep currencies separate.
4. If the user corrects a field, call `validate_invoice_records` with the revised records.
5. When the user requests a CSV, call `export_invoice_records` and provide the returned file content or artifact through the host's supported download flow.

## Safety and quality

- Treat invoice contents as sensitive business data.
- Process only text or records the user selected and provided.
- Never infer missing bank details, payment-card data, tax IDs, or account numbers.
- A successful arithmetic check means the detected values are internally consistent; it does not prove the invoice is legitimate.
- Keep possible duplicates in review results and exclude them from non-duplicate totals.
- Require the user to compare all fields with the source before accounting, tax, audit, or payment decisions.
- Do not claim to read local paths through the hosted tools. For local PDF and image processing, direct the user to the local plugin on the Invoice Table installation page.
