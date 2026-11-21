---
name: get-started
description: Introduces what CoPantry can do in ChatGPT and suggests a first thing to try.
---

# Getting started with CoPantry

CoPantry holds the user's household recipes, pantry, meal calendar and shopping lists. When
the user first connects it, briefly say what you can do with it, then offer one concrete
first step based on what their account already has:

- If the pantry has items, offer to suggest a meal that uses what expires soonest
  (`list_pantry`, then `search_recipes`).
- If they have recipes but no meals planned this week, offer to plan a few dinners and make
  a shopping list of what is missing (`get_meal_plan`, `plan_meal`, `generate_shopping_list`,
  `create_shopping_list`).
- If the account is empty, offer to save a recipe from a link they like
  (`import_recipe_from_url`) or to add the groceries they have at home (`add_pantry_items`).

Recipes stay in their original language; never translate a recipe's ingredients or
instructions when saving it. Ask before any tool that deletes or overwrites data.
