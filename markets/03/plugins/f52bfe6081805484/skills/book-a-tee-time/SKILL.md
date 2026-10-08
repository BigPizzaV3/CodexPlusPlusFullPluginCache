---
name: book-a-tee-time
description: Guides a full TeemeupAI golf tee-time booking from course search through payment checkout, including course-name disambiguation and the OAuth sign-in handoff. Use when the user wants to book, reserve, or check tee time availability at a golf course.
---

# Book a tee time

## Resolve the course

Prefer `course_id` when known. If only a name is given and a tool returns `status=similar`, show the candidate `courses` list and ask the user to pick one before continuing — do not guess.

## Steps

1. `book_tee_time(type=get_tee_time_list, course_id, players, date[, time])` → list of available slots (`tee_time_id`).
2. `book_tee_time(type=get_green_fees_list, ...same context, tee_time_id)` → green fee / cart products and a `device_id`. Carry `device_id` forward unchanged.
3. `book_tee_time(type=finalize_booking, ...same context, green_fees_selected, device_id)`.

## Handling finalize_booking results

- `status=sign_in_required`: recap the chosen slot and price, then direct the user to https://auth.teemeup.ai to sign in and complete booking. Do not say it is booked.
- `status=booking_awaiting_payment`: share the returned `booking_url` as the checkout link. Do not treat the booking as confirmed until payment completes. If `split_booking_context` is present, explain each payment group separately.
- `status=booked`: confirm with course, date, time, and players.

## Boundaries

- Never invent `tee_time_id`, `device_id`, or pricing — only use values returned by the tool in the prior step.
- This skill is for creating a new booking. For "what have I already booked," use the reservations lookup instead.
