---
name: get-started
description: How to use Seemor to decide where to eat and to check a specific restaurant. Covers which Seemor tool answers which kind of dining question, how to relay grades, caveats and coverage honestly, and what to do when a daily limit is reached.
---

# Seemor: restaurant grades from what reviews actually say

Seemor reads what people wrote in restaurant reviews and menus, grades each restaurant (A+ to F, or a preliminary band such as "B-range" for lightly analyzed places) and explains the grade in plain words: what to order, how loud it is, whether it suits a date, a family or a group, and what people complain about. Every tool is read-only. Nothing books a table, changes the diner's account or charges anything.

## Which tool answers which question

- **recommend**: the diner wants to decide where to eat for an occasion ("quiet Italian for a date night in Chelsea", "dinner for six near Shibuya station"). Call it once per ask with the full request in `query` and the place in `location`. The result is ranked and final. Do not re-run it with reworded variations and do not call `lookup_restaurant` on each result to double-check it. For follow-ups about one place, use `lookup_restaurant` or `ask_about_restaurant`.
- **search_restaurants**: the diner wants to browse a list near a named place by distance or filters (cuisine, price level, minimum grade), not a judgement about which to pick. For picking, use `recommend`.
- **explore_area**: the diner wants the shape of an area's dining scene ("what is Shoreditch like for food?"): grade distribution, top cuisines, price range and highlighted restaurants. Not for finding one restaurant or for a personal recommendation.
- **find_restaurant**: the diner names a restaurant. It returns matching places with their Seemor IDs; pass `city` when the name is common. Chains return one row per branch, so ask which branch when it matters.
- **lookup_restaurant**: full details for one Seemor ID (grade, summary, what people love, concerns, signature dishes, cost estimate). Use it for the single place the diner asked about, not for every result of `recommend`.
- **ask_about_restaurant**: one specific question about one restaurant ("what should I order?", "is it good for groups?"). Needs a Seemor ID from `find_restaurant` or `search_restaurants`. One question per call.

## Planning several meals

For a trip or several occasions, call `recommend` once per meal slot with the anchor (hotel, landmark or neighborhood), the time of day, the party and the diner's stated constraints, and carry forward dislikes the diner stated earlier. You own the plan and the bookings; Seemor owns the per-meal choice. Use `find_restaurant` only for places already named. The trip-dining skill has the full workflow.

## Places and locations

Every recommendation or search needs a place named in words: a city, neighborhood or landmark the diner mentioned. If the diner has not named one, ask which city or area they mean. Do not guess a city and do not send the diner's own device location unless the diner gave it. When a name is shared by several places ("Victoria", "Soho"), pass the city or country too, or relay the `candidates` the tool returns and ask.

## Relaying results honestly

- Give each place its grade or preliminary band and the reasons it fits. A caveat beginning "Misses" names something the place does not deliver; relay it rather than smoothing it over.
- When `result_groups` is present, present the groups top to bottom in the order given, using each group's own `message` as written, and keep the rows in their given order.
- `coverage_level` tells the truth about depth: `full` rows carry a letter grade; `basic` rows are quick reads graded from review analysis, with `grade` null and a `preliminary_band`; `none` rows have no analysis yet. Say so when results are quick reads or when a result `message` notes a thin pool, instead of searching again.
- A `place_note` ("In Hoboken") means the place is outside the area asked for. Say so; never imply it is inside.
- `repeat_ask: true` means the same answer was already given for the identical ask. Say so rather than presenting it as new.
- Seemor's grades come from reviews and menus, not visits. It cannot confirm opening hours, availability or allergy safety, and it cannot book tables.

## Daily limits

Connected accounts have a small free number of `recommend` runs and `ask_about_restaurant` answers per day; searching, finding, looking up a restaurant and exploring an area do not count. When a result carries `limit_reached`, relay its `message` to the diner as written and do not retry. The message reads, for example:

"You've used today's 10 free Seemor recommendations in ChatGPT. You can keep going in the Seemor app at https://app.seemor.ai with the same account. The limit resets at midnight UTC."
