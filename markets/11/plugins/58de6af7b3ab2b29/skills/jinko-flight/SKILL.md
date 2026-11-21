---
name: jinko-flight
description: Discover destinations and search, compare, refine, and select Jinko flights. Use for flexible-date calendars, live fares, price monitoring, and visual flight comparisons including schedules, stops, baggage, and fare conditions. Use jinko-booking for cart, checkout, payment, and post-booking changes.
---

# Jinko Flight

Use current tool descriptors as the parameter and response authority.

## Connection and scope

- Connect to `https://chatgpt.mcp.gojinko.com/` with anonymous streamable HTTP. Send no `Authorization` or `X-API-Key`.
- Send `search_intent` to the flight search tools only as a short summary of the stated flight preferences, such as "cheapest nonstop, morning departure", with no names, dates of birth or other personal details. Do not forward the conversation for analytics.

## Search and presentation

- Destination unknown: use `find_destination`, then `flight_calendar` for a chosen destination.
- Route known but dates flexible or absent: use `flight_calendar`.
- Exact dates or a bookable live result: use `flight_search` with exactly one of `search` or `price_check`.
- Scheduled tracking for exact dates: use `price_monitoring`. Stale cached results do not authorize a silent live search.

Read [flight workflows](references/flights.md) before searching. Read [Flight Search — Generative UI](references/flight-presentation.md) before presenting, comparing, refining, or selecting flights. Preserve all existing rules for cached versus live prices, passengers, filtering, schedules, baggage, and approval.

For hotel searches use `jinko-hotel`. Once the user asks to add a selected fare, book, pay, inspect a booking, refund, or exchange, read [Jinko Booking](../jinko-booking/SKILL.md). Pass the exact selected live token and search context; a selection alone does not authorize a cart action.

## Shared response rules

- Treat `search_criteria` as the record of what the server actually searched. State the resolved place, dates, party, currency, and material filters when presenting results.
- Quote returned money display strings verbatim. Do not reconstruct customer-facing amounts from minor-unit values or decimal-place fields.
- Never fabricate travelers, photos, prices, availability, policies, or confirmation states.
- Never silently remove passengers or relax a filter after an empty result or error.
- Retry only when the tool result says the same request is retryable, and at most once. Never loop.
- A search result is not permission to add an item, checkout, pay, cancel, refund, or exchange. Obtain the user's selection and any explicit approval required by the workflow.

