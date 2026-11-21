---
name: simplify-current-lesson
description: Simplify an in-progress How to Draw lesson when the learner says the plan is too hard or detailed. Replace it with fewer, clearer actions for the same subject, then guide the user from the new beginning.
---

# Simplify the current lesson

1. Identify the subject and current plan from conversation context or model-visible `display-drawing-instructions` output. Ask for the subject only if unavailable.
2. Use the stated difficulty to choose fewer steps, simpler construction shapes, and fewer details while preserving the subject's defining features.
3. Briefly explain the adjustment and that the new plan restarts the walkthrough.
4. Call `display-drawing-instructions` with the complete simplified `instructions` array. This replaces the stored plan for the chat session.
5. Invite the user to use **Begin**. For requested steps, write cumulative self-contained SVG markup and call `display-drawing-step` with the correct zero-based `step_index` under the new plan.

Deliver a revised ordered plan and guided steps. Do not suggest the previous plan remains available through the app after replacement.
