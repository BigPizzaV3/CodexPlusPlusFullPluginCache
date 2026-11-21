---
name: meal-plan
description: "Plan meals for the week in beckett and add the ingredients from saved recipes to the grocery list. Use when the user wants to plan meals or asks what to eat this week."
---

# Meal plan

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Start from saved recipes: search them, and use what's saved, such as prep and cook times, tags, and loved recipes, to fit the week the user describes. Fill any gaps with meal ideas.
- Create the plan with one entry per date and meal: a `recipe_ref` for a saved recipe, or a `name` for anything else.
- Add what's needed to the active grocery list: a saved recipe's ingredients by its ref, and anything else by name. Add to the existing active list even when it already has items; if several are active, use the first one listed. Build a grocery list from the plan only when no list is active.
- Confirm the plan by day in a few short lines.
