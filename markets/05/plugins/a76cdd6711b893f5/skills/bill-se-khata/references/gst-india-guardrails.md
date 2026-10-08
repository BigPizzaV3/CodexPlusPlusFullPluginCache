# India GST guardrails

This skill captures source documents for bookkeeping and review. It does not make a final GST filing, place-of-supply, reverse-charge, blocked-credit, or input-tax-credit eligibility decision.

GST law, rates, portal behavior, and filing requirements can change. When the user asks for a legal interpretation, current rate, filing position, registration status, or ITC conclusion, verify against current official GST or CBIC material before answering.

## Capture from the document

Rule 46 invoice particulars include, where applicable: supplier name, address and GSTIN; unique invoice number; issue date; recipient identity and GSTIN/UIN if registered; HSN or service accounting code; description; quantity and unit for goods; total and taxable values; discounts; tax rates and amounts for CGST, SGST/UTGST, IGST, or cess; interstate place of supply; delivery address where different; reverse-charge status; and supplier signature or digital signature.

The workbook captures these fields when visible. Their absence creates a review signal; it does not by itself prove that the document is invalid.

Distinguish:

- Tax Invoice
- Bill of Supply
- Invoice-cum-Bill of Supply
- Cash Memo or ordinary Receipt
- Restaurant Bill
- Credit Note
- Debit Note
- Unknown

A bill of supply generally does not separately charge tax. Do not turn one into a tax invoice through inference.

## Tax treatment

- Capture printed tax rates and amounts as facts.
- Do not infer a missing GST rate from the product category without current verification and user confirmation.
- Do not maintain a supposedly permanent rate table in the workbook.
- Keep receipt-level tax summaries separate when item-level rates are not shown.
- Flag contradictory CGST/SGST and IGST patterns; do not silently correct them.
- GSTIN syntax validation does not prove active registration.
- Keep GSTR-2B matching distinct from source extraction.

## Input tax credit

Set ITC_Review_Status to Review required unless the user provides an approved accounting rule or explicit professional determination. Captured GST is not automatically claimable ITC.

Restaurant, catering, staff-meal, client-entertainment, personal-use, mixed-use, and non-business expenses deserve explicit review. Record the business purpose supplied by the user, but do not convert that description into a final eligibility decision.

Recommend review by a chartered accountant or qualified GST professional before filing or claiming credit when the outcome matters.

## Official references

- CBIC invoice rules: https://cbic-gst.gov.in/gst-invoice-rules.html
- GST taxpayer welcome kit: https://tutorial.gst.gov.in/downloads/news/welcome_kit_for_new_taxpyers.pdf
- CBIC accounts and records rules: https://cbic-gst.gov.in/accnt-record-rules.html

These links are reference starting points, not a substitute for checking later amendments and notifications.
