# Aviasurf MCP review inventory

Production MCP endpoint: https://mcp.aviasurf.com/mcp

## Release 1.1.0

The production MCP has been deployed and release-checked as version 1.1.0 with 9 tools and 6 widgets. The main addition is `destination_profile`, which renders a destination profile with monthly climate normals and available place facts. Existing flight-search tools remain read-only and do not book, issue tickets, process payments, cancel tickets, or handle refunds.

## Tool inventory

All nine production tools are read-only/idempotent travel information or search-handoff tools. Existing tool names and behavior remain compatible; 1.1.0 adds `destination_profile`.

- `cheapest_destinations`
- `compare_airports`
- `destination_profile`
- `flight_prices`
- `flight_prices_filtered`
- `open_search`
- `price_calendar`
- `resolve_place`
- `route_facts`

## Review status

Production release check on 2026-10-23 reported version 1.1.0, 9 tools, 6 widgets, and 35 successful checks with 0 failures. `destination_profile` was also exercised in ChatGPT with the prompt “What is Batumi like in November?” and rendered its interactive widget.

The positive review cases use relative dates and minimal constraints. Flight-price results are indicative cached observations, not guaranteed live availability. `destination_profile` climate values are 1991–2020 normals, not forecasts.

## Demo

Reviewer-accessible demo recording: https://youtu.be/4t1nFVoidrU
