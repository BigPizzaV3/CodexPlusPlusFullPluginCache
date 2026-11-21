---
name: properties-update-listing-draft
description: Change draft fields on an unfinished PropBot listing, including price.
---

Use this skill for that request.

Permission: propbot.properties.write.

1. Call properties_private_listing_update for the fields they named, on the same hat used to read it. Do not change listing status. Do not publish. Do not withdraw. Photos use the properties-add-listing-photo skill, not this tool.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
