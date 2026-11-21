---
name: reminders
description: "Add to-dos and reminders to beckett with a due date and alert time, and list what's due. Use when the user asks to be reminded of something, adds a to-do, or asks what's due."
---

# Reminders and to-dos

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Create to-dos and reminders as tasks. When the user says "remind me," set `due_at` and `reminder_minutes_before`: `[0]` to be reminded at that time, or the lead time they ask for. If they didn't say when, ask.
- For a repeating to-do, set `recurrence`, plus `recurrence_interval` for every few days, weeks, or months, such as 2 with `weekly` for every other week.
- Appointments and other scheduled occurrences are events, not tasks.
- To see what's due, list their open tasks.
- Times use the account's time zone in beckett. Don't ask for a time zone; write times without a UTC offset unless the user names a zone.
