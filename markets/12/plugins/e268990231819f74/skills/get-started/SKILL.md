---
name: get-started
description: Help a renter find an apartment community, check prices and availability, and book a tour with LeasingAI.
---

# Get started with LeasingAI

1. Call `get_property_overview` first. If it returns a community, the renter already chose it (they came from its website or picked it earlier): answer about that community and do not show a picker. If it returns a picker instead, let the renter pick one from it.
2. Answer questions with `get_property_overview`, `get_property_details`, `get_pricing_and_availability`, `get_floorplans` and `get_location`.
3. To book a tour, show times with `get_tour_availability`, then call `book_tour` with the renter's name and email.
4. Use `get_tour`, `reschedule_tour` or `cancel_tour` for a tour the renter already booked.
