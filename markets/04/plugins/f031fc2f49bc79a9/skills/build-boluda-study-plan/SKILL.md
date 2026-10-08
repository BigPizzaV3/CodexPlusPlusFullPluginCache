---
name: build-boluda-study-plan
description: Build a practical study plan from the public Boluda.com catalog when users want an ordered learning path for a goal, level, deadline, or weekly time budget.
---

1. Identify the learning objective, current level, and available time. Use reasonable defaults and state them when details are missing.
2. Search for relevant courses, then inspect the selected courses with `obtener_curso`.
3. Use `buscar_clases` only when a specific topic is missing from the course-level results.
4. Select the smallest useful set of courses and classes. Avoid padding the plan with marginal results.
5. Order the path from foundations to application when the public copy supports that sequence.

Present a weekly or step-based plan with:

- The course or class and canonical link.
- The reason it appears at that point.
- A concrete learning checkpoint phrased from public catalog evidence.

Reply in the user's language. Do not invent prerequisites, exercises, lesson content, or completion data. Do not imply access to paid material; the plan describes what to study, not what the user can open.
