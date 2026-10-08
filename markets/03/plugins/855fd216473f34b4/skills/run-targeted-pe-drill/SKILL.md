---
name: run-targeted-pe-drill
description: Run a focused Civil, Mechanical, or Electrical PE practice drill using PE Prep Pro's reviewed MCP questions and server-side grading. Use when a student wants a quiz by discipline, topic, or difficulty.
---

# Run Targeted PE Drill

Run a compact practice loop without leaking answers.

## Workflow

1. Resolve the exact discipline and topic with `list_disciplines`. If the requested topic is unavailable, offer the nearest returned topics.
2. Call `create_practice_set` for one to five questions. Default to three unless the student requests a different count.
3. Show questions and options exactly as returned. Preserve units and review metadata.
4. Wait for the student's committed choices. Do not calculate or critique while an item is unanswered.
5. Call `grade_practice_set` once with the matching token and an answer for every item in that token.
6. Explain each result from the returned worked explanation and sources. Distinguish arithmetic errors, unit errors, and concept errors only when supported by the student's work.
7. Offer one follow-up drill or one concept brief; avoid an open-ended sequence unless requested.

## Rules

- A token expires and is revision-bound. Create a new set rather than reconstructing a token.
- Do not place answers in an ungraded prompt, hint, title, or recap.
- Do not claim NCEES endorsement or reproduce protected handbook, code, or standard text.
- Use `report_content_issue` for suspected factual, calculation, citation, ambiguity, or typo problems.
