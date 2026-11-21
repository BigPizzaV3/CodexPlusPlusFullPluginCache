---
name: drawing-practice-sprint
description: Set up a short How to Draw practice sprint when the user wants a time-limited sketch challenge. Choose one technique focus, display a compact plan, and close with reflection; timing remains the user's responsibility.
---

# Run a drawing practice sprint

1. Use the user's subject and time limit. If omitted, choose a simple familiar subject and five minutes, and state the defaults.
2. Pick one technique focus, such as basic shapes, silhouette, or proportion. Keep the plan short, with one action per instruction.
3. Call `display-drawing-instructions` with the complete ordered `instructions` array. State the focus and invite the user to use **Begin**.
4. For requested steps, write a self-contained cumulative SVG and call `display-drawing-step` with `svg` and the zero-based `step_index`.
5. When the user reports finishing, ask for one observation about what worked and one adjustment for another attempt. Suggest a single next practice target.

Deliver a compact guided challenge and short reflection. Do not claim the app runs a timer, observes completion, or saves results.
