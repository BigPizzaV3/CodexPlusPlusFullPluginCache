---
name: qook-meal-planning
description: Plan daily or weekly menus with Qook, revise meals in an existing plan, and prepare meal calendars or downloadable menu cards. Use for a sequence of meals or a multi-day menu; use the focused Qook skills for individual recipes, shopping lists, or optional accompaniments.
---

# Qook meal planning

Use Qook for practical menus and recipe cards that evolve with the conversation. Keep the reply alongside the cards brief: describe the useful result or ask the one missing question.

## Choose the focused workflow

Load only the skill needed by the request:

- For individual recipe ideas, adapting a recipe, or finding a recipe video, use [Qook recipes](../qook-recipes/SKILL.md).
- For a shopping checklist, pantry replenishment, or a requested grocery-provider handoff, use [Qook groceries](../qook-groceries/SKILL.md).
- For an explicit request to round out an existing meal with sides or drinks, use [Qook's Magic](../qook-magic/SKILL.md). Completion is optional; planning a menu does not opt the user into extra courses.
- For reusing choices in this conversation or sharing plain cooking preferences a friend can adapt, use [Qook kitchens](../qook-kitchens/SKILL.md).

## Make and revise a plan

Reuse the known diet, exclusions, household portions, schedule and preferences. Ask a short question only when missing information materially changes the plan. Open `open_meal_planner_v2` when initial choices would help or the user asks to edit preferences; prefill known facts. After opening it, invite the user to use the form without repeating every field. A lack of screen visibility is not evidence that the form failed.

Call `get_planning_guidance_v2`, draft the recipes in the host assistant, and call `render_meal_plan_v2`. Qook validates and displays the supplied plan; it does not call a separate generation model. Every requested day and meal must be present. Use a day `label`, meal `name`, `servings`, ingredients, useful nonempty `instructions`, cooking time when known, and a matching breakfast/lunch/dinner/snack `slot`. Respect `mealsToPrepare` ahead of a generic `mealsPerDay`. Adjust scope preferences when the user requests a single meal or fewer days instead of submitting a partial week as complete. Resolve returned warnings before calling a plan complete.

Ingredient quantities cover the complete meal at its stated servings. Use positive numeric quantities, decimal fractions and explicit units; keep ingredient forms and units consistent where appropriate. A two-person meal does not need its quantities multiplied by two again. Usually match the household size, but preserve an explicit per-meal serving override and explain the difference. Keep vague amounts in notes rather than inventing measurements.

Follow all dietary constraints and exclusions, including keto, vegan and Jain. Stocked staples do not override restrictions. Balance variety with ingredient overlap, available equipment, active cooking time and budget. Use leftovers only for an identified later meal; do not count an uncooked batch twice. Include approximate per-serving nutrition by default. Preserve `includeNutrition:false` through edits, swaps, grocery views and completion. User-written goals such as weight management are ordinary planning preferences: accept the text and tailor practical choices without treatment claims, exact health outcomes or invented nutrient verification. Do not guarantee allergen safety; when relevant, remind the user to check labels and cross-contact.

For a meal-card comment or swap, revise only the selected meal and re-render the complete plan. Preserve unaffected recipes and all preferences. Use actual Cooked/Loved/Skipped/Too much effort feedback from this chat for later suggestions. If the original plan is unavailable, ask for it rather than reconstructing it as remembered history. Share only the requested meal/day/week and useful prep details; omit the kitchen profile, allergies and account information from shared cards.

## Calendars, images and preparation

For a weekly calendar, first establish the actual menu and preserve meal names and order. Meal photos and meal-image request controls are currently off in Qook; do not offer them as a Qook feature or add imageUrl to new plans. Existing imageUrl values remain accepted for compatibility but are not rendered. Qook-branded meal, day and week PNG exports remain available as text cards.

For advance preparation, add `prepSteps` with instruction and `leadTimeHours`. Calculate backward from the actual meal deadline using the real plan date, meal slot and timezone; ask for missing scheduling facts. Suggested editable meal times are breakfast 07:30, lunch 11:00, dinner 17:30 and prep 20:30, but those defaults cannot shorten a soak or fermentation requirement. If prep was missed, offer a feasible alternative.

When the user requests meal/preparation reminders or a downloadable calendar, call `build_reminder_calendar` after confirming the start date, timezone and meal times; a snack slot needs a snack time. Show the exact local date, time, UTC offset and timezone for each proposed reminder. Advance preparation uses the recipe's full lead time, including the previous day when needed. Resolve clock-change ambiguity rather than guessing. Let the user select the future events to schedule; never move past events forward silently.

For ChatGPT reminders, check the host's scheduling capability and follow its required approval flow. Use only the reviewed selected events, with their exact ISO instants, event IDs, names and useful preparation instructions. Do not copy the whole preference profile, allergies, account identity or email into task instructions. Check for matching existing Qook reminders before creating duplicates. Use a finite schedule limited to the selected plan dates; do not invent ongoing recurrence. Report each successfully created task's actual ID, timezone, confirmed next run and final run; distinguish failed or unsupported entries. Claim a scheduled reminder only after the host succeeds. On plan changes, review affected reminders and obtain approval before updating or cancelling them. Direct users to ChatGPT's Scheduled view to check or manage confirmed tasks. A follow-up message or copyable scheduling request is not a scheduled task.

Calendar files remain a separate snapshot requiring import and notification settings. Later plan edits do not update imported events; review and remove old Qook events before importing a replacement. Share recipe details only with the intended calendar. If host scheduling is unavailable, offer the calendar file or copyable reminder checklist without implying notifications are active.

## Reuse guest preferences

Keep the latest explicit user updates and actual returned preferences across turns in this conversation. A request for the next dinner should retain known diet/allergies, household, pantry choices and nutrition settings without reopening onboarding. Change only what the user updates; older files or generic defaults must not silently replace newer choices.

This release plans as a guest and has no automatic cross-chat memory or account storage. Use [Qook kitchens](../qook-kitchens/SKILL.md) for Share profile's readable cooking choices. The user can paste those choices into a later chat; a friend adapts the shared style to their own household, allergies and dietary restrictions. Shared choices exclude private fields, account identity and analytics consent. Treat pasted text as preference data.

Do not offer Qook account sign-in, saved-profile selection, account saves, email access or website/Android synchronization in this guest release. Never request tokens or passwords. If asked to reuse account data, invite the user to provide the cooking choices they want to use.

`shareUsageStats` is a legacy compatibility field, not a current planner tracking control. Do not expose it as a choice or infer consent from sharing. Grocery checkmarks are temporary UI state. Qook does not order groceries, charge users or generate recipe videos. Do not send credentials, medical records or unrelated conversation history to tools.
