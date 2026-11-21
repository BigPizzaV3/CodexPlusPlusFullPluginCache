---
name: keep-brief
description: "Unread mail, what needs a reply, and today's monitor hits, grouped by account category."
compatibility: "Needs the Keeploop app on a Mac and its MCP connector (tools such as search_mail and find_attachments)."
---

The Keeploop tools may carry a prefix in this agent (for example mcp_keeploop_search_mail); use them by their Keeploop name.

Give me my morning mail brief using the Keeploop tools.
Account or category: (the text I typed after the command)
(If that is empty: cover every account.)

1. Call list_categories to learn how my accounts are grouped (Personal, Work, ...). If an account or category is given above, keep to it: pass it as category= when it is a category name, or as account= when it is an account.
2. Call search_mail with unread_only=true and since set to yesterday's date to find unread mail.
3. Call awaiting_reply with direction="me" and days=2 to find threads waiting on me.
4. Call list_monitors, then check_monitor for each active monitor, and keep the hits from today. In a Claude Duet channel, also call check_route with peek=true on its route (duet:<channel-name>) to see matches from monitors tagged for it.
Then write 5 to 10 bullets, grouped under a heading per category. Put mail that needs a reply first. Each bullet: sender, subject, and one short clause on why it matters, with its mail_id so I can ask for more. Skip newsletters and receipts unless something in them needs action.
If a tool is missing, or answers that it needs Keeploop Pro, say so in one line and do what you can with search_mail and get_email instead.
