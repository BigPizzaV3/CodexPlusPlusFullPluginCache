---
name: stowra-kit-builder
description: Build and maintain reusable Stowra gear kits, or copy a kit into a trip loadout. Use when the user wants a reusable bundle such as a sleep system, first-aid kit, or activity setup; do not use for a one-off packing list with no kit workflow.
---

# Stowra Kit Builder

A kit is a reusable bundle, not a trip. Use Stowra records as the source of truth and never invent kit, gear, line, loadout, or section IDs.

## Resolve the kit and gear

- Use `list_kits` to find candidate kits and `get_kit` to inspect a kit's current lines before changing it.
- Use `list_gear_items` to resolve the gear the user names. If a required item does not exist, ask whether to create it with `create_gear_items`; do not silently create substitutes.
- If several kits or gear items match, ask the user to choose before writing.

## Build and maintain kits

- `create_kits` creates empty reusable bundles. Add existing gear with `add_kit_items` only after resolving each gear item ID.
- Use `update_kits` to rename a kit or change its description while preserving fields the user did not mention.
- Quantities and classifications belong to kit lines. Use `get_kit` before `update_kit_items` or `remove_kit_items`, because those tools require kit-line IDs rather than gear-item IDs.
- `remove_kit_items` permanently removes the selected lines unless its returned batch is undone; it does not remove the underlying gear.
- `delete_kits` moves the bundle to trash while leaving gear untouched. `restore_kits` requires an ID retained from the delete result or earlier context because trashed kits are hidden from listing.
- Never broaden an update or removal beyond the lines or kits the user identified.

## Copy a kit into a trip

- Resolve the source with `get_kit` and the destination with `list_loadouts` or `get_loadout` before calling `add_kit_to_loadout`.
- Supply a section ID only when the destination section has been resolved from `get_loadout`.
- Copying creates loadout lines that remember their source kit; later kit changes do not alter an already packed trip.
- Report any skipped kit lines. Trashed gear is skipped rather than copied, and an empty or fully skipped kit cannot be added.

## Report the outcome

Summarize the resulting kit or copied loadout lines, distinguish line IDs from gear IDs, and include the returned batch ID. If the user asks to reverse a change, call `undo_batch` with that exact batch ID; never guess a batch.
