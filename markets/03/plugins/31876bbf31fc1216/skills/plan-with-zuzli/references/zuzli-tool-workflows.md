# Zuzli tool workflows

## Discover the live contract

Use the Zuzli tools exposed in the current session. Do not rely on a cached tool list or a schema copied into this Skill. Before any create, replace, add, or update workflow, call `get_trip_schema` and follow the current contract exactly.

Use Zuzli as the canonical store while keeping planning responsibility in ChatGPT:

- ChatGPT researches and chooses real places, precise locations, route order, transport intent, timing, and content.
- Zuzli validates, stores, returns, and presents the itinerary. It may derive technical fields only as allowed by the current contract.
- Inspect the canonical write response for defaults, transformations, warnings, and the trip URL.

## Resolve the right trip

1. Use `list_my_trips` when no unique slug is already established.
2. Match destination and dates, not title alone.
3. Ask the user to choose when multiple plausible trips remain.
4. Use `get_trip` immediately before planning an edit or answering a status question.
5. Never create a duplicate merely because conversation memory lacks the slug.

## Create a trip

1. Call `get_trip_schema`.
2. Build the full trip in the current schema with researched locations and complete rich stops.
3. Express the intended transport mode and route guidance in the fields currently supported. Do not leave a consequential transport decision for the server to invent.
4. Call `validate_trip` as a dry run.
5. Fix all errors and investigate warnings that affect usability.
6. Call `create_trip` only after the main design is approved.
7. Inspect the canonical result, then call `get_trip` when needed to verify stored content and server-derived route data.

## Update safely

Choose the narrowest tool that matches the intent:

| Intent | Preferred operation |
|---|---|
| Change facts or content of one stop | `update_stop` with a minimal patch |
| Insert a new place into a day | `add_stop` at the explicit position or after-stop anchor |
| Reorder or move a stop to another day | `move_stop` |
| Remove one approved stop | `remove_stop` |
| Record reported completion | `mark_stop_completed` |
| Record a reported skip | `mark_stop_skipped` |
| Redesign multiple days or remove unsupported fields | `replace_trip`, only after reading and preserving the full trip |
| Delete the whole trip | `delete_trip`, only on an explicit user request with the exact trip resolved |

For partial updates, send only fields that should change. Preserve sibling keys, arrays, IDs, and other stops. For a structural replacement, start from the latest Zuzli object rather than an old local copy.

After every write:

1. Check success, validation findings, defaults, transformations, and warnings.
2. Read the canonical trip when the write response does not contain enough saved data.
3. Verify location, ordering, timing, route mode, links, and unaffected data.
4. Correct unexpected technical transformations before telling the user the task is done.

After `mark_stop_completed` or `mark_stop_skipped`, call `get_trip` and verify that the stop ID appears in the matching progress collection. Treat completed and skipped as mutually exclusive outcomes; if the server rejects a transition, report it rather than rewriting the itinerary to simulate progress.

## Handle tool and contract limits

- If a needed capability is absent, state the limitation briefly and preserve the correct trip data using the safest supported workflow.
- If a cached session does not yet expose progress or `mark_stop_skipped`, do not guess or simulate it by deleting the stop. Ask for the last outcome, continue from the confirmed location, and explain simply that this chat cannot update that progress yet. Suggest a fresh chat only when it is a useful next step; do not mention tool contracts or caching unless asked.
- If live routing or opening data is not supplied by Zuzli, browse authoritative current sources and store the verified result.
- Never bypass a failed validation by deleting useful fields or inventing placeholder locations. Fix the actual problem.

## Keep writes aligned with user intent

Do not write brainstormed options as the active plan. Once the user approves a new plan or gives a direct operational instruction such as “replace lunch with this restaurant,” “we finished the museum,” or “skip the next stop,” perform the corresponding safe write in the same turn. Ask only when the target or consequence is genuinely ambiguous.
