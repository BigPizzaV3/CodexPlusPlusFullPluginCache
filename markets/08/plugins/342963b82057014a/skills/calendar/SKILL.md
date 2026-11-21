---
name: calendar
description: "Add appointments and events to the beckett calendar, move them, and show the schedule for a day or week. Use when the user shares an upcoming event with a day or time, or asks about their schedule."
---

# Calendar

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- When the user shares an upcoming appointment or event with a day or time, such as "Henry's school play is Friday at 6," add it to the calendar and confirm in one line. Ask only when the day or time is unclear.
- Appointments, meetings, and other scheduled occurrences are events. Set the start and end times or `all_day`, `recurrence` for repeats, the `location`, the people involved in `person_refs`, and `reminder_minutes_before` when they want an alert.
- To see a day or week, list events with `from_at` and `to_at` for that range.
- To-dos with a due date are tasks, not events; see the reminders skill. Calendars themselves are containers that hold events.
- Times use the account's time zone in beckett. Don't ask for a time zone; write times without a UTC offset unless the user names a zone.
