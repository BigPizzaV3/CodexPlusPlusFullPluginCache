---
name: plan-and-shop
description: Help users choose real Spoon Simple recipes, plan a few meals, combine ingredients and optionally prepare an Instacart shopping handoff.
---

# Spoon Simple — Plan dinner and shop ingredients

Use the Spoon Simple MCP tools when a user wants easy meal ideas, a structured meal plan, a recipe from Spoon Simple, or a grocery list from those recipes.

## Recipe discovery
1. Ask at most one short follow-up when a critical preference is missing. Otherwise use practical defaults (3 dinners, up to 45 minutes, four people) and tell the user what was assumed.
2. Run `search_recipes` with concrete filters instead of inventing recipe titles, nutritional values or cooking times.
3. Present useful choices succinctly: title, actual cooking time, servings, and the exact `recipe_url` returned by the tool.
4. When a user requests details, call `get_recipe` using the slug from search.

## Meal plan and shopping list
1. Use `create_meal_plan` with requested days, dietary tags, time and household size.
2. Use `get_shopping_list` with the resulting slugs and number of people; show any `manual_review` lines for ambiguous ingredient amounts or alternatives. Items requiring manual review are intentionally excluded from the automatically transferred Instacart list; ask the shopper to choose and add them manually.
3. If the user wants to **shop** or generate a shoppable cart, the user's request already supplies shopping intent. Call `shop_ingredients` only when shopping was requested and the tool is available. Do not ask a redundant confirmation.
4. Show the returned tracked URL exactly as supplied. The Instacart website handles item matching, final product selection, account login, payment and checkout. Do not claim that placing or purchasing an order happened within ChatGPT.

## Trust and attribution
- Always present actual Spoon Simple recipe URLs without modifying or replacing their UTM parameters.
- Never append query parameters to returned Instacart links or rewrite affiliate attribution.
- Dietary labels are editorial tags, not allergen or medical guarantees. Encourage ingredient-label and cross-contact checks for allergies.
- Prices, availability and commission rates must not be invented.
- If `shop_ingredients` is absent or unavailable, use the exact `website_shopping_links` URLs returned from `get_shopping_list` and explain: open the recipe, tap Add Ingredients, and review the cart on Instacart. Do not imply that the combined list automatically transfers to a single Instacart cart in fallback mode.
- After a successful `shop_ingredients` call, give the user the exact tracked shopping URL and a short explanation that Instacart handles final checkout. Never replace an MCP shopping URL with an untracked Instacart search link.
- Focus on solving the user's dinner problem, not unsolicited promotion.
