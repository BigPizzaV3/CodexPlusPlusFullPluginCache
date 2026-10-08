---
name: metro-transit
description: Use Metro MCP for live DC Metro or NYC Subway arrivals, stations, service incidents, accessibility, buses, trains, routes, and transfers.
---

# Metro Transit

Use Metro MCP when a request depends on current public transit data in
Washington, DC or New York City.

## Choose the request

- Identify `dc` or `nyc` from the user's location. Ask which city only when the
  request is genuinely ambiguous; do not silently choose one.
- Search for a station before requesting predictions when the station name is
  partial or ambiguous. Preserve the user's selected station from any returned
  candidate list.
- Use station predictions for arrivals, incidents for service disruptions, and
  elevator incidents for accessibility questions. Combine them when trip
  reliability depends on more than one feed.
- Use bus stops or routes to resolve identifiers before requesting bus
  predictions or positions. Use train positions only when vehicle locations,
  rather than arrival estimates, answer the question.
- Route information is richest for NYC. Do not imply unsupported DC route
  metadata exists.

## Present results

- Treat arrivals, incidents, outages, and vehicle positions as time-sensitive
  snapshots. State relevant update times when the tool returns them.
- Name the city, station or route, direction, and units needed to interpret the
  result. Distinguish scheduled or estimated values from guarantees.
- If the live feed is unavailable or has no result, say so plainly. Do not
  invent arrivals, incidents, accessibility status, fares, or service advice.
- Metro MCP is anonymous and read-only. Never claim to buy fares, change
  service, send background alerts, or track a rider's location.
