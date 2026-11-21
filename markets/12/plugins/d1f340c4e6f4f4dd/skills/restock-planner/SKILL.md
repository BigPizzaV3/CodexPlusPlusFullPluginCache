---
name: restock-planner
description: Plan Amazon FBA restocks with Sotrics inventory data and forecasts, so the seller reorders before products run out.
---

Use this when the user asks about stock levels, stockouts, days of supply, reorders or purchase orders.

1. Call `get_inventory` to list SKUs with available and inbound units, days of supply and stockout risk.
2. For the riskiest three ASINs (fewest days of supply that still sell), call `get_restock_forecast` with each ASIN to get the stockout date, reorder date and suggested quantity.
3. Optionally call `get_purchase_orders` to check whether a purchase order is already on the way for those products.
4. Answer with a short table: product, days of supply, expected stockout date, reorder by date, suggested quantity, and whether a purchase order already covers it.
5. Mention the forecast confidence the tool reports. Never invent stock numbers; Sotrics is read only and cannot create shipments or orders.
