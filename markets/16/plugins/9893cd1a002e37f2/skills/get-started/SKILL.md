---
name: get-started
description: Connect or troubleshoot the Swoogo plugin and verify access to the user's events. Use for initial setup, missing Swoogo tools, or authentication errors; not for unrelated Codex configuration.
---

# Get started with Swoogo

1. Read [the shared workflow rules](../../references/workflow-rules.md).
2. Use the host's plugin connection flow for the bundled `swoogo` MCP server at `https://mcp.swoogo.com`. Have the user finish Swoogo sign-in and OAuth consent in the host or browser. Never request passwords, API secrets, or tokens in chat.
3. Discover the connected tools. Use the exposed tool names and schemas; the host may add a namespace to the `swoogo_` names. If connection is still pending, report that state instead of claiming access or creating another plugin.
4. Once connected, call `swoogo_get_events` with `per_page: 5` for a small read-only check. An empty successful result verifies the connection but does not prove the account contains no events beyond the user's permissions.
5. Show the returned event names, IDs, dates, and status, labeling the list as a sample when more pages exist. Offer the appropriate workflow: an event briefing, registration assistance, agenda management, or attendance reporting.

On 401, reconnect using OAuth. On 403, explain the missing permission and use the existing Swoogo administrator/support route. On rate limits, respect retry guidance. Do not change authentication settings, bypass permissions, register anyone, send email, or write a record to test access.

Finish with the connection result and one useful next action. Never report setup as verified before a successful authenticated read.
