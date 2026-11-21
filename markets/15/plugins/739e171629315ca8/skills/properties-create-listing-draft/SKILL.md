---
name: properties-create-listing-draft
description: Create an unfinished PropBot listing draft with a required property type.
---

Use this skill for that request.

Permission: propbot.properties.write.

1. Call properties_public_property_type_list with no parent id. Choose one parent type id from that list.
2. Call properties_public_property_type_list again with that parentTypeId. Choose one child type id that belongs to that parent.
3. Confirm the hat: the person, or one company or group from the membership list. Call properties_private_listing_create with parentTypeId and childTypeId. Do not send a guessed type name, propertyType, or an empty subtype list.
4. The listing stays unfinished. Repeat the saved fields, including the parent and child type ids. Do not publish it. Photos use the properties-add-listing-photo skill, not the listing update tool.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
