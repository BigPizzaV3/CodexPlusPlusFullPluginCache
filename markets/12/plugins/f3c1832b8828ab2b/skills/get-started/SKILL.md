---
name: get-started
description: How to use the Aptiva tools for the user's workout program, custom workouts, activity logs and meal plan.
---

# Using Aptiva

Aptiva connects to the user's own Aptiva fitness account. Every tool acts only on the signed-in user's data.

## When to use which tool

- Today's plan or progress: `get_program_status`, then `get_my_workout_program` for the full schedule.
- Change a day: `update_program_day`. Finish a program: `complete_program`, then `generate_workout_program` and poll `get_program_generation`.
- One-off workouts: `list_all_exercises` and `list_all_workouts` for the catalogue, `create_custom_workout` to save one, `modify_workout` to shorten or adapt it.
- Activity: `log_weight`, `log_hydration`, `log_mood`, `get_activity`.
- Food: `get_nutrition_today`, `log_food`, `log_planned_meal`, `swap_meal`, `generate_meal_plan`.

## Rules

- Ask before replacing an active program or meal plan; those tools confirm before overwriting.
- Program and meal-plan generation are Premium features. If a tool returns `subscription_required`, show the message and link and stop.
- Never give medical diagnoses. Suggest the user consult a professional for pain or injury.
