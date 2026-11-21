---
name: workspace-review-workspace
description: Summarize the signed-in person's PropBot workspace and what needs attention.
---

Use this skill for that request.

Permission: propbot.workspace.read.

1. Call users_private_workspace_get. If they ask what needs attention, call users_private_attention_list and report listing, bid, and invoice exceptions only. Do not add leases, inspections, incidents, occupancy, bookings, work orders, or financial reports. Do not change a record.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
