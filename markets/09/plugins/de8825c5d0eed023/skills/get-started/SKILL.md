---
name: get-started
description: Get started with ChefSense. Use the first time the user uses ChefSense, or when they ask what ChefSense can do.
---

The user found ChefSense moments ago and knows nothing about it yet. Their pantry and recipe book are empty. Show them what ChefSense does in one exchange: they name three things from their kitchen, and ChefSense turns them into three recipes saved to their recipe book.

1. If their first message is already a specific task, such as saving a recipe from a link, do that and skip this.
2. Make the offer in a sentence or two, for example: "ChefSense keeps track of what's in your kitchen and turns it into recipes. Tell me three things in your fridge or pantry and I'll make you three recipes with them." If they opened with a question like what to make tonight, answer it with this offer.
3. When they reply, add what they named with `add_pantry_items_bulk`. Two or five items are fine too. If they send a photo, read the items from it yourself instead of starting a scan. If they mention a diet or allergy, save it with `update_diet_profile` first so the recipes respect it.
4. Call `generate_recipe` once, with a prompt built around their items, such as "three dinners using chicken thighs, spinach and rice". That one call makes three recipes, with pictures, and saves all three to their recipe book. It uses one of their monthly ChefSense recipe generations. Tell them the recipes are on their way; it can take a minute or two.
5. Poll `list_recipes` until the three new recipes appear. For each, give the title, how long it takes and which of their items it uses. Offer to show one in full with `get_recipe`.
6. Say in a sentence what ChefSense did: their items and three recipes are saved in their ChefSense account, so they can come back to them in any chat.
7. Offer one more thing to try now: share a recipe link they love and get its shopping list, send a photo of a receipt or their fridge to see what to use first, or say what they eat or avoid so every recipe fits.

If `generate_recipe` says they've reached their limit, write three recipes yourself from the same items and offer to save the one they like with `save_recipe`.

ChefSense can't guarantee a recipe is safe for an allergy. If they mention one, remind them to check labels.
