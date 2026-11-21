---
name: repair-drawing-step
description: Repair an unclear How to Draw step when the user says an existing guide image or instruction is confusing. Explain the adjustment and show a revised SVG for the same step; rely on the user's report rather than claiming to see their sketch.
---

# Repair a drawing step

1. Locate the current `step_index`, instruction, and SVG from conversation context or model-visible `display-drawing-step` content. Ask which step is affected if it cannot be identified.
2. Identify the specific difficulty from the user's description. If unclear, ask which shape, placement, or proportion looks wrong.
3. Explain one or two actionable corrections. Preserve the stored instruction's intent and useful geometry from earlier steps.
4. Write a clearer self-contained cumulative SVG for the same step. Keep framing consistent where possible; use an opaque white background, dark strokes, and no text or labels.
5. Call `display-drawing-step` with the revised `svg` and the **same** zero-based `step_index`. Check its returned instruction matches the step being repaired. Invite a retry before continuing.

This revises the guide image, not the stored plan. For a different instruction sequence, call `display-drawing-instructions` with a new plan and explain that it replaces the current one. Do not claim to inspect the user's drawing unless it was supplied in conversation.
