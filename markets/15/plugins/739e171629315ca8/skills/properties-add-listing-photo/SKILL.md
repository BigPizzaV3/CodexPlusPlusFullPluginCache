---
name: properties-add-listing-photo
description: Add an outside photo to a PropBot listing gallery.
---

Use this skill for that request.

Permission: propbot.properties.write.

1. After properties_private_listing_create, call properties_private_listing_image_ingest once per photo. Pass the property id, one https URL, and category exterior or interior.
2. Leave the description as text. Do not put the source image URL in the description.
3. Publish only when the person asked. Call properties_private_listing_publish, then repeat that call with confirm set to true.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
