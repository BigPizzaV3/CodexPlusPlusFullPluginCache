# Receipt extraction and review

Use this workflow for photographed, scanned, printed, handwritten, multilingual, or multi-page receipts.

## Document grouping

- Inspect all images before creating rows.
- Group pages only when document continuity, supplier, invoice number, dates, line sequence, and totals support the grouping.
- Keep separate documents separate even when photographed together.
- Record the page count and one source reference at receipt level.

## Read in layers

First identify document type and header facts. Then extract item rows. Finally inspect tax summaries, totals, payment details, footer notes, QR or IRN indicators, and handwritten annotations.

Prioritize:

1. Supplier legal or trade name
2. Invoice date and number
3. Supplier GSTIN
4. Item descriptions, quantities, units, prices, discounts, and totals
5. Taxable value and CGST, SGST/UTGST, IGST, and cess
6. Grand total, payment mode, recipient, place of supply, and reverse-charge wording

## Raw, normalized, and provenance

Keep Item_Description_Raw close to the source, including original script where possible. Use Item_Description_Normalized for search and analytics. Do not translate a brand name into a generic product.

For every non-obvious derived value, set Value_Source:

- Printed — explicitly visible
- Calculated — exact arithmetic from printed inputs
- Allocated — distributed from a receipt-level amount
- User corrected — confirmed correction
- Unknown — unresolved

Allocation_Method must explain any allocation, for example Pro rata by taxable value. Leave it blank for printed values.

## Confidence

Use a 0-to-1 confidence score as an extraction signal, not a probability guarantee:

- 0.90 to 1.00: clear and directly visible
- 0.75 to 0.89: readable with minor ambiguity
- 0.50 to 0.74: plausible but needs review
- below 0.50: unreliable; leave critical values blank and create a review issue

Critical fields include supplier identity, invoice date, invoice number when present, grand total, GSTIN, and tax amounts. A high-confidence field can still fail arithmetic or consistency checks.

## Common receipt traps

- Parse Indian grouping such as 1,23,456.78 as a number.
- Treat ambiguous numeric dates as review items unless nearby text resolves the order.
- A printed percent near an item is not automatically GST; use labels and tax summaries.
- Service charge, gratuity, tip, delivery, packaging, convenience fee, discount, cess, and round-off remain separate.
- Inclusive-tax prices require explicit provenance. Do not reverse-calculate tax unless clearly necessary and label the result Calculated.
- When tax appears only in a summary, do not invent item-level rates.
- Do not infer HSN/SAC from item descriptions for filing. A tentative classification may appear only in review notes.
- A cash memo or bill of supply is not automatically a GST tax invoice.
- A logo can be a brand, while a footer may contain the legal seller. Capture both.
- Item brands or manufacturers are not the seller unless the document says so.
- Mask full card, bank, UPI, phone, and loyalty identifiers when they are unnecessary for bookkeeping.

## Reconciliation

Run the checks that the visible information permits:

- quantity × unit price, less line discount, against line amount
- sum of line amounts against subtotal
- printed tax summary against captured tax totals
- taxable value plus taxes, cess, other charges, and round-off against grand total
- CGST and SGST/UTGST rates and amounts against each other when the document presents an intra-state split
- simultaneous CGST/SGST and IGST as a consistency warning

Use the configured tolerance, initially INR 1.00. Passing within tolerance does not authorize changing a printed value.

## Review issue types

Use precise issue types: Unreadable, Missing critical field, Ambiguous date, Arithmetic mismatch, Tax inconsistency, Possible duplicate, Document grouping uncertain, Possible personal expense, GST classification review, ITC review, or GSTR-2B mismatch.

If only a total is legible, create one line named Unitemised receipt total, set Needs_Review to Yes, and explain which details were unreadable.

## Duplicate detection

Compare normalized supplier GSTIN or supplier name, invoice number, invoice date, and grand total. Also consider source-image identity when available. Mark Candidate and ask for review; never delete or merge automatically.

## Real-time response

After writing the workbook, show a compact receipt summary:

- supplier
- invoice date and number
- count of item rows
- grand total
- captured CGST, SGST/UTGST, IGST, and cess
- workbook created or updated
- open high-confidence-impact review items

Do not overwhelm the user with every empty optional field.

## Forward-test scenarios

Test behavior with: a clean itemized GST invoice; a handwritten non-GST receipt; a restaurant bill with service charge; an interstate IGST invoice; a bill of supply; a multi-page invoice; a duplicate upload; an ambiguous date with arithmetic mismatch; a total-only receipt; and a document showing separate seller and manufacturer names.
