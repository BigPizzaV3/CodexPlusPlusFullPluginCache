---
name: kazna-orders
description: Review past Kazna author orders (sales analytics) with read-only MCP tools.
---

# Kazna orders

Use MCP server `Kazna`.

## Steps

1. Call `list_orders` and summarize recent statuses, product titles, and amounts.
2. For a specific order, call `get_order` with numeric `order_code`.
3. Do not expose buyer phones; tools already omit them.

## Constraints

- This is historical analytics only — no checkout, refunds, or product creation.
