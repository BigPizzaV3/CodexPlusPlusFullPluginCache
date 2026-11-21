---
name: pitch-colour-variants
description: Create, list and remove alternative colour palettes (variants) for a UiChemy project so the user can compare looks, for example a dark version or a brand-colour option for a client. Use when the user asks for colour options, an alternate palette, a dark mode version, or to compare colour schemes.
---

Use this skill when the user wants to see more than one colour direction for a site without losing the one they have.

Steps:
1. Identify the project. Call `uichemy_list_variants` to see what variants it already has before adding another.
2. Call `uichemy_get_colors` to see the colour roles of the current palette.
3. For each option the user asked for, call `uichemy_create_variant` with `projectId` and a clear `name` (for example "Deep green and cream"). Pass `colors` only when you have the exact concept colours from the tool output. Leave `colors` out to seed the variant from a built-in concept.
4. Tell the user the variants are saved next to the applied palette and that they switch between them in the UiChemy sidebar. Call `uichemy_open_preview` so they can look.
5. If the user wants a palette applied now, use `uichemy_set_palette` after you confirm which one.

Rules:
- Creating a variant does not change the applied palette. Say so.
- `uichemy_delete_variant` cannot be undone. Name the variant, ask the user to confirm, and call it only after a clear yes.
- Do not claim a colour combination is better for conversion or accessibility unless a tool result shows it.
