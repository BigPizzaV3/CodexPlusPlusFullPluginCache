---
name: use-gallery-design
description: Use one specific vibrant.design gallery design as the reference for UI work - get its DESIGN.md and build notes (analyzing it first only after the user confirms the credit cost) and build from it. Use when the user pastes a vibrant.design link, names a Vibrant design, or asks to build something "like" a design they saw on Vibrant.
---

# Use one Vibrant gallery design

Uses the Vibrant MCP server. If its tools are not available, tell the user they can connect at https://vibrant.design/dashboard/agents, then work from the page's screenshot.

## 1. Resolve the design

Pass the link's slug or short id as `projectId` (for `https://vibrant.design/p/night-hero`, use `night-hero`). If the user only described it, call `search_designs` and confirm the match with them. Then call `get_design_status projectId=…`.

## 2. Get the files

- `ready`: `get_design_md projectId=…` (save as `docs/design/<slug>.DESIGN.md`, or as `./DESIGN.md` if the user wants it as the project's design system) and `get_design_style projectId=…` (build notes, save next to it as `<slug>.build-notes.md`).
- `analyzing`: poll `get_design_status` every few seconds.
- `none` or `error`: call `analyze_design` **without** `confirm`. It returns the credit cost and the balance: tell the user both and ask. Only if they say yes, call it again with `confirm=true`, then poll `get_design_status`. If it says there is no plan or not enough credits, tell the user and stop the paid path; never retry around it. Offer to continue from the screenshot instead.

Both reads need an active plan. Without one, use the cover image and page as a visual reference and mention once that a plan unlocks the files (https://vibrant.design/pricing).

## 3. Build

- Open the media links and look at them first. Values marked inferred are estimates.
- If the project already has a design system, keep its tokens and take structure, rhythm and motion from the reference.
- Take ideas, not content: never copy its copy, logos, brand or product names, or images, and don't make a 1:1 clone. Write the copy for the user's product.
- Mobile-first, semantic, keyboard accessible, WCAG AA, `prefers-reduced-motion` respected.

To find more references in the same spirit, call `find_similar_designs projectId=…`.
