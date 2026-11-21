---
name: notifications-list-notifications
description: List the signed-in person's PropBot notifications.
---

Use this skill for that request.

Permission: propbot.notifications.read.

1. Call notifications_private_notification_list. Do not change a notification.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
