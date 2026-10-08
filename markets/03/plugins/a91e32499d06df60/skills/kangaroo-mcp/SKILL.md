---
name: kangaroo-mcp
description: Use the authenticated Kangaroo Rewards MCP server for marketing campaign and loyalty-program questions, explanations, and recommendations.
---

# Kangaroo Rewards MCP

Use the Kangaroo Rewards MCP tools when the user asks about campaign performance,
send status, click rates, attributed revenue, loyalty-program performance, or
recommendations based on their Kangaroo data.

Keep the response grounded in the returned business data. Explain metrics in
plain language, identify the relevant time period, and distinguish reported
values from recommendations or inferences. Do not invent campaign names,
customers, or performance numbers.

The server requires an authenticated connection. If the connection is missing,
ask the user to authenticate the Kangaroo MCP server in ChatGPT or Codex and
then retry. Do not ask the user to paste bearer tokens or other credentials into
the conversation.