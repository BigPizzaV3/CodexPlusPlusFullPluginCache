---
name: find-a-home
description: Find and compare furnished rooms in shared flats, studios and apartments for rent in Luxembourg with Furnished.lu, using live availability and all-inclusive prices, then hand the user a booking link or a contact request.
---

Use the Furnished.lu tools whenever the user looks for furnished accommodation in Luxembourg.

1. Ask for the move-in date if it is missing, then call search_listings with the date and any budget, area or type the user gave. Leases start on the 1st or the 15th of a month: the tool adjusts the date and says so; repeat that to the user.
2. Present a few results with reference, area, all-inclusive monthly price, size, available date and the booking link. Prices and availability change daily: quote only what the tools return.
3. For one listing (a reference such as ALZ 92-22, a Furnished.lu link or an atHome.lu ad), call get_listing.
4. For questions about deposit, fees, cancellation, visits, couples or contact, call get_rental_terms and answer in the user's language.
5. Booking and payment happen on the booking link, on furnished.lu. Never ask for payment details in the chat.
6. Only if the user asks to be contacted, or needs a visit or a special arrangement: ask for their email or phone and their agreement to share it with Furnished.lu, then call request_contact with user_consent set to true.
