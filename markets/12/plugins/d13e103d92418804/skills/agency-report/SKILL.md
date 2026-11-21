---
name: agency-report
description: Report across several client stores at once. Use when an agency or owner with more than one connected store asks for month-end numbers, a one-table comparison of stores, or a client report.
---

1. Call `list_stores` to see which stores are connected.
2. Call `multi_store_report` with the period (for example `last_month`). It returns one row per store: net revenue, orders, average order, refunds and top product.
3. Present one table. Never add numbers from stores that use different currencies.
4. If a store could not be read, say which one and why (the message tells you), and offer to retry.
5. For any store the owner wants to dig into, call the other tools with that store's address in the `store` argument.
