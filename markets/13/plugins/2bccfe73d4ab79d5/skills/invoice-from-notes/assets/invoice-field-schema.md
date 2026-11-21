# Invoice field schema — Mizar

Canonical JSON: `invoice-schema.json`. All money values are **strings** with 2 decimals (`"110.00"`) to avoid float errors. Dates are ISO `YYYY-MM-DD`.

## Seller (`seller`)

| Field | Required | Notes |
| --- | --- | --- |
| name | yes | Legal/business name |
| address | yes | Multi-line string |
| email | no | |
| tax_number | conditional | Company tax registration number of the business (DE: business Steuernummer), if no vat_id. Alias: `company_tax_number`. Not a personal ID. |
| vat_id | conditional | Business VAT number (e.g. DE123456789); required for EU reverse charge / intra-EU. Alias: `vat_number`. Not a personal ID. |
| bank.iban, bank.bic, bank.account_holder | conditional | Required unless `payment_instructions` given |
| payment_instructions | no | e.g. "PayPal: billing@…" |

## Client (`client`)

| Field | Required | Notes |
| --- | --- | --- |
| name | yes | |
| address | yes | |
| vat_id | conditional | Client company's business VAT number; required for reverse charge. Not a personal ID. |
| po_number | no | Client purchase order |

## Invoice meta

| Field | Required | Notes |
| --- | --- | --- |
| number | yes | Unique, sequential; user-provided. Never invented. |
| issue_date | yes | Default: today in user's timezone — state it |
| service_date / service_period | yes (DE) | Single date or `{from, to}` |
| due_date or payment_terms_days | yes | Due date = issue_date + days |
| currency | yes | ISO 4217; MVP: `EUR`, `USD` |
| language | no | `en` (default) or `de` |
| status | no | `draft` or `final`. Missing required field ⇒ must be `draft` |

## Line items (`lines[]`)

| Field | Required | Notes |
| --- | --- | --- |
| description | yes | What was delivered |
| quantity | yes | Decimal string; hours, pieces, days |
| unit | no | `h`, `day`, `pcs`, `flat` |
| unit_price | yes | Net unless `prices_include_tax: true` |
| tax_rate | yes | Percent string: `"19"`, `"7"`, `"0"` |

`amount = round_half_up(quantity × unit_price, 2)` — computed, never typed in.

## Adjustments

| Field | Required | Notes |
| --- | --- | --- |
| discount | no | `{type: "percent"|"fixed", value}` applied to net before tax, pro-rata per tax rate |
| prices_include_tax | no | Default `false` |
| tax_note | conditional | Required text when any line is 0 % (exemption or reverse charge) |
| notes | no | Free text footer |

## Totals (computed — `compute_totals.py` / `compute_invoice_totals`)

`net`, `discount_total`, `tax_by_rate: [{rate, base, tax}]`, `tax_total`, `total`.
Tax is computed per rate group on the (discounted) base, rounded half-up to 2 decimals.
