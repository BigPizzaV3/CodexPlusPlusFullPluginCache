---
name: keep-waiting
description: "Mail you sent that nobody has answered yet, oldest first, with a nudge suggestion."
compatibility: "Needs the Keeploop app on a Mac and its MCP connector (tools such as search_mail and find_attachments)."
---

The Keeploop tools may carry a prefix in this agent (for example mcp_keeploop_search_mail); use them by their Keeploop name.

Show me what I am waiting on other people for, using the Keeploop tools.

1. Call awaiting_reply with direction="them" (default days=7).
Then list each thread, oldest first: who I wrote to, subject, when I sent it, and whether a nudge makes sense now. Include each mail_id. Do not draft nudges unless I ask.
If a tool is missing, or answers that it needs Keeploop Pro, say so in one line and do what you can with search_mail and get_email instead.
