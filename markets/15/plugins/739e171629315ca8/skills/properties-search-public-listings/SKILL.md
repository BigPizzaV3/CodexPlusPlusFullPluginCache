---
name: properties-search-public-listings
description: Search homes already published on the public PropBot market.
---

Use this skill for that request.

Permission: none.

1. Call properties_public_listing_search. Return only listings that are already public. Do not describe drafts or a private portfolio.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
