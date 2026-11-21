# Peskio plugin — golden prompt set

Spec 2026-09-30 §4.2 and §7. Run in ChatGPT Developer Mode against a local instance (plan A Task 21)
and again on production (Task 22). **S** = one of the five submission prompts. Plan-B rows (diver mode)
are expected to be answered in angler framing or declined until plan B ships.

| # | Persona | Lang | Prompt | Expected tool calls | Pass when | Plan |
|---|---|---|---|---|---|---|
| Q1 | angler | EN | Best time to fish at Cadaqués this weekend? **S** | `places_search` → `conditions_compare_days` | names the better day, best window, a reason, link | A |
| Q2 | angler | ES | ¿A qué hora es la marea alta en Sitges mañana? **S** | `places_search` → `tides_get_table` | local high-tide times, datum, link | A |
| Q3 | angler | EN | Is tomorrow good for spearfishing at L'Escala — visibility? | `places_search` → `conditions_get_day` (`discipline: spearfishing`) | verdict + visibility range, both called estimates | A |
| Q4 | angler | EN | Kayak fishing off Palamós Saturday morning — wind and swell? | `places_search` → `conditions_get_day` (`discipline: kayak`, `include: [hourly]`) | morning hours' wind/waves, verdict | A |
| Q5 | angler | EN | Where near Barcelona is best for shore fishing tomorrow? **S** | `places_search` → `spots_find_best` (`discipline: shore`) | ranked spots with links | A |
| Q6 | angler | EN | Clearest water for spearfishing near Nice this week? | `places_search` → `spots_find_best` (`rankBy: visibility`) → `conditions_compare_days` | clearest spot and day, estimate caveat | A |
| Q7 | tide | EN | When's the next big spring tide in Saint-Malo? | `places_search` → `tides_get_table` (`minCoefficient: 95`, date order; page forward if empty) | date + Peskio-estimate coefficient | A |
| Q8 | angler | EN | Sunrise and solunar major periods at Ericeira on Saturday? | `places_search` → `conditions_get_day` | sunrise, major periods in local time | A |
| Q9 | angler | EN | Boat fishing today or wait until Thursday? (after naming a place) | `conditions_compare_days` (`discipline: boat`) | compares the two days | A |
| Q10 | angler | EN | Too rough for rock fishing in A Coruña today? | `places_search` → `conditions_get_day` (`discipline: rock`) | verdict + negative reasons; no safety verdict | A |
| Q11 | angler | EN | Water temperature in Split right now? | `places_search` → `conditions_get_day` (`include: [hourly]`) | SST at the current hour, freshness | A |
| Q12 | angler | EN | Why is Saturday rated poor? (after a compare) | `conditions_get_day` | factors / negative reasons / explanation | A |
| Q13 | angler | EN | Is Port de la Selva sheltered from a tramontana (north wind)? **S** | `places_search` → `places_get_profile` | answers from `shelteredFrom`/`exposedTo` | A |
| Q14 | tide | EN | Lowest tide this week at Arcachon for bait digging? | `places_search` → `tides_get_table` (`rankBy: low_tide`) | lowest low per day, datum | A |
| Q15 | angler | EN | When's the full moon, and is it good for fishing? (place named) | `tides_get_table` (`rankBy: moon`) + `conditions_get_day` | phase date + bite | A |
| Q16 | angler | EN | 3-day trip on the Costa Brava next week — where each day? | `spots_find_best` at 2–3 named centres → `conditions_compare_days` | a plan per day with links | A |
| Q17 | angler | EN | Murky at Valencia after the rain? Near a river mouth? | `conditions_get_day` + `places_get_profile` | visibility factors; river-mouth unknown said as unknown | A |
| Q18 | all | EN | How reliable is this forecast? | (from previous output) | freshness, confidence, tide source, clarity source | A |
| Q19 | tide | EN | What's the tide range here — big or small tides? | `places_get_profile` | regime, spring range, datum | A |
| Q21 | diver | EN | Visibility at the Medes Islands this weekend — and at 20 m? | `conditions_get_day` | plan A: surface estimate only, "at depth unknown" | B |
| Q22 | freediver | EN | Best day this week to freedive at Cap de Creus — clear and calm? | `conditions_compare_days` (`rankBy: visibility`) | clearest + calm day | B |
| Q23 | diver | EN | When is the current weakest at Sesimbra tomorrow? | `conditions_get_day` (`include: [hourly]`) | lowest-current hours, never "slack water" | B |
| Q24 | diver | EN | Surge at the entry — is the swell coming straight in? | `conditions_get_day` + `places_get_profile` | swell direction vs exposure | B |
| Q25 | diver | EN | Water temperature at Nice — 5 mm or 7 mm? | `conditions_get_day` | SST + freshness; suit advice hedged | B |
| Q26 | snorkeller | EN | When will fish be most active to watch at Port-Cros? | `conditions_get_day` | activity windows, no fishing words (plan B) | B |
| Q27 | snorkeller | EN | Where near Dubrovnik is the clearest, calmest water tomorrow? | `spots_find_best` (`rankBy: visibility`) | ranked spots | B |
| Q28 | diver | EN | Is the water green — plankton bloom? | `conditions_get_day` | plan A: clarity class; plan B: chlorophyll | B |
| Q29 | diver | EN | Night dive tonight — sunset and moon? | `conditions_get_day` | sunset, moon illumination | B |
| Q30 | diver | EN | How much light is left at 30 m at midday? | `conditions_get_day` | plan A: "not available"; plan B: blue light at depth | B |
| Q31 | tide | EN | Tide times Biarritz today | `places_search` → `tides_get_table` | extremes, datum, link | A |
| Q32 | tide | FR | Coefficient de marée à Saint-Malo aujourd'hui ? **S** | `places_search` → `tides_get_table` | coefficient as Peskio estimate, in French | A |
| Q33 | tide | EN | Next grandes marées in Brittany? | `places_search` (Brest or Saint-Malo, named as the representative port) → `tides_get_table` (`minCoefficient: 95`, date order) | dates ≥ 95, says which port | A |
| Q34 | tide | FR | Meilleurs jours pour la pêche à pied à Cancale ce mois-ci ? | `tides_get_table` (`minCoefficient: 70`, `daylightLowOnly: true`) | daylight lows on big tides | A |
| Q35 | tide | EN | Low tide at Mont-Saint-Michel on Sunday — how low? | `tides_get_table` | low time + height + datum; crossing caveat | A |
| Q36 | tide | PT | Tabela de marés para a Nazaré, próximas duas semanas | `tides_get_table` (`days: 14`) | 14-day table | A |
| Q39 | all | EN | Where's good near me right now? | `spots_find_best` without placeId (else asks for a town) | never asks for GPS | A |

## Regression-only (inform, decline the judgement / not available)

| # | Prompt | Expected |
|---|---|---|
| Q37 | Is it safe to dive today? / Can I walk to the island at 3 pm? | gives conditions or low-tide times, declines a safety verdict |
| Q38 | Thermocline? Temperature at 20 m? Jellyfish? Marine reserve? | "Peskio doesn't have that"; no invented depth estimate from surface or seasonal values |
| Q20 | What fish can I catch at X? / How deep is it off X? | "Peskio doesn't have that" |
| — | Is it safe to sail across the Strait of Gibraltar tonight? | no safety verdict; at most information with the disclaimer |

## Negative (the plugin must not be invoked)

| Prompt | Expected |
|---|---|
| Weather in Madrid tomorrow | no Peskio tool call |
| Recipe for grilled sea bass | no Peskio tool call |
| Book a ferry from Tarifa to Tangier | no Peskio tool call |

## Results

| Date | Where | Model | Pass | Fail (ids) | Notes |
|---|---|---|---|---|---|

## ChatGPT regression checks after production connection (2026-10-04)

Run in fresh chats with the full plugin selected, not just the bare MCP connection.
The private account test package must bind the registered production app and include
these skills. Portable MCP-only packages can be desktop-only; the public upload
must still exclude private app bindings.

- Nearby shore spots at L’Escala: every recommended row has its exact canonical,
  UTM-tagged Peskio URL; no generic map resolves duplicate beach names to another region.
- French Saint-Malo coefficient: explicit "estimation Peskio", local times and exact link.
- Safety crossing request: Peskio cannot assess safety; no vessel/crew judgement,
  recommendation to proceed, or promise to assess the crossing specifically.
- Temperature at 20 m: unavailable; no number at depth inferred from surface/seasonal data.
- "Near me": attempt spots_find_best without placeId; needs_place asks for a town,
  never GPS coordinates. Production logs confirmed needs_place in the owner's test.
- Madrid weather, recipe and ferry booking: no Peskio tools.
