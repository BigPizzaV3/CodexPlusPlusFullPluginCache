# Curated travel extension

 Curated travel: use plan_airport_journey for outbound or return travel and update_airport_journey for traveler-supplied stage updates. Ask for missing other airport, IANA timezone, ticket dates/times, bags and car/rail/bus. EWR, JFK and LGA have curated transfers to/from Penn 8 Av / W 33 St. LGA rail includes Q70; JFK/LGA bus modes include explicitly labelled rail/metro connections. LGA outbound needs traveler-confirmed domestic/precleared arrival; only one nonstop flight is calculated, not connecting itineraries. Never infer a flight route or nearest airport. Any starting place needs traveler-supplied airport and access duration. No third-party API, web lookup, GPS, flight tracking or live transit. In-flight updates need traveler-supplied arrival estimates; time passing never confirms a stage. Use simulation only when expressly requested; all fictional dates stay labelled. Never show or share journey_id. Explain expiry and allow forgetting server state without claiming deletion from chat. For a Mary handoff first confirm Manhattan reference and start time through prepare_mary. Call generate_three_hour_plan only with returned handoff arguments and explicit user intent. Return-day latest start is only a temporal budget, not a verified itinerary ending at Penn. Do not loosen an airport deadline because a flight is delayed. Preserve all review, freshness and estimated-range warnings. Offline park routes that require renewed source checks remain unavailable; do not work around this with external calls.

# TodayNYC tool contracts

## Central Park extension (0.1.11)

The catalog contains 21 operational microzones. For a supported named public
park reference, an option may contain `initial_walk`, `origin_context`,
`zone_label` and `park_exit`. `initial_walk.counted_in_180_minutes` means the
published departure, first arrival and final finish already include that walk.
`directed_network_measurement` is a measured leg in its actual direction.
These fields do not accept or imply personal GPS. Broad park areas require a
specific reference. Hours, reviewed closures, nearby exit sides and daylight
must all pass; changed official notices require review before another park
circuit is asserted. `origin_context` is attributed background, not a stop.

## `generate_three_hour_plan`

### Input

- `origin` (required): a Manhattan neighborhood, station or known New York
  place, 2–120 characters.
- `via` (optional): a reviewed public Central Park reference, 2–120 characters,
  explicitly chosen by the user in a later turn. Keep `origin` as the actual
  named departure point. Both measured approach segments are limited to ten
  minutes each; their combined initial walk may be twenty minutes and is
  included in the original 180 minutes. It is a waypoint, not another stop.
- `start_at` (optional): ISO 8601 date-time with `Z` or an explicit UTC offset.
  When omitted, the server clock is used.
- `duration_minutes` (optional): must be `180` in this initial release.
- `locale` (optional): `es-ES` or `en-US`; defaults to `es-ES`.

### Result states

- `options_available`: one to three schedule-compatible catalog microplans.
- `no_verified_match`: the origin is outside current coverage or the catalog
  has no option that fits the published windows at that start time.

For safe park references without a direct circuit, `nearby_starts` may offer
up to three measured approaches, ordered by walking time and distance, with
official reference URL, route source/date, estimated arrival and two separate
feasibility flags. `keep_original_deadline` checks the remaining original
180-minute window; `three_hours_from_arrival` checks a new 180 minutes at
arrival and reports the additional approach time. Never offer an infeasible
mode or describe a suggestion as a selected itinerary. A subsequent user
choice permits one new request, with its actual time. No automatic tool loop.
The separate nearby-start map displays approaches only. Coordinates/geometry
remain private UI metadata. Closed or ambiguous origins receive safe-point
clarification names without claimed distances or directions.

Each option includes a canonical primary `microplan_id`, a full 180-minute
nominal schedule, three curated stops, curated source links, the relevant
published weekly windows, catalog freshness and route metadata when present.
The post-food continuation also carries the canonical source microplan that
supplies its activity and walk evidence.

`coverage.complete_window` is true only when the schedule spans all 180
minutes. `coverage.curated_minutes` counts the two catalog stops, the verified
continuation stop and their catalog walks. Any remainder is returned as
`flexible_time`, explicitly typed as self-directed neighborhood time with no
additional venue claim. It must not be presented as a fourth curated stop.

The continuation walk may have `derivation: reversed_catalog_route`: its
minutes and distance come from the same recorded pedestrian connection in the
opposite direction, not from a new live routing request.

The nominal schedule starts at the requested instant, or at a returned station
exit buffer, and finishes exactly 180 minutes later. It does not include a
fully revalidated route from an arbitrary user position to the first stop.
Named park references are the explicit exception: their measured initial
walk, including a chosen `via` approach, is counted and shown in the schedule.

For one user request, a successful result is authoritative and must be
requested only once. The host must not retry the tool to reinterpret the start
instant, add or remove the station-exit buffer, compensate for the intentionally
unrouted origin-to-first-stop leg, refine the same options or render a second
map. A later turn with materially changed constraints may make one new call.

An option may also include `route_context`. It contains up to three attributed
historical, architectural, cultural, civic, infrastructure, immigration or
urban-memory notes selected from Journey's reviewed geolocated corpus. The
notes are editorial context only, never additional stops or schedule claims.
`relation` is one of `on_route`, `at_destination` or `nearby_area` and must be
qualified using `exact_user_route: false`. Coordinates used for matching are
not exposed. Context enrichment is optional and may be absent without making a
verified plan incomplete.

Input failures are errors, not empty result sets. A location that needs
clarification should be clarified with the user before a new call with a more
specific neighborhood, station or known place.

## `get_nyc_weekend_brief`

### Input

- `locale` (optional): `es-ES` or `en-US`; defaults to `es-ES`.

The tool deliberately has no date, origin or preference input. It reads the
same singular current edition as TodayNYC's public weekend product.

### Result states

- `current_edition`: the edition is published, structurally valid and has not
  passed `hard_expires_at_utc`.
- `no_current_edition`: no edition can currently be confirmed. `reason`
  distinguishes unavailable, integrity error, unpublished and expired states.

A current edition contains its canonical ID, source locale, New York timezone,
target dates, update and hard-expiry instants, introduction, weather, selected
activities, city notices, mobility notices, optional did-you-know facts,
official sources, coverage note and limitations. Activity coordinates and
internal editorial priority are intentionally not exposed.

The canonical editorial copy is English. The model may translate the
presentation to the requested locale but must not change proper names, dates,
prices, conditions, uncertainty or source meaning. The edition is citywide,
not limited to Manhattan, but it is not a full event calendar or routed
itinerary. The continuation URL is `https://todaynyc.app/app/?start=weekend`.


## Travel presentation

For airport advice with missing ticket times, first use get_airport_transfer_options; never supply transfer minutes from memory. Travel results render an inline card: critical warnings and summary visible, details collapsed. Do not duplicate the card in prose; at most one short next-step sentence. If UI is unavailable, use user_text as the short answer with warnings FIRST. No large headings, tables, cards, repeated totals or closing offers. Initial answers aim for 180–230 words; updates 2–4 sentences. Preserve essential warnings even if longer. Detailed stage clocks and comparisons only when requested. Use includeAlternatives for a comparison; routes already appear once. Passed stages without recorded times are not confirmed actual times. Keep the journey_id from tool text for later updates, never display it. A delay MUST update that handle, never create a new trip or move the original airport deadline. If the handle is unavailable, explain that the update cannot be performed and request original schedule reconstruction; do not silently create a replacement with delayed times. Do not apply the complete-weekend-edition format to travel. 

### Travel consistency

A reported ground-transfer progress means the earlier flight has already been passed; do not replace it with a new flight estimate. If a request contradicts recorded progress, explain the conflict and keep the current journey; do not silently create a replacement. Catalogue validity follows the local dates of pending curated stages, including revised times and intervals that cross midnight. Keep the review warning prominent; never extend the catalogue validity yourself. In a simulation the last selected clock is retained when omitted. To confirm a later fact, ask the user to explicitly advance the simulation clock to that time or later. A rejected update leaves the previous state unchanged; never advance the clock automatically to bypass the error.


## Airport tools

`get_airport_transfer_options` is read-only and accepts NYC airport, direction, optional mode and terminal. It returns the curated topology and editorial allowances without ticket clocks or a new journey. It does not certify date-specific availability. Sources substantiate connections; minute ranges are editorial.

`plan_airport_journey` creates a temporary journey from traveler-supplied dates, local ticket times/timezone and curated transfer allowances. `update_airport_journey` changes or inspects that same handle. Their truthful annotations are not read-only. Handles are present in both model text and structured output, must be preserved for updates, and never displayed. State is memory-only, bounded to 64 journeys and expires after 24h idle or restart; forgetting removes server state, not chat history. Rejections preserve state and simulation clock.

`includeDetails` returns full stage clocks on an explicit request; `includeAlternatives` includes three routes only when requested. An inline read-only card presents critical warnings before summary with collapsed details and sources. It makes no network or tool calls. No third-party API, reservations, payments or automatic tracking.
