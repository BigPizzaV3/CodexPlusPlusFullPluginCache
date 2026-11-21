---
name: save-a-recipe
description: Save a recipe to the user's ChefSense recipe book from a link, a photo of a cookbook page or recipe card, or text in the conversation. Use when the user asks to save, keep or add a recipe to their recipe book.
---

Get a recipe into the user's ChefSense recipe book accurately, without duplicates.

1. Work out the source:
   - **A link:** fetch and read the page yourself, then call `save_recipe_from_url` with the `url` and the structured fields. If they already saved that link, ChefSense returns the existing recipe instead of a duplicate; tell them.
   - **A photo you can read:** read it yourself, then use `save_recipe`.
   - **The user wants ChefSense to read the photo:** use `start_recipe_scan`, poll `get_recipe_scan` until it's `draft_ready`, show the draft, and save it with `finalize_recipe_scan`, passing `edits` for anything they correct. Scans count toward their monthly ChefSense scans, so only do this when they ask for it.
   - **Text in the conversation**, including a recipe you wrote: use `save_recipe`.
2. Before saving, show the title, servings, ingredients and instructions you'll save. Ask about anything you couldn't read or that looks wrong.
3. Structure it:
   - Ingredients: one entry per ingredient with `name`, plus `quantity`, `unit` and `notes` (such as "finely chopped") where given.
   - Instructions: one string per step, in order. Call them instructions when you talk to the user.
   - Prep and cook time in minutes, if known.
   - A `source_hint` saying where it came from, such as "cookbook page".
4. Confirm it's saved and offer next steps: shop for it, or adapt it for someone in the household.

Saved recipes can be removed with `undo_last_change` straight afterwards.
