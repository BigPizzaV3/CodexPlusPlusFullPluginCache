---
name: get-started
description: Set up Comnview after it is installed. Checks the connected Comnview account and what this connection may do, shows the newest projects, and suggests what to try first. Use right after installation, or when the user asks what Comnview can do here or whether it is connected.
---

# Get started with Comnview

Comnview is where clients review websites, pictures (screens) and PDFs by pinning comments on them. This skill checks the connection and helps the user pick a first task. It changes nothing in the account.

The user's own instructions always come first. If they ask for something specific, do that instead of this walkthrough.

## Steps

1. Call `whoami`.
   - If it fails because Comnview isn't connected, tell the user to connect Comnview from the plugin's settings and sign in on comnview.com, then stop.
   - Report, in one or two lines: the account name and what this connection may do (read only, read and reply, or full).
   - If the connection is read only, say that replying and resolving need "read and reply", and pinning comments, capturing pages, uploading and sending need "full". The user can reconnect and choose a different level.
   - If the account doesn't have AI agent access, say so and that it's managed on comnview.com. Don't mention plans or prices.
2. Call `find_projects` with no filter (newest first). Show up to five projects: name, kind (website, pictures or PDF) and open comment count if it is returned. If there are none, say so.
3. Suggest three first tasks, using real project names from step 2 where possible:
   - "Summarize the open feedback on <project>"
   - "Draft replies to the comments still waiting for me on <project>"
   - "Do a design audit of <a web address> and pin the issues"
4. Close with what to expect:
   - Replies and comments are posted as the user, and clients get the usual email.
   - You will show any reply, upload or email before you send it.
   - Deleted pages, projects and own comments go to Trash for 30 days and can be restored.
   - The connection can be removed any time in Profile > Agents on comnview.com.

## Rules

- Don't create, change or send anything in this skill.
- Report only what the tools return. Don't guess account details, project names or counts.
- Signing in is the user's own step. If a Comnview call says it isn't connected, the sign-in expired or the access is too low, tell the user how to connect it in this app's settings and stop. Never sign in to comnview.com yourself, ask for or open sign-in emails, look in the user's mailbox for Comnview links, or create, copy or paste tokens.
