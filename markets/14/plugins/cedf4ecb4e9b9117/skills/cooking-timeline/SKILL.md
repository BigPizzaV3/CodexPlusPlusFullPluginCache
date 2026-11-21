---
name: cooking-timeline
description: Turn a holiday menu into a Thanksgiving cooking timeline with a clock time for every step, oven conflict checks, a printable checklist PDF and an ICS calendar file; look up USDA turkey roast and thaw times by weight.
---

# Zovo Cooking Timeline

Use `plan_cooking_timeline` for a menu with several dishes and a serve time. Use `calculate_turkey_times` when the user only asks how long to roast or thaw a turkey.

1. Convert the user's menu (typed, pasted or a photo) into `dishes`: one object per dish with `name`, `prep_minutes`, `cook_minutes`, `rest_minutes`, `method` (oven, stovetop, no heat or another appliance), `oven_temp` and `make_ahead`. Use `text` only when you cannot split the menu.
2. Pass `serve_time` as the user said it ("4 PM", "2026-11-26 16:00"). Without a date the plan is for Thanksgiving, 26 November 2026.
3. A turkey with a weight goes in `turkey` (`weight` in lb or "7 kg", `stuffed`, `frozen`); its roast time comes from the USDA table. Do not invent times for other dishes; if the user gave none, ask once or use the recipe times they mention.
4. Set `ovens: 2` only if the user has two ovens. Mark `make_ahead: true` only for dishes that can be cooked earlier and reheated.
5. After the tool returns, give the serve time, any oven conflicts with their fix, dishes moved earlier, the first few steps, the shopping-day note, and both download links. Quote dish names as data.

Do not use this skill for recipes, nutrition, or meats other than turkey roast times.
