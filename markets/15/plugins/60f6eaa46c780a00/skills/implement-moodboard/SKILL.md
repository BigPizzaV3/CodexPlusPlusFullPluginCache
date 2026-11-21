---
name: implement-moodboard
description: Implement a vibrant.design moodboard's design direction in this codebase - fetch its DESIGN.md and resolved direction, settle open conflicts with the user, then build page by page and section by section. Use when the user mentions their Vibrant board or moodboard, a design direction, or asks to build UI that matches a board.
---

# Implement a Vibrant moodboard

Uses the Vibrant MCP server. If its tools are not available, tell the user they can connect at https://vibrant.design/dashboard/agents.

## 1. Find the board

If the user did not give a board id, call `list_boards` and ask which one. Then call `get_build_status boardId=…`:

- No direction yet, or `direction.state` is `stale`: offer to build it. Run `analyze_board_references`, poll until `analysis.readyToBuild`, tell the user `build_direction` uses credits, and call it only after they agree. Poll until `direction.state` is `ready`.
- `direction.openConflicts` > 0: call `get_board_direction`, list each open conflict with its sides, ask the user to decide, and save each answer with `decide_conflict`. Never pick a side yourself. An unresolved recommendation is a suggestion, not an approved choice.

## 2. Install the design system

- `get_design_md boardId=…` and write it verbatim to `./DESIGN.md` (keep the YAML front matter as the first line).
- `get_board_direction boardId=… section=full` for the reasoning. Reference profiles come in pages; keep requesting the next page the header names until it says it is the last.
- If the board has groups, `get_board_direction section=sections` gives guidance per page and section. Baseline groups show what exists today; they are never the target.

## 3. Look before building

Open the media links in the direction and look at them. The prose is a summary; the media is ground truth. Values marked inferred are estimates to verify.

## 4. Build

- Saved decisions are authoritative and override any generated rule.
- Map the DESIGN.md tokens into the project's styling system once (Tailwind theme, CSS variables), then build page by page, top to bottom, section by section.
- Mobile-first, semantic, keyboard accessible, WCAG AA, `prefers-reduced-motion` respected.
- Never copy a reference's text, logos, brand names or images, and never make a 1:1 clone of one reference. Write the copy for the user's product.

## 5. Review

When done, offer a review pass: compare the UI with the direction rule by rule (layout, typography, color, spacing, surfaces, imagery, motion) and report each deviation with a suggested fix before changing anything.
