---
name: store-health-check
description: Give a Hustle Got Real seller a read-only review of one store, covering listings, pending items, recently ended listings, orders and sales over a period. Use when the user asks how their store is doing, for a daily or weekly review, or what needs attention.
---

Use this skill for a read-only store review. Explicit user instructions always take priority over these steps.

1. Call `hgr_list_stores` and resolve the store; ask if several match. If its `connectionStatus` is "needs reconnecting", say so first, because listings will not sync until it is reconnected in Hustle Got Real.
2. Gather, using small limits:
   - Active listings: `hgr_list_active_listings` with `fields` such as productId, title, salePrice, stock, sourcePrice and sourceStock, sorted by stock ascending, to spot listings at or near zero stock.
   - Pending listings: `hgr_list_pending_listings`, noting items waiting for review or in an error state.
   - Ended listings: `hgr_list_ended_listings` sorted by `terminatedOn` descending to show what ended recently.
   - Sales: `hgr_get_sales` grouped by day for the period the user asked about, default the last 7 days.
   - Orders: `hgr_search_orders` for recent orders.
3. Report in short sections: needs attention, listings, orders and sales. Give counts and a few concrete examples with product IDs.
4. Suggest next steps the plugin can do, such as editing a listing or adding products, and ask before doing any of them.

Rules:
- This workflow never changes anything.
- Use only returned numbers. If a tool returns nothing, say there is no data for that period rather than estimating.
- Do not reveal buyer names, addresses or contact details.
