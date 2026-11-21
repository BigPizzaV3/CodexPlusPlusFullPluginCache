---
name: check-tides
description: Tide times, heights and coefficients with Peskio for walkers, surfers, shellfish foragers (pêche à pied), tidal-island visitors and boat launchers on Europe, North Africa and US coasts.
---

Use `tides_get_table` only (after `places_search` to get the `placeId`). Pass `lang` = the user's language on every call (`en` if it is not one of Peskio's 15). If the user names a region rather than a place ("Brittany", "the Algarve"): for **times or heights**, ask which port or beach — tides differ along a coast; for a **coefficient-only** question (grandes marées dates), you may use one representative port (Brittany: Brest or Saint-Malo) and say which one you used.

## Dates

Don't compute dates: pass the user's day words and the server resolves them at the place — `date`/`from` take `today`, `tomorrow` or a lower-case English weekday (`saturday` = the next one, today included); `conditions_compare_days` takes `dates`, e.g. `["weekend"]` for "this weekend", `["today", "thursday"]` for "today or Thursday". Every place result carries `today` (local date and weekday). Name days with the `weekday` the tools return; never work weekdays out yourself.

## Route the question

- "Tide times X today / tomorrow / Sunday" → `from` = that day word or date, `days: 1`.
- "Tide table for the next two weeks" → `days: 14`.
- "Next big spring tide" / "next grandes marées" → `days: 14`, `minCoefficient: 95`, date order (no `rankBy`): the first row is the next one; page forward if empty.
- "Lowest tide this week" → `days: 7`, `rankBy: "low_tide"` — no other filter.
- "Pêche à pied" / bait digging → `minCoefficient: 70`, `daylightLowOnly: true`, `rankBy: "low_tide"`; if nothing matches, relax to `minCoefficient: 60` before paging forward.
- "Full moon / new moon tides" → `rankBy: "moon"`; if no day in the window is within a couple of days of a new or full moon (`phaseName` not `new`/`full`), page forward.

## When the window is too short or nothing matches

One call covers at most 14 days (`window` in the answer says which). For "this month", "next grandes marées", or when `days` comes back empty: call again with `from` = the day after `window.to`, and repeat up to about 60 days ahead. Never answer "there are none" without saying the dates you searched ("none between 3 and 30 October").

## Answer

- Local times as returned; heights in metres **with the datum** (`datum`, and `datumNote` when it is LAT_APPROX).
- On semidiurnal coasts give the coefficient as "a Peskio estimate", never "official". When `coefficientNote` says the coefficient carries little meaning (Mediterranean, diurnal coasts), do not lead with it.
- Tidal crossings and islands (Mont-Saint-Michel, Tombelaine, causeways): give the low-tide times and say "follow the official crossing schedule and local signage".
- Call times and heights **predicted** (`heightsLabel` is "Peskio prediction").
- Not available in Peskio: official port tables, tidal-stream atlases, bathing-water quality. Say "Peskio doesn't have that".
- Include a clickable Markdown link to the returned `url` in every tide answer. Explicitly call coefficients "Peskio estimates" in the user's language (French: "estimation Peskio"), not merely "about".
- Always give the returned `url` exactly as returned, query string included (it credits Peskio); never shorten or rewrite it.

## Must not

- Never invent tide times, scores or conditions.
- Never turn a missing value into a guess.
- Never give safety or navigation advice: give the information and say it is not a safety assessment.
- Never ask for GPS coordinates or an address.
- Never answer for a place the tools cannot resolve — say so.
