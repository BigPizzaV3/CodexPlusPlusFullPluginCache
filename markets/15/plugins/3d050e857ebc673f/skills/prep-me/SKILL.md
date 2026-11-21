---
name: prep-me
description: Prep me for a meeting. Use when the user wants to prepare for a client or project meeting (a brief, pre-read, agenda or talking points) from their Delegent work, with sources.
---

# Prep me

## 1. Pin down the meeting

- If the user named the meeting, use it. Otherwise find it: use a calendar tool you already have, or `delegent_get_calendar` for today and the next few days.
- Identify the workstream (client or project). If unclear, call `delegent_list_workstreams` and ask.

## 2. Gather evidence

- `delegent_get_context_for_task`, with a query such as "Prepare for <meeting> with <client>" and the workstream.
- `delegent_get_status` for the Overview, open tasks and upcoming dates.
- `delegent_get_source` for the last meeting transcript and any decision you will cite.
- `delegent_find_contacts` for attendees the user may need context on (see `whos-who`).
- `delegent_find_follow_ups` for unanswered email with these people.

## 3. Write the brief

Lead with what matters:

1. **Objective and decisions needed**
2. **What changed since last time**, with sources
3. **Open actions**: owner and due date, overdue flagged
4. **Unanswered emails** with the attendees
5. **Risks and sensitive points**
6. **Suggested agenda**
7. **Sources**: each key point traced to a Delegent note, meeting or email

Mark anything you could not verify as "Not found in Delegent". Never invent owners, dates or numbers. For a formal document in the firm's format, follow `draft-the-deliverable`.

## 4. Offer, don't assume

Offer to save the agenda or prep notes to the workstream with `delegent_capture_work`. Save only on a yes. If the user preps often, mention once that a morning brief can do this daily (`set-up-delegent`).

When using `delegent_get_calendar` for a Google account, set `include_google: true`; `include_outlook` retains its Outlook-only meaning. Treat partial or unavailable coverage as unchecked, not an empty calendar.
