---
name: personalize-drawing-lesson
description: Tailor a How to Draw lesson to a user's subject, experience, time, and style preferences when they ask for a personalized walkthrough. Use the app's ordered plan and SVG steps; do not claim to assess the user's sketch.
---

# Personalize a drawing lesson

1. Identify the subject and any stated experience, time, style, or medium. Ask for the subject if missing; use modest defaults for optional preferences.
2. Choose a manageable number of steps. Make each instruction one concrete drawing action, from construction to a recognizable finished subject.
3. Call `display-drawing-instructions` with the complete ordered `instructions` array. This replaces the plan stored for the chat session.
4. Explain the plan's focus and invite the user to use **Begin**. For requested steps, write a self-contained cumulative SVG with an opaque white background and dark guide strokes, then call `display-drawing-step` with `svg` and the zero-based `step_index`.
5. Adapt coaching to user feedback. If the sequence must change, call `display-drawing-instructions` with a replacement plan and restart the walkthrough.

Deliver an ordered plan and guided example images. Do not imply that the app times the lesson, reads a physical sketch, or records skill level.
