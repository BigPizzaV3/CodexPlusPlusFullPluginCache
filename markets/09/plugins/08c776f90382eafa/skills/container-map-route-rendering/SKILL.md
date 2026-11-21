---
name: "container-map-route-rendering"
description: "Render a map of a container's route or journey. Use when asked about the route or journey of a container, vessel, or master bill."
---

Map payload (getContainerRoute, detail "full"):
- Summary is itinerary text (names, modes, ACT/PLN/EST). Full legs are GeoJSON: from/to = Feature Point, points = Feature LineString or MultiLineString. Coordinates are [lng, lat]. Leaflet, Mapbox, and Google Maps consume them as-is; great-circle between port names is not this map.
- Polylines split on eventClassifierCode: ACT = traveled (solid gray #808080, 2px); PLN/EST/REQ = remaining (same stroke, dasharray 2,4). Direction arrows along the line.
- Markers: unique from/to plus additionalLocations. Locations with no properties.id have no pin. type CONTAINER_LOCATION is the live container marker (vessel/rail/truck/yard from status), not a stop.
- Container pin: CONTAINER_LOCATION geometry (snapped onto the polyline) if present, else lastKnownPosition. Camera center on that point.
- Stop types: ORIGIN / DESTINATION (inland); ORIGIN_PORT / DESTINATION_PORT / TRANSSHIPMENT_PORT (anchor, #385273); NEXT_PORT (cyan #00acc1; smaller if it is neither destination nor a transshipment already on the route); NEXT_PORT_DISCREPANCY (orange #EF6C00); ORIGIN_RAIL_STATION / DESTINATION_RAIL_STATION; RECEIVING_FACILITY; RAIL_SIGHTING.
- Pacific / US-centric framing: longitude + 360 for lng < 80.
- Basemap: mercator streets (product: mapbox://styles/mapbox/streets-v9). Full payload is ~50–200 KB.
