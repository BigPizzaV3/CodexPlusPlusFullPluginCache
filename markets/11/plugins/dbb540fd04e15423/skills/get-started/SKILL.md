---
name: get-started
description: Set up Snapbooks after installing it — confirm the connection, show which companies the user can reach, and suggest first tasks in their books.
---

# Get started with Snapbooks

1. Call `get_user_context`. It returns the signed-in Snapbooks user and the companies (client accounts) they can access, each with an id. If the call asks for authorization, tell the user to sign in with their Snapbooks user and approve access; they can untick write access to connect read-only.
2. Tell the user which companies you can see, by name. If there are several, ask which one they want to work on first and use its id in every later call.
3. Explain in two or three sentences what you can do:
   - look up journal entries, documents, bank transactions, customers and suppliers, accounts, VAT codes, balances and reporting deadlines;
   - read supplier invoices, receipts and other documents;
   - prepare journal entries, invoices, bank postings, period locks and other changes, which happen only when the user presses Approve on the card shown in the chat.
4. Say what you cannot do: send payments or move money, file the VAT return or annual accounts, or show national identity numbers.
5. Offer three starting points, using the chosen company:
   - "What is due soon?" — `get_calendar_events` for the next 30 days.
   - "What is not posted?" — `search_bank_transactions` with `is_reconciled: false` for this month.
   - "What do we owe?" — `search_documents` with `kind: PAYABLE` and `unpaid_only: true`.

Use only account codes and VAT codes returned by `get_gl_accounts` and `get_tax_codes`; never invent them. Never say a change was saved before the user has approved it on its card.
