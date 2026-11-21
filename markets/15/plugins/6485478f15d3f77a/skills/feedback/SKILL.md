---
name: feedback
description: Review a Builderii board (an app flow, wireframes, a prototype, a flowchart or a sitemap) and leave clear, actionable comments on the screens and steps they're about. Use when the user asks for feedback, a design or UX review, a critique, or to check a flow on a Builderii board.
---

# Review a Builderii board

1. **Find and read it.** `search` or `list_boards` to find the board the user means, then `read_board` (and `get_diagram` for the details of a flow or app).
2. **Look for what matters,** most important first:
   - Flows: dead ends (screens or steps nothing leads out of), missing start, unreachable screens, missing error, empty and loading states, steps with no way back.
   - Screens: unclear primary action, buttons that go nowhere, labels that don't say what happens, missing fields the flow needs.
   - Diagrams: unlabelled decisions, branches that never rejoin, steps that say the same thing twice.
   - Open comments already on the board: don't repeat them.
3. **Agree first if it's big.** For more than about eight comments, list them for the user and ask which to post.
4. **Comment** with `add_comment`, one point each, pinned with `on` set to the exact text of the screen, button or step it's about. Say what's wrong and what to do: "No way back from Checkout: add a Back button to Cart".
5. **Sum up** in the chat: the two or three things that matter most, and the board's link.
