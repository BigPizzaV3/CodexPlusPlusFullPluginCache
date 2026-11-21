---
name: trip-dining
description: How to use Seemor when planning meals for a trip or several occasions. One recommend call per meal slot, verifying places that are already named, relaying grades and bands honestly, and handing off to booking apps.
---

# Planning several meals with Seemor

## 1. Who does what

You own the plan: the days, the neighborhoods, the times, the weather, the bookings. Seemor owns the per-meal choice: for each meal slot it returns one ranked, graded answer. Do not generate your own list of candidate restaurants and check them one by one with `find_restaurant`. That takes many calls and misses places Seemor would have ranked for the ask.

## 2. One recommend call per meal slot

For each meal, call `recommend` once with:

- **The anchor**: where the diner will be. A hotel address, a landmark, a neighborhood ("walking distance of 11 Rue Jules Chaplain", "near the Musee d'Orsay"). Put the place in `location` or in the query.
- **The time**: "Thursday dinner", "quick lunch", "late breakfast".
- **The party**: who is eating and how many. Kids and their ages, a date, a group of six.
- **The stated constraints and dislikes**, in the diner's own words. Carry forward what the diner said earlier in the conversation ("no escargot, steak frites works") into every later slot it applies to. Do not add emphasis or qualities the diner did not state.

A dish ask ("good beef bourguignon near the Marais") is a `recommend` ask. A minimum grade ("A- or better") is `search_restaurants` with `min_grade`, or say it in the `recommend` query.

**Worked example.** A family of four (kids aged 11 and 13) staying at 11 Rue Jules Chaplain, Paris, four days, no escargot or duck confit, steak frites is welcome. Thursday dinner near the Musee d'Orsay becomes one call:

- `query`: "Thursday family dinner with two kids aged 11 and 13 near the Musee d'Orsay, no escargot or duck confit, steak frites works"
- `location`: "Paris"

Friday lunch in the Marais is a second call, with the same party and dislikes and its own anchor and time. Repeat for each slot. Present each answer as it comes back: the groups in the order given, each group's message as written.

## 3. Places that are already named

When the diner, a guide or a booking app names a place, call `find_restaurant` with the name and `city` (a neighborhood also works, in English or the local language). Then call `lookup_restaurant` only for the one place the diner is deciding on. Chains return one row per branch: pick the branch by address or neighborhood, and ask when it matters. A result with no match means Seemor has no match for that spelling; try the name without a leading article (Le, La, Cafe, Chez) before telling the diner the place is not covered.

## 4. Reading results

- `full` rows carry a letter grade (A+ to F).
- `basic` rows are quick reads with a `preliminary_band`. The band is the floor of the range: "B-range" means at least B minus. A full analysis can be requested in the Seemor app.
- `none` rows are not yet analyzed. Say so instead of guessing.
- A caveat beginning "Misses" names something the place does not deliver. Relay it as written.
- When a message says the pool was thin or a filter was relaxed, relay it instead of searching again.
- "Not covered" means Seemor has not analyzed that place, not that the place is bad.

## 5. Handing off to booking apps

Seemor holds no booking, availability or opening-hours data. Use a booking or maps app for those and join on the restaurant's name and address. Rows carry `google_maps_url` and `website` when Seemor holds them, and `seemor_url` for the restaurant's Seemor page. Never state availability or opening hours from Seemor results.

## 6. Daily limits

Connected accounts have a small free number of `recommend` runs and `ask_about_restaurant` answers per day. Only runs that return results count; searching, finding, looking up a restaurant and exploring an area do not count. Plan the slots before calling so each call is a real meal choice. When a result carries `limit_reached`, relay its `message` to the diner as written and do not retry. For the remaining slots, the diner can keep going in the Seemor app with the same account, or you can verify places the diner names with `find_restaurant` and `lookup_restaurant`, which do not count.
