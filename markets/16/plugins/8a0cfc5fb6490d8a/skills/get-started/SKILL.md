---
name: get-started
description: First steps with YESbusiness in ChatGPT — pick the company, check the year's figures, see what is still unbooked, and how proposals are applied.
---

# Getting started with YESbusiness

1. Call `list_my_companies` first and use one of its `company_id` values in
   every other call. If the user has several companies and did not name one,
   ask which.
2. For "how is my year going", read `get_income_statement` and
   `get_balance_sheet` for the current year. Amounts are integers in cents of
   the company's home currency: divide by 100 before showing them.
3. For "what is still unbooked", read `list_unbooked_bank_transactions` and
   `list_unattached_documents`.
4. To book something, read `list_accounts` and `list_vat_codes`, show the
   user the entry you are about to prepare, then call `propose_booking` (or
   `propose_bank_transaction_booking` for an imported bank transaction). The
   user applies or rejects it from the card or from the deep link. Only a
   connection the user set to "Autonomous booking" can book directly, and
   only up to the amount cap they chose.
5. Subscriptions, payments, members and bank credentials are not available
   through this plugin: point the user to the YESbusiness app for those.
