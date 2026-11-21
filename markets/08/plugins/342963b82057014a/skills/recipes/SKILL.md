---
name: recipes
description: "Save recipes to beckett from a link, a photo, or an idea, ready to add to the grocery list, and find saved recipes. Use when the user shares a recipe link or photo, asks to save a recipe, or asks what they could make from their saved recipes."
---

# Recipes

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Save a recipe. For a link, pass it as `source_url`. For a photo or an idea, write out the name, ingredients, and steps, plus prep and cook minutes when you know them.
- Find saved recipes by name, ingredient, cuisine, tag, or `loved`.
- After saving, offer to add the ingredients to the grocery list, as the grocery-list skill describes.
