---
name: add-expense
description: "Record or correct an Otis expense, optionally billable to a client."
---

# Add expense with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: clients_list, expenses_list, expense_record.

1. Collect vendor, category, description, date and cost. Ask whether the expense belongs to a client and whether it should be billable; cost and billable amount are separate facts. Inspect prior records if this might be an edit or duplicate.
2. Use expense_record with expense_id for an edit. A billable_amount_minor creates or updates one linked billable atomically; do not call billable_record for it again. Preserve required existing values during replacement. Report what was saved; references are links, not uploaded attachments.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
