---
name: lapyme-sales-invoicing
description: Create, invoice, return, or credit sales in La Pyme when Argentine voucher rules, customer and point-of-sale resolution, tax treatment, totals, or fiscal issuance matter. Do not use for general sales analytics.
---

# La Pyme Sales And Invoicing

Use La Pyme's sales tools to complete the user's requested commercial or fiscal outcome without guessing identifiers or repeating a write.

## Choose The Operation

- Use `list_sales` to find a sale and `get_sale` to inspect one sale and return its in-product document review route.
- Use `save_sale` without `id` to create a sale. With `id`, it only updates supported metadata and tags; it does not replace items, totals, or payments.
- Use `invoice_sale` only when the user has explicitly requested fiscal issuance for an existing sale.
- Use `create_sale_return` for a return linked to an existing sale. Read the sale with `get_sale` first because each returned line needs its `saleItemId`.
- Use `save_credit_note` for a standalone credit note that is not a return against one recorded sale.
- Use `list_voucher_types` with the complete customer, point-of-sale, amount, currency, and exchange-rate context when voucher eligibility is uncertain.

Read `context://core-rules` and `context://fiscal-rules` when their rules affect the request.

## Build A Valid Sale

- Money values are cents. Interpret business dates in Argentina local time and send them as `YYYY-MM-DD`.
- Customer, point of sale, product, warehouse, and payment-method inputs accept visible names or identifiers. Prefer the user's visible reference. If resolution is ambiguous, use the returned candidates instead of guessing.
- A catalog item needs `product`, `warehouse`, `quantity`, and `unitPrice`. It inherits the product tax rate.
- A custom item needs `name`, `quantity`, `unitPrice`, and `taxRateId`.
- `taxRateId` uses AFIP identifiers: `3` is 0%, `4` is 10.5%, `5` is 21%, `6` is 27%, `8` is 5%, and `9` is 2.5%. A 0% line is not the same as an exempt line; exempt lines also use `isExempt: true`.
- `total` is the final amount in cents and must match the lines. Invoice A item prices are net of IVA. Invoice B, Invoice C, and voucher X item prices are final prices; voucher X does not discriminate IVA.
- USD sales need `exchangeRate` in Argentine pesos per US dollar. Set `sameCurrencyPayment: true` when an embedded payment collects the USD sale in USD.
- Do not combine `paymentMethods` with `isFullAmountPending: true`.

If a customer is not found, search with plausible name or email variants before creating a new customer. Create one only when the user requested a new customer or confirms that no existing match is correct.

## Protect Fiscal And Retry Safety

An exact request to create, invoice, return, or credit is sufficient authorization for that operation. Do not convert a request to inspect, calculate, or draft into a write.

Invoke a write once. If the result is uncertain, or a follow-up effect such as tag application fails after the sale was created, inspect the sale and continue from the returned recovery instruction. Do not resend the full creation or fiscal-issuance call. Report the created sale, issued voucher, partial failure, or unresolved input precisely.

Government identifiers must be entered in La Pyme. Do not request DNI, CUIL, or CUIT, search by them, or return document downloads. Select an existing contact by name or a returned internal id; preserve stored fiscal data. If fiscal configuration is missing, direct the user to La Pyme and retry only the uncompleted operation.
