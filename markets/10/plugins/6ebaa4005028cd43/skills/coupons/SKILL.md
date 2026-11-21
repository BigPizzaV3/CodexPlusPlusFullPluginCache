---
name: coupons
description: Find, inspect, create, edit, or delete Sell percentage and amount coupons with reviewed eligibility, limits, and expiry.
---

# Review a coupon change

Operation names below identify contracts, not direct conversation tools. Resolve them with `sellapp_find_merchant_tools`; call `sellapp_merchant_read` or `sellapp_merchant_write` using `{ "name": "sellapp_...", "arguments": { ... } }`. Native workspace, account, documentation and media tools remain directly callable. See the merchant operation rules for confirmation and store targeting. After a prepared result, summarize the unsaved proposal and stop. Only the user confirms it in the Merchant workspace; never confirm through a tool or click for them, including with Full Access.

Read [merchant operation rules](../../references/merchant-safety.md) and [exact tool contracts](references/tool-contracts.json).

Find coupons using `sellapp_v2_list_coupons` or `sellapp_v2_search_coupons`, then inspect one with `sellapp_v2_get_coupon` in the explicit store. Inspect restricted products and variants with `sellapp_get_product` and `sellapp_get_product_variant`; every restriction must belong to the same store and selected product.

Use the existing `PERCENTAGE` or `AMOUNT` type. Percentage discounts range from 1 to 100. Amount discounts and `minimum_amount` are decimal values in the store currency's major unit. Do not convert them to variant-price minor units. Ask for missing coupon code, type, discount, eligibility, limit, or expiry intent. A nullable limit or expiry must retain the exact meaning in the schema; never assume the user wants an unlimited coupon.

Present the store, code, discount with units/currency, store-wide or selected-product eligibility, any variant restrictions, minimum amount, use limit, and timezone-aware expiry. Use `sellapp_v2_create_coupon`, `sellapp_v2_update_coupon`, or `sellapp_v2_delete_coupon`. Prepare, show the returned preview, obtain approval, and confirm identical arguments and idempotency key. For edits, omitted fields retain the current values; use an empty variant restriction array only for an intentional removal of those restrictions.

Reload the coupon after a completed save and report the persisted configuration. Deletion must target the inspected coupon. Promotions and automatic discounts belong to the Merchant workspace's Promotions page, where the merchant manages them; do not change them from the conversation. This plugin does not offer coupon batches, checkout, or applying a coupon to a new order.
