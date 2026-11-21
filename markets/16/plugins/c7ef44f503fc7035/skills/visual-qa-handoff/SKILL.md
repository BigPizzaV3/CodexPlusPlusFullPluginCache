---
name: visual-qa-handoff
description: Verify a 3D website against its brief through route-by-route screenshots, responsive states, functional controls, and iterative fixes.
---

# Visual QA and Handoff

Use after implementation or when asked to review an existing 3D website. For prompt-only work, turn this checklist into measurable acceptance criteria and do not claim a visual test occurred.

## Process

1. Read the acceptance brief and build a page/state matrix covering every route, direct URL entry, representative scroll point, main interaction, mobile view, reduced motion, and 2D fallback.
2. Run the project's existing build, tests, and lint checks when available. Record exact commands/results; distinguish build success from visual and interaction validation.
3. Capture reference and implementation views at comparable viewport sizes and states when access is authorized. Compare scene composition, camera position, scale, typography, spacing, colors, materials, section transitions, overlays, controls, loading and errors.
4. Track each visible mismatch with page/state, screenshot evidence, expected result, actual result, likely cause, smallest fix, and retest.
5. Test direct navigation, refresh/deep link behavior, keyboard operation, touch controls, pause/reduced motion, form validation, preview restrictions/fallbacks, and WebGL/asset failure.
6. Fix material issues in the user's project when the user requested implementation and tools allow it. Rerun only checks relevant to changed behavior, then capture the changed state again.
7. Hand off known limitations and open defects. Do not claim exact replication, full photorealism, real-time data, mobile coverage, accessibility conformance, or a live deployment without evidence for that claim.

## Handoff

Report files and routes changed, tested viewports and states, command and browser results, unresolved issues, and whether the result is a prompt, local implementation, preview, or deployed site. Keep preview, local, deployed, and public evidence distinct.

