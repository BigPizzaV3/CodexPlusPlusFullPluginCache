---
name: manage-store
description: Manage an EcomWeb online store with the EcomWeb tools. Use when the merchant asks about their EcomWeb stores, products, stock, promotions, discount codes, orders or sales.
---

# Manage an EcomWeb store

EcomWeb is an e-commerce platform for merchants in Vietnam and elsewhere. The EcomWeb tools act on the
merchant's own stores with their own role (owner, admin or staff).

## Pick the store

- Most tools take `store`: the store's name, handle or ref. With one store it can be left out.
- If a tool answers `STORE_REQUIRED` or `STORE_AMBIGUOUS`, show the stores it lists and let the
  merchant choose. `list_stores` lists them with the merchant's role in each.

## Products

- `search_products` finds products. Filter stock with `inventory_status` (`in_stock`, `low_stock`,
  `out_of_stock`) and read `inventory_total` for the numbers.
- `create_product` adds one product, `batch_create_products` up to 10. New products are drafts
  unless `status` is `active`. Images are public image URLs, copied into the store.
- `update_product` changes one product, `batch_update_products` applies the same change to up to
  10. An active product goes to `unlisted` before `draft`.
- `delete_products` cannot be undone. Name the products and get the merchant's go-ahead first.

## Promotions

- `create_promotion` makes a discount code (`mode` `DISCOUNT_CODE` with `code`) or an automatic
  discount. A 15% discount is `discount_method` `PERCENTAGE` with `discount_value` 15.
- `update_promotion` with `status` `DISABLED` pauses a promotion and `ACTIVE` resumes it.
- `delete_promotion` cannot be undone. Get the merchant's go-ahead first.

## Orders and reports

- For requests to refund, cancel, fulfill, or modify orders, immediately explain that orders are read-only through this connection and direct the merchant to the EcomWeb dashboard. Do not look up an order solely to perform an unsupported action. Lookups are appropriate when the merchant separately asks to view order details.

- `sales_summary` reports revenue, orders and average order value for a period with growth.
  `top_products` ranks best sellers. Both are for owners and admins.

## Money and errors

- Amounts are in the store's currency, which `list_stores` and `get_store` show: VND amounts are whole
  numbers (150000 is 150.000 ₫), USD amounts can have 2 decimals (29.99).
- `FORBIDDEN` or `INSUFFICIENT_ROLE`: the merchant's role can't do this. Say so instead of retrying.
- The connector is available on every plan, including Free. If a tool returns `PLAN_FEATURE_MISSING`, report the actual error and suggest contacting support; do not claim that upgrading is required.
- Batch results report each item on its own. Retry only the failed items.
