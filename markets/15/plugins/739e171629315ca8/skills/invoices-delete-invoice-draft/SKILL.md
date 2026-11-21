---
name: invoices-delete-invoice-draft
description: Delete an unpaid PropBot invoice or quote draft the person asked to remove.
---

Use this skill for that request.

Permission: propbot.invoices.stage.

1. Delete only when they asked to remove that unpaid draft. Call invoices_private_invoice_delete. Do not issue an invoice and do not collect payment.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
