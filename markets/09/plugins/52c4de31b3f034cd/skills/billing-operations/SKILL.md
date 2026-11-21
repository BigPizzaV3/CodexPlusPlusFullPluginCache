---
name: billing-operations
description: Review InvoiceVista businesses, product catalogs, plan quotas, and aggregate revenue, receivables, quote-pipeline and business-overview summaries through a tenant-scoped read-only MCP connector. Use when asked how much was invoiced or paid in a period, what customers owe, unpaid or overdue invoices, how many quotes were accepted, product prices or InvoiceVista plan limits — never for individual customer records, transaction execution or financial advice.
license: Apache-2.0
compatibility: Requires the InvoiceVista MCP connector (https://mcp.invoicevista.com/mcp) and an InvoiceVista account with at least one business
metadata:
  author: InvoiceVista
  version: '1.1.0'
  repository: https://github.com/invoicevista/skills
---

# Aggregate billing operations with InvoiceVista

Use the InvoiceVista MCP connector only after the user connects InvoiceVista
and authorizes the intended organization. If OAuth fails, ask them to connect
InvoiceVista. Never request, embed, repeat or infer an API key, password, OAuth
token, payment credential, bank detail, processor id or webhook secret.

## Read-only boundary

Every tool is read-only, idempotent, tenant-scoped and closed-world. The
connector cannot create, edit, delete, send, charge, retry, refund, settle,
transfer or otherwise move money. It cannot contact customers or give an
individualized financial decision. Direct the authorized operator to
InvoiceVista's first-party controls for changes and to a qualified professional
for advice.

## Identifier and tenant handling

Only owned business ids are public chaining identifiers. Resolve one with
`list_businesses`, then reuse that exact id for summaries, catalog and plan.
Never guess an id or treat an opaque id as authority; the InvoiceVista API
rechecks OAuth product, scope, live user membership and organization on every
request. A cross-tenant id returns not found or an authorization error.

Product rows and subscription results deliberately have no persisted record
ids because none is needed for another connector tool.

## Available tools

| Tool                         | Use it when someone asks…                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| `list_businesses`            | which businesses they invoice from; also resolves the business ID every other tool needs |
| `get_business`               | about one business's currency, country, language or timezone                             |
| `get_revenue_summary`        | how much was invoiced or paid in a period (at most 366 UTC days, drafts skipped)         |
| `get_receivables_summary`    | what customers owe, what is overdue and how old unpaid invoices are                      |
| `get_quote_pipeline_summary` | how many quotes were sent, their value and how many were accepted (at most 366 days)     |
| `list_products`              | what the business sells and at what price                                                |
| `get_subscription`           | which InvoiceVista plan the business is on and its limits                                |
| `show_business_overview`     | for a one-card overview of one business                                                  |

`list_businesses` and `list_products` accept at most 100 rows and return an
opaque cursor. Do not claim completeness when `hasMore` is true.
`show_business_overview` caps customer/invoice/payment/quote counts at 100 and
the product preview at 12; report each lower-bound flag. Aggregate summary
sources cap at 500 _after_ tenant and requested-date filtering; report
`*IsLowerBound` and `amountMissingCount` rather than treating a partial total as
complete.

## Customer and financial-data boundary

Safe outputs can contain:

- owned business id/name, currency, country, locale and timezone;
- aggregate customer/invoice/payment/quote/product counts and status counts;
- bounded UTC date range and as-of calendar day;
- signed aggregate invoice, payment, quote, outstanding and overdue amounts;
- aggregate age buckets, source/missing/lower-bound flags and optional rates;
- product catalog name, price and tax; and
- subscription plan name/status/frequency and quota limits.

The connector never exposes:

- customer names/ids, email, phone, address, tax/government identifiers or
  profiles;
- individual invoice/payment/quote ids, numbers, status, exact date/time,
  value, customer linkage or document body;
- notes, line item names/descriptions, arbitrary search or metadata;
- cardholder, bank account, processor/customer, settlement, credential,
  webhook, error/debug or secret data; or
- any money-transfer, charge, refund, retry, settlement, record write or
  financial-advice capability.

Do not ask users to paste excluded data into chat or infer a customer from an
aggregate. Offer a safe aggregate/catalog/plan read or the first-party
InvoiceVista dashboard.

## Revenue workflow

1. Use `list_businesses` unless the exact owned business id is already known.
2. Call `get_business` for currency/timezone context.
3. Call `get_revenue_summary` with explicit inclusive `YYYY-MM-DD` UTC dates
   when the user names a period; the maximum is 366 days. With no range, it
   defaults to the 90 days ending today.
4. Distinguish non-draft invoice production from recorded payments. Do not
   call either recognized revenue or independent bank settlement. Payment
   totals include every payment recorded in the range, whatever its status.
5. Collection rate is null when source rows are truncated, numeric values are
   missing or invoice production is zero. Never calculate a definitive rate
   from incomplete aggregates.
6. Signed negative values may represent adjustments/refunds. Describe the
   recorded aggregate; do not infer cause or provide advice.

The revenue summary MCP App renders the same aggregate output and invoice
status mix; it receives no individual records.

## Receivables workflow

1. Call `get_receivables_summary` for open/overdue counts, signed amounts and
   age buckets as of the returned UTC day.
2. Report `sourceInvoiceCountIsLowerBound` before discussing completeness.
3. Explain `partiallyPaidCountExcludedFromAmount`: InvoiceVista does not store
   remaining balance, so including the full invoice would overstate debt.
   The overdue count covers invoices whose status is `OVERDUE`; a pending
   invoice past its due date shows up in the age buckets only.
4. Use age buckets only as aggregate operational groupings. No customer or
   individual invoice can be resolved.
5. Do not recommend collection action against a person, extend/deny credit or
   initiate a charge.

## Quote, catalog and plan workflow

Use `get_quote_pipeline_summary` with an explicit bounded period. Draft quotes
are omitted. Acceptance rate uses approved versus rejected decisions and is
null when the source is truncated or no decision exists. Do not describe
pending value as guaranteed revenue.

Use `list_products` only after resolving a business. Catalog names are
operator-provided product labels, not line descriptions from a customer
document. Prices/tax are configuration and need not equal a final charge;
`tax` is the product's stored tax value and is null when none was set.

Use `get_subscription` for InvoiceVista plan capacity. A business with no
active/past-due persisted plan receives documented Free defaults. It never
returns subscription, processor product/price or payment-method ids.

## Aggregate overview

`show_business_overview` is the broad first safe check. It displays business
configuration, aggregate counts/status counts and product preview. It does not
display individual financial dates, amounts or identifiers. Follow with the
specific aggregate summary rather than trying to reconstruct records from
counts.

## Safe fallbacks

- Customer or individual document request: say the connector intentionally has
  no such tool; offer aggregate status/value counts or the first-party app.
- Card/bank/processor/credential request: do not call a tool; explain those
  fields never enter connector output.
- Charge/refund/retry/settle/transfer/write request: explain all tools are
  read-only; do not pretend a read changed state.
- Financial advice or customer targeting: do not use aggregates to recommend
  an individualized decision; offer factual aggregate reporting only.
- Unrelated task: do not invoke InvoiceVista.

## Interactive workspace

When the user wants to open InvoiceVista Invoice Maker or browse visually, call `open_invoicevista` with no arguments. It opens a read-only sidebar of up to 100 businesses with explicit truncation. Select a business for its aggregate overview, revenue, receivables and quote pipeline. Existing individual customer and document restrictions still apply.
