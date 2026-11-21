---
name: workspace-list-my-groups
description: List the PropBot groups the signed-in person belongs to.
---

Use this skill for that request.

Permission: propbot.workspace.read.

1. Call groups_private_membership_list. Name each group id that came back. Do not open a group profile in this skill.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
