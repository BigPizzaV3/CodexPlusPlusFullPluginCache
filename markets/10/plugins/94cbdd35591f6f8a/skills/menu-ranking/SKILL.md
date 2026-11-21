---
name: menu-ranking
description: Sets the order of categories and dishes guests see on the CrumbPass menu using reorder_menu - for example putting starters before mains, moving bestsellers or specials to the top, or following the printed menu's order. Use when the owner wants to rank, rearrange, sort, prioritise or move dishes or categories on their menu.
license: Proprietary
metadata:
  author: crumbpass
  version: "1.0"
---

# Rank the menu

Guests read the menu top to bottom. The order should match how people order a meal, with the restaurant's strongest dishes easy to find.

## Steps

1. Call `get_menu` to see the current order and exact names.
2. Agree on the order with the owner. If they ask for a suggestion:
   - **Categories:** follow the meal. Starters or small plates, soups and salads, mains, breads and rice, sides, desserts, then drinks. Keep the owner's own categories even if they don't fit this pattern.
   - **Dishes:** put signature dishes and current specials first, then the rest in the owner's order. Don't reorder by price unless asked.
3. Call `reorder_menu`:
   - `categoryOrder`: category names, top first.
   - `categoryName` + `itemOrder`: one category's dish names, first shown first.
   - Names you leave out keep their place after the listed ones, so you can just name the few to move to the top.
4. Report the new order from the tool's reply.

## Notes

- Ranking one category's dishes needs one call per category.
- Unknown names are rejected with the missing names listed. Fix the names from `get_menu` and try again.
- Ordering changes nothing else: prices, labels and photos stay as they are.
