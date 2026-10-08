---
name: stowra-gear-inventory
description: Inspect and organize a user's Stowra gear inventory, including item details, weights, stock, tags, updates, trash, and restore. Use for requests about gear the user owns or tracks; do not use for general shopping advice or trip planning alone.
---

# Stowra Gear Inventory

Use Stowra as the source of truth. Never invent record IDs, weights, prices, tag IDs, or inventory facts.

## Resolve the target

- Start with `list_gear_items` when identifying an item, checking for duplicates, or reviewing inventory.
- Use `get_gear_item` when full details, photos, tags, or sports are needed.
- If several records plausibly match, show the candidates and ask the user which one they mean before writing.

## Create or update gear

- Before `create_gear_items`, search for likely duplicates. Create only the items the user actually requested.
- Weights use milligrams. Do not estimate a missing weight. Use `weightSource: "measured"` only for a user-measured value and `"manufacturer"` for a documented specification.
- `update_gear_items` applies the same supplied fields to every selected ID. A name can be changed only when exactly one ID is supplied.
- A weight update must include both `weightMg` and `weightSource`; never infer the provenance of an existing weight.
- Preserve omitted fields. Do not fill optional brand, model, category, price, stock quantity, or notes from assumptions.

## Manage tags and removal

- Use `add_gear_item_tags` to attach an existing tag and `remove_gear_item_tags` to detach one.
- Both tools require an existing `tagId`. The current MCP surface cannot list or create tags. If no trustworthy tag ID is available from prior results or the conversation, explain that limitation instead of inventing one.
- `delete_gear_items` moves gear to trash; it does not delete kit or loadout lines. `restore_gear_items` requires an ID retained from the delete result or earlier context because trashed gear is hidden from listing.
- Never broaden a destructive request beyond the item IDs the user identified.

## Report the outcome

Summarize what was read or changed, call out failures or ambiguous matches, and include the returned batch ID for writes. If the user asks to reverse a change, call `undo_batch` with that exact batch ID; never guess or substitute the most recent batch.
