---
name: manage-product-feeds
description: Connect, change or delete ProductByte product sources, resolve source setup, change import schedules and inspect sources and destinations. Use for shop connections, feed URLs, Merchant Center sources and catalogue freshness; destination inspection does not create or repair a destination.
---

Use the ProductByte MCP tools from this plugin. Tool names below are the server names; use the corresponding names exposed by the host.

- Resolve the selected project with `workspace-get` when needed. Read `sync-source-list` for sources and `sync-destination-list` for destinations relevant to the request. Describe names, statuses, last completed runs and available counts.
- Connect Shopify, WooCommerce or bol through `sync-source-connect` only when the customer requests that connection. Hand over the returned ProductByte link and its hints; the customer installs or authorizes the connection themselves. Re-read sources after they finish.
- For a product feed URL supplied by the customer, use `sync-source-feed-create` with that address. For Google Merchant Center, read `sync-source-google-feed-list`, let the customer choose the feed, and pass its returned URL, language and target market unchanged to `sync-source-google-merchant-create`.
- A `waiting` source needs the customer's setup answer. Present the proposed locale and currency from `sync-source-list`; send both through `sync-source-update` after the customer accepts or supplies them. Providing both starts the waiting import, so do not do this during a read-only inspection.
- Change source names or reading frequency through `sync-source-update` only as requested, passing only changed fields and the agreed schedule. A manual schedule does not read automatically.
- When the customer asks to refresh a source, use `sync-source-import` once and read its state with `sync-source-list`. An import already running is left to finish. Respect a returned `retry_at` and report pending work without triggering repeated imports.
- Delete a source with `sync-source-delete` only when the customer asks. Its products leave the catalogue and it cannot be undone.
- A successful connection or started read is not proof that products have landed. Verify completion and catalogue availability separately with the returned last-import state and `product-search` when needed. Feed or destination counts do not establish that product search is ready; identify a discrepancy without fabricating products.
- For destinations, explain the actual delivery status, filter and last published count from `sync-destination-list`. Only a live destination is delivering. Report unavailable configuration or repair actions accurately instead of promising a destination change the tools cannot perform.
