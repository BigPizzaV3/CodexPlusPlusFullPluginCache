---
name: logo
description: Use when the user wants a logo, wordmark, monogram, emblem or brand mark for a business, product, channel or person, made as an SVG with SVGMaker.
---

A logo is a mark that has to survive being small, one colour and stamped on things. It is not an illustration of the business.

Ask in one message, each with a recommended answer:
- The exact name, spelling and capitals. A logo with a typo is a total loss.
- Which kind: wordmark (the name as type), monogram (initials), symbol, or symbol plus name side by side. Recommend symbol plus name.
- The one thing the mark should suggest, and any colours they already use, as hex if they have them.

Rules:
- Never invent a tagline, an industry, a city or a founding year. Only use words they gave you.
- Never ask for a mark "like" a real company's logo. Take the quality (simple, bold, one gesture), not the shape.
- Leave out anything small: a tagline set small or a "since" year will not read.

Make it with `svgmaker_generate`. The prompt: the exact name in quotes, set large, in the kind they chose; a flat, solid-fill design of one idea in 1-5 shapes; centred; one or two named colours; no gradients, shadows or thin lines; must read at 16px and in solid black.

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: icon`, `style: flat`, `color_mode: few_colors` (`monochrome` for a one-colour mark), `text_style: only_title` when the name is in the logo.

To try another direction, make a new logo with `svgmaker_generate`. To change this one (colour, spacing, one shape), use `svgmaker_edit` with its generation id.
