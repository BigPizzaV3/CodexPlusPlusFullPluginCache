---
name: t-shirt
description: Use when the user wants artwork printed on a T-shirt, hoodie, tote bag, mug or other merch, such as a chest print, back print or shirt graphic, made as an SVG with SVGMaker.
---

The result is the print file: the artwork alone on a transparent background, not a picture of a shirt. The garment's colour is part of the design.

Ask in one message, each with a recommended answer:
- How it will be printed: screen print or vinyl means 1-3 flat colours; DTG or DTF takes full colour. Recommend flat colours when they are unsure; it prints on any press.
- The garment colour. A design for black and a design for white are different drawings.
- The placement: full front (about 12 in wide), left chest (about 3.5 in) or back.
- Any words, exactly as they must print. Never invent a slogan.

Rules:
- No black ink on a black shirt and no white on a white one. Where the shirt should show through, leave it empty.
- A short slogan can be set large as part of the graphic: put the exact words in quotes. Small text will not print cleanly; leave it out.
- Never make a mirrored file for vinyl. They switch Mirror on in their cutting software.

Make it with `svgmaker_generate`. The prompt: "bold t-shirt graphic of <subject>, thick clean outlines in <one of the ink colours>, flat solid colours <2-4 named colours>, high contrast against a <garment colour> garment, no black on a dark garment, no white on a light garment, no gradients, no shadows, transparent background". Name the outline colour every time; left unnamed it comes back black.

Settings, unless the user chose otherwise: `aspectRatio: portrait` for a full front (`square` for a chest print), `background: transparent`, `composition: centered_object`, `image_complexity: illustration`, `style: flat`, `color_mode: few_colors`, `text_style: embedded_text` only when there is a slogan.
