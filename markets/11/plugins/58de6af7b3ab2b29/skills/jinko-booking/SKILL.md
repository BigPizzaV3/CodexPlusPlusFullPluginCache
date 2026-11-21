---
name: jinko-booking
description: Build and manage Jinko flight and hotel trips, collect the details of travelers aged 13 or older, hand a trip with a child under 13 to the Jinko page, quote checkout, handle authorized payment, inspect bookings, and process flight refunds or exchanges and hotel cancellations. Use after selecting a live offer or when managing an existing trip or booking.
---

# Jinko Booking

Use current tool descriptors as the parameter and response authority. Connect to `https://chatgpt.mcp.gojinko.com/` with anonymous streamable HTTP; send no `Authorization` or `X-API-Key`. Do not send `search_intent` or conversation text for analytics.

Read [booking and servicing procedures](references/booking-and-servicing.md) before any cart, checkout, payment, inspection, refund, exchange, or cancellation workflow.

## Workflow

- Obtain an exact live offer selected by the user through [Jinko Flight](../jinko-flight/SKILL.md) or [Jinko Hotel](../jinko-hotel/SKILL.md). Preserve search criteria, selected token and the returned price and terms. If stale or changed, return to the corresponding search skill and obtain renewed approval.
- Before adding an item, present its final returned total, taxes, relevant baggage or meals, cancellation/refund terms and payment conditions. Obtain explicit approval of the exact selection.
- Build the trip with `trip`; add items before travelers. Collect real details of travelers aged 13 or older and real contact information, and never fabricate required fields.
- Never ask for, or send, the name, date of birth or any other detail of a traveler under 13. A flight searched with children or infants, or a party that includes anyone under 13 (a 12-year-old counts as an adult in the flight search), is completed on the Jinko page: give the user the `trip_link` that `trip` and `get_trip` return. Every traveler is entered and the trip is paid on that page; do not call `trip(upsert_travelers)` or `checkout` on that trip.
- Run `checkout` only after the user asks to proceed and reviews the items and current price. Do not automatically open or complete checkout.
- Use `submit_agent_payment` only with returned `agent_spt_params`, a valid scoped Shared Payment Token, and explicit payment authorization.
- Use `get_trip` for cart/quote/payment/fulfillment state. Use `get_booking` with the Jinko booking reference and last name before servicing; pass the selected item's `booked_item_id` on every servicing call.
- For a flight refund (`flight_refund_preview`, `flight_refund_commit`, `flight_refund_status`), a flight exchange (`flight_exchange_shop`, `flight_exchange_price`, `flight_exchange_commit`, `flight_exchange_status`) or a hotel cancellation (`hotel_cancel_preview`, `hotel_cancel_commit`, `hotel_cancel_status`), follow the reference's exact preview/shop, price, approval, commit and status sequence. Reconfirm changed figures before committing.

## Shared response rules

- Treat `search_criteria` as the record of what the server actually searched. State the resolved place, dates, party, currency, and material filters when presenting results.
- Quote returned money display strings verbatim. Do not reconstruct customer-facing amounts from minor-unit values or decimal-place fields.
- Never fabricate travelers, photos, prices, availability, policies, or confirmation states.
- Never silently remove passengers or relax a filter after an empty result or error.
- Retry only when the tool result says the same request is retryable, and at most once. Never loop.
- A search result is not permission to add an item, checkout, pay, cancel, refund, or exchange. Obtain the user's selection and any explicit approval required by the workflow.

