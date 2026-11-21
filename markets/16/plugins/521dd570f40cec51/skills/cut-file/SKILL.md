---
name: cut-file
description: Use when the user wants an SVG for a cutting machine such as a Cricut or Silhouette Cameo, such as a vinyl decal, iron-on design, monogram, cut lettering or a solid silhouette, made with SVGMaker.
---

A cut file is cut, not printed: the blade follows the edge of every filled shape. So it is a set of bold, closed, filled shapes with no fine lines.

Ask in one message, each with a recommended answer:
- The machine and the material. Vinyl holds detail down to about 1mm; iron-on needs 1-1.5mm, glitter iron-on 1.5-2mm.
- The finished size.
- One colour or layered. For layered, the colours in stacking order; each colour is its own sheet of material, so keep it to what they will cut.
- Any lettering, exactly as it should cut, and the font feel.

Rules:
- Lettering under about 8mm tall rarely weeds. Bold lettering can be part of the art: put the exact words in quotes. Small or thin letters: leave them out and tell the user to add them in Cricut Design Space or Silhouette Studio, then weld and attach them.
- Script letters must join into one shape; thin serifs will not weed.
- A stencil loses the middle of every O, A and B unless it is bridged. Ask if it is a stencil.
- For a silhouette, pick the pose and angle that reads: a horse side-on, legs apart, not head-on.
- Never make a mirrored file for iron-on. They switch Mirror on in their cutting software.
- The free Basic Edition of Silhouette Studio cannot open SVG. Tell Silhouette users they need Designer Edition or a DXF from another tool.

If they attached a logo or drawing, do not redraw it: run `svgmaker_convert` on the attached file. If the subject sits on a busy background, run `svgmaker_remove_background` first.

To draw a new one, use `svgmaker_generate`: "<subject>, bold solid shapes, one colour <hex>, no fine lines, no outlines, no gradients, transparent background".

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: icon`, `style: silhouette` (`flat` for a layered cut), `color_mode: monochrome` (`few_colors` for layered).
