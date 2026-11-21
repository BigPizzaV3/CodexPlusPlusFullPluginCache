---
name: mood-board-font-pairing
description: "Compare and recommend Google Font heading and body pairings for Mood Board when the user wants typography that fits an existing board or a stated visual mood. Preview families and explain their roles and tradeoffs. Do not use for uploading custom fonts, building a complete UI theme, arbitrary specimen text or layout control, or licensing conclusions without verified sources."
---

# Mood Board Font Pairing

## Inputs

Use the board or stated mood, the intended medium and audience, any required
language or script, and fixed font families or palette colors. Prefer the latest
model-visible board contents when available.

## Workflow

1. Identify the typography goal in plain language, such as quiet editorial
   headings with approachable body text. Retain fixed families and colors.
   Ask about language or reading needs only when they would change the choice.
2. Propose two heading and body pairings. Make the pairs differ in a meaningful
   way while supporting the same brief. Prefer established Google Fonts families
   and explain why each family suits its role.
3. When family availability, script coverage, or licensing matters and is
   uncertain, verify it using available official Google Fonts sources. If
   verification is unavailable, state what remains unverified rather than
   promising coverage or licensing terms. Do not infer these from a preview.
4. Render a dedicated comparison board through `display-mood-board` when a
   visual comparison is wanted. Use four `font` items with only `type` and
   `family`, two `note` items naming each pairing and its roles, and optionally
   the existing `palette`. Keep `moodBoard.items` at ten or fewer, follow the
   registered schema, and use an optional `reason`.
5. Read the returned `structuredContent.moodBoard`. Explain the heading and body
   contrast, fit with the board, and the likely reading tradeoffs. Distinguish
   the widget's family preview from testing actual text at production sizes.
6. Recommend one pairing and give concise usage guidance. When the user wants
   to apply it to an existing board, render the complete retained board only
   when it fits the tool contract and uses reusable image sources. Otherwise
   guide the user to change or add font cards in the existing widget.

## App use and limits

- Use exact Google Fonts family names. Leave weights, sizes, custom sample text,
  typography roles, and grouping labels out of `font` tool arguments; put role
  guidance in notes or the conversation.
- Use a `palette` only when its supplied colors are known, retaining their exact
  six-digit hex values and at least two colors. Do not invent an existing palette
  from unseen imagery.
- Let the widget load previews from Google Fonts. Its font catalog is a
  client-side feature; do not claim to query it through an app tool or request
  its API key. A manual family name remains usable without catalog suggestions.
- Treat any new rendering as a board with fresh UUIDs. Do not promise to retain
  positions, private upload mappings, or export details, and never silently trim
  an existing board to the ten-item input limit.
- Leave `resolve-mood-board-images` to the widget. Do not call the app-only helper
  or assume that private state or file-ID-to-source mappings are visible.

## Deliverable

Provide the comparison previews when requested, the recommended heading and body
families, their intended roles, and any unresolved coverage or implementation
choices. For text-only requests, return the comparison without calling tools.
