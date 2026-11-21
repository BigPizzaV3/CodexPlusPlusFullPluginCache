---
name: check-ins
description: "Set up check-ins that beckett sends on a schedule, such as a weekday nudge to log a run or a Sunday prompt to plan the week, and change or pause them. Use when the user wants to set up, change, or pause a recurring prompt or nudge in beckett."
---

# Check-ins

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- A check-in is a recurring prompt beckett sends to ask the user for an update. Create one with its `type` (`recurring_check_in`, `habit_nudge`, `task_reminder`, or `event_reminder`), the `time`, a short `label`, the `frequency` (`daily`, `weekday`, `weekly`, `custom`, or `interval_days`), and the `prompt` to ask.
- To change a check-in, find it, then update its time, frequency, or prompt. To pause one, set `active` to false; to resume it, set `active` to true.
- The account's Morning briefing, Evening check-in, and Weekend review, if they picked them in setup, are check-ins too; change or pause them the same way. beckett sends check-ins only while the account has access.
- A one-time reminder is a task, not a check-in; see the reminders skill.
