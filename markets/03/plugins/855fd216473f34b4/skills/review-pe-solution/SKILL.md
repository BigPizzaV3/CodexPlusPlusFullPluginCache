---
name: review-pe-solution
description: Review a student's attempted solution to a PE Prep Pro practice item after the student commits an answer. Use to compare setup, arithmetic, units, and reasoning against the reviewed server-side explanation without inventing citations.
---

# Review PE Solution

Review the student's process after an attempt, not before it.

## Workflow

1. Require the practice item ID or a current PE Prep Pro attempt token plus the student's selected option and written work.
2. If the item is still ungraded, call `grade_practice_set` with the student's explicit answer. Never decode, inspect, or speculate about token contents.
3. Inventory the student's givens, target quantity, equation, substitutions, units, and final selection.
4. Compare only against the tool-returned correct option, explanation, sources, and revision metadata.
5. Report the earliest consequential divergence, then any downstream arithmetic or unit effects.
6. End with one corrected solution path and one short transfer lesson.

## Boundaries

- Do not invent source sections, equations, or handbook language.
- Say “not established by the supplied work” when a step cannot be verified.
- Do not equate a practice solution with a project engineering review.
- If the reviewed explanation itself appears defective, stop relying on it and submit a content issue with the user's permission.
