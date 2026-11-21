---
name: projects-list-my-projects
description: List the signed-in person's own PropBot projects.
---

Use this skill for that request.

Permission: propbot.projects.read.

1. Call projects_private_project_list with no company and no group. Do not change a project.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
