---
name: booking-review
description: Review Apex rental bookings and event details for an authorized date range.
---

# Booking review

Use this skill for read-only scheduling and event-operations questions.

## Workflow

1. Confirm the user has an authorized Apex Rental Pro connection.
2. Ask for an inclusive start and end date when the request concerns a period. Use `list_bookings`.
3. For one booking, use `get_event_details` only after the user provides its booking ID or selects an ID from the list.
4. Summarize dates, event name, equipment, delivery or pickup details, and customer-visible details only when returned and needed for the task.
5. Clearly label missing, conflicting, or unavailable fields.

## Example prompts

- “List deliveries and pickups from 2026-06-01 to 2026-06-07.”
- “Show the equipment and schedule for booking 1842.”

## Guardrails

- Treat booking data as sensitive business information. Show only the minimum fields needed.
- Never expose API keys, passwords, payment-card data, government identifiers, or unrelated customer records.
- Never claim that a booking was changed, confirmed, cancelled, or communicated. These tools are read-only.
- Do not guess a booking ID, date, customer, or status. Ask a clarifying question.
- Do not send messages, contact customers, or make operational commitments.
