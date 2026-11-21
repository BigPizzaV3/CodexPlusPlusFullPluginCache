---
name: datalastic-maritime
description: Research vessels, ports, marine weather, and maritime records with the connected Datalastic MCP tools. Use for vessel lookups, ship specifications and engines, ownership and inspection research, area searches, and maritime briefings.
---

# Datalastic maritime research

Use this workflow for maritime research with the connected Datalastic MCP server. Follow the user's requested scope and source preferences. General nautical explanations and fictional ships do not require this workflow.

## Resolve the subject

Use a supplied IMO, MMSI, or other supported identifier. For a vessel name, use `find_vessels` and distinguish matching ships using returned identifiers, flag, and type. Ask for clarification when multiple plausible matches remain. Preserve the resolved identity throughout follow-up questions; do not guess an identifier.

For ports, use `find_ports` to resolve names or UN/LOCODEs, then `get_port` for details. A reported vessel destination may be abbreviated or ambiguous; distinguish a resolved destination from a hypothetical port supplied by the user.

Inspect the available tool descriptions and input schemas before calling tools. The mapping below describes documented capabilities, not guaranteed parameters or availability. If a required tool is unavailable, explain the missing capability rather than simulate a result.

## Select only the tools needed

| Request | Tools |
| --- | --- |
| Latest reported vessel position | `get_vessel` |
| Position with destination, ETA, departure, or draught | `get_vessel_pro` |
| Vessel specifications, dimensions, and tonnage | `get_vessel_info` |
| Vessel search or multiple positions | `find_vessels`, `get_vessels_bulk` |
| Historical AIS track | `get_vessel_history` |
| Vessels around a location or port | `get_vessels_in_radius` |
| Ports and terminals | `find_ports`, `get_port` |
| Marine and atmospheric weather | `get_weather` |
| Engines and propulsion | `intel_engine` |
| Ownership and management | `intel_ownership`, `intel_companies` |
| Inspections and casualties | `intel_inspections`, `intel_casualties` |
| Dry-dock and classification records | `intel_drydock`, `intel_class` |
| Recorded sale, purchase, or demolition transactions | `intel_spd` |
| Schematic sea route and distance | `sea_route` |
| Estimated position outside terrestrial AIS coverage | `estimated_vessel_position` |

Request engine, ownership, and other intelligence records only when relevant to the user's task. Follow supported pagination when a complete list is requested, and deduplicate vessel records by their returned identifiers.

## Minimize unnecessary credit usage

Choose the lowest-cost available tool that fully answers the request, using known pricing and the live tool descriptions. Do not sacrifice requested information merely to save a call.

- Default to vessel Basic (`get_vessel`) for latest reported position, speed, heading, and navigation status. Vessel Pro (`get_vessel_pro`) is more expensive; do not use it for a simple question such as "Where is this ship?"
- Use `get_vessel_pro` only when its additional fields, such as recognized destination port, ETA, departure, or draught, are needed for the user's request, or the user explicitly requests Pro. For "Where is this ship and when will it arrive?", call Pro directly instead of calling Basic and then Pro.
- Do not switch to Pro merely because Basic returns an empty or stale position. Pro is not a guaranteed remedy for missing or old AIS observations. Explain the data gap and select a further lookup only when its documented capability addresses the request.
- For specifications, use `get_vessel_info`; the word "details" alone does not justify a Pro position lookup. Resolve the fields needed from the conversation or ask a focused question when the scope is unclear.
- Reuse resolved vessel identifiers and relevant results from the current conversation when they are still suitable. Include their timestamps. Refresh time-sensitive data when the user requests an update or freshness is necessary; never present reused data as newly retrieved.
- For several vessels, consider `get_vessels_bulk` when its fields and documented cost fit the request. Do not assume a bulk call is cheaper without pricing evidence.
- Clarify an ambiguous date range, area, or dataset before a broad historical query or export. Do not fetch unrelated intelligence records or every possible briefing section by default.
- Do not invent credit prices or savings. Quote exact costs only when supplied by maintained pricing information or server metadata. Routine Basic lookups do not need an extra permission question merely because they consume credits.

## Present evidence clearly

- Identify vessels and ports with their returned names and identifiers.
- Include observation timestamps for positions and distinguish last reported AIS positions from estimated positions. Do not present stale observations as the ship's exact current location.
- Preserve units, forecast dates, and stated time zones. Distinguish forecasts and reported ETAs from observed events.
- Separate registry specifications from live observations. Mark missing fields as unavailable rather than filling them from assumptions.
- An empty inspection or casualty result means no matching records were returned; it does not establish a clean safety history.
- Attribute retrieved facts to Datalastic. If the user requests additional sources, label those findings separately.
- Describe sea routes as schematic estimates for research and visualization, not navigational instructions. Do not infer operational clearance or seaworthiness from the records.

For a vessel briefing, combine only the requested sections: latest status, vessel and engine profile, destination and port details, weather, and relevant maritime records. End with material gaps or uncertainty. A narrow lookup should receive a narrow answer, not a full briefing.

## Authentication and entitlements

Use the platform's connection flow if authentication is needed; do not ask users to paste passwords, API keys, or tokens into the conversation. Distinguish connection failures, entitlement errors, and empty datasets.

Some intelligence tools require the Maritime Reports add-on. Use `intel_info` when needed to explain the current account's access. State missing entitlements neutrally; do not promote subscription upgrades, sell credits, or direct users to checkout. Stop repeated calls to a capability after an entitlement failure until access changes.

## Requested data exports

Use `report_request` or `intel_report_request` only when the user requests an export. These start asynchronous jobs and can consume account credits; explain any known cost or scope before starting and clarify ambiguous large requests. Do not create exports merely to answer a simple lookup.

Use the returned job identifier with `report_status`; use `report_list` to find an existing report when appropriate. Avoid duplicate jobs and tight polling loops. If a report remains pending, report its state without claiming completion. On an uncertain job-creation response, check existing jobs before retrying.

When ready, provide the returned download link. Treat signed URLs as private to the requesting user. For an expired link, check `report_status` for a fresh link rather than regenerating the export. Do not claim to have inspected the report contents unless they were actually retrieved and read within the user's requested scope.
