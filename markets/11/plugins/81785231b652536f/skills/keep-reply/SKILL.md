---
name: keep-reply
description: "Threads where someone is waiting on you, prioritized, with a suggested next step each."
compatibility: "Needs the Keeploop app on a Mac and its MCP connector (tools such as search_mail and find_attachments)."
---

The Keeploop tools may carry a prefix in this agent (for example mcp_keeploop_search_mail); use them by their Keeploop name.

Show me what needs my reply, using the Keeploop tools.

1. Call awaiting_reply with direction="me" (default days=7).
2. For any thread where the ask is unclear from the snippet, call get_email on its mail_id.
Then give me a prioritized list, most urgent first: sender, subject, how long it has waited, and a one-line suggested action (reply with X, decline, forward to Y, or no reply needed). Include each mail_id. Do not draft anything unless I ask.
If a tool is missing, or answers that it needs Keeploop Pro, say so in one line and do what you can with search_mail and get_email instead.
