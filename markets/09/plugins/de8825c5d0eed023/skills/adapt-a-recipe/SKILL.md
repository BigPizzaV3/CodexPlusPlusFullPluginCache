---
name: adapt-a-recipe
description: Adapt one of the user's saved ChefSense recipes, for example to suit a household member's diet, swap an ingredient, or change the servings, and save it as a new version. Use when the user asks to change, adapt, scale or make a saved recipe suitable for someone.
---

Change a saved recipe without losing the original. Every save creates a new version, and the earlier one is kept.

1. Find the recipe with `search_recipes` or `list_recipes`, then `get_recipe`.
2. If the change is about someone, such as "so Jordan can eat it", call `get_household` and use that person's diets, allergies and dislikes. Household members with their own ChefSense account don't share their diet profile, so ask the user what they need to avoid.
3. Choose how to adapt it:
   - **You rewrite it (the default):** make the changes yourself. Explain each substitution and how it affects texture, flavor or cooking time. Scale quantities sensibly; seasoning and leavening don't always scale linearly.
   - **The user asks for ChefSense to rework it:** use `iterate_recipe_start` with their instructions. If it comes back with questions, ask the user and send their answers with `iterate_recipe_answer`. Poll with an empty `answers` array until it's done. This counts toward their monthly ChefSense recipe generations.
4. Show the adapted recipe and ask before saving.
5. Save your rewrite with `update_recipe`, passing only the fields that changed and a short `change_summary` such as "gluten-free for Jordan". Ingredients and instructions are replaced as a whole when you pass them, so pass the complete list.

Point out any ingredient that commonly contains a hidden allergen, such as soy sauce (wheat) or pesto (nuts). ChefSense can't guarantee a recipe is safe for an allergy, so remind them to check labels. `undo_last_change` reverses the save.
