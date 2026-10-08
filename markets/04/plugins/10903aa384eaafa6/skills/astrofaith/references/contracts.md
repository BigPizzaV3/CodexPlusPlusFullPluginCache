# Astrofaith MCP contracts

## Create a saved profile

`birthData.options` is canonical. Deprecated top-level `zodiac` and
`houseSystem` aliases are accepted only when they do not conflict.

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

Example focused chart output:

```json
{
  "profileId": "<saved-profile-id>",
  "output": {
    "depth": "deep",
    "sections": ["summary", "planets", "angles", "houses", "aspects"],
    "maxAspects": 30,
    "sortAspectsBy": "orb"
  }
}
```

Core birth, options, engine, output, and connection-context metadata are always
retained. `sortAspectsBy: "priority"` preserves engine order;
`sortAspectsBy: "orb"` sorts tightest aspects first.

The summary's notable aspects intentionally rank major aspects involving
luminaries, angles, the chart ruler, and personal planets before less central
points; tightness breaks ties within the same significance tier. This is not a
list of the globally tightest aspects.

## Find planet-in-house transit periods

Use `find_transit_house_periods` with a saved natal profile, planet, natal
house, and inclusive local-date range. It calculates the natal cusps once, then
uses the Swiss Ephemeris to refine every ingress and egress to the reported
precision. Repeated direct and retrograde crossings are returned as separate
events and intervals.

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
    "chartSections": ["summary", "planets", "angles", "houses", "warnings"],
    "maxCrossAspects": 50,
    "sortCrossAspectsBy": "orb"
  }
}
```

The comparison response is authoritative as a unit: `inner` is the natal chart,
`outer` is the transit chart, and `comparison.aspects` contains the cross-chart
aspects. Do not infer cross-chart aspects from two separate tool responses.

Successful chart and comparison results include `links.openInAppUrl` and
`links.renderUrl`. The interactive link preserves the saved profile and transit
bi-wheel state; the render link contains deterministic calculation inputs and
does not require access to the saved profile. Plugin OAuth does not create an
Astrofaith browser session, so a private interactive link can require a separate
browser login.

## Correct errors safely

Validation errors may include `field`, `allowedFields`, `example`, and
`schemaTool`. Correct only the named field; do not drop provenance or other user
data merely to make a retry pass. Use `birthdata_capabilities` if the
connection's effective scopes or saved-data contract are unclear.
