---
name: review-plan
description: Check a Simple House Planner plan against the planning conventions and its warnings, and list the fixes before making them. Use when someone asks whether a plan works or what to improve.
---

# Review a plan

Tools: `list_projects`, `describe_plan`, `query_project`, `edit_project`.

1. Find the plan with `list_projects` if the person did not name one in this chat, and call `describe_plan` for every floor.
2. Check the facts and the warnings: every room is enclosed and reachable, bedrooms and bathrooms have sensible areas, habitable rooms have a window, hallways are at least 1000 mm wide, a stair reaches each upper floor, no furniture stands in the way through a door or in front of a window, and closets, appliances and toilets have 600 mm free in front.
3. Use `query_project` for questions the description does not answer, for example the free length of a wall.
4. List the problems and the fixes in plain words, and ask before you change the plan with `edit_project`.

These checks are design aids, not proof that a building meets the law.
