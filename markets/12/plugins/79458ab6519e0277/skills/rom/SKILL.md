---
name: rom
description: Use when the member asks to log, review or plan gym training in their ROM account, such as workouts, exercises, personal records, weekly training, workout templates, weekly goals or trainer programs.
---

# Working with a ROM account

ROM is the member's gym workout logbook. The ROM tools read and update the member's own account only.

## Logging

- Before logging a workout or creating a template, call `search_exercises` and use the returned exercise IDs. Follow each exercise's `loggingType` (weight and reps, reps only, time, distance) when building sets.
- If a search returns several close matches, ask which one the member meant instead of guessing.
- Weights are kilograms unless the member says pounds; then pass `weightUnit: "LB"`.
- Times without an offset are read in the member's time zone. Pass `timeZone` when you know it.
- After saving, report what ROM returned (the saved workout, any new personal records) rather than restating the request.

## Editing

- Updating a workout or template replaces the whole record. Fetch it with `get_workout` or `get_workout_template`, change what the member asked for, and send the full edited copy.

## Reviewing progress

- Tie every total, date range and record to the data the tools return. Say so when a page of results is partial.
- Keep training totals and personal records clearly separate.

## Ask first

- Confirm with the member before deleting a workout or template.

## Out of scope

ROM can't make purchases, renew coaching packages, change billing, delete the ROM account or send messages from here. Say so plainly and point the member to the ROM app or support at https://app.rom.fitness/integrations/support.
