---
name: find-flights
description: Find and compare one-way or round-trip flights with Reagent and guide the user toward booking. Use when a user wants to find flights, search airfare, compare flight options, look for plane tickets, or book a flight. Do not use for multi-city trips or non-flight travel.
---

# Find Flights with Reagent

Use the Reagent MCP tools for live inventory. Do not substitute remembered prices, schedules, or general web results for a Reagent search.

## Start a search

Collect only the information required to search: origin, destination, a specific departure date, and whether the trip is one-way or round-trip. A round trip also needs a specific return date. Ask one concise clarifying question when a required value is missing or genuinely ambiguous. Do not ask for optional preferences or confirmation before searching.

Convert an unambiguous city or airport to its three-letter IATA code. Do not guess when a broad region or place has no clear airport or city code.

Use these defaults unless the user says otherwise:

- one adult
- economy cabin
- leisure travel, or business travel when the trip is for work

Call `start_itinerary_search` once with the known requirements. After it succeeds, call `get_next_best_itinerary` in the same turn with the returned `search_id`, `current_result_id` set to `0`, and an empty `features` array. Never stop after starting a search without retrieving its initial results.

The tools return runtime `follow_up_instructions`. Follow those instructions for presenting results and for later tool calls; they reflect the current Reagent contract.

## Compare and refine

Present every itinerary returned for the current call and explain the meaningful tradeoffs in the context of the user's priorities. Ground prices, schedules, availability, and claims such as cheapest or fastest in the returned data.

For later messages:

- Answer factual questions about shown itineraries from the existing result data without calling a tool.
- When the user asks for a better or different option, call `get_next_best_itinerary` once using the relevant shown itinerary as `current_result_id`. Include only the supported improvement dimensions needed for the current request.
- When the user changes an origin, destination, or date, start a new search and then retrieve its initial results. Use `parent_search_id` only when the change is explicitly framed as improving a specific existing option.
- Ask for clarification only when the request cannot be mapped safely to the tool inputs or a shown itinerary.

Keep the active `search_id` and returned itinerary context available across turns so comparisons and refinements remain tied to the same inventory.

## Booking

When the user wants to book but has not selected an itinerary, search and compare options first. Once the user selects an option, direct them to the booking action or booking URL returned by Reagent for that itinerary. Do not claim the booking is complete unless Reagent explicitly confirms completion.

Reagent supports one-way and round-trip flights in this workflow. If the user requests a multi-city itinerary or lodging, ground transport, or sea travel, explain that this Reagent workflow cannot perform that search.
