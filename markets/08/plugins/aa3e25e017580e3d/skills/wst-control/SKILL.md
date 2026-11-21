---
name: wst-control
description: Use WST Commander as the direct tool gateway to the user's paired computer. Trigger whenever the user explicitly names WST Commander or asks to use WST Commander for system diagnostics, files, workspace inspection, processes, services, safe commands, or approved app actions.
---

# WST Commander direct control workflow

Use WST Commander MCP tools as the execution layer for the user's paired computer.

1. If the user explicitly says **WST Commander**, treat that as an explicit tool choice. Use WST Commander tools for the task.
2. Do **not** substitute Remote Desktop Commander, Desktop Commander, or another computer-control plugin merely because it exposes similar capabilities.
3. If WST Commander authentication is missing, invoke the WST Commander OAuth linking flow. Do not silently fall back to another desktop-control plugin.
4. If WST Commander is unavailable after authentication or returns an error, report the WST Commander-specific blocker. Use another desktop-control plugin only when the user explicitly requests that alternative.
5. Prefer actual WST Commander tool calls over explaining manual steps.
6. For operational changes follow current-state capture -> change -> verify.
7. Read-only diagnostics may run directly; respect ChatGPT permission prompts for write/action tools.
8. Never claim an action succeeded unless the WST Commander tool result confirms it.
9. Keep the interaction in the current ChatGPT conversation.
