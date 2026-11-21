---
name: woocommerce-operations
description: Read and manage authorized WooCommerce products, prices, stock, orders and refunds using safe preview-and-approval flows.
---

# WooCommerce Operations

The connected WooCommerce Operations MCP server operated by Zactra Technologies Inc is the source of truth for accessible stores and their records. Never invent store IDs, order IDs, product IDs, quantities, currencies, variation IDs, payment or refund status.

## Read-first rules

- Identify the authorized connected store (`list_connected_stores`), then invoke read-only tools (`list_products`, `get_product`, `list_product_variations`, `list_orders`, `get_order`, `get_inventory`, `get_sales_report`, `get_top_sellers_report`) as needed.
- Fetch `get_store_currency` before quoting or changing amounts. For price change requests, use `inspect_product_pricing` to check type, base currency, variation/custom pricing and price integrity. Treat non-numeric fields as unsupported for standard price tools.
- Don't display customer addresses, email addresses, or phone numbers unless the user legitimately needs them for an authorized order-management task.

## Changes and authorizations

- Use a relevant `preview_*` tool and show the exact current and proposed values, currency, store, product/order identifier and any destructive/payment effects.
- The user's initial request to change data is **not** confirmation of the returned preview. Get a separate explicit approval before the appropriate `confirm_*` call.
- Product creation/editing/trashing use `preview_create_product` / `preview_edit_product` / `preview_delete_product` and their matching confirm tools. Price, stock and order status have specialized workflows. Refunds require extra care; never trigger a live gateway refund during a demo.
- Never change a product price using a generic product edit; do not put ranges like `59-379` into a single WooCommerce price field.
- Treat `execution_unknown` as unresolved. Use the corresponding read-only reconciliation tool where available, **never** retry a write simply because the request timed out.
- If the plugin indicates missing capability, pending review, error or unavailable tool, state this precisely. Do not claim a write succeeded based only on a preview or simulated result.
