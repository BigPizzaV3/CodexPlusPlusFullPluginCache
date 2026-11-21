---
name: screen-time
description: Use when someone asks about their screen time, phone or computer use, which apps take their time, phone pickups or notifications, or how focused or productive their days were, in Gyroscope.
---

# Screen time, apps and pickups

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead.

## Getting the data

- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.
- Start with `load_screen_time` for the range they asked about, by day, week
  or month: computer and phone time, productive and unproductive time,
  pickups, notifications, first and last pickup, and the top apps per device.
- For the hours of a day ("when was I on my phone last night?"):
  `load_screen_time_day`, up to 7 dates.
- For one app or website over time: `load_app_usage` with `app` (part of the
  name is enough). Without `app` it ranks their apps by time.
- Load the totals first and only drill into days or apps the question needs.

## Reading it right

- Phone time comes from Screen Time imports in the Gyroscope app, so some days
  have none. Say how many days the phone numbers rest on (`phone_days`), and
  compare averages over those days, not raw totals across weeks with
  different coverage.
- Productive and unproductive come from each app's category in Gyroscope.
  Present them as that, not as a judgement of their day.
- Line screen time up with sleep, steps or places when they ask what changed,
  using their numbers as the proof points.
- Write durations of an hour or more in decimal hours, and shorter ones in
  minutes.
