---
name: generate-design-tokens
description: Convert a supplied or currently selected palette into semantic design tokens, color roles, and implementation-ready CSS variables, Tailwind theme values, or design-token JSON. Use for naming palette colors, creating primitive and semantic color layers, or preparing colors for a design system. Do not use to invent a broad brand identity, extract image colors, or design an entire UI without an input palette or seed.
---

# Generate design tokens

## Establish the target

- Identify the source palette, target platform or format, theme count, naming convention, and required states.
- If no format is specified, provide a small platform-neutral token model and CSS custom properties.
- Preserve user-provided color values unless derivation is requested. Explain any generated tints, shades, or replacements.

## Model the tokens

1. Separate **primitive tokens** (value-oriented names such as `blue-600`) from **semantic tokens** (purpose-oriented names such as `color-action-primary`).
2. Create only tokens supported by a real use case. Avoid huge interpolated scales by default.
3. Cover the relevant roles: canvas, surface, elevated surface, text, muted text, border, primary action, accent, focus, and requested status states.
4. Keep semantic names stable across light and dark themes; change their mapped primitives rather than their meaning.
5. Do not use transparency to conceal an unknown composited result. When alpha is necessary, document the expected backdrop.
6. Flag high-risk foreground/background pairs for contrast verification. Do not assert WCAG conformance without calculated ratios.

## Produce artifacts

- Show a concise role-to-value mapping and then output the requested code format in a fenced block.
- Keep names syntactically valid for the target and use one authoritative value per primitive.
- Invoke `palette-picker` with the unique source and derived colors that benefit from visual editing. Order foundational neutrals first, then brand/action and status colors; explain this ordering in `reason`.
- When the user edits the palette later, remap tokens by role rather than by array position alone.

