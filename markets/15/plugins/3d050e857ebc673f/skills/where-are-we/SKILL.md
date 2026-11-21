---
name: where-are-we
description: Where are we? Use when the user asks where a project stands, what is outstanding or overdue, or wants to clean up and update their Delegent tasks.
---

# Where are we?

## One workstream

1. `delegent_get_status`: Overview (brief, decisions, risks, open questions, next steps), open tasks with refs, upcoming events, recent activity.
2. Summarise: status in one line, what changed recently, overdue or at-risk actions, upcoming dates, open questions.
3. For "why", use `delegent_get_context_for_task` and cite sources (see `what-did-we-decide`).

## Across workstreams

`delegent_list_my_tasks`. Use `due_before` for "this week" and `scope: assigned_to_me` for work others gave the user. Group by workstream, overdue first. `delegent_list_inbox_items` shows assignments and questions waiting in Delegent.

## Priorities

When the plate is crowded, sort open tasks into:
- **Drive**: important and urgent
- **Plan**: important, not urgent
- **Delegate**: urgent, not important
- **Drop**: neither

Suggest priority changes; apply with `delegent_update_task` on a yes.

## Updating

- Complete, reopen, re-date or reprioritise with `delegent_update_task`.
- Tasks assigned by someone else can only be marked done or reopened.
- Suggest changes for stale items and act only on the user's answer.
- Suggest Overview corrections with `delegent_propose_overview_update`.
- Delete only with `delegent_delete_note` when the user asks. The user approves each deletion themselves, in a prompt from this app or in their Delegent Inbox; on `approval_required`, ask them to approve, then call again with the same arguments plus `action_id`.

Summarise what changed at the end.
