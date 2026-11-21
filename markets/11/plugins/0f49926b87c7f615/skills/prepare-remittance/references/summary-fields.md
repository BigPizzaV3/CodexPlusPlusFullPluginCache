# Payment-summary field contract

Build a new PDF containing only:

| Field | Source and handling |
| --- | --- |
| Project and vendor display names | Verified selected records; omit private internal notes |
| Invoice number/date | Selected authoritative invoice; label unknowns |
| PO number | Verified saved PO; an unissued number remains unissued/unknown |
| Payment amount and currency | Recorded payment or explicitly attributed user report |
| Method and payment date | Actual method/date; never relabel an unsupported method |
| Payment reference | Reviewed non-sensitive confirmation/reference only; omit or mask if it contains account details |
| Status/evidence | User-reported sent, bank-confirmed sent or vendor receipt only as supported; separate posted match and settlement |
| Invoice total, applied amount and remaining balance | Fresh canonical payable/application read; unknown stays unknown; identify partial payment |
| Prepared date | Date the summary was prepared, not a bank processing date |

No account balances, full account/routing/card numbers, credentials, statement pages, unrelated bank transactions or hidden embedded source files. Do not include a source URL containing a private download token. Inspect visible pages, text, metadata and attachments. Use a neutral title such as “Payment summary”; do not label a host-generated PDF as bank confirmation. A summary can report an unreconciled payment truthfully.
