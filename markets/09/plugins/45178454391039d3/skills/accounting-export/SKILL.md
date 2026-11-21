---
name: accounting-export
description: Move a Zid store's sales, returns, payment fees and payouts into an accounting system or ERP such as Qoyod, Daftra, Wafeq, Zoho Books, Odoo, Xero or QuickBooks. Use to prepare a sales-invoice or journal import file, reconcile ZidPay payouts and fees with bank deposits, check that every order reached the books, or close a month.
---

# Accounting export

Turns a period of Zid sales into what the accounting system expects, and checks
that the books and Zid agree.

## Ground rules

- The merchant's explicit instructions, and their accountant's, take precedence over this skill.
- This skill reads Zid and produces files and reconciliations; the merchant
  imports them. Accounting-system credentials (API keys, passwords) stay in that
  system or the merchant's automation tool.
- Use the accountant's chart of accounts, tax codes and posting choices. When one
  is missing, ask rather than invent an account.

## 1. Scope

- **Period** and **what goes**: one sales invoice per order, one summary journal
  per day, payouts and fees, or all three.
- **Target system** and whether a connector already posts Zid orders there:
  `zid_account.list_installed_apps`, then [references/systems.md](references/systems.md).
  An installed app is a candidate, not proof: compare a recent sample of Zid order
  numbers with the accounting system. When the sample shows the connector posting,
  reconcile (step 5) instead of exporting the same sales again.
- **E-invoicing**: `zid_settings.list_einvoicing_units`. When a unit is
  `active`, Zid already issues the ZATCA e-invoices for those sales. The sale goes
  into the accounting system as a record that does not issue or report another
  e-invoice (a draft invoice or a journal, per the system's notes in the
  reference). Confirm that choice with the merchant before building the file.
- **Prices and VAT**: `zid_settings.get_tax_settings` shows whether prices
  include VAT.

Done when the period, the documents, the target, the e-invoicing answer and the VAT basis are settled.

## 2. Read Zid

| Need | Read |
| --- | --- |
| Orders in the period | `zid_orders.list_orders` with `dateFrom`, `dateTo`, `paymentStatus` and `perPage` 100, every page; lines, discounts, shipping and VAT per order from `zid_orders.get_order` |
| Large periods | `zid_orders_manage.export_orders` with `exportType` `detailed` (one row per product), `dateFrom` and `dateTo`; Zid emails the file, and it needs the merchant's approval |
| Returns | `zid_orders.get_credit_notes` for each returned or partly returned order |
| Period totals to check against | `zid_reports.sales_report` (revenue, discounts, shipping, tax, cost of goods, returns; `components` such as `payment_methods` or `channel`). When reports are unavailable for the store, total the orders instead |
| ZidPay payouts | `zid_payments.list_zidpay_deposits`, then `zid_payments.get_zidpay_deposit` with the numeric `depositId` for the transactions in each payout |
| ZidPay fees not yet paid out | `zid_payments.get_account_statement` with `settlementStatus` `not_yet_paid_out` or `payout_pending` (fees, VAT on fees, net, running balance) |
| Refunds | `zid_payments.list_refunds` |
| Zid Ship costs and cash on delivery | `zid_shipping.list_shipping_charges` (labels, COD fees, returns), `zid_shipping.list_cod_collected`; other carriers from their invoice or settlement report |

## 3. Build the file

Map to the target's template from [references/systems.md](references/systems.md).
When the merchant has the template, match its exact headers.

- **Keys**: the Zid order number as the invoice number or reference, and the SKU
  as the item code. Duplicate handling differs by system: before a rerun, check
  the existing references (or use the target's External ID where it has one).
- **Lines**: one per product, plus shipping and cash-on-delivery fees as lines;
  discounts per line or as a discount line, the way the target takes them.
- **Money**: plain decimals in the store currency, no symbols; VAT inclusive or
  exclusive as settled in step 1, with the target's tax code name.
- **Returns**: a credit note (or reversing journal) referencing the original invoice.
- **Customers**: the customer number or name the target matches on; business
  customers carry their VAT number.
- **Size**: split files at the target's row limit; keep each invoice's lines in one file.

## 4. Payouts and fees

For each ZidPay payout: payout amount = payments in it − refunds − fees − VAT on
fees. Post the fees and their VAT to the accounts the accountant names, and
match the payout to the bank deposit by its reference. Do the same for courier
cash-on-delivery remittances.

## 5. Check

- Order count and totals in the file equal the Zid totals for the period; list
  any difference with its order numbers.
- With a connector posting orders: compare the accounting system's sales export
  for the period with the Zid orders by order number, and list orders missing
  from the books, present twice, or with different totals.

Done when the totals agree or every difference is listed by order number.

## Output

The import file (CSV or the target's template), a summary of orders, net sales,
VAT, shipping, discounts, returns and fees for the period, the payout
reconciliation, and every row that needs the merchant or accountant.
