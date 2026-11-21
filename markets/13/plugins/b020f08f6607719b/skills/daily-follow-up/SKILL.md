---
name: daily-follow-up
description: Build a real estate agent's follow-up plan for the day from BoldTrail - hot leads, new leads, unanswered questions, open tasks and upcoming appointments - and help act on it. Use when the user asks what to do today, who to call, who their hottest leads are, or asks to be coached.
---

# Daily follow-up plan

Help the agent decide who to contact today and act on it, using their own BoldTrail data.

## Gather

Call only what the request needs:

1. `coach` for the agent's top suggested actions.
2. `getContactActivityStream` with `filter` set to `hot_leads` for high-intent contacts. Use `new_leads`, `questions` or `showings` when the user asks about those specifically.
3. `getTasks` with `completed` set to false for open tasks.
4. `getAppointments` for today's and upcoming appointments.

## Present

- Lead with no more than three actions, most important first. For each, name the contact, why now (for example "viewed 4 homes since yesterday" or "asked about 12 Oak St"), and the suggested step: call, text, email or task.
- Then, briefly, open tasks that are due or overdue and today's appointments.
- If a source returns nothing, say so in one line. Do not fill gaps with guesses.
- Do not show internal IDs or raw field names.

## Act

When the user picks an item:

- Calls, texts and emails reach the contact and cannot be undone. Draft the message, show the recipient and the text, and send only after the user confirms. One contact at a time.
- For "remind me" or "later", create a task with `createTask` instead of sending anything.
- After completing a task the user mentions, mark it done with `completeTask` and confirm.
