---
name: familywise-plan-the-week
description: Review and plan a requested FamilyWise week using current meals, events, routines, reminders, lists, and allowed busy-time context. Use when the user asks to plan, fill, adjust, or review a week. Do not use for medical planning, unapproved calendars, or autonomous batch changes.
---

# Plan the Week

1. Call `familywise_get_meal_plan` for the requested dates and `familywise_get_planning_context` when ordinary schedules, events, or opted-in busy times matter.
2. State the exact Home, date range, freshness, missing rows, and unavailable context.
3. Propose one granular meal, component, event, list, routine, or reminder change at a time. Use only returned IDs, versions, and memberRef values.
4. Show the exact effect and ask for confirmation in a separate turn. Use a fresh idempotency key only after confirmation.
5. Re-read the changed record. Stop on conflict, wrong Home, denied role, unknown result, or any protected-data request.

Do not claim the plan found everything the family forgot and do not run in the background.
