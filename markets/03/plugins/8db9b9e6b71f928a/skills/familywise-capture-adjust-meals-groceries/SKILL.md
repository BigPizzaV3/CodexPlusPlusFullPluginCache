---
name: familywise-capture-adjust-meals-groceries
description: Capture or adjust one FamilyWise meal or recipe with canonical category, structured ingredients, meal slots, pairings, add-ons, and reviewable grocery or schedule follow-through. Use when the user asks to save, correct, plan, or shop from a meal. Do not fetch arbitrary URLs or silently apply multiple writes.
---

# Capture or Adjust Meals and Groceries

1. Read saved content and run the duplicate check before a save or category correction.
2. Keep `foodCategory` separate from `mealSlots`. Ingredients are separate bounded items, never one semicolon-delimited blob. Preserve pairings and add-ons appropriate to the selected category.
3. FamilyWise does not fetch a recipe page or image URL. Use only text the user supplied or approved in this chat; direct meal-image transfer is unavailable in this connector version.
4. Preview one save or update with its exact Home and fields, then wait for explicit confirmation.
5. Re-read the saved record. Derive grocery candidates only from returned structured ingredients, preview each list change, and confirm each granular write.
6. Stop on duplicate, stale version, wrong Home, unknown result, or a protected-data request.
