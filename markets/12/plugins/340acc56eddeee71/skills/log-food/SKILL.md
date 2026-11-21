---
name: log-food
description: Use when someone tells you what they ate or drank, or asks to log a meal, snack, drink, coffee, alcohol, water or supplement in Gyroscope, including "the same as yesterday's breakfast".
---

# Logging food and drinks in Gyroscope

Everything logged goes into the member's own Gyroscope account, just as if
they had typed it in the app, so a wrong entry is a real cost to them. If no
Gyroscope tools are available, follow the connect-gyroscope skill instead.

## Before logging

- Anything consumed can be logged: meals, snacks, water and other drinks,
  coffee, alcohol, supplements, vitamins, powders and electrolytes.
- When the description is clear enough to estimate (a named dish with its main
  parts, a packaged item, a drink and its size), estimate and log it.
- Accuracy is the point. Portion size, cooking method and sides move the
  numbers a lot, so when a dish varies too much to estimate well and they gave
  no detail, ask one short question first. If they answer, or tell you to just
  log it, estimate from a typical portion and log it.
- Use the member's timezone from `gyroscope_status` for each time. "Just now"
  means now, and a named meal without a time means that meal today.

## Logging

- Call `save_food` with your estimate of all four: calories, protein, carbs and
  fat. Gyroscope keeps those and adds fiber, sugar and micronutrients itself.
  If you truly cannot estimate, send the caption alone and Gyroscope analyzes
  it.
- The caption is what they consumed, in plain words, never the numbers.
- Leave `meal` out unless they named one. Gyroscope files the entry by their
  meal schedule.
- Several items eaten together are logged together, one item each.
- For a repeat of an earlier meal, find it with `load_food` on that day, then
  use `log_again` with the item id, which keeps any photo.

## After logging

- Confirm in one line: what was logged, when, and the estimate you used.
- A retry with the same details lands on the same entry, so a repeated call
  never doubles a meal.
- The connection cannot edit or delete entries. If they want a fix or a
  removal, say it is done in the Gyroscope app.
