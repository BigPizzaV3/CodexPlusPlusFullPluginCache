---
name: create-invoice
description: "Prepare an Otis invoice from available work, review tax and discounts, and issue only after exact-draft approval."
---

# Create invoice with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: clients_list, client_save, billables_list, billable_record, invoice_get, invoice_draft, invoice_check, invoice_issue, invoice_cancel_draft.

1. Identify the client and requested work or existing draft. Read saved client details and billables, following pagination and remaining_minor rather than only state=unbilled. Ask for missing client, price, dates, partial amounts, discounts and tax facts. Record new work only if the user requests it; never create duplicate source items.
2. Use invoice_draft for a new draft, or invoice_get for an existing one. Resolve invoice_check blockers; changed source facts may require cancelling and recreating the draft. Do not silently cancel another draft or reallocate its work.
3. Show the exact draft contents, tax treatment, discounts and total. A create-invoice command is not approval to issue. Only after the user approves that specific draft and total, call invoice_issue with confirmed=true and expected_total_minor. Generate any document from the returned snapshot; issuance does not send it.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
