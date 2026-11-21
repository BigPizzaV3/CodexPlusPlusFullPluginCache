---
name: properties-get-listing-context
description: Show the related PropBot context for one listing the person can already open.
---

Use this skill for that request.

Permission: propbot.properties.read.

1. Call properties_private_listing_context_get for the listing and hat they named. Leave invoices out of the answer unless propbot.invoices.read is granted.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
