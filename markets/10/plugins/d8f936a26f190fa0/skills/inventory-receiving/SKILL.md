---
name: inventory-receiving
description: Record an incoming vendor delivery in Zylu and verify stock changes. Use when a user asks to receive stock, record a delivery invoice, or add purchased inventory.
---

Record an incoming inventory delivery for one Zylu business.

1. Establish the business context. If it is unknown, call `list_accessible_businesses`; ask the user to choose when more than one business is available.
2. Resolve the vendor with `search_vendors` and products with `search_products`. Do not infer IDs from names. If a vendor or product cannot be found, explain the missing record instead of creating one unless the user explicitly asks for that.
3. Collect and restate the receipt details before writing: vendor, invoice number, purchase date, and every line item's product, whole quantity, unit purchase price, optional tax treatment, and optional expiry date.
4. Call `create_inventory_receipt` only after the user has explicitly asked to record the delivery and the details are unambiguous. Do not set `allow_duplicate` unless the user explicitly authorizes a duplicate invoice number.
5. Verify the returned receipt: invoice number, vendor, received lines, total cost, and each product's `new_stock`. Report discrepancies or failed items clearly.

The tool changes product stock. Do not represent a draft as recorded, and do not use a purchase order workflow unless the user specifically asks to create or receive a purchase order.
