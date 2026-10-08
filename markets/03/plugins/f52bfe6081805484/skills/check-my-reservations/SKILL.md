---
name: check-my-reservations
description: Looks up the signed-in user's own upcoming, past, or date-ranged tee-time reservations. Use when the user asks about their bookings, upcoming reservations, past rounds, or reservation history — not during a new-booking or availability search.
---

# Check my reservations

## When to use

Only call `get_my_reservations` when the user explicitly asks about their own bookings or history. Never call it as part of a new booking or tee-time availability flow.

## Steps

1. Pick a `filter`: `upcoming` (default), `past`, `date` (pass `date`), or `range` (pass `from_date` and `to_date`).
2. If the response is `status=sign_in_required`, tell the user to sign in at https://auth.teemeup.ai, then retry.
3. Summarize each reservation with course name, date, time, and players. Omit `booking_status` unless the user asks for it.

## Boundaries

- Identity comes from the signed-in session — never pass or infer a user id as an argument.
- Do not use this skill to start or modify a booking; it is read-only.
