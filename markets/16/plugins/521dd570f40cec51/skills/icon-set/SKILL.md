---
name: icon-set
description: Use when the user wants a set of matching icons in one style, such as icons for a dashboard, an app, a website or a menu, made as SVGs with SVGMaker.
---

The set is the result. Twelve good icons in twelve styles is a failed set.

Ask in one message, each with a recommended answer:
- The full list of icons by name. If they only gave a theme ("icons for a finance dashboard"), propose a concrete list and get it confirmed.
- What it is for and the size it is read at. Recommend 24px UI.
- One style (outline, glyph, flat), one colour as hex.

Before making anything, tell them the set is one `svgmaker_generate` call per icon, each spending credits, and confirm the count.

Fix the shared rules once and write them as one sentence, for example: "outline icon, one even 2px stroke, rounded ends and corners, 3-6 simple shapes, front-facing, centred with even padding, no background, no text, single colour #1F2937".

Rules:
- Put that rules sentence in every prompt, word for word. Only the subject changes.
- Icons that share a subject share a base shape: user, user-plus and user-minus are the same user with the extra in the same corner.
- Two ideas that would look alike (analytics, reports) need different metaphors. Settle which is which before making them.
- Use the same settings on every icon, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: icon`, `style: line_art` (`flat` for glyph or flat), `color_mode: monochrome`.
- To fix one icon that drifted, use `svgmaker_edit` on it with its generation id and the same rules sentence, instead of making it again from scratch.

After the set, repeat the rules sentence to the user so the next icon they ask for can match.
