---
name: travel-recap
description: Use when someone asks where they went, about a trip, the places, restaurants or cities they visit most, their jetlag, or how travel changed their sleep, eating or routine in Gyroscope.
---

# Places and travel

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead.

## Getting the data

- Places is optional and off unless the member switched it on. If
  `load_places` answers `insufficient_scope`, give them the link it includes
  and say it applies to their next question. Do not retry until they say they
  have allowed it.
- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.
- `load_places` returns visits with the place, its category, the city, arrival
  and departure, up to 7 days per call. For a long span, use `load_history`
  with kind `gvisits` (visits) or `travels` (trips, distance and mode) by
  month.
- `load_weather` gives the weather where they were on a date, for a trip
  recap or a "what was it like" question.

## Writing the answer

- For a trip, give the cities and the main places in order, with how long they
  stayed, and the distance when they ask how far they went.
- For favorites, count visits and name the places, restaurants, cafes and
  cities that come up most.
- For how travel changed their routine, line up the trip's dates with
  `load_sleep`, `load_food` or `load_steps` and compare them with the weeks
  at home.
- For jetlag, work out the time zones crossed and the direction from the
  arrival and departure times, then suggest how to plan the next few days.
- Location history is sensitive. Share only what answers their question.
