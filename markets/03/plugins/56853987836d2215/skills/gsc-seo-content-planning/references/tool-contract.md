# GSC MCP tool contract

Load this reference when choosing tool inputs, applying filters, or interpreting an error.

## Tool sequence

### `list_gsc_orgs`

- Inputs: none.
- Returns only organizations included in the ChatGPT OAuth grant for which the user still has an active membership.
- Listing organizations does not start the free GSC data trial.

### `list_gsc_properties`

- Required input: `orgId` from `list_gsc_orgs`.
- Returns the read-only Search Console properties connected to that organization.
- Listing properties does not start the free GSC data trial.

### `get_gsc_seo_planning_data`

- Required input: `orgId`.
- Optional inputs:
  - `siteUrl`: exact property URL returned by `list_gsc_properties`. The server uses the first available property only when this is omitted.
  - `country`: three-letter lowercase GSC country code, such as `hkg`.
  - `device`: `DESKTOP`, `MOBILE`, or `TABLET`.
  - `minImpressions`: integer from 1 to 100000; the server default is 50.
- A successful non-empty analytics read can start the free organization's seven-day full-data window.

## Returned planning data

The response can include:

- `requestedRange`, `effectiveRange`, and `comparisonRange`
- `access` mode and comparison availability
- `totals`, `previousTotals`, and `changes`
- `topQueries` and `topPages`
- `queryPageRelationships`
- `risingKeywords` and `fallingKeywords`
- `strikingDistanceKeywords` (average positions 5–20 after the impression threshold)
- `lowCtrPages`, including heuristic expected CTR
- `cannibalizationCandidates`
- `limitations`

The current period normally covers 28 finalized data days and compares with the preceding 28 days. Search Console data has an approximately three-day finalization delay. After a free organization's seven-day window ends, the effective period is limited to the latest three finalized days and comparison data is omitted.

## Error handling

- `GSC_NOT_CONNECTED`: direct the user to the returned `integrationsUrl`. If `managerActionRequired` is true, explain that an organization manager must connect GSC.
- `GSC_PROPERTY_NOT_FOUND`: ask the user to connect or select a Search Console property using the returned integrations URL.
- `MCP_UNAUTHORIZED`: ask the user to reconnect the app or grant the intended organization.
- Other provider or request failures: report the returned code and plain-language effect. Do not infer data that was not returned.
