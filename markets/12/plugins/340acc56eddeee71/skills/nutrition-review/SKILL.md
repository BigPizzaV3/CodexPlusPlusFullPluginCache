---
name: nutrition-review
description: Use when someone asks about their eating patterns, calories, protein or macros over time in Gyroscope, how their eating relates to their weight, or wants meals planned around their own targets and the foods they already eat.
---

# Reviewing nutrition and planning meals

If no Gyroscope tools are available, follow the connect-gyroscope skill
instead. To log something they ate, use the log-food skill.

## Getting the data

- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.
- What they ate: `load_food` for the dates in question, up to a few weeks in a
  few calls.
- Totals over time: `load_trend` with metric `calories` or `protein`, weekly
  or monthly.
- Sodium, potassium, saturated fat, cholesterol, calcium, iron and
  magnesium come with every item and day from `load_food` and `load_day`.
  For another nutrient (a vitamin, zinc), pass `nutrients` with its name
  and unit (`vitamin_d_mcg`) to `load_food`, or to `load_history` with
  kind `food` for a month at a time. A null or empty cell means
  Gyroscope's analysis of that item did not cover it; say how many items
  a day's total rests on.
- Their targets: use the calorie and protein targets they give you. If they
  have not said them, ask once.

## Patterns

- Name the meals and foods that come up most, when they tend to eat, and how
  calories and protein compare with their targets.
- When they are working on their weight, line up weekly calories with weekly
  weight (`load_trend` with metric `weight`, or `load_history` with kind
  `weight` for the weigh-ins)
  and say how the two moved together.
- Say how many days each pattern rests on.

## Meal plans

- Build from their real targets and the meals they already eat, adjusting
  portions and swaps rather than starting from nothing.
- Give rough calories and protein per meal so the plan can be checked against
  the target.
- Plans are suggestions. Log a meal only when they say they ate it.
