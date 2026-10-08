---
name: stowra-trip-loadouts
description: Plan and manage Stowra trip loadouts, including packing-list gear, sections, participants, readiness, packing status, and weight summaries. Use for a specific trip or packing list; do not use for general travel, route, or weather advice.
---

# Stowra Trip Loadouts

A loadout is a trip-specific packing list. Use Stowra as the source of truth and never invent loadout, section, profile, gear, or line IDs.

## Resolve the trip and related records

- Use `list_loadouts` to find the trip and `get_loadout` to inspect its sections, participants, and lines before changing it.
- Resolve named gear with `list_gear_items` and named people with `list_profiles`. Profiles represent people in the workspace, not login accounts.
- Ask the user to choose when several loadouts, gear items, sections, or profiles plausibly match.

## Build the packing list

- Use `create_loadouts` for new trips, preserving omitted dates or descriptions instead of inventing them.
- Use `update_loadouts` for an existing trip's name, description, dates, or status while preserving omitted fields.
- Add individual gear with `add_loadout_items`. When the user wants a whole reusable kit, resolve it with `list_kits` and `get_kit`, then use `add_kit_to_loadout`.
- Add organization with `add_loadout_sections`. Set `containerGearItemId` only to a resolved gear item that represents the physical container.
- Add people with `add_loadout_participants`, then use `update_loadout_participants` only for readiness changes.

## Update or remove trip data

- `update_loadout_items` and `remove_loadout_items` require loadout-line IDs from `get_loadout`, not gear-item IDs.
- Updating several loadout lines applies the same supplied values to each one. Preserve omitted fields.
- Use `update_loadout_sections` for section labels, order, or containers. `remove_loadout_sections` keeps the section's lines but leaves them outside any section.
- Use `remove_loadout_participants` only for the resolved profiles. Their profiles remain in the workspace, and existing line assignments are preserved.
- Removing a loadout line does not remove the underlying gear.
- `delete_loadouts` moves trips to trash and leaves inventory gear intact. `restore_loadouts` requires an ID retained from the delete result or earlier context.
- Never broaden a destructive request beyond the exact trips, lines, sections, or participants the user identified.

## Explain weight and readiness

- Use `list_loadout_weights` for total and base weights. Values are in milligrams; convert units for presentation only when useful and retain exact values when precision matters.
- Base weight excludes worn and consumable items. `unknownCount` means the totals are understated; do not treat unknown weights as confirmed zeroes.
- After multi-step changes, use `get_loadout` when the user needs the final organized packing list.

## Report the outcome

Summarize the trip state, changed records, skipped or failed operations, packing/readiness status, and any weight caveats. Include the returned batch ID for writes. If the user asks to reverse a change, call `undo_batch` with that exact batch ID; never guess a batch.
