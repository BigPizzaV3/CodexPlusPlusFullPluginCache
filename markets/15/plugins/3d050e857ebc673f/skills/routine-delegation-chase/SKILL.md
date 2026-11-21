---
name: routine-delegation-chase
description: Delegation chase routine. Use when setting up or running the optional twice-weekly check on tasks the user assigned to others that are overdue or quiet.
---

# Routine: delegation chase (optional)

**Default schedule:** Tuesdays and Thursdays 10:00.

## Run instruction

> Run my Delegent delegation chase. Use Delegent[, and my <mail app>].
> 1. Tasks I assigned to others that are overdue or due in the next two days and still open.
> 2. For each: the owner, days overdue, the last related email or meeting, and whether they have replied to me.
> 3. Draft a short, friendly nudge for each one that needs it.
> Do not send anything or change any task. Put the nudges under "Needs you".

## How to run it

Use `delegent_get_status` for workstreams where the user assigned work, and `delegent_find_follow_ups`. When the user replies "send the Bo one", create an Outlook or Gmail draft with `delegent_create_email_draft` and say it is ready to review and send from the selected mailbox. Never send.
