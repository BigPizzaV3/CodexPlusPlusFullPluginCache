---
name: get-started
description: Get started with Bobibo in ChatGPT. Use when the user first connects Bobibo or asks what Bobibo can do.
---

# Get started with Bobibo

Bobibo is client management for creatives and service businesses. After the user connects their Bobibo account:

1. Offer to show this week's schedule (`bobibo_list_jobs`) or overdue invoices (`bobibo_list_invoices` with `status: "overdue"`).
2. To book a job, find the client first with `bobibo_list_clients`, confirm the date and time, then call `bobibo_create_job`.
3. To bill a client, draft with `bobibo_create_invoice_draft`, show the draft, and only call `bobibo_send_invoice` after the user confirms the recipient.

Always confirm before rescheduling or canceling a job or sending an invoice. Bobibo can't delete clients or invoices, charge cards, or issue refunds; point the user to the Bobibo dashboard for those.
