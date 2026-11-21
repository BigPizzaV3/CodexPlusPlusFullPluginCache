---
name: illustration
description: Use when the user wants one illustration or scene, such as an empty-state spot, a website hero, a blog header, an editorial picture or a children's-book style scene, made as an SVG with SVGMaker.
---

An illustration is one picture with one idea in it. It has more room than an icon and no words set around it.

Ask in one message, each with a recommended answer:
- What it is for: a spot (square, simple, no background) or a hero or header (wide, with a clear side left for text). This sets the crop and the detail.
- The subject and what is happening. "A person" is a mannequin; "a person watering a plant" is an illustration.
- The look (flat, line art, cartoon, isometric, engraving, linocut) and any colours as hex. Recommend flat.

Rules:
- One main subject, clearly largest and highest in contrast; everything else smaller and quieter.
- One treatment ("flat vector, solid fills, no outlines, no gradients"), 3-6 colours with one accent kept for the main detail, light from the upper left.
- Describe screens, signs, books and notes as plain shapes ("short grey bars", "an empty panel"). Named, they come back covered in fake letters.
- Headlines and captions are set on top afterwards. Never ask for them inside the art.
- Match detail to display size: a spot shown at 200px carries no fine texture or thin lines.

Make it with `svgmaker_generate`. Settings, unless the user chose otherwise:
- Spot: `aspectRatio: square`, `background: transparent`, `composition: centered_object`, `image_complexity: illustration`.
- Hero or header: `aspectRatio: landscape`, `background: opaque`, `composition: full_scene`, `image_complexity: scene`.
- Both: `style: flat` unless they named a look, `color_mode: few_colors`.

Use `quality: high` only for a square result; high quality always comes back square.
