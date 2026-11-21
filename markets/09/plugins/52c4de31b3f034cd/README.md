# InvoiceVista plugin for Claude

Review aggregate invoicing operations inside Claude. This plugin bundles
InvoiceVista's hosted OAuth connector with one skill for safely navigating
owned businesses, product catalogs, plan quotas, revenue, receivables, quote
pipeline and aggregate operational counts.

## Requirements

An [InvoiceVista](https://www.invoicevista.com/) account with access to the
intended organization. The plugin connects to
`https://mcp.invoicevista.com/mcp`; the signed-in user's current organization
membership remains the authorization boundary. There is no API key to paste
and nothing to self-host.

## What you can ask

- “List my businesses and show the aggregate overview for the first one.”
- “Compare invoiced and collected totals for the last 90 days.”
- “Show aggregate open and overdue receivables.”
- “Summarize the quote pipeline for 2026 Q1.”
- “List the product catalog and current plan quotas.”

## Aggregate-first safety

All eight tools are read-only, tenant-scoped, bounded and field-allowlisted.
The connector never returns customer records or individual invoices, payments
or quotes. It excludes personal/contact/tax/address data, document ids/numbers,
exact customer-linked financial dates/values, notes, line text, card/bank and
processor data, credentials and raw upstream errors.

Business-level signed aggregate amounts, counts, currency and catalog
names/prices/tax are operational records—not bank-settlement proof or financial
advice. The connector cannot create/edit/delete records, charge, refund, retry,
settle, transfer or otherwise move money.

## Local validation

```shell
claude plugin validate ./plugin
claude --plugin-dir ./plugin mcp list
```

The connector should appear as `plugin:invoicevista:invoicevista` and request
OAuth on first use.

Connector documentation:
<https://www.invoicevista.com/developers/#mcp>
