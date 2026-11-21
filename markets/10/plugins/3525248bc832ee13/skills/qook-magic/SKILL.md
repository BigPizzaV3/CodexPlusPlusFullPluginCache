---
name: qook-magic
description: Round out an existing meal with optional sides, drinks or condiments when the user requests Qook's Magic, meal completion, or what goes with a dish. Keep the main recipes unchanged; this is separate from replacing a meal or planning a new menu.
---

# Qook's Magic

Honor the latest guest preferences and detailed dietary restrictions supplied in this conversation. Clarify contradictions before suggesting accompaniments; optional sides cannot override those restrictions.

Complete an existing meal only when the user asks. Start from the latest full plan and selected meal/day scope; ask for the plan or clarify the selected meal if it is unavailable or ambiguous. An ordinary recipe or menu request does not opt the user into sides, drinks, dessert or extra courses.

## Choose useful accompaniments

Preserve all core recipes, ingredients, servings and instructions. Reuse known diet/allergy exclusions, dislikes, household portions, budget, time and kitchen stock. A free-text goal such as weight management can guide practical choices without prescribing treatment or guaranteeing health outcomes. Goal text never outranks an allergy, dietary restriction or explicit time/budget limit.

Call `get_planning_guidance_v2` with the existing preferences and the user's goal when supplied, then draft a small useful set of accompaniments in the host. Favor complementary flavor, texture and everyday meal balance, and reuse ingredients already needed. A quick cooling side or appropriate drink may help; a meal already complete may need nothing. Do not invent a requirement for another course or automatically add all supported kinds. Keep preparation feasible, including advance work. State only a short reason such as “A cucumber side adds freshness using ingredients already on your list.”

## Merge without replacing the meal

Call `add_meal_accompaniments` with:

- `plan`: the latest complete plan, with existing preferences and recipes.
- `additions`: selected zero-based `dayIndex`/`mealIndex` pairs and the final `accompaniments` array for each selected meal.
- `goal`: the user's optional free-text goal, when provided.

Each accompaniment has a `name`, `kind` (`side`, `drink`, `condiment` or `dessert`), ingredient quantities for the whole parent meal's servings, and useful preparation `instructions`. Supply cooking time when known and optional approximate per-serving nutrition consistent with the user's nutrition setting. Avoid vague or fabricated measurements. A meal supports up to four accompaniments; that limit is not a target.

The tool replaces the selected meal's accompaniment array deterministically and preserves the core meal. Include existing approved accompaniments in the final array if the user wants to retain them while adding another. Repeating the same completion must not accumulate duplicates. Use an empty array only when the user asks to remove that meal's accompaniments. Leave unselected meals and preferences intact. The tool merges supplied content; it does not generate recipes itself.

Review the returned plan/warnings, then describe only the useful additions. Keep core nutrition separate from accompaniment estimates; do not label it a complete-meal total if any estimate is missing. Preserve `includeNutrition:false` and never turn a user goal into a health guarantee. If the user requests groceries, call `build_grocery_list_v2` with the revised full plan so accompaniment ingredients are included once at the parent meal's servings; no extra serving multiplication or unit conversion. Shared text cards and the weekly calendar should use this final plan. Meal photos and meal-image requests are currently off; do not add image URLs or promise an image board.
