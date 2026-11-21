---
name: sales-overview
description: Summarise the user's sales and orders across all their marketplaces. Use when the user asks what sold, how much they made, which marketplace sells best, or for orders in a date range.
---

# Sales across marketplaces

1. Call `get_orders` with `date_start` / `date_end` (YYYY-MM-DD) for the period the user means. Page
   through with `page` until every order is in.
2. Summarise by marketplace: number of orders and total value per currency. Never add up different
   currencies.
3. List notable items if the user wants detail. Don't show buyer personal details unless they ask.
4. An empty result means no orders in that period. Say so and don't retry.
