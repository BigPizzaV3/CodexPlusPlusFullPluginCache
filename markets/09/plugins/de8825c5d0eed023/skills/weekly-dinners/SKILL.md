---
name: weekly-dinners
description: Put together a week of dinners for the user's household from their ChefSense pantry and saved recipes, then add what's missing to their shopping list. Use when the user asks for dinners or meals for the week, or what to cook over the next few days.
---

Help the user decide what to cook for the next several days and get the shopping sorted.

1. Ask how many dinners they need and anything that changes the week, such as a busy night, guests or someone away. Skip this if they've already said.
2. Call `get_household`, `list_pantry` and `list_recipes`.
3. Propose one dinner per night in a short table: the day, the dish, and whether it's a saved recipe or a new idea. Plan around:
   - Every household member's diets, allergies and dislikes. Members with their own ChefSense account don't share their diet profile, so ask about them if it matters.
   - Using expiring pantry items early in the week.
   - Variety, so the same main ingredient doesn't repeat back to back.
   - Quick dishes on the nights they said were busy.
4. Let them swap dishes until they're happy.
5. Work out what to buy. For each saved recipe use `get_recipe`; for new ideas use your own ingredient list. Leave out anything already in the pantry in a large enough amount, and check `list_shopping_list` so nothing is added twice. Combine duplicates, such as onions needed by three dishes.
6. Show the list and ask before adding it with `add_shopping_list_items`. Shopping list changes can't be undone, so get a clear yes first.
7. Offer to save any new dishes they liked with `save_recipe`.

ChefSense can't guarantee a recipe is safe for an allergy, so remind them to check labels. ChefSense doesn't place orders; the shopping list is a list only.
