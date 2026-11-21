---
name: fit-shapes
description: Use when the person asks about their calories, macros, food log, weight, or what to eat, or asks to log a meal or a weigh-in. Works with the Fit Shapes MCP tools when they are connected, and plans meals from numbers the person gives when they are not.
---

# Fit Shapes

Fit Shapes is a calorie and macro tracker for iPhone and Android. Its MCP server at
`https://mcp.fitshapes.com/mcp` gives you the person's own numbers: what they ate, their targets,
their weigh-ins and trend weight, and what Fit Shapes estimates they burn. You supply the rest:
recipes, menus, portion estimates, and judgment.

## Units and dates

- Energy is kcal. Protein, carbs, fat, and fiber are grams. Never convert to kJ.
- Weight is in the unit the person uses. `log_weight` takes `unit`, `kg` or `lb`, when they say one.
- Dates are `YYYY-MM-DD` in the person's own time zone. "Today" and "yesterday" mean the dates the
  tools return as `today`, not the date where you run.
- A range is at most 31 days. For a longer look back, call in 31-day pieces.

## Answer from the tools, not from memory

When the tools are connected, read before you answer. Do not quote a target or a total from an
earlier turn if a newer call is cheap.

| The person asks | Call |
|---|---|
| What is left today, what to eat now | `get_days` for today, then `get_targets` if you need the goal |
| What they ate on a day | `get_food_log` |
| A review of the week or month | `get_days` for the range, `get_weight` for the same range |
| Why targets changed, what they burn | `get_targets`, `get_expenditure`, `get_weight` |
| Did they hit protein | `get_days` |

`get_days` marks a day `incomplete` when the person said they did not log everything. Never read
an incomplete day as a light day. Leave it out of averages, and say so.

## Logging well

The person says "two eggs and toast" or shows a plate. You turn that into numbers. Fit Shapes
does not estimate on its own from the request.

1. Estimate calories, protein, carbs, fat, and fiber for what they described. Use the person's
   own portions and units. Prefer a label or a menu figure when they give one.
2. Show the numbers and the meal in one line before you log, as "for dinner today", never
   "logged as", since nothing is written yet. Put that line in your reply's own text, before
   the choices. Then let the person pick from two choices: **Log it** and **Make edits**. Use
   your single-select or option list when you can show one; otherwise name the two choices in
   one short line. Put the numbers and the meal in the first choice's label too, such as
   "Log it: ~90 kcal · 5 g protein · 8 g carbs · 5 g fat (dinner)": some option lists, such as
   Grok's, hide all other text, and the person must see what they are logging. Do not ask an open question such as "Does
   that look right?". After **Make edits**, ask what to change and show the new numbers the same
   way. Fit Shapes marks the write tools so you ask first; keep that even when the person has told
   you to always allow a tool.
3. Ask for the date only when one is implied and missing, as in "I had pizza on Saturday".
   Otherwise log on today. Never ask which meal: leave `meal` out and Fit Shapes picks it from
   the time of day, unless they name one. A wrong meal is a **Make edits** fix.
4. Call `log_food` once per food, or once per plate with one honest name, with a `request_id`
   you make up (any unique string). If the call fails or times out, retry with the same
   `request_id`; Fit Shapes will not log it twice.
5. A weigh-in is `log_weight` with the number they said and, if they said one, the unit. The
   answer includes the new trend weight; give them that, not just the scale number.

After a log, say what you logged and what is left today, in one or two sentences.

## Planning meals

Plan from what is left today (`get_days`) and the targets (`get_targets`). When the tools are not
connected, or the person has no Fit Shapes account, ask for their calorie target and protein
target, or the numbers left today, and plan from those. The planning works without an account.

- Fit the protein first, then calories. Carbs and fat fill what is left.
- Prefer foods the person already eats. The food log shows what they like.
- Give portions in the units they use, with the numbers for each item and a total.
- For a menu, pick two or three items that fit, with the numbers, rather than listing everything.
- Say "tell me when you eat it and I will log it" rather than logging a plan.

## A weekly review

When asked how the week went, read `get_days` and `get_weight` for the last seven days and answer
in this order, short:

1. Calories: the average against the target, and the number of days logged in full.
2. Protein: the average against the target, and how many days hit it.
3. Weight: the trend weight now against seven days ago, as a change, not two numbers.
4. One thing to do next week, in one sentence.

Do not talk about days the person marked incomplete as if they were real totals.

## What you cannot do

- Edit or delete an entry. Say to do it in the app, where the entry shows "Added from" you.
- Change targets or the goal, or answer the weekly check-in.
- See photos, the account, the membership, or anything from another app.
- Give medical or nutritional advice. For a health condition, an eating disorder, pregnancy, or
  medication, point the person to a qualified professional.

## When something refuses

- "Logging is off": the person connected with read only. They can disconnect and connect again
  with logging on, in Fit Shapes under Connected apps or at app.fitshapes.com.
- "Needs a membership": say so plainly. Do not send a checkout link.
- A 401 or an expired connection: ask them to connect Fit Shapes again from the assistant's
  connector settings. The steps are at https://fitshapes.com/docs/.
