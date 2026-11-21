---
name: cook-with-what-i-have
description: Suggest meals from the user's ChefSense pantry, using up what's expiring first. Use when the user asks what they can cook or make with what they have, or how to use up food before it goes off.
---

Help the user cook from what's already in their kitchen, starting with what's about to expire.

1. Call `list_pantry` and `get_household`. Note the items with the nearest expiry dates and everyone's diets, allergies and dislikes. Members with their own ChefSense account don't share their diet profile, so ask about them if they're eating too. If the pantry is empty, follow the `get-started` skill instead.
2. Check what they already know how to make: `search_recipes` with the expiring ingredients, or `list_recipes`.
3. Suggest two or three dishes. For each, say which expiring items it uses, what else it needs from the pantry, and anything they'd have to buy. Prefer saved recipes that fit; otherwise suggest your own ideas.
4. If they pick one:
   - A saved recipe: show it with `get_recipe`.
   - Your own idea: write it out. If they want to keep it, save it with `save_recipe`.
   - If they ask for ChefSense to come up with a recipe, use `generate_recipe`. It runs in the background and counts toward their monthly ChefSense recipe generations, so only use it when they ask.
5. After they've cooked, offer to update the pantry: `update_pantry_item` for partly used items, `remove_pantry_item` for anything used up. Ask before changing anything.

Leave out any dish that breaks someone's diet or includes an ingredient they dislike, and say why if it was an obvious choice. ChefSense can't guarantee a recipe is safe for an allergy, so remind them to check labels.
