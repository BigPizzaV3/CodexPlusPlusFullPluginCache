# Booking and servicing

## Build a trip

1. Obtain a live `flight_search` fare token or a live `hotel_search` rate token and let the user select it.
2. Call `trip(add_item)`. Omit `trip_id` only when creating a new trip.
3. A multi-room `rooms` add books 2–8 rooms of the same hotel and the same stay dates as one booking, with one selected `htl_*` token per room. Not every hotel rate can be booked this way; a rate that cannot is refused when it is added. When it is refused, explain the limitation and stop; do not split the stay into duplicate hotel items or add the same hotel repeatedly.
4. Call `trip(upsert_travelers)` only for travelers aged 13 or older, with real user-provided names, a date of birth for every traveler, gender for flights, and contact details. `traveler_type` is always `adult`. Phone numbers use international `+` format. After adding a flight, send `upsert_travelers` in a call of its own.
5. For flight bags, quote with `checkout`, inspect `available_ancillaries` through `get_trip`, obtain the user's selection, call `trip(select_ancillaries)`, then run a fresh `checkout`. Each selection call replaces the prior ancillary set.

## Travelers under 13

- Never ask for, or send, the name, date of birth or any other detail of a traveler under 13. Search with counts and ages only: `traveler_counts` for flights, `children_ages` for hotels.
- A flight priced for a child or an infant: `trip(add_item)` and `get_trip` return `trip_link` with `travelers_on_jinko_page: true`. Give the user the link: on that Jinko page they enter every traveler, adults included, and pay. `trip(upsert_travelers)` and `checkout` on that trip are refused with `TRAVELERS_ON_JINKO_PAGE`.
- Anyone else under 13, such as a 12-year-old counted as an adult in the flight search: give the user the `trip_link` of the trip the same way. `trip(upsert_travelers)` with a traveler under 13 is refused with `TRAVELER_UNDER_13` and saves nothing; do not send that traveler's details again.
- Hotels (a trip with no flight): enter only the guests aged 18 or older as travelers; a hotel counts anyone younger as a child. Guests under 18 stay as the ages given in `hotel_search` `children_ages`.
- `trip` and `get_trip` show a traveler under 13 with `traveler_ref` and `traveler_type` only; `get_booking` shows `traveler_type` only.

## Checkout and payment

- Call `checkout` only when the user explicitly wants to proceed, the chosen items and travelers are current, and the user has seen the price basis. Do not auto-open `checkout_url`.
- If travelers change, or the quote expires, run `checkout` again and use only the latest payment artifacts.
- The normal human path is the returned `checkout_url`.
- Use `submit_agent_payment` only when the latest checkout returned `agent_spt_params`, a valid scoped Shared Payment Token exists, and the user explicitly authorized payment. A 3DS or decline response may require the human checkout URL.
- A `booking_ref` alone does not prove payment. Read payment verification and `fulfillment.status`.

## Booking references

- `trip.booking_ref` / `booking_ref` in the form `JNK-XXXXXX` is the Jinko reference used by `get_booking` and servicing tools.
- `trip.bookings[].supplier_references` (and `items[].supplier_references` in `get_booking`) hold the airline record locator or supplier confirmation, as `issuer` and `reference`. Do not pass a reference as `booking_ref`.
- Use `get_trip(trip_id)` for cart, quote, payment, and fulfillment state.
- Use `get_booking(booking_ref, last_name)` before servicing. Select the intended `items[]` entry and pass its `booked_item_id`, with the same `booking_ref` and `last_name`, on every servicing action. Keep the same `booked_item_id` after an exchange.

## Flight refund

Follow `preview -> explicit user approval -> commit -> status`.

- The preview cancels nothing. Show its penalty, customer refund, covered documents, excluded extras, and whether it is a refund or void.
- Commit with the preview's `svq_*` quote and copy its `refund` object field for field into `acknowledged`.
- `fee_known: false` means unknown, not free.
- `MANUAL_REQUIRED` needs the user's approval for manual handling and `manual_ok: true`; nothing reaches the airline until an operator acts.
- `flight_refund_check` is eligibility only and cannot authorize a commit.

## Flight exchange

Follow `shop -> price -> explicit user approval -> commit -> status` with the same booking identity and selected `offer_id`.

- Show the price response's customer figures and the new fare's refund, change, checked-bag, and carry-on terms.
- Pass `session_reference` from price to commit. When a refused automatic price returns none, a confirmed commit without it sends the request to Jinko support.
- Use the returned “You pay” or “You get back” amount directly. Do not reconstruct it from older top-level supplier fields.

## Hotel cancellation

Follow `preview -> explicit user approval -> commit -> status`.

- Show the preview's penalty, customer refund, and policy.
- Commit with the same booking identity, the `svq_*` quote, and the preview refund copied field for field as `acknowledged`.
- An unknown penalty is not free cancellation.

For all servicing, quote the tool's customer-facing money displays or exact acknowledged object. Do not recompute amounts or commit after figures change without renewed approval.

