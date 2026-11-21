---
name: birthdays
description: "Save birthdays in beckett as yearly events linked to the person, with a reminder before each one. Use when the user shares someone's birthday or asks to be reminded of one."
---

# Birthdays

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Find the person. If they aren't saved yet, add them.
- Create an all-day event: `all_day` true, `recurrence` `yearly`, and the person in `person_refs`. Set `reminder_minutes_before` to the lead time they want, such as a week before.
- If they ask to keep other details about the person, such as gift ideas, save them with `beckett_store_notes`.
