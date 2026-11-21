---
name: get-started
description: Introduce SeoPerseo after the user connects it, show what their account already contains, and explain how credits are spent.
---

Use this skill the first time the user works with SeoPerseo in a conversation, or when they ask what SeoPerseo can do.

1. Call `projects_list` to see which projects the connected account owns. If it returns nothing, tell the user to create a project at https://seoperseo.com first and stop.
2. Call `credits_balance` once and report the plan and remaining credits.
3. Tell the user, in two or three sentences, what is available right now:
   - stored evidence they can read for free: page audits, site scans, Inbox opportunities, saved work documents;
   - live checks that spend credits: page audits, SERP analysis, keyword research, AI-visibility checks.
4. Offer three concrete next steps based on what the account actually contains, for example "triage your Inbox", "summarise the latest audit for <domain>", or "run an audit on a page".

Rules:

- Never invent projects, domains, metrics or findings. Only report what a tool returned.
- Never call a credit-spending tool during onboarding.
- If a tool reports that the user is not signed in, tell them to reconnect the SeoPerseo connector and stop.
