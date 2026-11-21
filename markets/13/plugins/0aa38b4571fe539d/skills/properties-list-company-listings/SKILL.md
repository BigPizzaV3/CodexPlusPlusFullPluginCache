---
name: properties-list-company-listings
description: List private listings for one PropBot company the person belongs to.
---

Use this skill for that request.

Permission: propbot.properties.read.

1. Resolve one company id from the membership list. Call properties_private_listing_list for that company only. Say which company was read.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
