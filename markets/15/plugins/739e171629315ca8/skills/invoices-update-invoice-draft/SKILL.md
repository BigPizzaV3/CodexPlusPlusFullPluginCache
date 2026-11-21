---
name: invoices-update-invoice-draft
description: Update an unpaid PropBot invoice or quote draft.
---

Use this skill for that request.

Permission: propbot.invoices.stage.

1. Call invoices_private_invoice_update for the unpaid draft they named. Show the new status, amount, and due date. Do not issue it and do not collect payment.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
