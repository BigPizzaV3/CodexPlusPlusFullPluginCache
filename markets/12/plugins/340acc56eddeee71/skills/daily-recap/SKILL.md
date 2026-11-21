---
name: daily-recap
description: Use when someone asks how their day or week went, what they did on a date, or for a summary of their Gyroscope data.
---

# A recap of a day or a week

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead.

## Getting the data

- Call `gyroscope_status` once per conversation for the member's timezone and
  what this connection may access. Turn every relative date ("yesterday", "last
  week") into explicit YYYY-MM-DD dates in that timezone.
- `load_day` covers up to 7 days per call: food totals, sleep, steps, workouts
  and places when allowed. For more detail on one topic, use `load_food`,
  `load_sleep`, `load_steps`, `load_workouts`, `load_computer` or
  `load_places` for the same dates, or `load_screen_time_day` for how the
  hours went on screen.

## Writing the recap

- Lead with what matters most that day, then the rest in a few short lines.
  Use their numbers as the proof points.
- Mention only what is there. A category with no data gets one plain line or
  is left out, with no guessing about why.
- Write durations of an hour or more in decimal hours, and shorter ones in
  minutes.
- If the result lists categories this connection cannot access, say once which
  ones, and that they can switch them on from their connection page.

## Adding to their journal

- When they want to note something about their day for their Gyroscope coach,
  or track something Gyroscope has no tracker for, use `add_to_journal` in
  their words: "Today is my anniversary!", "Today I wore jeans and black
  boots.", "Today I had 4 meetings at work." with the number 4.
- One entry per thing, each with at most one number. If you wrote the entry up
  from what they told you, show it to them before adding it.
