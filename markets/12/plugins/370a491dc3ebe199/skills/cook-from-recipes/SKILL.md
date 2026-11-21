---
name: cook-from-recipes
description: Find, save or scale a FamilyWell recipe and put the missing ingredients on a shopping list.
---

To scale a recipe, find it with `recipes_list`, then call `recipes_scale` with the servings, a total amount, or how much of one ingredient the user has. Show the scaled ingredients as a short list.

To shop for it, call `inventory_list` to see what the family already has, then `recipes_add_to_shopping` with the list from `shopping_list_shopping_lists` and only the ingredients that are missing (by position). Tell the user what was added and what was skipped.

To save a new recipe, call `recipes_create` with the title, ingredients, steps and servings.
