---
name: log-meals
description: Log what the user ate to Ziva with accurate USDA matches and portions. Use when the user describes a meal, snack, or drink to record, asks to log a saved meal or recipe, or wants to correct a meal that is already logged.
---

Log food with the Ziva tools so the totals the user sees are trustworthy.

For each food item in a new meal:

1. Search with `search_usda_foods` using standard food labeling terms and no quantities. For "2 cups rice", search "rice".
2. If the results look irrelevant, simplify the query and search again. For "grilled chicken thigh", try "chicken thigh".
3. If there is still no relevant USDA match, use quick entry (`type="quick"`) with estimated macros. Quick entry is a fallback for foods with no USDA match, or for custom foods with known macros such as homemade sauces or restaurant items with published nutrition.
4. For matched items, choose the portion closest to what the user described.
5. Before calling `log_meal`, check that portion × quantity gives reasonable calories. A single item over 800 calories, or a snack over 1,200, usually means the wrong portion was chosen.
6. Call `log_meal` once with all of the verified items.

To log a saved meal or recipe, call `get_saved_item` first to get the full ingredient list. Then log each ingredient as returned: USDA ingredients with their `fdcId`, `portionId`, and `quantity`, and quick ingredients with their macros.

To change a logged meal, call `log_meal` with every item in the meal, not only the changed ones, because an update replaces the full item list.

Ziva records food and reports nutrition totals. Don't give medical advice or medication doses; if the user asks for that, suggest they ask their clinician.
