---
name: landit-context
description: Establish Landit connection readiness, explain supported capabilities, or resolve account context before Landit work.
---

# Landit context

Read [shared safety and identity](../../references/safety-and-identity.md) and [capabilities](../../references/capabilities.md) before tool use. The AI may browse verified template previews, but MUST NEVER open prospect Page links, including indirect fetches, screenshots, HEAD requests, or link checks.

1. Inspect the host's actually exposed tools. Use its supported OAuth connection flow when authentication is required; let the user sign in and consent. Never collect credentials or alter hosting/scopes.
2. Use list_templates as a harmless readiness check. Follow next_page only as needed, and until null when a complete catalog is requested. Empty results are valid, not an authentication failure.
3. Report tool discovery, successful authenticated read, fresh OAuth, and end-to-end workflow verification separately. Installing a ZIP proves none of them.
4. Do not infer the connected account from template names. If account selection is uncertain before a write, ask the user to verify the chosen connection in Landit/ChatGPT. There is no workspace-switch or profile tool.
5. Route template work to landit-templates, Page creation/status to landit-prospects, recorded activity to landit-page-insights, and asset instructions/sharing to landit-assets. Read the relevant skill before performing its workflow.

Explain unsupported actions honestly: no account signup, Knowledge Base editing, LinkedIn messages, general CRM management, embedded UI, or ChatGPT attachment uploads. Do not perform writes to demonstrate access.
