---
name: stayfritz-booking
description: Help travelers find StayFritz properties, review live quotes, and safely start or monitor a booking through hosted Checkout.
---

# StayFritz traveler booking

Use this skill when a traveler wants to search StayFritz accommodation, compare
available stays, get a live price quote, start a booking, or check a booking
that was already started.

## Required workflow

1. Collect the destination, arrival date, departure date, number of adults,
   number of children, and child ages when applicable. If a required value is
   missing or ambiguous, ask a concise follow-up question.
2. Call `search_properties` with the dated search. Do not invent availability,
   prices, property IDs, or policies.
3. Present useful matching properties with their names, location, dates,
   occupancy, price information when available, and important differences.
4. When the traveler selects a property, call `get_property_details` and show
   the relevant description, house rules, location, photos, and cancellation
   information.
5. Call `create_quote` for the selected property and exact dates and occupancy.
   Show the complete quote, currency, expiry, fees, and cancellation terms.
   Treat a quote as short-lived: obtain a fresh quote if it has expired or if
   the traveler changes dates, occupancy, property, or other pricing inputs.
6. Before `create_booking`, explicitly ask whether the traveler has reviewed
   the quote and agrees to continue to the hosted Stripe Checkout flow. Do not
   call `create_booking` without an affirmative answer and `consent: true`.
7. Call `create_booking` only once for the approved quote. Supply complete guest
   contact and address details and a stable `idempotency_key`. Explain that the
   returned URL opens Stripe-hosted Checkout and that payment details should be
   entered there, not in the chat.
8. After a booking attempt, use `get_booking_status` with the returned opaque
   `status_token`. Follow its `action` field. If it says `wait_and_poll` or
   `wait_and_reconcile`, poll the same token; never start a second booking.
9. If a supported payment capability is explicitly available and the traveler
   has authorized it, `pay_booking` may accept exactly one Stripe
   Confirmation Token or PaymentMethod ID. Otherwise use hosted Checkout.
   Never collect or transmit raw card numbers, CVC, expiry dates, wallet
   passwords, seeds, private keys, client secrets, or StayFritz credentials.
10. Report the final status clearly. Only a verified paid result may expose a
    confirmed reservation ID. Pending, abandoned, expired, failed, or
    indeterminate payment must not be described as confirmed.

## Safety and boundaries

- Search, property details, quotes, and status checks are read-only from the
  traveler's perspective, but availability and prices are live and can change.
- `create_booking` is state-changing. Always show the quote and cancellation
  terms and obtain explicit consent immediately before calling it.
- Use the same stable idempotency key if a booking request times out or the
  response is lost. Do not generate a new key while the first attempt may be
  pending.
- Never call `pay_booking` with both `confirmation_token` and `payment_method`.
  Never use public Stripe test fixtures or a test payment lane.
- Do not claim that a booking is confirmed based only on a Checkout URL,
  Checkout creation, a successful tool transport response, or an unverified
  provider response.
- Cancellation is not an anonymous public operation. Direct the traveler to
  StayFritz support rather than inventing a cancellation tool or policy.
- Do not expose opaque quote or status capabilities unnecessarily. Do not place
  them in URLs, analytics, logs, or free-form public text beyond what is needed
  to continue the traveler's flow.

## Response format

For search results, use a compact comparison and ask which property the
traveler wants to inspect. For a quote, separate the total, currency, fees,
dates, occupancy, expiry, and cancellation terms. For a booking handoff, show
the Checkout link and explain the next step. For status polling, state the
current status, the next action, and whether the traveler should wait, open
Checkout, contact support, or treat the booking as confirmed.