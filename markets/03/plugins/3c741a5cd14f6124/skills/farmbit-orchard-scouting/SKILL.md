---
name: farmbit-orchard-scouting
description: Use Farmbit to locate a real orchard, run a free 30-day Sentinel-2 check, reopen a preview, or inspect temporal evidence for fields in a linked Farmbit account. Trigger for orchard satellite checks, vegetation or moisture change questions, field monitoring status, and ground-check prioritization.
---

# Farmbit Orchard Scouting

Use Farmbit evidence to decide where a grower should inspect first. Keep location identity, agricultural eligibility, temporal processing state, and satellite limitations explicit.

## Choose The Workflow

### Check An Address Or Orchard

1. Call `farmbit_search_orchard_locations` with the user's address, orchard name, parcel, or locality.
2. If results are ambiguous, show the specific candidates and ask the user to choose. Do not guess from a locality-only match.
3. Call `farmbit_create_free_satellite_preview` with the selected `candidate_id`.
4. Interpret `eligibility` before discussing imagery:
   - `accepted`: continue with the returned preview and 30-day temporal state.
   - `needs_confirmation`: explain that the boundary must be reviewed or drawn in Farmbit. Do not claim that a Farmbit preview or temporal analysis exists yet.
   - `rejected`: state the returned reason and offer a new search. Do not call the place an orchard or estimate orchard acreage.
5. If a preview has `temporal.status: pending`, retain its `preview_id` and use `farmbit_get_free_satellite_preview` to check it again when the user asks for an update.

Use only one location mode per creation request:

- A selected search result: `location_mode: "candidate"` with `candidate_id`.
- A plain search when no candidate is available: `location_mode: "address"` with `address_query`.
- A prepared Farmbit location: `location_mode: "prepared_location"` with `location_id`; add `boundary_id` only when it belongs to that location.
- A point: `location_mode: "point"` with both `lon` and `lat`.
- A known block polygon: `location_mode: "geometry"` with `geometry` and its truthful `geometry_source`. Use `field_boundary` only when the user has explicitly reviewed or drawn that boundary.

### Inspect A Linked Field

1. If the user did not identify a field unambiguously, call `farmbit_list_fields`.
2. Match by the returned `field_id` and `field_label`; ask the user when more than one field is plausible.
3. Call `farmbit_get_field_temporal_evidence` with the selected `field_id`.
4. Use a 30-day lookback for current scouting. Use 60, 90, 180, or 365 days only when the user asks for a longer comparison.
5. Request only supported indices: `ndvi`, `ndwi`, `ndmi`, `ndre`, and `evi`.

## Report Evidence

Treat the temporal status as authoritative:

- `pending`: processing has not produced evidence yet.
- `partial`: report only available observations and explain what is still incomplete.
- `ready`: summarize the observed window, strongest supported change, confidence, limitations, and recommended next action.
- `no_scenes`: say that no qualifying Sentinel-2 scenes were available in the requested window.
- `failed`: state that processing failed and do not infer a field condition.

For `ready` or `partial` evidence:

1. Name the observation window and scene or observation count.
2. Describe where the strongest supported change occurred when the evidence provides a location or affected-area value.
3. Describe the signal as a satellite-observed pattern, such as vegetation increase, vegetation decrease, or moisture-related change. Do not diagnose a cause.
4. Include the returned confidence, quality, unavailable indices, and limitations.
5. End with the returned ground-check recommendation or a cautious first inspection step.

## Guardrails

- Never turn missing observations into a successful result.
- Never let agricultural appearance override a location mismatch.
- Never describe satellite evidence as proof of disease, irrigation failure, nutrient deficiency, or another diagnosis.
- Never invent values, dates, causes, boundaries, scenes, or recommendations.
- Distinguish a free public check from private linked-field evidence.
- Keep Farmbit links returned by the tools available for map review and follow-up.
