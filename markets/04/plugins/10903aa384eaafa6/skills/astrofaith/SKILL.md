---
name: astrofaith
description: Use Astrofaith to resolve locations, calculate authoritative Swiss Ephemeris charts, find planet-in-natal-house transit periods, and securely manage the connected member's saved birth profiles. Includes exact MCP payloads, provenance, settings, output selection, and environment data-boundary guidance.
---

# Astrofaith

Use the authenticated Astrofaith MCP server for authoritative chart calculation
and saved birth-data management. Treat returned birth data as private.

## Confirm context first

Call `birthdata_capabilities` before saved-data work. Every result includes
`astrofaithContext`: staging and production data are separate, and results
belong only to the Astrofaith member who approved the current OAuth connection.

## Recommended workflow

1. Use `resolve_location` to obtain a canonical label, coordinates, and IANA
   timezone. If it returns multiple candidates, ask the user to choose. A
   returned candidate can be reused unchanged as a calculation birth's
   `location` object or as a transit location; do not delete or rename its
   metadata fields.
2. Search with `birthdata_list` before creating a duplicate.
3. Create with `birthdata_create`, a unique `idempotencyKey`, canonical
   `birthData.options`, and structured provenance where known.
4. Calculate with `calculate_chart` using either `profileId` or explicit
   `birth`, never both. Saved zodiac and house settings are inherited unless
   explicitly overridden.
5. Use basic output for ordinary readings. Use deep output only when the task
   needs its extra audit detail, eclipses, or complete aspect data. Prefer
   `output.sections` and `maxAspects` to keep responses focused.
6. For "when is planet X in natal house Y?", call `find_transit_house_periods`
   once. Do not approximate the answer by sampling several `calculate_chart`
   results. Resolve and pass a canonical `transitLocation` when the user names a
   location; otherwise the saved profile location and timezone are used.
7. For a natal-plus-transit bi-wheel or cross-chart aspect question, call
   `calculate_transit_comparison`. Use its `inner`, `outer`, and
   `comparison.aspects` as one authoritative result instead of combining
   independent chart calls.
8. Return `links.openInAppUrl` when the user wants to continue interactively and
   `links.renderUrl` for a deterministic chart-only view. Explain that plugin
   OAuth and the Astrofaith browser login are separate sessions; a private
   saved-profile link may ask the user to log in again in the browser.
9. Read a record immediately before update or deletion and pass its `etag` as
   `ifMatch`. Confirm destructive deletion with the user.

Read `references/contracts.md` for exact payloads, supported values, source
provenance, ranking semantics, and error correction.
