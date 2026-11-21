---
name: groups-inventory
description: Manage Sell manual product groups and product membership, or inspect and change the supported variant stock count with concurrency protection.
---

# Organize products and inspect stock

Operation names below identify contracts, not direct conversation tools. Resolve them with `sellapp_find_merchant_tools`; call `sellapp_merchant_read` or `sellapp_merchant_write` using `{ "name": "sellapp_...", "arguments": { ... } }`. Native workspace, account, documentation and media tools remain directly callable. See the merchant operation rules for confirmation and store targeting. After a prepared result, summarize the unsaved proposal and stop. Only the user confirms it in the Merchant workspace; never confirm through a tool or click for them, including with Full Access.

Read [merchant operation rules](../../references/merchant-safety.md) and [exact tool contracts](references/tool-contracts.json).

Use `sellapp_list_groups` or `sellapp_search_groups`, then `sellapp_get_group` to inspect a manual group in the explicit store. Inspect membership with `sellapp_list_products_within_group`, `sellapp_search_products_within_group`, or `sellapp_get_product_within_group`. These are Sell's existing manual groups. This plugin does not offer smart or rule-based collections.

Use `sellapp_create_group`, `sellapp_update_group`, or `sellapp_delete_group` after presenting the store, current group, and proposed change. For membership, inspect same-store products with `sellapp_get_product`. Use `sellapp_add_products_to_group` to add selected products or `sellapp_remove_products_from_group` to remove selected products. Use `sellapp_sync_group_products` only when the user reviews the complete desired membership: replacement can remove omitted members. Every mutation prepares a preview and requires approval of the identical arguments before confirmation.

For inventory, read `sellapp_get_product_variant` and show the existing supported stock count and its meaning before proposing another value. Preserve the backend's exact zero and unlimited semantics; do not substitute zero for unlimited. Raw license-key counts are derived from serial inventory and cannot be edited by this plugin. Do not expose or manage license keys, upload digital deliverables, or alter booking capacity.

Use `sellapp_update_product_variant` with the top-level `stock` field for an existing supported variant. Send an integer count or `null` for unlimited stock, and omit `deliverable` so Sell preserves its current delivery instructions and files. Send the exact variant `updated_at` as `expected_updated_at`. Show the current and proposed counts, prepare, obtain approval, confirm, and reload. On a stale snapshot, show the fresh count and resolve the competing edit before preparing again.
