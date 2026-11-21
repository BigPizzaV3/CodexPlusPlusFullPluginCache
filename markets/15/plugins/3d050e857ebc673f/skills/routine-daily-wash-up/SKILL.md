---
name: routine-daily-wash-up
description: Daily wash-up routine. Use when setting up or running the scheduled end-of-day wash-up that summarises the day and writes meetings, decisions and task updates back to Delegent.
---

# Routine: daily wash-up

**Default schedule:** weekdays 18:00, user's timezone. It does two jobs: tell the user how the day went, and keep Delegent current.

## Auto-save level (choose at setup)

Unattended runs cannot ask questions, so the user picks the rules up front.

**Recommended ("save the safe stuff"):**
- **Saves automatically:** meeting transcripts matched to a workstream by clear client or project name (`delegent_import_meeting`); their decisions and actions (`delegent_capture_work`, citing the meeting); tasks marked done only when a source explicitly says they are done, citing it.
- **Only suggests** (always safe): Overview changes via `delegent_propose_overview_update`.
- **Never automatically, listed under "Needs you":** unclear workstream matches, assigning or sharing with anyone, deleting, emails, new workstreams, contacts. Assigning, sharing, deleting and forgetting also need the user's own approval in Delegent, which an unattended run cannot give: do not call those tools here.

**Alternative ("ask me first"):** save nothing; list everything under "Needs you".

## Run instruction (paste into the scheduled task)

> Run my Delegent daily wash-up for today. Use Delegent[, and my <mail/calendar/Teams app>].
> 1. Find today's finished meetings and their transcripts; skip any already in Delegent.
> 2. [Auto-save rule chosen at setup.] Cite the meeting for every saved item.
> 3. Tell me: what got done, decisions made, new actions (owner and due date), tasks due tomorrow, emails I still owe today.
> 4. List under "Needs you" anything that needs my decision: unclear matches, assignments, emails to send, and deletions.
> Never send email, assign, share or delete.

## How to run it

Follow `capture-this-meeting` per meeting, without the confirmation step (the chosen rule replaces it). Finish with `delegent_list_my_tasks` (due tomorrow) and `delegent_find_follow_ups` (owed today). Report exactly what was saved, with `open_in_delegent` links.
