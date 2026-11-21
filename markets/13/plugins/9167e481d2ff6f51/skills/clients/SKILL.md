---
name: clients
description: "Find Otis clients and maintain confirmed billing and tax details."
---

# Clients with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: clients_list, client_save.

1. Clarify whether the user wants to find, add or edit a client. List and paginate first to identify existing matches; resolve ambiguity before writing.
2. For a save, collect confirmed billing details and relevant country/region, business/consumer status, tax IDs and evidence. Use client_id for an edit and retain existing fields: client_save replaces details. Never infer country or tax status from currency. Explain that edits do not rewrite issued invoices and can make drafts stale.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
