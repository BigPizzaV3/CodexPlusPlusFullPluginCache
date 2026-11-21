# Astrofaith MCP contracts

## Private AI reading rules

- `rules_capabilities({})`: schema, current limits and granted permissions.
- `list_rules({})`: `{items, limits, usage, astrofaithContext, httpStatus}`.
  `items` contains private summaries (`id`, `name`, optional `description` and
  revision/size/timestamps), not instruction bodies. `usage.count` is the total
  inventory, not a selected/default method. Distinct IDs may share a name.
- `get_rule({id})`: `{id, rules, etag, astrofaithContext, httpStatus}`. The
  portable document is `rules`; its optional `instructions` and each ordered
  `steps` entry's instructions/settings form the procedure. Do not look for
  `data`, `instructions` at the result root, or treat the name as the procedure.
- `validate_rules({rules})`: canonical reusable `rules` and warnings.
- `create_rule({id, rules})`: create only, equivalent to API `If-None-Match: *`;
  existing IDs fail without overwriting.
- `update_rule({id, rules, ifMatch})`: replace using the last read revision.
- `delete_rule({id, ifMatch})`: delete using the last read revision.

Documents use `schemaVersion: "astrofaith.rules.v1"`, a name, optional private
instructions and ordered `steps`. The shared tool schema lists every supported
field; IDs, revisions and MCP context remain outside the document. Rule IDs use
one to 64 ASCII letters, digits, underscores or hyphens, excluding
`capabilities` and `validate`. The same document passes unchanged through REST
GET/PUT, validation, MCP and browser import/export. A 409 allowance error
preserves existing rules; a 412 requires reading and reviewing the latest state;
a missing update/delete revision returns 428. Validation does not execute rules.

For raw MCP `tools/call`, the JSON-RPC `result.structuredContent` contains the
tool-specific object above. `result.content[0].text` is the same object encoded
as JSON, for text-only clients. List/read results also include readable
assistance in subsequent content; this does not replace the canonical object or
select a method. A host may already unwrap `structuredContent` before exposing
the result to the agent. Inspect the returned shape once instead of repeatedly
unwrapping `data` or guessing an empty fallback. Check `isError`, `httpStatus`
and `error` before using the data: failure is not a successful empty list.

For example, a document with
`steps: [{id: "order", kind: "instruction",
instructions: "Read the Moon before the Sun."}]`
has an instruction even if its optional document-level `instructions` is absent.
Preserve all steps and any requested answer formatting; keep revisions and
account metadata outside the document when reusing it.

## Shared colour and font themes

- `theme_capabilities({})` returns the schema, defaults and granted permissions.
- `get_theme({})` returns `{theme, etag, astrofaithContext, httpStatus}`.
- `validate_theme({theme})` returns a canonical `theme` and contrast `warnings`
  without saving. Pass its complete document unchanged to update.
- `update_theme({theme, ifMatch})` replaces the saved theme. Copy `etag` from
  the prior read into `ifMatch`, including its quotation marks.
- `reset_theme({ifMatch})` restores defaults using the same precondition.

The reusable document is v2: `{schemaVersion: 2, name, tokens}` with 38 sRGB
colour roles and two local font-family lists. The tool schema lists every
supported token. Legacy v1 is explicitly converted, keeping colours/fonts and
removing structural settings; every response is v2. No remote fonts, arbitrary
CSS, text sizes or spacing are accepted. Account and revision metadata stay
outside the document. Read and validate require `theme:read`; update and reset
require `theme:write`. Newly approved write grants include read; old grants are
never broadened on use or refresh.

For API-key REST, use `GET/PUT/DELETE /api/v1/preferences/theme`,
`POST /api/v1/preferences/theme/validate`, and
`GET /api/v1/preferences/theme/capabilities` at the chosen API origin. GET, PUT
and DELETE return the bare theme with an `ETag` header. Send that header as
`If-Match` on PUT/DELETE. 428 means the revision is missing; 412 means stale or
invalid. Re-read before retrying. Theme documents are at most 64 KiB.

## Create a saved profile

Saved-record tools use `id`, not the calculation argument `profileId`:

- `birthdata_list({search})` searches the connected account; omit `search` to
  list records. `birthdata_groups({})` lists its group metadata.
- `birthdata_get({id})` returns the selected record and `etag`.
- `birthdata_create({birthData, idempotencyKey})` creates a record.
- `birthdata_update({id, birthData, ifMatch})` patches only provided fields.
- `birthdata_delete({id, ifMatch})` deletes the confirmed record.

For the last two, read first and pass the exact ETag as `ifMatch`. Use the
returned record's `id` as `profileId` only in calculation tools that accept a
saved profile. Never infer an ID from a person's name.

`birthData.options` is canonical. Deprecated top-level `zodiac` and
`houseSystem` aliases are accepted only when they do not conflict.

Optional `birthData.gender` is identity metadata: `female` (Woman), `male`
(Man), `non_binary`, `prefer_not_to_say`, or `null` (Unspecified). Keep privacy
choices distinct from a missing answer; never infer either from a name or a
calculation. PATCH omission preserves the saved value; explicit `null` clears
it. The gender field does not select the Bazi/Yi calculation convention.

```json
{
  "idempotencyKey": "profile-ada-19900517-v1",
  "birthData": {
    "name": "Ada Example",
    "personName": "Ada Example",
    "birthDate": "1990-05-17",
    "birthTime": "14:35",
    "locationLabel": "Sydney, New South Wales, Australia",
    "latitude": -33.8688,
    "longitude": 151.2093,
    "timezone": "Australia/Sydney",
    "options": { "zodiac": "tropical", "houseSystem": "placidus" },
    "isDefault": false,
    "groupIds": [],
    "notes": "Birth time transcribed from the certificate.",
    "provenance": {
      "sources": [{
        "name": "Birth certificate",
        "type": "document",
        "reference": "Original certificate inspected"
      }],
      "rating": { "system": "rodden", "value": "AA" }
    }
  }
}
```

Each provenance source requires `name`. Optional `type` values are `document`,
`website`, `book`, `database`, `correspondence`, and `other`. An optional `url`
must be HTTPS; use `reference` for an offline certificate, archive scan, book
citation, or correspondence. Rodden rating is a separate `provenance.rating`
object with values `AA`, `A`, `B`, `C`, `DD`, or `X`.

## Resolve and calculate

Call `resolve_location` with
`{"query":"Nanjing, China","date":"1990-07-30","time":"21:00"}`, then save or
calculate with the returned label, latitude, longitude, timezone, historical UTC
offset, and UTC date-time. IANA timezone rules are applied to the requested
local birth date and time.

For an explicit chart or transit comparison, place the complete selected
candidate unchanged at `birth.location` or `transit.location` and add `date` and
`time` beside it. For a transit-period search, pass the complete candidate as
`transitLocation`. Astrofaith uses `label` for display, uses coordinates and
timezone for calculation, and safely ignores resolver-only country, confidence,
classification, and historical-time metadata at the calculation boundary.

For `calculate_chart`, use either `profileId` or an explicit `birth` object
containing local `date`, local `time`, and a location query or a coordinate
pair. Supported calculation settings are:

- `zodiac`: `tropical` or `sidereal`; sidereal uses `ayanamsa: "lahiri"`.
- `houseSystem`: `placidus`, `regiomontanus`, or `wholeSign`.
- `node`: `"true"` means the true lunar node and `"mean"` means the mean lunar
  node. These are strings, not Booleans.
- `positionMode`: `apparent` or `true`.
- `coordinateFrame`: `geocentric` or `topocentric`.
- `blackMoonLilith`: `mean`, `true`, or `interpolated`.
- `housePlacementMode`: `strict` or `nextCuspOrb`.
- `dignities`: the versioned sign-to-planet map or a preset request. Reuse a
  complete returned `dignities.settings` document unchanged. Omission uses
  Modern; calculation permission does not read the private account map.

- `orbs`: a complete `astro.faith.orbs.v1` document. Reuse returned
  `options.orbs` unchanged. Omission uses built-in defaults, not private account
  preferences. Use `orbs_capabilities` for the schema and defaults; management
  requires explicit `orbs:read` / `orbs:write`.
- `orbContext`: `natal`, `transit`, `progression`, `solarArc` or `solarReturn`.
- `orbProfile`: optional explicit `natal`, `other`, `cross`, `solarReturn` or
  `custom` profile. Cross-chart aspects use the document's single
  `assignments.cross` choice independently of each chart's internal aspects.

Example focused chart output:

```json
{
  "profileId": "<saved-profile-id>",
  "output": {
    "view": "compact",
    "depth": "basic",
    "sections": [
      "summary",
      "planets",
      "angles",
      "houses",
      "dignities",
      "aspects"
    ],
    "maxAspects": 30,
    "sortAspectsBy": "orb"
  }
}
```

Request `output.view: "compact"` for a focused MCP `calculate_chart`: summary,
planets, angles, houses, dignities, aspects and warnings, with at most 20
aspects sorted by `orbDegrees`. Core birth, scalar calculation settings, engine
and connection context remain. Full `options.orbs`, `options.dignities` and
`dignities.settings` maps are omitted. Nodes, Lilith, lots, eclipses and aspect
configuration are available through explicit `sections` requests; `aspectConfig`
also requires `depth: "deep"`.

Read selection metadata for returned/available aspect counts, truncation and
omitted settings. `output.view: "full"` restores complete sections and settings
unless explicit filters narrow it. Retrieve the full view before reusing exact
custom settings; the compact scalar settings cannot reconstruct them.
`sortAspectsBy: "priority"` preserves engine order; `"orb"` sorts tightest first
by actual `orbDegrees`, not natal legacy `orb`. Legacy `deviation` equals actual
distance; `maxOrbDegrees` is the allowed tolerance.

REST `POST /chart` uses the same `output.view`, `sections`, `maxAspects` and
`sortAspectsBy` contract but retains its full-view default for existing clients.
Existing MCP calls without a view selector retain their published options
envelope; complete reusable canonical settings are available separately as
`calculationSettings`. Explicit `output.view: "full"` returns canonical
`options`. Use those complete settings, not the legacy closed options object,
when composing a new calculation with all current features. `depth` controls
audit detail independently of the view.

The summary's notable aspects intentionally rank major aspects involving
luminaries, angles, the chart ruler, and personal planets before less central
points; tightness breaks ties within the same significance tier. This is not a
list of the globally tightest aspects.

## Bazi and Yi Astrology

`calculate_bazi` accepts exactly one of `birth` or `profileId`; `calculate_yi`
accepts exactly one of `birth`, `profileId` or `bazi`. Birth calls reuse the
canonical `birth.location` contract and saved-profile ownership checks. Saved
profiles additionally need `birthdata:read`; all calculations need
`calculations:read`. Use a birth year from 1801 through 2398. Choose
`rules.timeBasis` from `civil`, `meanSolar`, `apparentSolar`; choose
`rules.dayBoundary` from `midnight`, `zi`. Defaults are `apparentSolar` and `zi`
(23:00 day change). Year/month solar-term boundaries use the original UTC
instant regardless of clock policy.

Optional `sex` selects a traditional `male`/`female` calculation convention. It
is independent of gender identity and must never be inferred from a profile.
Omit it from both the request and retained BaZi data to return `variants.male`
and `variants.female`, with shared pillars once. Birth-based results also keep
birth data and clocks once. Bazi retains shared `luck: null` and puts each Da
Yun in the matching variant. Yi places convention-dependent numbers, hexagrams,
Yuan Tang and cycles in each variant.

For direct BaZi-to-Yi composition, use
`calculate_yi({ bazi: baziResult.data })`. Pass the complete BaZi `data`, not
its transport envelope. This mode consumes validated pillars and calendar
context without resolving a birthplace or invoking astronomy. Its minimal input
is `bazi: { pillars, calendar: { solarYear, solarHalfYear } }`; an optional
`schemaVersion` must be `astro.faith.bazi.v1`. Pillars use the canonical
returned `index`, `stem`, `branch`, and `text` fields. `solarYear` is the actual
Lichun-based year, not a sexagenary index; `solarHalfYear` is `winterToSummer`
or `summerToWinter`. The eight characters alone cannot determine this context.
Use `reverse_bazi` to resolve possible birth windows when it is unknown.

Retained `sex`, `annualStartYear`, and `annualCount` in BaZi input are
inherited. If also supplied at the request level, they must agree. To select
different controls, supply the minimal pillars/calendar document with the
desired outer controls. Clock rules do not recalculate supplied pillars;
conflicting rule metadata is rejected. No profile read is needed for explicit
BaZi input.

Direct-input Yi results retain a normalised `bazi` document and identify
`calendarCalculation.source: "suppliedBazi"`. They contain no invented birth
time, solar clock or astronomy provenance. Pass that whole Yi `data` unchanged
to `calculate_yi` to repeat the calculation. A birthless Yi result is not a
birth input for `calculate_bazi`.

Existing birth-based results retain `birth`, `rules`, supplied `sex` and annual
controls. Passing their whole `data` at the top level remains supported by
either tool and recomputes from birth. This compatibility path differs from
explicit `bazi` reuse. Never wrap the request in `data`. Add an explicit `sex`
to select one method from a comparison. Optional `annualStartYear` and
`annualCount` (0–20) filter annual output. Comparison defaults to empty annual
sequences; a start year alone requests up to ten years. With an explicit
convention, Bazi keeps its ten-year default and Yi keeps its complete
traditional age sequence. Line arrays run bottom to top, yin=0/yang=1. Heluo age
one is the birth solar year, then advances at Lichun; sequence length is not a
lifespan prediction. Full conventions and primary-source references are in the
intended environment Docs `/chinese-calculations.md`. These tools do not produce
wheel-render links.

## Find planet-in-house transit periods

Use `find_transit_house_periods` with a saved natal profile, planet, natal
house, and inclusive local-date range. It calculates the natal cusps once, then
uses the Swiss Ephemeris to refine every ingress and egress to the reported
precision. Repeated direct and retrograde crossings are returned as separate
events and intervals.

Alternatively supply `natal: {birth, options?}` instead of `profileId`, with the
same planet, natal house and range fields. Use exactly one source. An explicit
natal input needs only `calculations:read`; a saved profile also needs
`birthdata:read` and the usual ownership check.

```json
{
  "profileId": "<saved-profile-id>",
  "planet": "Jupiter",
  "natalHouse": 2,
  "dateFrom": "2020-01-01",
  "dateTo": "2030-12-31",
  "transitLocation": {
    "label": "Sydney, New South Wales, Australia",
    "latitude": -33.8688,
    "longitude": 151.2093,
    "timezone": "Australia/Sydney"
  }
}
```

The range uses the transit location's timezone and includes all of `dateTo`. An
interval marked `startsAtRangeBoundary` or `endsAtRangeBoundary` may continue
outside the requested dates. If the server returns `TRANSIT_RANGE_TOO_LARGE`,
narrow the range using the maximum-day guidance in the error; do not silently
reduce the requested period.

## Calculate a natal and transit comparison

Use `calculate_transit_comparison` when the user needs a bi-wheel, transit
positions against natal houses, or cross-chart aspects. The saved profile is the
inner natal wheel; `transit` is the explicit outer chart.

```json
{
  "profileId": "<saved-profile-id>",
  "transit": {
    "date": "2026-09-01",
    "time": "12:00",
    "label": "Sydney, New South Wales, Australia",
    "latitude": -33.8688,
    "longitude": 151.2093,
    "timezone": "Australia/Sydney"
  },
  "output": {
    "view": "compact",
    "chartSections": [
      "summary",
      "planets",
      "angles",
      "houses",
      "dignities",
      "warnings"
    ],
    "maxCrossAspects": 50,
    "sortCrossAspectsBy": "orb"
  }
}
```

The comparison response is authoritative as a unit: `inner` is the natal chart,
`outer` is the transit chart, and `comparison.aspects` contains the cross-chart
aspects. Do not infer cross-chart aspects from two separate tool responses.
`comparison.houseOverlays` maps each `outerPoint` to its strict
`houseInInnerChart` and its `effectiveHouseInInnerChart` under the configured
house-placement policy. For this transit comparison the inner chart is natal.
The outer point's `house` remains its own transit-chart house.

Explicit compact comparison output returns focused inner/outer sections and at
most 20 cross aspects sorted by `orbDegrees`. Internal wheel aspects are omitted
in the compact view; request `aspects` in `chartSections` when needed. Use
`output.view: "full"` for complete chart settings and selection, or explicit
`chartSections`, `maxCrossAspects` and `sortCrossAspectsBy` for a focused
response. Read selection metadata before claiming all cross aspects were
returned. Existing `calculate_transit_comparison` calls without a view selector
preserve their original inner/outer sections (summary, planets, nodes, angles,
houses and warnings) and the established 50 cross-aspect limit, sorted by orb,
unless the caller specifies sections/limits. Complete reusable options remain in
each wheel's `calculationSettings`. REST `POST /workspace` accepts the same
controls and retains its full-view default.

When available, `links.openInAppUrl` opens a chart interactively. When
reproducible without exposing custom orb settings, `links.renderUrl` provides a
deterministic chart-only view. Otherwise `links.renderUnavailableReason`
explains why the render URL is omitted; preserve the authoritative JSON result.
A saved-profile interactive link may use browser account defaults rather than
the caller's custom orb document. Plugin OAuth does not create an Astrofaith
browser session, so an interactive link can require a separate browser login.

## Correct errors safely

Validation errors may include `field`, `allowedFields`, `example`, and
`schemaTool`. Correct only the named field; do not drop provenance or other user
data merely to make a retry pass. Use `birthdata_capabilities` if the
connection's effective scopes or saved-data contract are unclear.

## Private dignities, aspects and orb preferences

`dignities_capabilities({})` / `orbs_capabilities({})` return schemas, defaults,
limits and current permissions. `get_dignities({})` returns
`{dignities, etag, astrofaithContext, httpStatus}`; `get_orbs({})` returns the
equivalent envelope with `orbs`. The documents compose unchanged into
calculation `options.dignities` / `options.orbs`; context and revisions stay
outside the document. A calculation does not silently read these preferences.

Use `validate_dignities({dignities})` / `validate_orbs({orbs})` before saving.
Use `update_dignities({dignities, ifMatch})` / `update_orbs({orbs, ifMatch})`
with the complete canonical document and exact ETag, including its quotation
marks. Resets are `reset_dignities({ifMatch})` / `reset_orbs({ifMatch})`.
Validation/read need the corresponding `:read` grant; replacing/resetting needs
`:write`. A 428 means missing precondition and 412 means stale or invalid:
re-read and review the intended changes, never retry by dropping the revision.
Save/reset affects My Astrofaith defaults and subsequent browser use; it does
not recalculate an already displayed chart.

## Full calculation workspaces

`calculate_workspace` uses the REST `/workspace` document. `inner` and
`outer.wheel` each accept either `birth` or `profileId`, not both; optional
`name` and `orbProfile` remain outside the birth object. Every calculation needs
`calculations:read`; any saved profile also requires `birthdata:read` and must
belong to the connected member. The inner profile supplies saved chart settings
unless top-level `options` explicitly override them.

```json
{
  "inner": { "profileId": "<saved-profile-id>" },
  "outer": {
    "enabled": true,
    "comparisonType": "solarReturn",
    "solarReturnYear": 2027,
    "wheel": {
      "birth": {
        "date": "2027-05-17",
        "time": "12:00",
        "location": {
          "label": "Sydney, Australia",
          "latitude": -33.8688,
          "longitude": 151.2093,
          "timezone": "Australia/Sydney"
        }
      }
    }
  },
  "output": { "view": "compact", "maxCrossAspects": 20 }
}
```

`comparisonType` accepts `transit`, `progression`, `solarArc`, or `solarReturn`.
Supply the target date/time/location appropriate to the selected mode; a
solar-return year asks the engine to solve the return instant rather than
treating the supplied noon as the answer. Preserve the returned computed timing
and derivation. A single-wheel workspace can disable `outer`. Use
`comparison.houseOverlays` for outer points in inner houses; an outer point's
own `house` is not the inner house. The full view is the default; explicit
compact or section filters reduce output without changing calculations.

## Fixed-longitude event searches

`find_longitude_crossings` accepts the exact REST `/longitude-crossings`
request, for example:

```json
{
  "planet": "Jupiter",
  "longitude": 120,
  "referenceUtc": "2026-10-01T00:00:00Z"
}
```

It finds nearest strict events before/after the reference, including supported
stationary touches, rather than every transit aspect in a user-chosen date
range. The strict solver can return `LONGITUDE_SEARCH_UNRESOLVED`; that does not
mean there are no events. Longitudes are degrees in `[0, 360)`; 360 is invalid.
Dates require seconds and an explicit UTC offset. Options support the advertised
zodiac/position policy; do not infer a different policy.

`find_longitude_event` instead takes `planet`, `longitude`, `startUtc`,
`direction` (`future` or `past`) and optional `options`. The start is exclusive.
Preserve `status`, actual longitude/residual and
`quality.nearestEventEstablished`, `reasons` and `affectedInterval`. `candidate`
is explicitly uncertain: a station candidate need not reach the target, and a Df
warning concerns search certainty, not measured position error.
`not_found_within_range` is bounded evidence, not proof that no future/past
event exists. Do not turn candidates into exact dates or omit uncertainty.

## Reverse Four Pillars

`reverse_bazi` takes `pillars`, `startYear`, `endYear`, and optional `location`
and `rules`, matching REST `/bazi/reverse`. Reuse the `pillars` from
`calculate_bazi`, specifying a narrow relevant Gregorian year range. An explicit
location is recommended; omission uses a reference UTC+08:00 civil clock, not an
inferred birthplace. Solar time requires a location. Defaults are civil without
a location and apparentSolar with one; `dayBoundary` remains explicitly
selectable.

Matches are time intervals, not recovered exact birth timestamps. A
`representative` is a sample-only calculation input reusable unchanged by
`calculate_bazi` or `calculate_yi`; a missing representative has a reason. Do
not save that sample as the person's exact birth time without the user's
independent confirmation. Complete result `data` can be reused for a repeat
reverse search without stripping derived fields.
