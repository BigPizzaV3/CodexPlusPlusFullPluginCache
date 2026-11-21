---
name: keep-find
description: "Find a file someone sent you, or one sent while they were on Cc, by describing it; read the best match, and save or send it on if asked."
compatibility: "Needs the Keeploop app on a Mac and its MCP connector (tools such as search_mail and find_attachments)."
---

The Keeploop tools may carry a prefix in this agent (for example mcp_keeploop_search_mail); use them by their Keeploop name.

Find an email attachment for me, using the Keeploop tools.
What I am looking for: (the text I typed after the command)
(If that is empty, ask me for it before calling any tool.)

1. Call find_attachments. Pull a filename word into query, a person into participant (it matches the sender, To and Cc, by address or name; use sender only when it must be the sender), and the file type into kind (pdf, image, doc, sheet, or any). If nothing matches, retry with fewer filters, or call search_mail with participant and has_attachments=true and then get_email.
2. Pick the best match and call read_attachment with its mail_id and attachment_id. If Mail has not downloaded it yet, the tool fetches it (up to a minute); if it says it is still downloading, call it again.
Then tell me which file it is (name, sender, date, mail_id) and what it says in a few lines. List up to three other candidates. Call save_attachment only if I ask for the file itself. To send files to someone, list each one by its mail_id and attachment_id in `attachments` of save_draft or save_reply_draft (or send_email / send_reply if I said send); do not save them first. Never use shell commands, AppleScript or Mail.app for any of this.
If a tool is missing, or answers that it needs Keeploop Pro, say so in one line and do what you can with search_mail and get_email instead.
