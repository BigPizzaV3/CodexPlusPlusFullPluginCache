---
name: order-help
description: Look up and update WooCommerce orders. Use when the owner asks where an order is, wants order details, a customer's orders, unpaid or stuck orders, or wants to mark an order completed or add a note.
---

- To find orders, use `find_orders` (filters: status, period, `older_than_days`, amount, customer email, product). Names in lists are shortened on purpose.
- For one order, use `get_order` with the order number. Share only what the owner asked for; do not repeat full addresses or emails unless needed.
- To change status or add a note, use `update_order`: preview first, show the owner, and call again with `confirm: true` and the `preview_id` only after a clear yes.
- A note to the customer is emailed by WooCommerce. Always ask whether a note should be private or visible to the customer.
- Marking an order completed also emails the customer. Say so in the preview.
- Refunds are not possible here. Tell the owner to use WooCommerce's refund button.
