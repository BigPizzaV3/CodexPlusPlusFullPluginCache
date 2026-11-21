---
name: online-test-prep
description: Find the user's applications at the online test or interview stage and gather Tradermaths prep resources for each. Use when the user asks what tests or interviews are coming up or how to prepare for a firm.
---

1. Call `list_board` with `status` set to the online test stage (and again for the interview stage if the user asks about interviews).
2. For each role, call `get_prep_resources` with its `role_ref` (and `stage` if known). For a firm the user hasn't tracked, pass `firm` instead.
3. Reply with one short section per role: firm and role, current stage, and the prep links returned. Only use links the tool returned; don't invent resources or test dates.
4. If nothing is at these stages, say so and offer the weekly application review instead.
