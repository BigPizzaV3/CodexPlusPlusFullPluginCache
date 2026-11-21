---
name: icon
description: Use when the user wants one icon, such as a settings, cart, app or feature icon, made as an SVG with SVGMaker. For several matching icons use the icon-set skill.
---

An icon is one idea at one weight, read at 16-48px. It is not a small illustration.

Ask in one message, each with a recommended answer:
- What it means, not just what it shows. A "settings" icon is a metaphor before it is a cog. Recommend the metaphor people already read.
- Where it is used and how big: toolbar 20-24px, feature row 32-48px.
- The style: outline (one even stroke, rounded ends), glyph (one solid shape, detail as cutouts) or flat (solid fills). Recommend outline.
- The colour, as one hex (or two for duotone).

Rules:
- 3-6 simple shapes, never more than 8. Anything that vanishes at 24px is noise.
- Centred, even padding on every side, front-facing, no text or letters, no plate behind it unless they asked.
- A reference photo is the subject, not the target. The result is an icon, never a small copy of the photo.

Make it with `svgmaker_generate`. Put every rule in the prompt: "<object> icon meaning <idea>, <style>, N simple shapes, centred with even padding, no background, no text, single colour #1F2937".

Settings, unless the user chose otherwise: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: icon`, `style: line_art` (`flat` for glyph or flat, `isometric` for isometric), `color_mode: monochrome` (`few_colors` for duotone).
