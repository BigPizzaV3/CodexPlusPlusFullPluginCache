---
name: discover-tattoos
description: Find tattoo inspiration from Tatty by theme, style, placement, and size; compare available visual directions and source-backed tattoo references.
---

Help the user choose a tattoo direction from actual Tatty results. Explicit user preferences take priority. This workflow covers inspiration; it does not authorize generation, publication, artist bookings, or tattoo health advice.

Use `search_tattoo_designs` with the user's supplied query and filters. Read its live schema for supported values and bounds. Ask a focused question only if missing information would materially change the results; otherwise search with what is known. Public search and public design details need no login or guest session.

Compare distinct matching references when available, using returned previews, titles, IDs, provenance, match information, and allowed actions. Show the useful results first. If coverage is sparse, a size or placement is only a suggested fit, or a match is weak, say so. `missingPreferences` describes gaps in the result's match or metadata, not preferences the user forgot to supply; do not ask them to repeat settings already given. Return fewer references when that is what the service finds; do not fabricate examples, images, source citations, cultural meanings, or popularity claims.

Use `get_tattoo_design` only with an ID returned by the service when the user needs detail or selects a reference. For a guest-generated design, pass the original `sessionKey` only in the tool arguments; never show it in prose, links, or telemetry. Read [reference rules](references/reference-rules.md) when results include different provenance or reuse permissions.

An original digital concept is an illustration, not a finished or healed tattoo. Editorial reconstructions remain inspiration with their supplied sources and limits. Do not infer copying, download, import, or exact try-on permission from public visibility.

After useful results, provide the returned source or website link when it helps the user. Offer a personal original variation only as a possible next task. Use an eligible returned continuation for browser preview or download, and provide the Tatty app download route when useful. Describe only the actions the record actually permits. Guest artwork does not establish automatic import into the current app. Do not require an app download to see available references or insert upgrade offers.
