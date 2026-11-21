---
name: image-to-svg
description: Use when the user has a PNG, JPG or WebP, such as a logo, drawing, clipart, sticker or photo, and wants it as an SVG, with its background removed, or changed. Picks between converting, removing the background and editing.
---

Pick the tool by what the user wants done to their image:

- Keep it as it is, just as a vector: `svgmaker_convert` on the attached file. This traces the image; it does not redraw it.
- Cut the subject out: `svgmaker_remove_background` on the attached file. It returns the cutout as an SVG, so do not convert it afterwards.
- Change what it shows (colours, a new element, a different style): `svgmaker_edit` with the attached file and a prompt that says exactly what changes and what stays the same.
- Their image is an SVGMaker result from earlier in the chat: `svgmaker_edit` with its generation id. `svgmaker_convert` does not take generation ids, because those are already SVGs.

Rules:
- Use the file the user attached. If there is none, ask them to attach it.
- Ask only when it is unclear whether they want it traced as it is or changed. Recommend tracing as it is.
- A photo traced as a vector becomes flat colour regions and loses fine texture. Say so before converting a photo, and offer an illustrated version with `svgmaker_edit` instead.
- For a logo, the cleanest trace comes from a large, sharp image on a plain background. If theirs is small or blurry, say the result may lose detail.
- One step at a time: run the first tool, show its card, then run the next on that result.
