---
name: properties-find-quiet-listings
description: Find the signed-in person's PropBot listings that have gone quiet or need attention.
---

Use this skill for that request.

Permission: propbot.properties.read.

1. Call properties_private_listing_attention_list for the person. If they named one company or group they belong to, use that hat instead. Report only listing exceptions that came back.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
