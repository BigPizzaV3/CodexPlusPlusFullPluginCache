# Cerca tool guide

The host-discovered schema is authoritative. References are `cerca:<id>` or
`google:<place-id>` returned by a tool; never construct an ID from a place name.

| Tool | Main inputs | Purpose |
|---|---|---|
| `get_travel_context` | destination; optional coordinates/radius | Personal places, avoid list, friends' recommendations, editorial picks and taste |
| `list_my_places` | optional status, destination, category, query, sort, page, per_page | Recall and filter the connected user's saved/rated places; follow `next_page` |
| `search_places` | query; optional near or coordinates | Search existing Cerca places and retrieve references |
| `get_place` | place_ref | Available place details, own status/notes, permitted friend activity and editorial rating |
| `get_taste_profile` | none | Category/tag affinities, declared interests, rating style and city experience |
| `list_friends` | optional query | People the user follows, excluding the official Cerca account |
| `compare_with_friend` | friend; optional destination/coordinates | Shared places, recommendations and caution groups for a visible profile |
| `get_import_status` | optional import_id | Progress of the user's Google Maps list import; defaults to most recent |
| `save_place` | place_ref, google_maps_url, or name+near; optional note | Save to want-to-go; note is private and may replace an existing note |
| `rate_place` | place identity, rating; optional note/reasons | Create/update rating; remove want-to-go save; rating note is public |
| `update_note` | place_ref, note | Replace/clear a private save note or public rating note |
| `remove_place` | place_ref | Delete the user's save or rating and note after confirmation |
| `import_places` | 1–25 items, each with place identity and status | Batch saves/ratings with individual outcomes |
| `import_google_maps_list` | shared list URL | Start a background want-to-go import; check returned import_id |

Read tools require `places:read`. The six mutation tools require
`places:write` and are absent from a read-only connection's discovery.

`get_place` may enrich provider details. Resolving a new save/rating by name
may use Google Places. These lookups are metered; the default per-user limit
is 50 per day, alongside a global limit. Do not promise exhaustive global
search, live reservation availability or guaranteed opening-hours accuracy.
