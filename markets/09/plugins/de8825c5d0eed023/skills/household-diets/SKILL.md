---
name: household-diets
description: Set up or update the diets, allergies and disliked ingredients of the user and the people they cook for in ChefSense. Use when the user mentions someone's diet, allergy or dislikes, or asks to update their household or diet profile.
---

Keep everyone's diet profile accurate, because every suggestion and recipe in ChefSense relies on it.

1. Call `get_household` to see who's in the household and their current diets and dislikes. Use `get_diet_profile` for the user's own profile.
2. Work out the change from what the user said, such as "Dana is vegetarian now and hates cilantro". If it's unclear who they mean or whether something is an allergy or just a dislike, ask.
3. Show the before and after for each person and ask before saving.
4. Save it:
   - **The user themselves:** `update_diet_profile` with `add_diets`, `remove_diets`, `add_dislikes` and `remove_dislikes`.
   - **Another household member:** `update_household_member` with a short `change_summary`. Diets and dislikes are **set**, not added to, so pass the complete new list: their current entries from `get_household` plus or minus the change.
5. Report what was saved. Anything ChefSense didn't recognise comes back in `skipped` or `warnings`. Tell the user and suggest the closest match.

You can update the user and the people they manage. Someone with their own ChefSense account in the household manages their own profile, so suggest they update it themselves. Diet and dislike changes can be reversed with `undo_last_change`; a whole `update_household_member` call is undone at once.

Allergies matter for safety. Record them, and remind the user that ChefSense can't guarantee a recipe is safe for an allergy and to check labels.
