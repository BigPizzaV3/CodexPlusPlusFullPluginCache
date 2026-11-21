---
name: lapyme-business-reporting
description: Answer La Pyme business and accounting questions when choosing a report source, period, dimensions, measures, filters, or the correct reporting tool matters. Do not use for a simple lookup of one known record.
---

# La Pyme Business Reporting

Choose the smallest reporting path that answers the user's question, state material assumptions, and preserve La Pyme's money and date semantics.

## Route The Question

- Use a `list_*` tool for filtered records and a `get_*` tool for one known record.
- Use `run_report` for totals, grouped analysis, rankings, trends, comparisons, and operational analytics across sales, purchases, payments, commissions, treasury, or inventory.
- Use `get_accounting_report` for income statements, trial balances, journal entries, summarized journals, account ledgers, and receivables/payables aging (`accounts_receivable` for "quién me debe", `accounts_payable` for "a quién le debo"). Do not use `run_report` for accounting statements.
- Use `get_accounting_report` for account ledgers and summarized journals, and the named cost-center tools for references.

Read `reporting://catalog` when the correct source, measure, dimension, filter, or measure semantics are not already clear. Read `context://reporting-rules` for period and interpretation rules.

## Shape Operational Reports

- `run_report` needs a source. Select measures that answer the question and add dimensions only for the requested breakdown; omit dimensions for a total.
- Use dimension `filters` for entities and attributes. Use `resultFilters` for computed measures. Do not put measures in dimension filters.
- Use natural entity references when supported. For product-name text searches, use the catalog's product-name filter instead of treating a partial name as an exact product identifier.
- Use a compact page size and follow `nextCursor` until the requested result set is complete. Do not treat the first page as the full result.
- For custom product or contact fields, read the catalog and use the canonical metafield dimension or an unambiguous visible name.
- For "clientes que dejaron de comprar" or "clientes inactivos", run a `sales` report over the last 12 months grouped by `customer`, filtered with `customerRecency` in `61-90`, `91-180`, and `181+`, and ranked by `total`. `customerRecency` is how long ago the customer's last purchase was, counted from today; it also works as a dimension for the whole distribution.
- For "nuevos vs recurrentes", group `sales` by `customerType`. It classifies each sale by whether it was the customer's first purchase, using their whole history. Sales to the default Consumidor Final are `unidentified` in both dimensions; say so when they are a large share.

## Apply Date And Money Semantics

- Interpret periods in Argentina local time (`UTC-3`) and use `YYYY-MM-DD` dates.
- Money measures use cents unless the field explicitly says otherwise. Computed metrics can contain fractional cents.
- For sales, the default commercial date basis attributes linked credit notes to the original sale date. Use the fiscal date basis for AFIP books, fiscal exports, or voucher-issue-date totals.
- Read the catalog before interpreting percentages, balances, rates, or inventory snapshot measures.
- Do not combine a period preset with explicit start and end dates.

## Handle Accounting Reports

- Start with `income_statement` for revenue, expense, gross-margin, EBITDA, or net-result questions. Use `account_ledger` when the user asks for the movements behind one account.
- `account_ledger` needs one account reference: id, code, or name. Use the returned options when a visible name is ambiguous.
- Pagination applies to journal entries, summarized journal, and account-ledger rows, not to statement totals.
- State when the tool's default accounting period was used because defaults differ by report type.

If a report is empty, inspect the period, date basis, filters, resolved references, and pagination before concluding that the business value is zero. Present the answer in the user's requested currency and language while keeping the underlying units explicit.
