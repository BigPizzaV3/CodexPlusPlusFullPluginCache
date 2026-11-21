---
name: invoices-get-invoice
description: Open one PropBot invoice the person can already see.
---

Use this skill for that request.

Permission: propbot.invoices.read.

1. Call invoices_private_invoice_get for the invoice and hat they named. Show status, amount due, and due date. Do not change it.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
