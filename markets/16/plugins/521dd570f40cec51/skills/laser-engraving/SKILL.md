---
name: laser-engraving
description: Use when the user wants artwork for a laser engraver or laser cutter such as a Glowforge, xTool or LightBurn setup, such as an engraved coaster, sign, cutting board or wood or acrylic piece, made as an SVG with SVGMaker.
---

SVGMaker makes the ENGRAVE artwork: solid black filled shapes. The cut outline and real text are added in the laser software, which every laser program does well.

Ask in one message, each with a recommended answer:
- The finished size in millimetres, the material and its thickness.
- What is engraved and what is cut. SVGMaker makes the engraved part.
- Any engraved words, exactly as they should appear.

Rules:
- Engraved text below about 2.5mm tall loses its thin strokes. Leave small text out of the art and tell them to add it in LightBurn, Glowforge or xTool.
- Bold shapes, no hairlines: thin lines burn away or vanish.
- Parts that fit together (box joints, slots, lids) need a kerf allowance measured on their own machine. Never guess a number.
- Tell them to add the cut outline as a thin red stroke and any scores as thin blue strokes in their laser software.

If they attached a logo or drawing, do not redraw it: run `svgmaker_convert` on the attached file, after `svgmaker_remove_background` if it sits on a background.

To draw a new one, use `svgmaker_generate`: "<subject>, solid black filled shapes, bold detail, no thin lines, no text, transparent background".

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: illustration`, `style: silhouette` (`engraving` for an etched look), `color_mode: monochrome`.
