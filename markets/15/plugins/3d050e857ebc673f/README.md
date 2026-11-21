# Delegent for Claude

Delegent is the context layer between your discussions and your work. This plugin connects Claude to your Delegent account so Claude can prepare for client meetings, answer "what did we decide?", chase follow-ups and build deliverables from your firm's templates, with sources you can open and check.

## What it does

- Build a client meeting brief from your notes, meetings and synced email, with cited sources.
- Show what is open across your workstreams, and update or complete tasks.
- Show who you owe a reply and who owes you one, with follow-ups drafted in your mailbox for you to send.
- Find the note, meeting or email behind a project decision.
- Save decisions, action items and meeting transcripts to the right workstream when you ask.
- Prepare PowerPoint, Excel and Word deliverables from your firm's templates, grounded in your cited work.
- Set up a morning brief, midday check, daily wash-up and weekly review as scheduled routines.

## What is in the plugin

- **Connector:** `.mcp.json` declares one remote server, `https://app.delegent.team/api/mcp`. You sign in to Delegent with OAuth 2.0 the first time you use it. No API key or token is stored in this plugin.
- **Skills:** instruction files in `skills/` (meeting prep, status, capture, hand-off, templates, follow-ups, routines and more). They contain text only. They run no code, install no packages and call no other service.

## What data goes where

Claude calls Delegent tools only to read or write your Delegent workspace. Nothing in this plugin sends data to any other destination. Assigning a task, sharing a workstream or template, and deleting or forgetting something each wait for your explicit approval. Delegent never sends email: it can only create a draft for you to review and send yourself. Text retrieved from your sources is treated as evidence, never as instructions.

## Requirements

A Delegent account (https://delegent.team). Email search covers messages already synced into Delegent.

## Support and policies

- Support: https://delegent.team/support
- Privacy policy: https://delegent.team/privacy
- Terms: https://delegent.team/terms

## License

All rights reserved. See LICENSE.
