---
name: get-started
description: How to read and log a person's own fitness tracking in Marrow (activity, workouts, strength sets, meals, water, weight, sleep, mood). Use when the user asks about their training, steps, sleep, food, weight or progress, wants a weekly review, or asks to log a meal, a workout or a lift.
---

# Marrow

The `marrow` server is the user's own Marrow log, synced from their
phone: the same numbers the app shows. Answer from it, never from
assumptions.

## Getting connected

The user needs the Marrow app with Cloud MCP turned on. When ChatGPT
signs in, a page asks "Which Marrow is this?": in Marrow they open
Connects, then AI, open ChatGPT and tap Copy your link, paste it, then
type the six-character code into Marrow and tap Approve.

## When run as setup

Call `daily_brief` once to check the connection. If it answers, say in
one or two lines what Marrow can do here and offer three things to try:
"How did I sleep this week?", "How am I doing today compared with my
usual?" and "Log a meal for me". If the call asks for sign-in, walk the
user through Getting connected above. Do not log anything during setup.

## Which tool answers what

- Today, or "how am I doing": `daily_brief`. Activity, food and water
  against the user's targets, last night's sleep, training and mood,
  each against the user's own recent normal. Start here.
- Is a number usual for this person: `baselines`. Compare with their
  own normal, not with other people.
- What is different lately, weekly reviews: `what_changed`.
- Before concluding something did not happen: `data_quality`. A gap in
  syncing is not a zero.
- Detail: `metric_daily`, `metric_samples`, `workouts`,
  `strength_log`, `nutrition_log`, `sleep_log` (the source for
  nights), `targets`, `health_summary`.
- Every read takes `days` back, or `from` and `to` on the phone's
  calendar (YYYY-MM-DD).

## Logging

Only when the user asks. `log_meal`, `log_water`, `log_weight`,
`log_workout`, `log_strength`, `log_sleep`, `log_mood`, `edit_entry`,
`delete_entry`, `set_targets`, `undo_entry`. The phone applies each
change. If a write answers that adding entries is turned off, tell the
user where the switch is: Marrow, Connects, AI, ChatGPT, Allow AI
write. Never log, change or remove anything the user did not ask for.
Confirm what was logged in one line.

## Limits

- Only the signed-in user's own log. Nobody else's can be read.
- No bulk delete. `delete_entry` removes one food entry at a time. The
  whole copy is deleted in the Marrow app: Connects, Cloud MCP, Delete
  the copy.
- Anything without a log tool cannot be logged from here. Say so and
  point to the app on the phone.
- Water and weight cannot be undone from here once applied. The user
  removes them in the app.

## Wording

Plain, encouraging coaching tone. Describe what the numbers show,
compare with the user's own normal, suggest a next step. Stay with
what the log shows and draw no conclusions past it. Quote units. Say
plainly when data is missing or stale.
