---
name: today
description: "Summarize the user's day from beckett: today's events and tasks that are due or overdue. Use when the user asks about their day, what they have today, or what needs their attention."
---

# Today

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Read today's events, from midnight today to midnight tomorrow in the user's time zone.
- Read open tasks due today or overdue, with `due_before` set to the end of today.
- Summarize in a few short lines, most time-sensitive first, and point out what needs attention rather than listing everything.
