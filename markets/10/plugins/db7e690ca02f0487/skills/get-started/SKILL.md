---
name: kontocsv-bank-statement-conversion
description: Inspect bank, card or payment statement PDFs and transaction CSV files, then prepare and run supported accounting exports with an authenticated KontoCSV account when the user has enough existing credits.
---

Use this skill when the user wants structured accounting data from a bank statement, credit-card statement, payment statement or transaction CSV.

1. If the host provides an attached PDF or CSV as a file parameter, call `ingest_attached_bank_statement`. If direct attachment transfer is unavailable, call `create_secure_upload_session` only when the host can upload the user's file to the returned secure destination.
2. Call `inspect_bank_statement` before any conversion. Report relevant document facts and supported export profiles. Do not spend credits during inspection.
3. If the user only asked to inspect, validate or understand compatibility, stop after inspection.
4. For a requested conversion, call `prepare_bank_statement_conversion`. This tool may report only existing credit availability and conversion requirements. It must not be used to advertise prices, purchases or upgrades.
5. If the result is `insufficient_credits`, explain that the connected account does not currently have enough existing credits. Do not offer a price, checkout URL, subscription, upgrade or purchase flow inside the plugin.
6. If the result is `ready`, tell the user the required and available credit counts and ask for explicit confirmation before starting the conversion. Do not set `confirmedByUser` to true unless the user has explicitly confirmed the conversion after seeing the credit requirement.
7. After confirmation, call `convert_bank_statement_for_accounting` once with the prepared quote token.
8. Use `get_conversion_status` for the already-started job. Never start a duplicate conversion merely because a job is still queued or processing.
9. When the job permits a download, call `download_accounting_export`. If the result is marked `review_required`, say so clearly instead of describing it as fully validated.
10. Never invent opening balances, closing balances, account identifiers, currencies or transactions. If MT940 or CAMT.053 is unavailable because balance evidence is insufficient, report that limitation and use another supported format only if the user requests it.
11. Never request bank-login credentials, passwords, TANs, payment-card details or other authentication secrets.
12. Do not use this workflow for unrelated documents or for general document summarization.

KontoCSV's directory profile uses only credits already available in the connected account. Purchases and checkout are outside this plugin.
