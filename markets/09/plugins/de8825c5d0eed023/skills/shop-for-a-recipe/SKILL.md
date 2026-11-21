---
name: shop-for-a-recipe
description: Add the ingredients a recipe needs, minus what's already in the pantry, to the user's ChefSense shopping list. Use when the user asks what they need to buy for a recipe or to add a recipe's ingredients to their shopping list.
---

Turn a recipe into the shortest useful shopping list.

1. Find the recipe:
   - A saved recipe: find it with `search_recipes` or `list_recipes`, then `get_recipe`.
   - A recipe from the conversation or a page they shared: use its ingredient list as written.
2. Call `list_pantry` and `list_shopping_list`.
3. Sort the ingredients into three groups:
   - **Already have:** in the pantry in a large enough amount.
   - **Already on the list:** on the shopping list and not checked off.
   - **Need to buy:** everything else.

   Treat staples such as salt, pepper, oil and water as "already have" unless the pantry shows they've run out. If the amount in the pantry is unclear, put the item under "need to buy" and say so.
4. Show the three groups, scaled to the servings they want if that's different from the recipe.
5. Ask before adding the "need to buy" items with `add_shopping_list_items`, with quantities and units where the recipe gives them. Shopping list changes can't be undone.

ChefSense doesn't place orders; the shopping list is a list only.
