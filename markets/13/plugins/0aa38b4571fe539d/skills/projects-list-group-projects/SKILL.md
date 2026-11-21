---
name: projects-list-group-projects
description: List PropBot projects for one group the person belongs to.
---

Use this skill for that request.

Permission: propbot.projects.read.

1. Resolve one group id from the membership list. Call projects_private_project_list for that group only.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
