# Flight presentation

## Capability and freshness

Use interactive comparison components only when the current host exposes them. Otherwise use structured Markdown or a table. Do not invent a renderer API, fixed component, or Jinko widget.

Treat results from `find_destination`, `flight_calendar`, and `price_monitoring` as indicative cached one-adult estimates. Label them accordingly. A live `flight_search` result supersedes a cached estimate and is required before presenting a fare as bookable.

## Compare live options

For each live itinerary and fare, show returned values for:

- airline or marketing carrier;
- local departure and arrival dates and times, airports, and route;
- total duration, stop count, and layovers;
- total display price, currency, and the passenger party it covers;
- cabin or fare name and checked/carry-on baggage allowances.

Label missing baggage data as unknown. Never infer baggage from cabin, airline, or fare name. Emphasize meaningful differences such as schedule, duration, nonstop versus connecting, price, baggage, and returned refund or change conditions instead of repeating identical facts.

## Refinement

When supported, provide host controls for price, departure or arrival time, stops, and baggage. Explicit user presentation and filter choices override defaults.

A local sort or filter changes only the currently loaded results; label that scope and never imply global completeness. To seek new inventory, call `flight_search` with the corresponding supported fields, including `max_price`, time ranges, `max_stops`, or `checked_bag_included`, while preserving the route, dates, passenger party, cabin, and other hard constraints. Do not silently relax any constraint.

## Selection and booking boundary

Keep the selected itinerary, fare, and `trip_item_token` tied to the live search criteria that produced them. A change to route, dates, passengers, cabin, hard filters, or returned pricing invalidates the selection or requires a new live `flight_search` confirmation.

Before adding or booking a flight, refresh or confirm it live and present the final returned total for all travelers, route and local times, duration and stops, known or unknown baggage, and returned refund/change conditions and fees. Ask for explicit approval of that exact option before `trip(add_item)`, checkout, or payment. Never proceed automatically. When the party includes anyone under 13, the booking continues on the Jinko page at the `trip_link` that `trip(add_item)` returns; never collect a child's details in the conversation.
