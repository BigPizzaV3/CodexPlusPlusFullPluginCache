---
name: first-recipe-to-shopping-list
description: Save a recipe to ChefSense for someone who has just started using it, and turn it into a shopping list. Use when a user new to ChefSense shares a recipe link, pastes a recipe or asks to save one.
---

The user found ChefSense moments ago and knows nothing about it yet. They've handed it a recipe they like. Save it, then give something back in the same reply: the shopping list for making it.

1. Save the recipe:
   - **A link:** read the page yourself and call `save_recipe_from_url` with the `url` and the recipe's fields.
   - **Text in the conversation, or a photo of a cookbook page:** read it yourself and call `save_recipe`.
2. Add the ingredients to their shopping list with `add_shopping_list_items`, with the recipe's quantities and units. Leave out basics most kitchens have, such as salt, pepper, oil and water.
3. Reply with the shopping list itself, then say in a sentence or two what ChefSense did: the recipe is saved in their ChefSense recipe book and the list is kept for them, so they can ask for either in any chat. Mention once that both are also in the ChefSense phone app, for when they're at the store. Name the basics you left off so they can ask for them.
4. Offer one more thing to try now: tell you three things in their fridge, and ChefSense will make three recipes with them.

The saved recipe can be removed with `undo_last_change` straight afterwards. Shopping list changes can't be undone.
