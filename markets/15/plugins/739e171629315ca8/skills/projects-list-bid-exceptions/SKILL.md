---
name: projects-list-bid-exceptions
description: List PropBot projects or bids that need attention.
---

Use this skill for that request.

Permission: propbot.projects.read.

1. Call projects_private_bid_attention_list for the person, or for one company or group they named and belong to. Report only the bid exceptions that came back.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
