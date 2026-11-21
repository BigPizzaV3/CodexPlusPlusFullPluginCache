# Accounting systems

Where each system takes Zid sales and how. The merchant's own template is
authoritative when it differs from these headers: systems update templates
per account and per language.

## E-invoicing caution

When Zid's e-invoicing unit is active, the sale was already reported to ZATCA.
Systems that issue or report e-invoices when an invoice is approved or posted
(Qoyod, Daftra, Wafeq, Zoho Books with Fatoora, Odoo's Saudi journals) could
report it a second time. Import such sales as drafts or as
journal entries until the merchant's accountant confirms how the system treats
imported invoices.

## Systems

| System | Zid connector | Sales import | Journal import | API |
| --- | --- | --- | --- | --- |
| Qoyod (قيود) | Apps 874 (Qoyod) and 3158 (Qoyod from Fai). Fai sends new orders as sales invoices, on arrival or at a chosen status, and can number them with the Zid order number. | Sales → Sales Invoices → Import; the account's Excel template; up to 5,000 rows. Columns include reference, customer reference, issue date, due date and location; Saudi Phase 2 accounts also need the payment method. | Accounting → Manual Journal Entries → Import: entry sequence, date, description, account type, account code, contact or tax, debit, credit; dates `dd/mm/yy`; debits equal credits per entry. | `https://api.qoyod.com/2.0`, `API-KEY` header; invoice `reference` and product SKU are unique |
| Daftra (دفترة) | App 3015 (Daftra Link): products, orders as invoices, contacts and stock. | Sales → Manage Invoices → Import (CSV, XLS, XLSX); map columns; choose Draft or Issued; own numbers or auto-numbering. | Journal list → Import: `Code`, `Date`, `Type`, `Description`, `Account name`, `Debit`, `Credit`, `Cost Centre`; same code = one entry; 10,000 rows per file. | `https://{subdomain}.daftra.com/api2` |
| Wafeq (وافق) | Through app 6150 (Zid Integration, third party): paid or completed orders with products, tax, discount, customer and order number. | Reports → Uploaded Files → Import Invoices; template `.xlsx`; 2,000 rows. Headers include `Unique identifier`, `Customer name`, `Customer Code`, `Invoice number`, `Currency`, `Date`, `Due date`. | Reports → Uploaded Files → Import Manual Journals; 6,000 rows: `Unique identifier`, `Date`, `Account`, `Currency`, `Debit`, `Credit`. | `https://api.wafeq.com/v1`, `Authorization: Api-Key …`, 200 requests a minute; creating an invoice and reporting it to ZATCA are separate calls |
| Zoho Books | App 5350 (Zoho Books Accounting, Apps Bunches): completed or paid orders become invoices and returns credit notes. App 3928 (Reachware) covers several systems. | Sales → Invoices → Import (CSV, TSV, XLS); `Invoice Date`, `Invoice Number` and `Customer Name` required. | Accountant → Manual Journals → Import. | Zoho Books API v3 (OAuth, `organization_id`); pushing to Fatoora is its own step |
| Odoo | App 1062 (TECFY, third party): orders as invoices at the statuses the merchant picks, plus products, stock and customers. | Invoices list → Action → Import records (`.xlsx`, `.csv`); run Test first; dates `YYYY-MM-DD`; an `External ID` from the Zid order number makes reruns update instead of duplicate. | Journal entries list → the same import. | The instance's JSON-2 API, one call per second; posting a Saudi-journal invoice and "Process now" sends it to ZATCA |
| Xero | Apps 3168 (Reachware) and 843 (third party). | Sales overview → Import; Xero's CSV template; 500 items; `ContactName` and `InvoiceNumber` required; repeat the invoice number on each line. | Advanced → Manual Journals → Import: `*Narration`, `*Date`, `*AccountCode`, `*TaxType`, `*Amount`; cannot post to receivables or payables. | Xero API (OAuth) |
| QuickBooks Online | App 3174 (Reachware, third party). No built-in ZATCA Phase 2. | Settings → Import data → Invoices; 100 invoices and 1,000 rows per file; `Invoice no.`, `Customer`, `Invoice date`, `Due date`, `Item amount`, `Item tax code`. | Settings → Import data → Journal entries; 1,000 rows, 2 MB: `Journal No`, `Journal Date`, `Account Name`, `Debits`, `Credits`, `Description`, `Name`. | QuickBooks API (OAuth) |

## Columns any sales import needs

1. Invoice key: the Zid order number, date and status.
2. Customer: the target's customer code when known, otherwise the name. Add
   phone, email or VAT number only where the target's template requires them
   (VAT number for business customers' tax invoices).
3. Lines: SKU or item code, description, quantity, unit price, discount, line amount.
4. Tax: tax code, rate, amount, and whether prices include VAT.
5. Shipping and fees as their own lines or fields; the invoice total.
6. Payment: status, date, method and reference.
7. An import batch id and the source row, so a failed import can be rerun without duplicates.
