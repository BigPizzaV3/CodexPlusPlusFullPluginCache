---
name: invoices
description: "Review Otis drafts, issued invoices and recorded balances, or cancel a specifically requested draft."
---

# Invoices with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: invoices_list, invoice_get, invoice_check, invoice_cancel_draft.

1. Read and paginate invoices, then inspect the selected invoice or its readiness with invoice_get and invoice_check. Balances reflect reported payments, not verified bank activity.
2. Cancel only a specifically requested unissued draft with its reason; explain released reservations. Issued corrections and voids are unavailable. Creating or issuing an invoice uses the create-invoice workflow with separate exact-draft approval. Reporting a payment uses the payments workflow.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
