---
name: find-a-stay
description: Help the user find a stay in South Korea on Wehome by area, guests, and budget.
---

Use the Wehome `search_stays` tool when the user wants a place to stay in South Korea.

1. Put the area, station, or theme the user named into `location` (for example "Hongdae", "Gwangalli", "Hanok").
2. Pass `guests` and, when the user gives a budget, `max_price_krw` as the nightly limit in KRW.
3. Set `late_checkin_preferred` to true when the user says they will arrive late.
4. Show the matching stays with KRW price, rating, and the listing link. Booking and payment happen on wehome.me through that link. Results do not confirm availability for specific dates, so tell the user to check dates on the listing.
5. If nothing matches, suggest a nearby area or a higher budget.

Wehome only covers South Korea. For other countries, tell the user Wehome cannot help with that trip.
