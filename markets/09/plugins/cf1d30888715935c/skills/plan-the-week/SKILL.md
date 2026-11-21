---
name: plan-the-week
description: Build, check and share a small team's weekly staff schedule with Stratum Shifts. Use when someone wants to make, fix, fill, copy or publish a staff schedule, rota or roster.
---

# Plan the week

Work through the user's schedule with the Stratum Shifts tools, in this order, skipping what is already done.

1. Call `get_workplace` first. If there is no team yet, ask who works there (names, the jobs each can do, hour limits, days or times they cannot work) and what each day needs (for example two baristas 07:00 to 15:00 on weekdays). Do not invent people, roles, limits or rules; ask for what is missing.
2. Save the team with `add_staff` and the daily needs and rules with `set_up_workplace`. Remember `shifts_needed` replaces the whole pattern, so include every shift the user wants kept.
3. Fill the week with `fill_week`. Always pass `week_start`: "this", "next" or "last", or any date in the week the user means; for "next week" pass "next". `publish_week` takes it the same way.
4. Read the issues the result reports. Explain anything that is still uncovered or bends a rule, in plain words, and offer concrete fixes (who could take it, or which rule to relax). Make changes with `edit_shifts` or `update_staff` only after the user agrees.
5. When someone cannot work a date, record it first with `update_staff` (`add_time_off`), so no later fill puts them back that day. Then take them off that day's shift with `edit_shifts`, and either give it to someone the user names or run `fill_week` to find a cover.
6. When the user is happy, publish with `publish_week`. Publishing makes a link anyone with it can open, so confirm first, and confirm again before emailing staff.

Dates are YYYY-MM-DD and times are 24-hour HH:MM in the workplace's local time. A shift whose end is earlier than its start finishes the next day.

If a feature needs the Team plan, say so once, point to the plans page the tool gives, and carry on with what the current plan allows. Never push an upgrade.
