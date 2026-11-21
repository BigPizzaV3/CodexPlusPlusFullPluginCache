---
name: payments
description: "Review or record reported partial/full payments for issued Otis invoices."
---

# Payments with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: invoices_list, invoice_get, payments_list, payment_record.

1. Clarify whether the user wants to review payments or record one. Read the relevant invoice and payments; paginate results. These are reported facts, not verified bank activity.
2. Before payment_record, establish the issued invoice, actual received amount/date and stable business-wide reference. Reuse that reference for the same payment. Resolve mismatches or overpayments rather than splitting them to hide a conflict. Payment reversals and unapplied credits are unavailable. Return the recorded payment and updated invoice balance.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
