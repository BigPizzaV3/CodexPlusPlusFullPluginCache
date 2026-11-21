---
name: menu-import
description: Turns a restaurant menu from a photo, PDF, screenshot, spreadsheet or pasted text into a clean CrumbPass menu with categories, prices and diet marks, then imports it with bulk_import_menu. Use when the owner wants to add many dishes at once, digitise a printed menu, copy a menu from another source, or set up a new restaurant's menu.
license: Proprietary
metadata:
  author: crumbpass
  version: "1.0"
---

# Import a menu into CrumbPass

The connected restaurant is fixed by the owner's authorization. Every tool acts on that one restaurant.

## Steps

1. **Read what exists first.** Call `get_menu`. Note existing category and dish names so the import adds to the menu instead of duplicating it. Matching is by name, case-insensitive.
2. **Extract the menu.** From the owner's source, list each category and its dishes with name, price and description. Keep the owner's wording, spelling and order. Do not invent dishes, prices or descriptions.
3. **Normalise.**
   - Prices are numbers in the restaurant's currency: `₹350` → `350`, `350/-` → `350`. If a dish has several sizes, create one dish per size ("Pizza (Regular)", "Pizza (Large)") unless the owner says otherwise.
   - If a price is missing or unreadable, leave the dish out and list it for the owner instead of guessing.
   - Category names: short and as printed ("Starters", "Main Course", "Desserts").
4. **Set diet marks only from evidence.** Use the menu's own marks (green/red dots, "veg", "non-veg", "contains egg") or unambiguous ingredients. `isVegetarian` is required: set it true only for veg dishes. Also send `diet` (`veg`, `egg` or `nonveg`). When unsure, ask the owner. A wrong veg mark is a serious error for guests. The dish-labels skill has the full labelling rules.
5. **Confirm before writing.** Show the owner a compact summary: categories, dish count, any dishes skipped and why, and anything uncertain. Import only after they agree.
6. **Import in batches.** Call `bulk_import_menu` with at most about 40 dishes per call. Report what was created after each call.
7. **Finish.** Call `get_menu` again and summarise the result. Offer the next useful steps: labels (spice, highlights), photos, and ordering.

## Edge cases

- **Duplicates:** if a dish already exists with the same name, do not import it again; offer `update_menu_item` for price or description changes instead.
- **Combos and add-ons:** import as ordinary dishes with a clear name ("Extra cheese") only if they have their own price.
- **Hidden or seasonal dishes:** import them, then ask whether to hide any with `update_menu_item` (`isActive: false`).
- **Starting over:** `clear_menu` permanently deletes every category and dish. Show the complete current menu and obtain explicit approval before calling with `confirm: true`.

Tool details: [tool reference](references/tools.md).
