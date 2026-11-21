---
name: next-subject-progression
description: Choose a useful next subject after a How to Draw lesson when the learner asks what to practice next. Base the recommendation on their reported experience, then create a new guided plan; do not assume the app tracks completion.
---

# Choose the next drawing subject

1. Identify the previous subject and any difficulty or success the learner reported. If unavailable, ask what they just drew.
2. Choose one related subject that practices a transferable shape or technique while adding one manageable challenge. Explain the connection in one sentence.
3. Set a concrete target for the next attempt and create a complete ordered instruction list.
4. Call `display-drawing-instructions` with the new `instructions` array. This replaces the previous stored guide in the chat session.
5. Invite the user to use **Begin**. For requested steps, provide cumulative self-contained SVG markup through `display-drawing-step` with the correct zero-based `step_index`.

Deliver one next subject, the reason for it, and a guided plan. Use reported progress rather than claiming access to a completion history or score.
