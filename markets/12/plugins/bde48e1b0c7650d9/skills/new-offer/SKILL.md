---
name: new-offer
description: Start a new offer or add a new client in OfferCopilot. Use when the user wants to write an offer on a listing, or to add a buyer, renter or seller to their client list.
---

1. To add a client, collect their full name, email and role (buyer, renter or seller), plus a phone number if the user has one, then call `create_client`. If the email is already used by one of their clients, give the user the existing client's link instead.
2. To start an offer, collect the listing address or MLS number and whether it is a purchase or a lease. Pass the price and deposit only if the user stated them.
3. Call `start_offer` and give the user the `offer_url`. The offer is written and finished in OfferCopilot, where the user confirms the listing, picks the client and chooses the terms.

Do not choose a price, deposit, condition, date or any other term on the user's behalf, and do not fill in a value the user did not give. If the user asks for advice on terms, say that the terms are theirs to set in OfferCopilot.
