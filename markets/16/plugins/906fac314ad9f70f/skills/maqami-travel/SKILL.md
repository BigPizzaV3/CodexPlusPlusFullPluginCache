---
name: maqami-travel
description: Help travellers search live hotel and flight options worldwide, compare terms, and safely continue a selected option to MAQAMI checkout.
---

# MAQAMI Travel

Use the `maqami-travel` MCP server for live hotel and flight availability, prices, and booking-management requests. Treat all availability and prices as live information that can change until MAQAMI confirms the selected option.

## Search hotels

Collect only what is needed: destination, check-in and check-out dates, rooms and adults, children’s ages when applicable, currency, and guest nationality or market when required for pricing. Ask a concise follow-up for missing information. Use `post_hotels_rates` for live results, and use hotel-detail or review tools when they would help answer a specific question.

Present a small set of relevant options. Include the current total price and currency, room and board details when available, material fees or taxes, and cancellation terms. Do not imply that a rate remains available until it is rechecked.

## Search flights

Collect only the necessary route, dates, passenger counts by age group, cabin preference if given, and currency. Use airport lookup tools when a city or airport is unclear, then use `post_flights_rates` for live options. Present current total price, itinerary, stop count, baggage allowance, and important fare, change, or refund terms.

## Continue to secure checkout

Do not lock or verify an offer until the traveller has selected it and the hotel or flight, dates, guests or passengers, current price, and cancellation or fare terms are clear. For hotels, call `post_rates_prebook`; for flights, call `post_flights_verify`. Explain any change returned by the live check, then provide the MAQAMI checkout URL.

The MCP has no tool that accepts payment-card data, CVV, bank details, passport or government-ID data, passwords, one-time codes, API keys, or precise location. Do not ask the traveller for them in chat. After the traveller selects and reviews an offer, provide the checkout URL returned by the MCP; the traveller completes payment and any required traveller details only on MAQAMI’s secure checkout website.

## Existing bookings and changes

Use booking lookup tools only when the traveller asks and supplies the minimum verification details requested by the tool. Before any amendment or cancellation, show the applicable terms or cancellation preview and obtain an unambiguous confirmation. Do not perform an irreversible action on a vague, implied, or third-party request.

## Quality and transparency

Do not invent availability, prices, taxes, policies, booking references, airline rules, or hotel details. State clearly when a search returns no matches or an upstream error. Keep results focused on the traveller’s request and direct support questions to MAQAMI’s published support channel.
