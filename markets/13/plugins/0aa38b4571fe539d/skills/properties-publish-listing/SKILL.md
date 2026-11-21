---
name: properties-publish-listing
description: Publish one PropBot listing after the person confirms that exact listing. For agents and brokers.
---

Use this skill for that request.

Permission: propbot.properties.write and propbot.properties.publish.

1. Show the listing id, address, and current status. Ask them to confirm this listing should become public. Then call properties_private_listing_publish. Report the new status. If publish is not granted, stop.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
