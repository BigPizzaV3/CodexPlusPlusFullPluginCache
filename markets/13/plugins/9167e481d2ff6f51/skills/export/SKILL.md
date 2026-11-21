---
name: export
description: "Export Otis records or audit history as paginated JSON using current read permissions."
---

# Export with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: records_export.

1. Ask which record kinds to export: business, client, billable, expense, invoice, payment or audit. Use records_export for each selected kind and follow next_offset until null; do not silently present one page as the whole export.
2. Keep the selected business clear and preserve recorded values and currency. State which kinds were exported and any incomplete pages. Exports are not transactional backups and cannot be imported/restored by Otis. Viewers may export records they can access.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
