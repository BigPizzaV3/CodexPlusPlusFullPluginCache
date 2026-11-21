---
name: gst-invoice
description: Make an Indian GST tax invoice (GST invoice format, GST bill format) as a PDF and Excel file with the generate_gst_invoice tool, with CGST + SGST or IGST by place of supply, a GSTIN check, an HSN summary and amounts in words.
---

# Zovo GST Invoice Maker

Use `generate_gst_invoice` when the user wants a GST invoice, GST bill or tax invoice for India.

1. Put the details into fields: `seller` {name, gstin, address, state}, `buyer` {name, gstin if registered, address, state}, `items` [{description, hsn, qty, unit, rate, discount, gst_rate}]. Convert pasted text or a photo of an order into these objects. `details` is only a fallback.
2. `rate` is the price per unit before GST. If the user's prices include GST, set `prices_include_gst: true`. `gst_rate` is the total rate (18, not 9 + 9).
3. Do not guess a GSTIN or an HSN code. If the user gives none, leave it empty; the tool flags what is missing. Do not pick the GST rate for an item yourself; ask if it is not given.
4. Optional: `invoice_number`, `invoice_date` (day first, e.g. 28/10/2026), `place_of_supply`, `ship_to`, `reverse_charge`, `bank`, `terms`, `copies` (1, 2 or 3), `page_size`.
5. After the tool returns, give the total and the tax split (CGST + SGST or IGST) with the reason (place of supply vs seller state), repeat any GSTIN or HSN warnings word for word, and share the PDF and Excel links.

Do not use this skill for invoices outside India, GST return filing, e-invoices with an IRN or QR code, or e-way bills.
