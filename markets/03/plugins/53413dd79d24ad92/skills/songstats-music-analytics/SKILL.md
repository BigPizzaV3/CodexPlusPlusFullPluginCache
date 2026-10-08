---
name: songstats-music-analytics
description: Analyze authorized Songstats music data for artists, labels, collaborators, and tracks. Use for catalog discovery, current or historical performance, release momentum, audience geography, playlist and curator drivers, track comparisons, and source-level trends through the connected Songstats MCP server.
---

# Songstats Music Analytics

Use Songstats as the source of truth for account-scoped music analytics. Resolve
the subject and access context before requesting performance data, then select
the smallest workflow that answers the question.

## Resolve identity and access

1. Start with `list_accessible_profiles` for "my artist," "our label," a
   collaborator, or any profile name. Use `profile_type`, `query`, `limit`, and
   `offset` when needed.
2. Use `list_profile_tracks` for releases belonging to one accessible profile.
3. Use `search_catalog` only when the subject is not resolved from accessible
   profiles or their tracks. Search results are global: inspect `accessible`
   and preserve `access_context` before querying a result.
4. Resolve ambiguous names to a public Songstats ID. Ask the user to choose
   when multiple plausible matches remain.
5. Do not use the deprecated `search_songstats` alias unless compatibility
   requires it.

## Choose the workflow

- For a current artist, label, or collaborator overview, call the matching
  `get_*_insights` bundle. Start with `source=all` unless the user requests a
  specific platform.
- For a track, prefer a result from `list_profile_tracks` and pass its
  `access_context` to `get_track_insights`. If only `songstats_track_id` is
  available, allow the tool to resolve an accessible parent.
- For trends or period comparisons, request `historic_stats` with explicit
  `start_date` and `end_date`. Use `stats` for current totals.
- For geography, request `audience` first, then `audience/details` with one
  relevant two-letter `country_code`. Use track `locations` when the question
  concerns a release rather than a profile.
- For associated drivers, use `top_tracks`, `top_playlists`, `top_curators`,
  `activities`, or catalog data with a visible source and metric.
- For an uncommon read-only question, call
  `songstats_enterprise_api_guide`, then `describe_enterprise_endpoint`, then
  `call_enterprise_endpoint` with only documented parameters.

Keep comparisons to five profiles or tracks by default. Use the same source,
metric definition, and explicit date window for every subject.

## Interpret results

- Convert relative periods into explicit dates and state the selected window.
- Distinguish current totals, absolute change, and percentage change.
- Compare only like-for-like metrics. Never invent a cross-platform composite
  score.
- Treat playlists, curators, activities, and locations as associated evidence;
  do not claim causation from correlation alone.
- State the Songstats objects, sources, access scope, and dates used.
- Treat missing fields as unavailable, not zero.
- When a bundle returns `partial=true`, use successful sections and identify
  the unavailable endpoints.

## Handle limits and unavailable access

- Respect `retry_after`; do not automatically retry a limited request.
- If authorization is expired or the profile is inaccessible, explain the
  returned recovery action instead of working around Songstats access controls.
- If the Songstats MCP connection is unavailable, ask the user to connect or
  reauthorize Songstats. Do not replace private account analysis with open-web
  estimates or model memory.
