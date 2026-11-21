---
name: food-diary
description: Food (Еда) diary workflow for meal logging, corrections, daily meal plans, diary summaries, favorites, nutrition goals, and weight progress.
---

# Food diary

Complete the requested Food task and answer in the user's language.
Food MCP results are the source of truth.

## Complete the diary task first

- Discover and use the installed Food tools by their actual names and schemas.
  Resolve the calendar date in the user's timezone. Ask only when the food
  itself is unclear or several favorites match; otherwise record directly. For usual foods, search
  `get_favs` for each product and follow pagination; reuse the selected snapshot.
  If the requested portion differs, scale its saved nutrition by the quantity
  ratio in the same unit; clarify incompatible units rather than guessing.
- Use nutrition the user states or a saved favorite holds. Otherwise look up
  typical values for the food, preparation, and portion from a reliable source
  (for example USDA FoodData Central or the product label online) and record
  them without asking. Say briefly that they are estimates and name the source.
  If the portion is missing, use a typical serving and state it. Values are per
  serving, not per 100 g. Food writes need all five nutrients; never fill an
  unknown one with zero.
- Save consumption with `record_meal`. For corrections or deletions, identify
  the entry and current revisions with `list_meals` and `read_day` before using
  `update_meal` or `delete_meal`. Preserve the tools' revision and retry rules.
  Confirm a write only after a successful result, including an identical replay.
- A successful meal write returns the updated day totals. Do not call
  `read_day` again just to show the day. Call `read_goal_progress` when
  discussing remaining intake. Use the returned totals rather than adding the
  write result to an old chat summary.
- For day reviews, read the requested day and its meal entries; for date ranges,
  use `read_nutrition_stats`. Follow pagination for complete entry lists. Report
  per-nutrient coverage, denominators, and provisional current-day status.
- A meal plan is a proposal, not consumption. Use favorites, stated values, and
  looked-up estimates to assemble it; show “План” separately from “Записано”.
  Only log planned meals when the user explicitly asks to record consumption.
  Food has no meal-plan persistence tool: do not claim that a proposal was saved.
- Use the relevant favorites, goals, or body tools for other Food tasks. Targets
  and weight plans are user choices. Preserve measured dates and coverage.

## Report confirmed data

Food returns data only and draws nothing. Answer in short text with the
confirmed entries and the day's totals; how to present them is ChatGPT's choice.

Keep unknown nutrition as “неизвестно” / “unknown”, including legacy data.
Label `knownValue` and `knownTotal` as partial known sums. Missing dates are gaps,
not zero intake. Goals use the current targets even for past dates. A calorie
budget differs from a protein target; exceeding protein is not a failure.
Never claim that all food eaten was logged.

Any chart uses only returned Food data. Keep credentials,
tokens, owner identifiers, and request IDs out of answers.

## Write safety

Never retry, undo, or repeat a successful Food write to change how the answer
looks. If a post-write read fails, keep the confirmed write and summarize its
returned items; state that day totals are unavailable rather than using stale
totals. If the write result is uncertain, resolve it using the tool's
identical-payload retry rules before claiming success; a new request ID could
duplicate food.
