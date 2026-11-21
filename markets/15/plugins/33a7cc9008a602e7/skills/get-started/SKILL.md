---
name: get-started-with-wazi
description: Help a user connect Wazi Tools and use its current read-only lead and task tools.
---

# Get started with Wazi Tools

1. Ask the user to connect their Wazi Tools account through the plugin's OAuth sign-in flow and choose the workspace they want to share.
2. Explain that this connection lists accessible leads and tasks only. It does not edit records or return lead contact details, notes, task notes, or archived items.
3. When the user asks about Wazi data, call `list_leads` or `list_tasks` as appropriate. Follow `nextCursor` when more records are needed, and say when results may be incomplete.
4. Do not infer access to a second workspace from the user's message. The OAuth grant is bound to the selected workspace.
5. To disconnect, direct the user to `https://app.wazi.tools/mcp/connections`.
