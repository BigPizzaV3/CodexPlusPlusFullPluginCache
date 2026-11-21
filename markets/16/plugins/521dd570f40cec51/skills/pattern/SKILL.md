---
name: pattern
description: Use when the user wants a repeating pattern or tile, such as for fabric, wrapping paper, wallpaper, digital paper or a web background, made as an SVG with SVGMaker.
---

A pattern is one square tile that repeats edge to edge.

Ask in one message, each with a recommended answer:
- What it goes on: fabric, wrapping paper, wallpaper, digital paper or a web background. That sets the scale: a ditsy print has motifs under an inch, a statement print 3-6 inches.
- The motifs and the palette: which subjects, 3-5 colours as hex, and the ground colour.
- Upright motifs or tossed in every direction. Recommend tossed for fabric and wrapping paper.

Rules:
- SVGMaker cannot promise a seamless edge. Say so before making it, and tell the user to check the tile repeated before they print.
- Ask for motifs evenly spaced with none touching the edges; that tiles most cleanly.
- Flat colour, no text.

Make it with `svgmaker_generate`: "seamless repeating pattern of <motifs>, <upright or tossed>, evenly spaced, none touching the edges, flat colours <hexes> on a <ground hex> ground, no text".

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: opaque`, `composition: repeating_pattern`, `image_complexity: illustration`, `style: flat`, `color_mode: few_colors`.

To recolour it, use `svgmaker_edit` with its generation id and the new hexes, instead of making a new pattern.
