---
name: projects-list-quotes
description: Read PropBot quotes on a project the person can already see. Do not accept or reject them.
---

Use this skill for that request.

Permission: propbot.projects.read.

1. Call projects_private_quote_list or projects_private_quote_get for the project and quote they named. Do not call accept or reject.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
