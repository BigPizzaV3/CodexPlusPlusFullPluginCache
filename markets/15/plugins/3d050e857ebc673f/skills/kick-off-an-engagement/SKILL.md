---
name: kick-off-an-engagement
description: Kick off an engagement. Use when the user starts new client work and wants a workstream set up with a brief, first tasks, key people and background.
---

# Kick off an engagement

## 1. Gather the basics

Ask only for what you do not already have (an SOW, email or notes in the conversation may cover it):
- Client and engagement name
- Objective and the decision the client needs
- Scope in and out
- Start date, key milestones, end date
- Accountable owner, and the client sponsor
- Team members to share with

Check for related prior work with `delegent_get_context_for_task` ("previous work with <client>") and `delegent_search_firm_knowledge` if enabled.

## 2. Show the setup plan

- Workstream name
- Brief (3–5 lines)
- First tasks, with owners and due dates
- Key milestones as dated events
- Contacts to add
- Durable facts to remember (e.g. "Client prefers PDFs")
- People to share with

## 3. Create it, after a yes

1. `delegent_create_workstream`
2. `delegent_propose_overview_update` for the brief and next steps
3. `delegent_capture_work`: first actions (with due dates), milestones as events, key decisions
4. `delegent_save_contact` for client stakeholders
5. `delegent_remember` for the durable facts, scoped to the workstream
6. Sharing and assignments follow `hand-it-off` (the user approves each one in this app or in their Delegent Inbox)

Finish with the `open_in_delegent` link. Offer an Engagement Brief document via `draft-the-deliverable`.
