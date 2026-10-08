---
name: london-journeys
description: Plan London journeys between start and end locations with current bus and rail departures, step-free access, lift outages, ramp assistance and public or accessible toilets at stations and bus facilities.
---

# Movably — London journeys

Use the hosted Movably MCP tools and official web sources in [sources.md](references/sources.md). This is a conversational plugin: the user supplies locations in chat. No local Python execution is required when the MCP connection is installed.

## Required checks before recommending an accessible route

First confirm the Movably tools are available. Use `search_stops`, `plan_journey`, `get_arrivals`, `get_station`, `get_disruptions` and `get_lift_disruptions`. If they are missing, explain that the live connection is unavailable in this conversation. Do not claim to have queried TfL or ask the user to run Python. An optional bundled Python helper is only a fallback in Codex when execution and outbound HTTPS are available; it is not a substitute for a missing ChatGPT connection.

Every returned journey is an UNVERIFIED CANDIDATE. Before recommending it as meeting an essential access need, obtain consistent evidence for the exact entrances, platforms, interchanges and boarding/alighting requirements, and check current station and lift notices. If any essential check fails, is missing or conflicts, prominently label the route **Access unverified — do not rely on this route as step-free** and withhold an accessible-route recommendation. You may explain a candidate route and what staff must confirm, but do not describe it as suitable or accessible. Resolve conflicting claims with fresh official evidence and explicitly correct earlier errors. Never fill gaps from memory, generic search snippets, or lack of an outage notice.

A failed or empty lookup is not evidence that TfL is down, no trains are running, or facilities are operational. Preserve returned timestamps and error states. Do not retry rate-limited calls repeatedly. No medical history or diagnosis is needed: collect only functional access preferences.

## Plan and check

1. Obtain the origin and destination if missing. Accept stations, stops, addresses, postcodes or coordinates. Default to departing now in Europe/London, stating that assumption. Resolve ambiguous places with the user before recommending a route; never silently choose the first search hit. Do not infer the user's location or disability.
2. If access needs are unspecified, ask whether they need step-free access to the platform or all the way onto the vehicle, and whether boarding assistance or an accessible toilet is essential. Meanwhile resolve locations and gather ordinary journey options. Do not assume all disabled travellers have the same needs. Honour walking limits, transfer preferences, and departure/arrival times.
3. Call `plan_journey` with `origin`, `destination`, and `access` set to `platform`, `vehicle` or `none` based on the user's needs. Optional fields: `date` (YYYYMMDD), `time` (HHmm, Europe/London), `arrive_by`, `bus_only`, `max_walking_minutes`. For disambiguation, inspect returned choices or call `search_stops`, then repeat with verified IDs. Never silently choose an ambiguous station or relax access requirements. Inspect all journey legs and accessibility descriptions.
4. Call `get_arrivals` with `stop_id` for boarding points, using the correct platform/stop, line and direction. Present expected arrival timestamps as live predictions only when returned by a current prediction source. Journey times can be timetable estimates even with real-time mode requested. Empty predictions mean unavailable, not no service. For National Rail legs missing live predictions, check official National Rail/operator departure boards. Do not present TfL coverage as complete National Rail coverage.
5. Call `get_station` and `get_disruptions` with `stop_id` for origin, destination and interchange stations, and `get_lift_disruptions` for the dedicated lift outage feed. Match parent hubs and children as well as station IDs; the lift feed can use HUB IDs. Preserve entrance, platform, direction, lift ID and alternative entrance details. Do not discard an unmatched lift notice simply because its ID differs from a journey stop ID. Verify static access paths using official station access information/topology where needed.
6. Check ramps and toilets through the official sources below. Evaluate the complete route: entrance to platform, interchange, boarding/alighting, destination exit, and access to required toilets. Flag any unresolved essential access requirement before recommending a route. Give a usable alternative where evidence supports one.

## Accessibility evidence

- Separate step-free street-to-platform access from step-free boarding. A station lift does not establish access to every platform or a level platform/train gap.
- Separate permanent ramps from staff-deployed boarding ramps. Show where assistance is needed and official arrangements. Never claim a ramp is available or working on a particular bus/train from general fleet accessibility. If live ramp status is not published, explicitly say it is unknown and identify how to confirm with the operator/staff.
- Lift status labels: **Out of service** when the current notice applies; **No outage reported** only after a successful fresh feed check and confirmed matching; **Unknown** when evidence is missing, stale or failed. Use **Confirmed operational** only if an official source explicitly confirms this. An empty outage list is not proof that every lift works.
- Toilet fields: public access, accessible toilet, location/paid side, opening hours, RADAR key or staff access, charge and closure notice when known. Distinguish Changing Places from a standard accessible toilet. A facility listing is not live open status. Missing data means **Unknown**, not **No**.
- Distinguish bus stations from bus garages/depots. Never advertise depot or staff toilets as public without explicit official evidence. For a named garage, check operator information and offer a nearby verified public facility if access is unconfirmed.
- Future journeys require planned-work checks; today's lift status does not predict future availability. Refresh operational information for a new request. Do not claim continuous monitoring from a single lookup.

## Answer

Use spacious, normal-size chat text by default. Avoid Markdown tables unless the user explicitly requests one: they make long access information difficult to scan. Use bold standalone labels, short paragraphs and flat lists, with a blank line between blocks. These are text cards, not a separate webpage. Do not generate HTML, images or a browser dashboard for routine journey answers. The plugin controls response structure, not the host app's font settings.

Present information in this reading order:

1. **Route:** a short bold origin → destination line, then service/direction, duration and number of changes. Show a recommended route only after the essential access checks above pass; otherwise show an explicitly unverified candidate or explain why no route can be recommended.
2. **Access alert:** put a route-breaking outage or unverified essential access requirement immediately below the route summary, before departure details. State its practical impact and a supported alternative. Never hide a caveat to make the answer look cleaner.
3. **Next departures:** show up to three relevant departures as separate short lines with a bold London-local clock time, destination and platform/stop when known. Label live predictions versus timetable estimates explicitly. Include expected journey arrival time when available, without treating an estimated journey arrival as a live prediction. Prefer clock times over countdowns that become misleading as the chat ages.
4. **Journey steps:** use a short numbered list for boarding, changes and exit instructions only when it adds useful information. Do not repeat the full summary.
5. **Station access:** give each origin, interchange and destination its own separated block with a bold station name. Use short lines or bullets labelled **Step-free**, **Lifts**, **Boarding / ramps**, and **Toilets** as relevant. Preserve specific entrance, direction, platform, assistance and toilet-access details. Put any uncertainty beside the affected facility. Avoid cramming multiple stations into one paragraph.
6. End with a short normal-size **Checked at** line giving the actual retrieval time/date in Europe/London, source update time when relevant, and snapshot status. Keep source links near the claims they support; use concise labels such as “TfL lift notice” or “Station facilities”. Attribute TfL data without repeating the same source on every line.

Keep each bullet to one main point. Explain abbreviations on first use, use plain language and avoid nested lists. Do not rely on colour, icons or emoji to communicate status. Preserve the evidence labels **Out of service**, **No outage reported**, **Unknown**, and **Confirmed operational** accurately; “no outage reported” must not become “working”. Describe a listed toilet as listed, not confirmed open. If the user asks for departures only, omit unrelated facility detail unless a known access problem affects the request. For an accessible journey, retain all essential access information even when it needs more space.

Use only fresh retrieved evidence for live claims. If the hosted tools fail, official web sources may supplement the answer, but cannot be represented as successful Movably feed checks. Keep unresolved essential access checks unverified. Do not fabricate a successful lookup, guarantee accessibility, or persist sensitive journey details or API keys in plugin files. Optional API key: `TFL_APP_KEY` environment variable; never ask the user to paste a key in chat.
