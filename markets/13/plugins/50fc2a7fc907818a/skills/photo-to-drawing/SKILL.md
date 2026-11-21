---
name: photo-to-drawing
description: Turn a photo of a product, part or piece of furniture into a dimensioned technical drawing with TechDraw AI. Use when the user shares a product photo and wants a drawing, blueprint, orthographic views or a spec sheet.
---

# Photo to technical drawing

## Steps

1. Ask for one clear photo of the object if none was shared, ideally the whole object at a three-quarter angle on a plain background.
2. Ask for one or two real measurements (overall height or width) if the user knows them; the drawing is only to scale with at least one.
3. Call `generate_technical_drawing` with the photo as `image` (5 credits). Pass `measurements`, `units`, `standard` (ISO or ANSI) and `paper_size` when the user stated them, and `trade` when the object belongs to one (see the trade-drawings skill).
4. The card shows the drawing with buttons for DXF, a render and a 3D model. Keep the reply short and do not repeat the link.

## Tips

- One object per photo; crop out the rest.
- Use `views` to pick front, top, side or isometric, and `notes` for anything else, such as a material callout.
