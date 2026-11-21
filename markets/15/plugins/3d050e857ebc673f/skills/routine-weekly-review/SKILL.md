---
name: routine-weekly-review
description: Weekly review routine. Use when setting up or running the optional Friday review of workstreams, stale items and clean-up proposals.
---

# Routine: weekly review (optional)

**Default schedule:** Fridays 16:00.

## Run instruction

> Run my Delegent weekly review. Use Delegent.
> 1. For my most active workstreams (up to five): status in one line, what changed this week, risks, open questions.
> 2. Stale items: overdue tasks, and undated tasks older than 14 days.
> 3. Propose clean-ups (complete, re-date, reprioritise, reassign) with the reason for each.
> 4. Draft a short client-facing update per active client, for me to review.
> Change nothing. Put every proposal under "Needs you" so I can approve by replying.

## How to run it

Follow `where-are-we` across workstreams. Client update drafts stay in the output. Create mailbox drafts only if the user asks in their reply.

When the user replies with approvals, apply them with `delegent_update_task`. Assignments follow `hand-it-off`.
