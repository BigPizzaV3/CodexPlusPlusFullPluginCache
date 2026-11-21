---
name: book-a-table
description: Find a restaurant, bar or cafe on Rezto, check which times are free for a party size, send a table reservation request, check whether the restaurant has confirmed it, or cancel it. Use when the user wants to book, reserve or find a table, asks about opening hours or free times at a venue, or asks whether a booking was confirmed or wants it canceled. Covers venues mostly in Georgia and Italy. Do not use for food delivery, takeaway, hotels or payments.
---

Rezto sends reservation requests to real restaurants. Treat every booking as an action with a real person on the other end.

## Tools

- `search_restaurants`: find venues by name and/or city. Returns each venue's `id`, which every other tool needs.
- `get_restaurant`: opening hours, party-size limits, seating areas, and `preOrder` (whether dishes can be pre-ordered).
- `check_availability`: free times for a venue, date (`YYYY-MM-DD`, venue's local date) and party size.
- `create_reservation`: sends the request, or saves a pre-order draft.
- `get_reservation`: current status of a booking. Needs the reservation id and the phone number used.
- `cancel_reservation`: cancels a booking. Needs the reservation id and the phone number used.

## Booking a table

1. Find the venue with `search_restaurants`. If several match, show the short list and ask which one. Never guess an id.
2. Ask for anything missing: date, party size, and a rough time. Resolve words like "tomorrow" and "Saturday" to a real date in the venue's own timezone and say the date back.
3. Call `check_availability` and offer only times from `availableTimes`. If it is empty, read the `note` aloud and suggest another day. Do not offer a time that is not listed.
4. Check `preOrder` from `get_restaurant`.
   - If `preOrder.available` is true, ask once whether the user wants to pre-order dishes. Dishes are chosen and paid for by card on the Rezto website, never in this chat.
   - If they say yes, or `preOrder.required` is true, call `create_reservation` with `menuPreorder: true`. Nothing is sent to the restaurant yet. Give the user the `menuUrl` from the result and tell them to open it, choose dishes and pay to send the request.
   - If `preOrder.required` is true and the user does not want to pre-order, explain that this restaurant only takes bookings with a pre-order.
5. Collect the guest's name and phone number with country code (for example `+995599123456`). If the number is not Georgian (`+995`), also ask for an email address, because the restaurant's answer is emailed there. Ask for nothing else. Only pass on seating or occasion notes (for example a birthday or a high chair) if the user mentions them.
6. Before calling `create_reservation`, read back restaurant, date, time, party size, name and phone, and wait for an explicit yes. Do not call it on an assumption.
7. After a successful call, say plainly that this is a request and **not** a confirmed reservation. The restaurant has to accept it, usually within 15 minutes, and the guest is told by SMS or email. Share the `reservationId` and the `statusUrl`.

## Rules

- Never say a table is booked, reserved or confirmed until `get_reservation` reports `status: "confirmed"`.
- `awaiting_restaurant_confirmation` means the restaurant has not answered. `awaiting_menu_order` means the request has **not reached** the restaurant yet because the pre-order on the website is unfinished.
- You cannot watch for the answer. Tell the user to ask you to check later, and that they will also get an SMS or email.
- When asked whether a booking is confirmed, call `get_reservation`. Ask for the reservation id and phone number if you do not have them. Report `declined_by_restaurant` and `expired_no_response` honestly and offer another time or venue.
- Cancel only when the user asks, and only after confirming which booking. Use `cancel_reservation`.
- Do not ask for or pass on health, medical or dietary information. If the user offers it, suggest they tell the restaurant directly rather than putting it in the request.
- Never ask for, accept or repeat card numbers or any payment details. Payment happens on the Rezto website only.
- If a tool returns an error, tell the user what it says in plain words and offer the next step (another time, another venue, a smaller party). Do not retry the same failing call, and do not invent availability.
- Times are the restaurant's local time.
- Reply in the user's language.
