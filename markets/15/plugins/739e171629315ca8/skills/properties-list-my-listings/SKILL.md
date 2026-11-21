---
name: properties-list-my-listings
description: List the signed-in person's own PropBot listings, with no company and no group.
---

Use this skill for that request.

Permission: propbot.properties.read.

1. Call properties_private_listing_list with no company id and no group id. Separate unfinished listings from listings that are already public.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
