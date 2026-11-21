---
name: review-mcp-design
description: Review and improve the actual visual design, usability, accessibility and interaction states of an MCP App UI using the curated design reference library.
---
# MCP App design review

Use when users want a more polished, less generic UI, show a reference website/screenshot, or request UX criticism. UI must remain suitable for the AI host iframe and task context.

1. Get the actual implementation and rendered UI or screenshot (not just component names). Capture the desired product personality and the main task.
2. Read `../../references/design-references.md` and `../../references/design-quality.md`. Curate only sources relevant to the case; verify external licenses.
3. Evaluate hierarchy, copy, typography, spacing, affordances, information density, contrast, keyboard use, reduced motion, narrow container, dark-mode legibility, and loading/empty/error/permission/success states.
4. Find specifically reproducible problems, not abstract advice. For requested implementation, modify code with small, scoped changes while preserving tool contracts and actual event handlers.
5. Inspect the rendered result again when tools permit. Do not fabricate screenshot evidence or claim accessibility certification based on appearance alone.
6. Report substantive fixes, measured checks, and limitations; prefer an individual design direction over default purple gradients, stacked generic cards and irrelevant motion.
