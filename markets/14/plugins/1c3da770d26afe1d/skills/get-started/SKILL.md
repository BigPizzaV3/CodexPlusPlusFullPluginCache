---
name: get-started
description: Help someone plan and book a fishing charter with Reelzy. Use when the user wants a fishing trip, a boat or a charter in a place, asks what is free on a date, or asks where Reelzy has boats.
---

# Plan a fishing charter with Reelzy

1. Find out where the person wants to fish. A country, island or port is enough. If they have not said, ask, or call `list_destinations` to show where Reelzy has boats.
2. Call `search_charters` with the place. Add the date (YYYY-MM-DD), the number of people, a fish ("marlin", "GT", "tuna") or a style ("trolling", "jigging", "inshore") when the person gave them. With a date the results only hold boats that are free that day, with the exact total.
3. For one boat, call `get_charter` for its fish, fishing styles, cancellation policy and whether it books instantly, and `check_availability` for the free departures and price on a date.
4. Quote only prices the tools returned, with the currency they came in. Do not estimate or convert prices yourself.
5. To book, give the person the `bookUrl` of the boat. Booking and payment happen on reelzy.co. Never ask for card details or try to take payment in the chat.

If a place has no boats, say so and offer the nearest boats the tool returned or the destination list. Existing bookings, cancellations and refunds are handled on reelzy.co or by the support team at reelzy.co/help.
