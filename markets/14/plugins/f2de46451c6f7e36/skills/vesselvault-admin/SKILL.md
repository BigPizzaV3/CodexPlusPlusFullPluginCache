---
name: vesselvault-admin
description: Use VesselVault's connected MCP tools to search leads and perform supported order, ticket, and part-quote workflows for the authenticated account.
---

# VesselVault administration

Use the connected VesselVault MCP tools for supported administrative workflows.

- Ask clarifying questions when the target lead, order, ticket, or quote is ambiguous.
- Before write or external-sync actions, summarize the intended action and important identifiers.
- Treat tool results as the source of truth; never claim an action succeeded unless the tool confirms it.
- Respect the permissions enforced by VesselVault for the connected user. If an operation is denied, do not attempt to bypass the restriction.
- Do not request passwords, access tokens, or other secrets in chat.
- Do not run arbitrary SQL or suggest bypassing application authorization.
