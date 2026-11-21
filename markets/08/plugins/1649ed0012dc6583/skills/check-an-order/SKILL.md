---
name: check-an-order
description: Check the status, payment, invoice or tracking of a customer's theprintspace (Creative Hub) orders.
---

Use this skill when the customer asks where an order is, whether it was paid, or wants the invoice or tracking.

- `list_orders` gives the customer's orders newest first with status; `get_order` gives one order in full: items, totals, `invoice_url`, and tracking once dispatched.
- Status `embryonic` with `payment_status` `unpaid` means an order placed by payment link that has not been paid. `get_order` then returns `payment.checkout_url` — the same Stripe page — while it is still open, or `payment.status` `link_expired`, in which case the order must be placed again.
- Status `new` with `payment_status` `paid` means the order is confirmed and in production.
- Never place a new order to "fix" an unpaid one without the customer's explicit yes; a repeat `place_order` with the same details returns the same order and link.
