---
name: lapyme-inventory-planning
description: Analyze La Pyme stock pressure and decide whether to buy, transfer, wait, or investigate, then create a transfer or purchase order when the user requests execution. Do not use for a simple lookup of one known stock record.
---

# La Pyme Inventory Planning

Treat replenishment and purchase planning as one decision: identify stock pressure, understand demand under availability, and choose whether to buy, transfer, wait, or investigate.

Read `context://inventory-rules`, `context://reporting-rules`, and `reporting://catalog` when the request needs analytical stock or demand evidence.

## Build The Evidence

- Use `run_report` as the primary tool for broad stock planning, sales velocity, coverage, supplier grouping, and product-by-warehouse comparison.
- Use `list_inventory` for a narrowed current operational lookup or to confirm a specific execution target. Do not request an unbounded product-by-warehouse matrix.
- Use `list_purchases` only to enrich a shortlist with recent supplier, cost, voucher, or balance context. Purchase history is not the primary demand signal.
- If the user did not supply a horizon, choose a sensible recent evidence period, commonly 90 days, and state the assumption.

Rank candidates by stock pressure and credible demand, not raw rotation alone. Consider available, reserved, and incoming stock. Pair sales velocity with days in stock and days out of stock because unavailable products can show artificially low sales.

Compare warehouses before recommending a purchase. If the organization has enough available stock in another location, recommend a transfer. Recommend buying only when organization-level available plus incoming stock cannot cover the horizon and the demand signal is credible. Recommend waiting when stock or incoming supply covers the horizon. Recommend investigation when supplier, cost, movement, or availability evidence is contradictory or incomplete.

## Execute Only The Chosen Action

- Use `save_transfer` after the user requests the transfer and the source, destination, products, and quantities are resolved.
- Confirm source availability before calling `save_transfer`; the tool can create a transfer from an already negative source balance.
- Use `save_purchase_order` after the user requests the purchase order and the supplier, destination warehouse, products, quantities, and expected costs are resolved.
- An exact execution request is sufficient authorization. Do not turn analysis or a recommendation into a write.
- Product report rows can represent a product with multiple variants. If a write returns variant candidates, select the user's intended variant or ask them; do not guess.

Return a compact ranked recommendation with the product, proposed action, current stock picture, demand signal, urgency, and missing evidence. After a write, report the created transfer or purchase order and any unresolved or skipped items.
