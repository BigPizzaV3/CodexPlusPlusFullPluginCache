---
name: dish-labels
description: Sets the guest-facing labels on CrumbPass menu dishes - veg, egg or non-veg diet marks, spice level, served hot or cold, Chef's special, Today's special and Special highlights, an offer on the dish, and an info note for allergens or pairings - using create_menu_item, bulk_import_menu or update_menu_item. Use when the owner wants to mark dishes as spicy, veg or non-veg, add specials, put an offer on a dish, add allergen or info notes, or tidy up how dishes are labelled.
license: Proprietary
metadata:
  author: crumbpass
  version: "1.0"
---

# Label dishes for guests

Guests decide what to order from these labels, and some guests rely on them for diet or allergies. Accuracy matters more than completeness.

## Rules

1. **Diet marks come from facts, never guesses.**
   - `veg`: no meat, fish or egg. `egg`: contains egg but no meat or fish. `nonveg`: contains meat, poultry or seafood.
   - If a dish name or description doesn't settle it, ask the owner. Never mark a dish `veg` to be safe.
   - Setting `diet` also sets the older `isVegetarian` flag (only `veg` counts as vegetarian).
2. **Allergen notes only from the owner.** Put allergen information in `note` only when the owner states it. Do not infer allergens from a dish name. If useful, suggest "Ask the team about allergens."
3. **Spice:** `1` mild, `2` medium, `3` hot. Use the owner's or menu's own indication; leave unset when unknown.
4. **Temperature:** set `hot` or `cold` only when it helps a guest choose (cold desserts, hot soups). Leave it unset otherwise.
5. **Highlights:**
   - `chefs_special` for the kitchen's signature dishes, `todays_special` for something available today only, `special` for anything else the owner wants to spotlight.
   - Keep highlights rare (a few per menu), or they stop meaning anything. Suggest removing stale `todays_special` labels.
6. **Offer on a dish:** `offerNote` is a short promise guests read ("20% off at lunch", "Free drink with this combo"). Use only offers the owner states, keep it under 80 characters, and include conditions. To clear it, send an empty string.
7. **Info note:** up to 280 characters for allergens, pairing, portion size or preparation. Plain sentences, no marketing claims the owner hasn't made.

## How to change labels

- **One dish:** show the owner the current label and proposed value, ask for approval, then call `update_menu_item` with `itemName`, only the labels to change, and `confirm: true`; everything else is kept.
- **Clearing:** `spiceLevel: 0`, `highlights: []`, `offerNote: ""` or `note: ""`.
- **Many dishes:** list every planned label change and get approval first; update them one at a time with `confirm: true`, and summarise what changed at the end.
- **New dishes:** include labels directly in `create_menu_item` or `bulk_import_menu`.

Every `update_menu_item` call requires `confirm: true` after the owner approves the exact displayed change. Do not call it as a preview.
