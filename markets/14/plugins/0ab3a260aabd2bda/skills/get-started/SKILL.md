---
name: jusnote-get-started
description: Help users query and summarize information available through their authenticated Jusnote workspace.
---

# Jusnote connector guidance

Use only the tools exposed by the connected Jusnote MCP server to retrieve information. The available data and operations depend on the connected account, server configuration, and permissions.

- Do not attempt to bypass Jusnote authentication or authorization. Treat access-control behavior as enforced by the Jusnote service and report errors returned by it.
- Use only tools actually exposed by the connected MCP server.
- Do not claim that create, edit, or delete operations are available unless the connected server exposes and documents those operations. If no such tool is available, explain that the requested action cannot be performed with the available tools.
- When a query is ambiguous, ask a concise clarification.
- Distinguish retrieved facts from inference and mention when information is unavailable.
- For important dates, amounts, deadlines, or legal conclusions, encourage the user to verify the original Jusnote record.
- Never attempt to access records outside the authenticated user's permissions.
