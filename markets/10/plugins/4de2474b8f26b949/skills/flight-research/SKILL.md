---
name: flight-research
description: Compare Google Flights itineraries for supplied routes and dates, or discover flexible-date flight deals with HasData. Use for fare research, not hotels, ticket booking or guaranteed live availability.
---

# Compare observed flights

Read `../hasdata-research/SKILL.md` and the Travel section of `../hasdata-research/references/tool-catalog.md`.

For a fixed itinerary use `hasdata_google_travel_flights_getGoogleFlights` with departureId, arrivalId and outboundDate. Use the supplied IATA airports, type and returnDate for a round trip; type oneWay has no invented return. Multi-city uses the live schema's multiCityJson. Ask for materially missing routes, dates or traveler details, not invented city IDs.

For flexible-destination or seasonal deals use `hasdata_google_travel_flights_deals_getGoogleFlightsDeals` with q and one explicit departure airport IATA code. A city label is not departureId. Do not force exact travel dates when the user explicitly wants flexible deals; report Google's returned date range as provider-chosen.

Preserve the supplied adults and passenger mix. For Google Flights and deals, omit optional children, infantsInSeat and infantsOnLap when their supplied count is zero: the upstream API rejects explicit zero for these fields. Send positive supplied counts using the live schema. Omission for an explicitly absent group is not permission to drop actual children or invent a positive count. Do not retry a rejected request automatically.

In the deals tool, route/date/class/stops/price/duration filters require arrivalId or Google can drop them silently. Resolve that destination first if the user's constraints need those filters. travelDuration cannot be combined with returnDate or tripLength. Inspect actual returned search context to distinguish requested from applied filters. Do not present an ignored filter as enforced.

Keep returned price/currency, airports, dates, stops, duration and traveler basis together. Do not infer baggage, taxes, return-leg completion or a final party total if absent. Reuse actual departure/booking tokens only for explicitly needed continuation within budget; retrieval is not ticket purchase. No automatic retry of intermittent flight-deals errors or cross-provider fallback.
