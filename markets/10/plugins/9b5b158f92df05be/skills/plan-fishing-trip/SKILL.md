---
name: plan-fishing-trip
description: Plan when and where to fish on Europe, North Africa and US coasts with Peskio — best day or hour, best spot nearby, conditions per discipline (shore, boat, rock, kayak, spearfishing), why a day is rated poor, what a place is like.
---

Use the Peskio tools to answer anglers. Every Peskio figure must come from tool output. Apply the capability boundaries below before searching or calling a tool.

## Capability boundaries

- A safety or navigation judgement (for example, "Is it safe to sail across the Strait of Gibraltar tonight?") is outside Peskio. Say Peskio cannot assess whether a crossing, dive or trip is safe. Do not offer a vessel/crew assessment, recommend proceeding, or turn a GO rating into permission to go. Offer factual conditions at a named coastal place only if the user wants them, labelled for planning, not safety.
- Temperature at 20 m or any other depth, thermocline and visibility at depth are unavailable. Say this directly without calling tools to approximate the missing quantity. Never derive a depth temperature by subtracting degrees from surface temperature, seasonal averages or web sources. You may offer the surface estimate separately, clearly identified as surface only.
- Inland weather (Madrid), recipes and bookings are outside the plugin. Do not call Peskio tools for them or claim Peskio supplied the answer.

## Dates

Don't compute dates: pass the user's day words and the server resolves them at the place — `date`/`from` take `today`, `tomorrow` or a lower-case English weekday (`saturday` = the next one, today included); `conditions_compare_days` takes `dates`, e.g. `["weekend"]` for "this weekend", `["today", "thursday"]` for "today or Thursday". Every place result carries `today` (local date and weekday). Name days with the `weekday` the tools return; never work weekdays out yourself.

## Route the question

1. Resolve the place with `places_search` (pass the user's words; add `country` when obvious). Use `candidates[0]` unless the result says `ambiguous`; only then ask which one. If none, say Peskio doesn't have that place and ask for a nearby town — never answer for another place without saying so. If the user names a whole region ("the Costa Brava", "Brittany"): for "where" or a multi-day trip, don't ask — use two or three well-known towns there as centres (below) and say which; otherwise ask which town or harbour.
   On every call pass `lang` = the user's language (`es`, `fr`, …; `en` if it is not one of Peskio's 15), so links open the page in that language.
2. Then:
   - **When** ("best day this weekend", "today or Thursday?") → `conditions_compare_days` (`days` up to 7, `discipline` when named; `rankBy: "verdict"` when they care about conditions more than the bite).
   - **A named day / "is it good"** ("tomorrow", "Saturday morning", "too rough today?", "why is Saturday poor?") → `conditions_get_day`. Add `include: ["hourly"]` for any time-of-day or "right now" question (water temperature now, wind at 7 am).
   - **Where near X** → `spots_find_best` with the resolved `placeId` (`radiusKm` up to 25, `hour` for "at 7 am", `discipline` when named, `rankBy: "visibility"` for clearest water). For a region wider than 25 km, call it at two or three named centres and combine.
   - **"Near me"** → `spots_find_best` without `placeId`. If it errors, ask for a town or beach name.
   - **"Right now" / "today"** → omit `date` (today at the place) and, if you know the current local time there, pass `hour` = the current local hour; without `hour` the tool already ranks only the hours of today that have not ended.
   - **What is this place like** (sheltered from a north wind? near a river mouth? big tides?) → `places_get_profile`.
   - **Tide-only questions** → `tides_get_table`.

## Answer

- Local times as returned (they carry the place's offset); verdict or score plus the main reason; the tide coefficient as "a Peskio estimate".
- Say "estimate" for water clarity and for anything spearfishing.
- If `astroOnly` is true, say there is no weather forecast for that day (too far ahead, or not available): tide, sun and moon only. If `freshness.weather` is `stale` or `absent`, say the forecast is old or missing.
- For each recommended place, include a clickable Markdown link using that row's `url`. A list of place names or a map does not replace the links.
- Do not resolve returned place names again with web search or a general map service: duplicate beach names can select a different region. Use the returned placeId, distance and canonical link as the identity. Do not add a name-only map or ratings from an unrelated map provider.
- Always give the returned `url` exactly as returned, query string included (it credits Peskio); never shorten or rewrite it. For a specific date, tell the user to open the page and pick that day in the day strip.
- Not available in Peskio: species, point depth, dive sites, marine reserves, temperature at depth, thermocline, visibility at depth (the visibility estimate is the surface layer only — see `visibility.note`), jellyfish, bathing-water quality. Say "Peskio doesn't have that".
- Every conditions answer carries `disclaimer`; say it in the user's language whenever you give a verdict. GO/marginal/NO describe fishing conditions for planning, not safety. Keep bite score distinct from any discipline conditions score; do not relabel one as the other.

## Must not

- Never invent tide times, scores or conditions.
- Never turn a missing value into a guess.
- Never give safety or navigation advice: give the information and say it is not a safety assessment.
- Never ask for GPS coordinates or an address.
- Never answer for a place the tools cannot resolve — say so.
