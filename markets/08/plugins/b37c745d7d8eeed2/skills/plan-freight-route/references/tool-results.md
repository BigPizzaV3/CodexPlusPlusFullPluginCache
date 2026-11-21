# What the NoMap tools return

Each tool returns readable text plus a structured object. The text is safe to
relay; the structured object is there when you need a specific field. Every
successful result carries `disclaimer` — the figures are a planning overview,
not navigational advice.

## plan_route

| Field | Meaning |
|---|---|
| `points` | The identified places in order: `id`, `name`, `country`, `unlocode`, `lat`, `lon`. These are the only place identifiers to quote. |
| `legs` | One entry per calculated hop: `mode`, `from`, `to`, `distanceKm`, `durationMin`, and `error` when that hop could not be routed. |
| `suggestedModes` | What the parser inferred from the request. This is the *suggestion*, not the result. |
| `modeFallbacks` | Present when a leg was calculated with a different mode than suggested — `{ suggested, from, to }`. Say so when reporting that leg. |
| `totalDistanceKm` | Sum across legs, or null when nothing could be calculated. |
| `planUrl` | Opens the same route in NoMap. Always offer it. |
| `mapImageUrl` | The map card as a URL. A URL is not a picture — call `route_map` to show the map. |

A leg with an `error` did not route. Report that leg as unavailable rather
than dropping it silently, and do not substitute a straight-line estimate.

## Failures

An unresolved request returns `ok: false` with `warning`, `suggestions` (up to
eight candidate places, some with UN/LOCODEs) and `failedQuery`. Show the
candidates and ask which one the user meant. Never choose for them — picking
the wrong Springfield or the wrong Victoria sends the cargo to another
continent.

## route_map

| Field | Meaning |
|---|---|
| `mapImageUrl` | Full-size card. |
| `title` | The route, e.g. "Rotterdam → Shanghai". |
| `widthPx` | Width of the returned image, or null when none was embedded. |
| `planUrl` | Same NoMap link as `plan_route`. |

The map arrives as a widget, or as an image block when `inlineImage` is true.
Show it as returned.

## search

Returns `results`, each `{ id, title, url }`. The `id` is what `fetch` takes.

## fetch

Returns `{ id, title, text, url, metadata }`, where `metadata` carries
`totalDistanceKm`, `mapImageUrl` and the disclaimer. The `id` is the original
route request, so `fetch` recalculates the route rather than reading a stored
record — a route fetched twice is computed twice and may reflect updated
routing data.
