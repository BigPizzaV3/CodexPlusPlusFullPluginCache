---
name: keep-draft
description: "Draft a threaded reply that sounds like you. Saves a draft only; never sends."
compatibility: "Needs the Keeploop app on a Mac and its MCP connector (tools such as search_mail and find_attachments)."
---

The Keeploop tools may carry a prefix in this agent (for example mcp_keeploop_search_mail); use them by their Keeploop name.

Draft a reply in my voice, using the Keeploop tools.
Message: mail_id (the first word of the text I typed after the command)
What the reply should say: (the rest of the text I typed after the command)
(If the mail_id or what to say is missing, ask me for it before calling any tool.)

1. Call get_email with that mail_id and read the whole message.
2. Call get_voice_profile with sender set to the address I received it on (my account's address) and to set to the person I am replying to. Follow its greeting, sign-off, length and tone.
3. Write the reply body, then call save_reply_draft with mail_id and body. Use reply_all=true only if the other recipients need to see it.
4. Show me the draft text and say it is saved in Mail's Drafts for me to review.
Do not send mail unless the user asked you to send it. Nothing is sent unless they allow it: Keeploop checks their permissions and may ask them on their Mac first. If a tool is missing, or answers that it needs Keeploop Pro, say so in one line and do what you can with search_mail and get_email instead.
