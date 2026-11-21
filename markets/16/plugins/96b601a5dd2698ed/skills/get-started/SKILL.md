---
name: woocommerce-operations-setup
description: Help merchants securely connect an authorized WooCommerce store and start read-only checks before approvals.
---

# WooCommerce Operations setup

Use the `zactra_woocommerce` MCP server to guide the merchant through connecting a WooCommerce store.

1. Begin with `list_connected_stores`. If there is no connected store, ask for the exact HTTPS storefront URL and display name, then use `start_store_connection` to generate an official WooCommerce authorization URL. Do not request WooCommerce API secrets, account passwords, or tokens in the chat.
2. After the user authorizes the connection, list only the stores owned by the authenticated account and ask which one to use when there is more than one.
3. Verify a basic read by listing products, and verify store currency using `get_store_currency` before interpreting any prices.
4. For any product price change, inspect pricing with `inspect_product_pricing` first. Do not confuse visitor-converted price displays with backend amounts. Custom product-options metadata must not be inferred or edited by generic price tools.
5. Explain that product writes, inventory changes, order status changes and refunds require a separate approval after preview. Never call confirm tools without the user's explicit approval of the exact preview.
6. Perform tests with a disposable staging store, not a live catalog or real gateway transactions. Clearly identify any unsupported custom store extension and any unverified outcome.
