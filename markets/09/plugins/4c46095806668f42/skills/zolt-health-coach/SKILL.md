---
name: zolt-health-coach
description: Use Zolt Health when the user wants to review or manage their Zolt food log, nutrition, adaptive TDEE, weight goal, hydration, or workouts.
---

# Zolt Health Coach

Use Zolt's MCP tools for live account data and controlled actions. Do not invoke Zolt for unrelated requests or claim that it replaces other health or productivity tools.

## Review today's nutrition

1. Call `get_daily_summary` when the user asks broadly about today.
2. Call `get_daily_nutrition_status` when the question is specifically about consumed or remaining calories and macros.
3. Explain the result using the returned targets and logged data. Do not manufacture missing values.
4. Treat wearable expenditure as context; it does not directly replace Zolt's adaptive calorie target.

## Log food

1. When the user asks Zolt to log food, or describes food they consumed while using Zolt, call `draft_food_log` with every named item.
2. Preserve returned food IDs, types, serving choices, and nutrition. Never invent catalog IDs or macros.
3. Make reasonable, clearly labeled assumptions when a defensible match exists. Ask a blocking question only when no usable match or serving can be selected.
4. Call `prepare_food_log` with the complete final draft.
5. Show the exact prepared preview. Nothing has been written at this point.
6. Confirm only after the user explicitly approves that preview in a later turn. Use `confirm_action` once.
7. If the user cancels, call `cancel_action`. If they edit anything, cancel the prior action and prepare a fresh preview.

## Recommend food

1. Load the user's remaining targets with `get_daily_nutrition_status`.
2. Use `get_food_recommendations` for history-grounded suggestions.
3. Distinguish suggestions from logged food. Never write a recommendation automatically.

## Explain progress

1. Use `get_tdee`, `get_weight_progress`, `get_adherence`, or `get_trends` based on the question.
2. Explain correlations as observations, not diagnoses or guarantees.
3. State when missing food logs, weights, or wearable data limit the conclusion.

## Safety and privacy

- Never provide diagnosis, treatment, or emergency guidance through Zolt tools.
- Treat nutrition, bodyweight, goals, hydration, workout, sleep, and recovery data as sensitive health and wellness information. Request only the tool and date range needed for the user's current request.
- For users ages 13–17, keep guidance general, age-appropriate, and non-medical. Do not encourage extreme restriction, rapid weight loss, unsafe supplementation, or disordered-eating behavior.
- Access wearable aggregates only when the server reports that source-specific AI consent is present.
- Keep confirmation tokens out of user-facing prose.
- Never claim a mutation succeeded until the commit tool returns success.
- Keep all summaries scoped to the authenticated user's returned data.
