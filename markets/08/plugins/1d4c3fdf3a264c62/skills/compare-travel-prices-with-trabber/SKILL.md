---
name: compare-travel-prices-with-trabber
description: Search and compare flights, multi-city flights, hotels and other accommodation, rental cars, trains, and flexible flight deals using Trabber. Use whenever the user wants to find travel options, prices, or availability in any of these categories, even if they do not mention Trabber, and when they want to filter, paginate, refine, resume, or combine searches for one trip. Do not use for travel questions that do not require a search, such as visas, weather, destination advice, sightseeing itineraries, or summarising an existing booking.
---

# Compare travel prices with Trabber

Find and compare the requested travel options with Trabber while reusing existing searches whenever possible. Follow each tool's schema and never invent unsupported options.

## Choose the entry point

- Use `explore_flight_deals` for flexible round trips when the dates, destination, or both are open. Present the returned price as a cached snapshot, include how long ago it was found, and provide its booking link. Do not call `search_flights` merely to shortlist or confirm these deals. Call it afterwards only when the user explicitly asks for a live search or current alternatives for a selected route and dates; a request to compare or plan a flexible trip is not by itself such a request.
- Use `search_flights` for a concrete one-way or round trip.
- Use `search_multi_city_flights` for a multi-city or open-jaw journey with two to six legs.
- Use `search_hotels` for hotels and other accommodation.
- Use `search_cars` for rental cars.
- Use `search_trains` for rail journeys.
- Use `list_my_searches` when the user wants to resume, revisit, or list previous Trabber searches, then pass its `search_id` to the matching results tool.

Ask one concise follow-up containing only required information that cannot be inferred reliably. Do not call a different vertical merely because it might be useful.

## Say where, and for which market

- Flights, multi-city flights and rental cars take three-letter IATA codes: prefer them to place names whenever you know them.
- Hotel destinations have no code. Pass only the name of the city, town or island in English, without its region or country, and put the country in `destination_country` (ISO 3166-1 alpha-2) whenever you know it, so that Barcelona in Spain is not confused with Barcelona in Venezuela. Add `destination_region` only when several places in that country share the name. If the tool answers with candidates, retry with the `destination_id` of the one the user means.
- Neighbourhoods, beaches, resort areas and landmarks are not hotel destinations. Search the town or city they belong to, then pick the properties in the area by their distance or coordinates with `get_hotel_results`.
- `market_country` is the country the user shops from: it selects the booking websites compared and the currency. It is not the destination. Omit it unless the user asks for another market or currency; Trabber remembers the last one used. Train search works only in the Spanish market, whatever the user's market is.

## Refine without relaunching

- Retain every returned `search_id` in the conversation context.
- Use the corresponding `get_*_results` tool to sort, filter, or paginate an existing search. Do not launch another live search only because the user changes sorting, maximum price, stops, times, airlines, rating, distance from the searched centre, or similar result filters.
- Request another results page when the user wants more options instead of repeating the same page.
- Use `get_flight_details` or `get_hotel_details` only when the user wants the full breakdown or all sellers for a specific result. Car, train, and multi-city results have no separate detail tool.
- Launch a new live search only when a search input changes, such as route, travel dates, passengers, rooms, or pickup and drop-off details.

## Coordinate a complete trip

- Search only the verticals requested by the user.
- Reuse the same passenger composition, market, language, currency context, and trip dates where they apply. Do not assume that every traveller needs a car or that accommodation dates always equal flight dates when the request suggests otherwise.
- Establish transport dates before deriving accommodation check-in and check-out or car pickup and return. Ask when arrival or departure timing makes those dates ambiguous.
- When a flexible flight deal establishes the destination and dates, use its snapshot price for any provisional cross-vertical total and label it accordingly. Do not require a live flight search before searching the other requested verticals.
- Keep each vertical's results and booking links separate. Do not present the combination as a package or imply that one reservation covers multiple sellers.
- Add totals across verticals only when the currencies match and the returned prices are comparable. State what the total includes.

## Present results

- Reply in the user's language.
- Preserve each seller's exact `booking_url` and show it as a clickable link beside the seller and price. For combined results, preserve both booking links and make clear that they are separate purchases.
- State that booking takes place with the selected seller and that its price and availability apply at checkout.
- Keep cached deal snapshots distinct from live-search results. Do not automatically confirm a cached deal with a live search.
- Respect `nearby_dates` and the requested `include_nearby_dates` preference. Make alternative dates explicit instead of presenting them as the dates originally requested.
- Never invent availability, baggage rules, cancellation terms, fees, or a combined trip price that the tools did not return.
