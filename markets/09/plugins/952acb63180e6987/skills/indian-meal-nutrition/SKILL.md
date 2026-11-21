---
name: indian-meal-nutrition
description: Answer what an Indian meal or dish contains (calories, protein, carbs, fat, fibre) and suggest IDYORA recipes for it, using IDYORA's published data. Use when the user asks about calories or protein in Indian food, wants to total up a meal such as "2 rotis, dal and sabzi", or asks for an Indian recipe that fits a goal like high protein or low calorie.
---

Use the IDYORA tools for every number. Do not answer from memory.

## Look up a dish

1. Call `search_food_calories` with the dish name. Try the common Hindi name in Latin script if the English name finds nothing (for example "anda curry" for egg curry).
2. If several dishes match, pick the one the user named. If it is unclear which they mean, ask.
3. Call `get_food_calories` with the slug to get values per 100 g and per typical serving.
4. Report the values exactly as returned, say whether they are per 100 g or per serving, and link the page `url`.

## Total up a meal

1. Look up each item as above.
2. Use the per-serving values when the user gave a count ("2 parathas") and a serving is returned. If no serving is returned, ask for a weight in grams, or give the per-100 g values and say so.
3. Multiply by the count and add the items. Show each line and the total so the user can check it.
4. If an item has no IDYORA page, say so and leave it out of the total. Do not estimate it.

## Suggest a recipe

1. Call `search_recipes` with a `filter` (meal, diet or goal) and, if useful, one keyword.
2. Offer two or three results with calories and protein per serving and their links.
3. Call `get_recipe` only when the user picks one or asks for the method.

## Limits

- This is general food information. Do not say a food treats, cures or prevents a condition, and do not give medication or dosing advice. For a medical question, suggest speaking to a doctor or dietitian.
- The tools are read-only. They cannot log meals, read an IDYORA account, or place orders.
- If the user gives a different instruction about format or detail, follow the user.
