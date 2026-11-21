---
name: properties-get-group-listing
description: Open one listing inside one PropBot group the person belongs to.
---

Use this skill for that request.

Permission: propbot.properties.read.

1. Use the group id from the membership list and the listing they named. Call properties_private_listing_get for that hat only.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
