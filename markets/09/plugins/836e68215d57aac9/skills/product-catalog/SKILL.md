---
name: product-catalog
description: Use when an admin wants the Ciarem AI agent to quote products, plans or services with exact prices, or asks to add a product, a menu or a price list.
---

# Product catalog

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can change catalogs.

1. **See what exists.** Call `list_catalogs`. Add to a catalog that fits before creating a new one.
2. **Agree on the shape.** Ask what they sell and what a customer needs to know about each item (price, size, duration). Show the fields you plan to add and wait for a yes: a field's key and kind can't change later.
3. **Create it** if nothing fits: `create_catalog` with the plural and singular the user uses and a one-line `description` of what the records are, which the AI reads. Then `add_catalog_fields` (up to 15 per call; MONEY needs `currency`, DROPDOWN and MULTI_SELECT need `options`).
4. **Add the records.** One `add_catalog_record` per item, with `values` keyed by each field's `key` and written as in a spreadsheet cell ("54.75", "50 ml"). For a long list, add the first three, show them, then continue. Never invent an item or a price: ask.
5. **Let the agents use it.** Call `get_ai_setup`, then `update_agent` on each agent that should quote these items. `catalog_ids` replaces the agent's list, so pass the ones it already has plus the new one.
6. **Test.** Call `test_ai_reply` with a price question about one of the items and show the answer.

Photos and files are added on the record's page in the Ciarem web app, not from here.
