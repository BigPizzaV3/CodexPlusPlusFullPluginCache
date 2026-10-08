---
name: bill-se-khata
description: Extract photographed, scanned, machine-printed, or handwritten Indian receipts and invoices into an itemised Excel purchase ledger with GST capture, reconciliation checks, analytics, and a human-review queue. Use when a user uploads receipt images, asks to update an Indian expense workbook, or wants receipt-led GST or spend analysis. Do not use for generic OCR or unrelated spreadsheet work.
---

# Bill se Khata

Turn each uploaded receipt into traceable bookkeeping data without converting uncertainty into invented facts.

## Start from the source

Inspect every uploaded image at sufficient detail before extracting data. Decide whether the upload contains one receipt, several receipts, or multiple pages of one invoice. Keep documents separate unless continuity, invoice number, and totals make the grouping clear.

If the user supplies an existing workbook, render and inspect it before editing. Preserve its established layout and append to compatible tables. If no workbook is supplied, copy assets/indian-receipt-ledger-template.xlsx to a user-facing output location and work on the copy.

Read references/receipt-extraction.md for every image-ingestion request. Read references/schema.md before creating, mapping, or appending workbook rows. Read references/gst-india-guardrails.md whenever GST, tax, input tax credit, filing, place of supply, or invoice compliance is involved.

## Process the receipt

1. Extract receipt-level facts, item lines, printed tax summaries, and separately stated charges.
2. Preserve visible wording in raw fields; place cleaned wording in normalized fields.
3. Record whether each value is printed, calculated, allocated, user-corrected, or unknown.
4. Reconcile line totals, taxable value, tax components, round-off, and grand total within the configured tolerance.
5. Add ambiguous, low-confidence, contradictory, missing-critical, or duplicate-looking fields to Review_Queue.
6. Append Receipts, Line_Items, Tax_Summary, Vendors, Review_Queue, and Audit_Log together so their stable IDs remain connected.
7. Update formula-driven summaries and verify the affected ranges, formula errors, and rendered sheets before export.

## Non-negotiable data rules

- Never invent a seller, GSTIN, invoice number, date, HSN/SAC code, tax rate, quantity, price, or tax amount.
- Leave unavailable values blank. Zero means the document explicitly shows zero or a valid calculation produces zero.
- Keep supplier legal name, trade name, outlet, recipient business, and item brand or manufacturer separate.
- Do not allocate receipt-level tax or discounts to items unless the user needs allocation. If allocated, record the method and provenance.
- Keep GST, cess, service charge, delivery fee, packaging, tip, other charges, discounts, and round-off distinct.
- Do not treat service charge as GST.
- Store dates, money, quantities, and percentages as typed Excel values rather than formatted text.
- Parse Indian digit grouping correctly while preserving the printed value in review notes when interpretation is uncertain.
- Mask unnecessary account or card details; retain only the last four digits when useful.
- Keep the source image reference at receipt level.
- Treat GSTIN checks as syntax checks unless current registration status was independently verified from an official source.

## Human review

Complete the workbook even when non-critical fields are uncertain. Ask one concise question only when a critical ambiguity would materially change the accounting and cannot safely remain pending. Otherwise preserve the extraction, set Review_Status to Needs review, and create explicit Review_Queue issues.

Default ITC_Review_Status to Review required. Receipt extraction is bookkeeping assistance, not a final filing or input-tax-credit decision.

## Chat handoff

After a successful update, report the supplier, invoice date and number, item count, grand total, captured GST components, workbook status, and the small set of fields needing review. Call tax values captured or under review, never claimable, unless the user has supplied an approved determination.

Do not finish until the workbook opens, formulas are free of obvious errors, all affected sheets have been visually checked, and the final Excel file is saved.
