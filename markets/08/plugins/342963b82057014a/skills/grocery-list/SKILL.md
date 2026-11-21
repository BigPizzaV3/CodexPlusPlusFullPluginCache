---
name: grocery-list
description: "Add items to the beckett grocery list, check them off, and read the list back. Use when the user mentions groceries they need or have picked up, or asks about their grocery list."
---

# Grocery list

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Find the active grocery list, with status `active`. Add to it even when it already has items. If several lists are active, use the first one listed, which is the most recently updated. Create a list only when the user asks for a new one or none is active.
- Add items by name. For a saved recipe, add its ingredients by the recipe's ref so they come in with quantities.
- For a meal that isn't saved as a recipe, work out the ingredients it needs, then add them by name.
- Check items off, and read the list back when asked.
