---
name: sleep-review
description: Use when someone asks about their sleep or sleep score in Gyroscope, how it has changed, or what lines up with it, such as workouts, steps, food, caffeine or travel.
---

# Reviewing sleep

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead.

## Getting the data

- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.
- Specific nights: `load_sleep` for those dates. Each date is the night that
  ended that morning, then any naps. When `confirmed` is false, the night is a
  rough estimate from raw data, so say so.
- Weeks or months: `load_trend` with metric `sleep`.
- What lines up with it: the same nights with `load_workouts`, `load_steps`,
  `load_food` or `load_computer`, `load_history` for caffeine, heart rate
  and HRV, and
  `load_places` when travel matters and Places is allowed. Look at two to four
  weeks or more, in a few calls rather than one huge one.

## Writing the answer

- Give the sleep score and hours first, then what changed and when.
- Write durations of an hour or more in decimal hours.
- For patterns, compare the better and worse nights on the things that
  differ, say how many nights each pattern rests on, and keep it plain when the
  sample is small.
- Point out patterns in their own data, and keep to what the numbers show.
