---
name: get-started
description: Connect Biggy and ask your first questions about incidents, changes, on-call and runbooks.
---

# Get started with Biggy

Biggy is BigPanda's AI agent for IT operations teams. It answers questions about your
incidents, changes, on-call schedules, knowledge articles and runbooks from the ITSM, on-call and
observability tools already connected to your Biggy organization.

## Connect

1. Enable the Biggy plugin and sign in with your own Biggy account when prompted.
2. Every request runs with your Biggy permissions and is attributed to you.
3. If your team has not set up Biggy yet, start at https://app.biggy.io.

## Try asking

- What incidents are open right now, and which ones are getting worse?
- Who is on call for the payments service right now?
- Which changes deployed in the last 24 hours could explain the database latency?

## How requests are handled

- Read questions (incidents, changes, on-call, knowledge) are answered by `ask_biggy`.
- Anything that changes a system (update a record, page a team) goes through `ask_biggy_act`,
  which proposes a plan and waits for your explicit approval before running it.
- Each answer links to the full Biggy conversation; open it for details, sources and follow-up.
