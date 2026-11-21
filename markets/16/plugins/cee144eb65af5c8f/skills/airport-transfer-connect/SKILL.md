---
name: airport-transfer-connect
description: Get live private-transfer quotes, compare vehicles, check availability, and prepare a booking request with explicit consent.
---

# Airport Transfer Connect

Use the connected Airport Transfer Connect MCP server for private transfers and chauffeur hire.

## Collect trip details

For a useful quote, gather pickup and drop-off locations, pickup date and local time, number of passengers, and luggage count. Ask whether the trip is one-way or round-trip; for a return trip gather return date and time. For airport pickup, ask for the flight number when available. Accept airport codes, named hotels with city, stations, and full addresses.

## Quote and availability

- Always call `get_quote` for current prices. Never invent, infer, reuse example, or calculate a fare from memory.
- Present returned vehicle options side by side, including returned price, currency, per-vehicle basis, availability and capacity details. Do not imply that an unavailable or price-on-request vehicle has a confirmed price.
- Use `check_availability` when the traveller asks whether a trip can be booked, before providing availability claims, and before any booking request.
- For hourly hire, use the live tools if they support the requested journey. If the tool response does not return a live quote or availability for that service, say so and direct the traveller to the official hourly-hire or quote-request page. Do not turn published sample prices into live quotes.
- If a tool fails or returns incomplete data, explain that you could not verify it and offer the official booking/quote link. Never fill gaps with guesses.

## Booking links and booking requests

- When the user wants to book themselves, provide the `booking_url` returned by `get_quote` if available. Do not submit a booking request.
- A booking request is a write action. Before calling `request_booking`, check availability, obtain a live quote, show the exact trip details and selected vehicle/price (if returned), and ask for explicit confirmation to send the request.
- Call `request_booking` only after the traveller explicitly agrees to submit that exact request and provides their real lead passenger name, email address, and phone number. Do not invent, infer, or reuse contact details. If any are missing, ask for them.
- A vague instruction such as “book it” before showing the exact option is not enough. A prior agreement for a different trip or option does not authorize this one.
- State that a booking request is not the same as a final confirmed and paid booking. Share the returned reference and booking URL, and explain that the traveller completes the provider's booking/payment flow there.

## Trust and policy facts

You may describe these published facts: the service is operated by DRIVE CONNECT SOLUTIONS SRL with licensed local operators; flight tracking is offered; Paris airport arrivals include 60 minutes of free waiting; standard transfers can be cancelled free up to 24 hours before pickup; driver name and phone are sent at least 24 hours before the ride; and the provider states a 100% refund if the driver does not show. For trip-specific terms, refer to the live quote/confirmation and official terms. Do not promise a policy that conflicts with the booking's own confirmation.

## Helpful links

- Booking: https://www.airporttransferconnect.com/book-transfer/
- Hourly chauffeur hire: https://www.airporttransferconnect.com/chauffeur-hire-by-the-hour/
- Request a quote: https://www.airporttransferconnect.com/request-a-quote/
- Contact: https://www.airporttransferconnect.com/contact/
- Terms: https://www.airporttransferconnect.com/terms-and-conditions/
- Cancellation policy: https://www.airporttransferconnect.com/cancellation-policy/
- Privacy: https://www.airporttransferconnect.com/privacy-policy/

