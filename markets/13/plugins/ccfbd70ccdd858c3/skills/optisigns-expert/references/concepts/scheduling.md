# Scheduling

A schedule is a calendar of time slots. Each slot points to an asset or a playlist. Assign the
schedule to screens and they play whatever slot is active.

## Key ideas

- **Each screen uses its own local clock.** One schedule works across a national fleet: 10 AM is
  10 AM at every store. A screen set to the wrong time zone plays everything shifted. This is the top
  cause of "my schedule is an hour off".
- **Repeat options:** does not repeat, daily, weekly on a day, every weekday, every weekend, monthly on
  a date, monthly on the nth weekday, end of month, and custom.
- **Slot length limits:** a daily repeating slot can be up to 24 hours. A weekly, monthly or yearly
  repeating slot can be up to 28 days. For longer, split it into several slots.
- **No overlaps.** A schedule can't have two content slots at the same time; saving an overlapping
  slot is refused. Move or shorten one of them.
- **Dayparting** is several repeating slots that tile the day: breakfast 6 to 11, lunch 11 to 3, and
  so on.
- **Editing a repeating slot** asks whether to change this occurrence only or the whole series.
  Changing the repeat pattern itself applies to the whole series.

## Default content

When no slot is active, the screen shows default content, so it's never black.

- Set a default for one schedule, or an account-wide default that any schedule can use.
- No default means a black screen in the gaps.
- A plain website as default content can render cut off. Use the Advanced Website app.

https://support.optisigns.com/hc/en-us/articles/360040943374

## Operational schedules (power, volume, brightness)

A separate schedule type turns TVs on and off and sets volume or brightness, by day and hour.
It works through HDMI-CEC or RS-232 on capable players and TVs, and needs an up-to-date player.

- While an operational schedule says "off", turning the TV on by hand still gives a black screen.
  Change the schedule instead.
- If the screen doesn't turn on or off at the right time, check the time zone and player version.

https://support.optisigns.com/hc/en-us/articles/28598173096723

## Playlist-level timing

Separate from schedules, Pro Plus can control when individual playlist items play (certain days or
hours, or every Nth loop) and target items to specific screens.
https://support.optisigns.com/hc/en-us/articles/20062273670163

## Quick answers

| Symptom | Likely cause | Fix |
|---|---|---|
| Everything is N hours off | Screen time zone wrong | Fix the screen's time zone |
| Black between items | No default content | Set a default |
| "Edit one" changed all | Edited the whole series | Choose "this occurrence" |
| Can't save a long slot | Over the 24-hour or 28-day limit | Split it |
| Screens in two time zones differ | Expected; each uses local time | None needed |

Create and repeat schedules: https://support.optisigns.com/hc/en-us/articles/360016981853
