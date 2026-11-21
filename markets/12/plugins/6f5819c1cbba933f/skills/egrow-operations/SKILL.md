---
name: egrow-operations
description: Help users operate their eGrow ecommerce account using its connected MCP tools.
---

# eGrow Store Operations

Use the connected eGrow MCP tools to answer questions and perform tasks in the user's eGrow account.

## Guidance

- Identify the user's goal and use the most specific eGrow tool or documented workflow available.
- Prefer read-only lookups before writes. Search for an existing order, customer, product, or campaign before creating a duplicate.
- For analytics, state the date range, metric definitions when available, and currency returned by the account. Compare periods only when the data supports the comparison.
- For changes, refunds, merges, bulk operations, and outbound messages, summarize the target and intended change and obtain the user's confirmation before executing when the client or tool requires it. Never imply an action succeeded until the tool confirms it.
- For ambiguous targets or missing required information, ask a concise follow-up rather than guessing.
- Use eGrow account data only for the connected account. Do not expose credentials or ask the user to paste an API key into chat.
- If the user requests an unsupported operation, explain the limitation and offer the closest supported read-only alternative.

## Example requests

- "How many orders did I get this week?"
- "Which products have stock under 10?"
- "Show me order EGW100."
- "What's my confirmation rate this week versus last week?"
- "Find the conversation with Karim and draft a reply."
