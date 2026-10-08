---
name: vipcars-rentals
description: Search and compare live airport rental cars through VIPCars.com, continue to an exact booking link, retrieve an existing G/R booking using its matching email, or direct a customer to the official modification/cancellation page. Use for VIPCars.com airport rentals and bookings. Do not use for non-airport rental searches or claim that checkout, modification, or cancellation was completed in chat.
---

# VIPCars.com rentals

## Search

1. Collect exact pickup and drop-off airports, dates, and times. Ask when either time is missing.
2. Resolve ambiguous airport names before calling tools. Never invent an IATA code.
3. Call `search_rental_cars` with exact IATA codes, the customer's source country and preferred supported currency. Use age 30 only when the user did not supply an age.
4. Treat the tool result as authoritative. Never invent or recompute cars, prices, availability, suppliers, policies, ratings, or URLs.
5. Present concise comparisons using total price, per-day price, supplier, collection type, transmission, capacity, inclusions, fuel policy, mileage, deposit, and rating when present.
6. Use each returned `booking_url` exactly. Use `complete_results_url` exactly for browsing all results. Never construct or alter either URL.
7. For more results, preserve all search inputs and filters and increment the page without exceeding `total_pages`.
8. Only send supplier and category filters. When filters change, restart at page 1.

The service supports airport pickup and drop-off only. Explain that boundary when a customer asks for a non-airport location.

## Existing bookings

1. Ask for the full booking reference and matching booking email.
2. Accept only references beginning `G` or `R` followed by digits.
3. Call `retrieve_booking` and summarize the returned status, vehicle, supplier, pickup/drop-off, payment summary, deposit/excess, fuel, mileage, and cancellation information.
4. Do not expose internal identifiers or infer missing terms.
5. When the customer wants to modify or cancel, call `get_manage_booking_link` with their full reference, matching email, and preferred two-letter language code.
6. Explain that opening the link does not change the booking; the customer must review and confirm on VIPCars.com.

Do not request card details or payment credentials in chat. Checkout always continues on VIPCars.com.
