---
name: terrain-watershed-brief
description: Prepare a public-point terrain and watershed context brief using USGS elevation and Watershed Boundary Dataset records. Use for modeled ground elevation, nested HUC context and source limitations, not surveys, elevation certificates, parcel flood zones or station-datum conversions.
---

# Terrain and watershed brief

Combine two kinds of geographic evidence while keeping modeled elevation and watershed membership separate from parcel-level determinations.

1. Use a user-supplied public research point or a clearly identified public point already in the request. Do not ask for a home address, obtain device location, invent coordinates or offer address lookup. Confirm latitude/longitude and units; reject invalid coordinates before a call rather than treating an error as no data.
2. Call `get_ground_elevation_at_point` with the point and explicit units. Read the returned elevation, status/no-data indicator, vertical reference, source dataset and resolution/vintage fields where supplied. Preserve source labels and missing metadata. A sampled elevation model value is not a field survey, building-floor elevation or certified site elevation. Resolution is not vertical accuracy, and retrieval date is not terrain survey date.
3. Call `get_watershed_at_point` for the requested levels (available HUC2/4/6/8/10/12; default 8/10/12). Keep HUC identifiers as strings with leading zeros, retain names and level labels, and distinguish nested units from separate unique watersheds. Retain all multiple boundary matches and any hierarchy inconsistency. Report the returned spatial relation and source coverage; do not infer flow direction, a drainage path, hydraulic connectivity, floodplain or flood risk from membership alone.
4. Present the point and its stated public context; modeled elevation with units and only documented vertical reference; a compact HUC table; source links and separate source/retrieval/cache dates; and any no-data, unmatched level or missing source metadata. Do not convert a sentinel, null, unsupported point, source failure or absent polygon into elevation zero, no watershed or safety.
5. When asked to combine with tides, explain that a coastal station's tidal-to-geodetic datum relationship is local to that station and epoch. Do not add or subtract its offset from arbitrary inland EPQS terrain or claim the two references are interchangeable. A defensible local conversion requires appropriate authoritative transformation/control evidence beyond these tools.

Decline property flood-zone, engineering, insurance, safety or elevation-certificate conclusions. Offer this source-qualified regional context and direct requests for a certified measurement or determination to the relevant qualified professional/authority; do not promise that a missing record excludes a hazard.
