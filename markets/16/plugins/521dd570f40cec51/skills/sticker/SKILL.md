---
name: sticker
description: Use when the user wants a printable sticker, a die-cut sticker, or a pack or sheet of matching stickers, made as an SVG with SVGMaker.
---

A sticker is printed and then cut. The shape has to cut cleanly, so it is one compact piece with a border around it.

Ask in one message, each with a recommended answer:
- One sticker or a pack. For a pack, the count (recommend 6; 12 is the most on one sheet) and the list of subjects: one main piece and the supporting ones.
- The size. Recommend 3 in for one sticker, 1.5-2 in each for a pack. Under 1 in the art must be one bold shape.
- The style and 4-6 colours.
- Any words, exactly as they should print. No words given means no word stickers; never invent slogans.

Rules:
- Every sticker: one compact connected shape, no floating bits, nothing thin at the edge, thick dark outline, flat bold colours, a thick white border around the whole shape.
- Words sit well inside the edge. Small words will not print cleanly; leave them out.
- A drawn QR code or barcode never scans. Do not draw one.
- The file has no separate cut line. Tell the user most print shops and Cricut Print Then Cut make one from the outline of a transparent PNG.

Make it with `svgmaker_generate`.
- One sticker: "sticker illustration of <subject>, one compact connected shape, thick dark outline, flat bold colours <palette>, thick white border around the whole silhouette, no text, transparent background".
- A pack: make four stickers at a time in a grid, with the same rules sentence and palette in every prompt. Separate prompts with different wording drift into different styles. Say how many calls it takes before starting.

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object` (`objects_in_grid` for a pack sheet), `image_complexity: illustration`, `style: cartoon`, `color_mode: few_colors`.
