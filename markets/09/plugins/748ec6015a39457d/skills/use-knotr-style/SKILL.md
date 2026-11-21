---
name: use-knotr-style
description: >-
  Lint user-facing prose against the profile’s Knotr style guides via MCP
  check_style (Vale). Use before shipping copy, emails, docs, or marketing text
  so outputs match the user’s voice. Prefer knotr-check-style for an explicit
  lint pass.
---

# Use Knotr style checking (MCP)

`check_style` is only available when the profile has at least one **active**
style guide. Prefer this path over guessing tone from memory.

## Check loop

1. `list_style_guides` — confirm an active guide exists (`status: active`).
   If none, tell the user to activate or create a guide in knotr.ai (or use
   `create_or_update_style_guide` with `mcp_write` if they ask).
2. Optionally `get_style_guide` for editorial guidelines / source context.
3. Call `check_style` with the draft `content` (optional `format`, default
   `md`; optional `style_guide_id`).
4. Fix reported issues (line, match, message, rule, suggested fix).
5. Re-run `check_style` until clean or the user accepts remaining issues.

## When to run

- Before finalizing user-facing prose the profile should “sound like”
- After substantial rewrites of emails, docs, landing copy, or skill text
- When the user asks to match brand / style / voice

## Authoring guides (light)

Creating or regenerating Vale rules is secondary. Use
`create_or_update_style_guide` when the user wants a new guide or to change
`source_text` / regenerate. Deep Vale on-disk sync remains an optional profile
IDE zip concern—not required for MCP `check_style`.
