---
name: text-to-drawing
description: Draw a part from a written description with sizes using TechDraw AI, such as a bracket, plate, flange or shelf. Use when the user describes a part in words instead of sharing a photo.
---

# Description to technical drawing

## Steps

1. Make sure the description has the main sizes: overall dimensions, thickness, and the size and position of holes or cutouts. Ask for any that are missing rather than guessing.
2. Call `text_to_technical_drawing` with the description as `prompt` (5 credits). Set `units`, `standard` and `paper_size` if the user named them.
3. The drawing is true to size, so the DXF from it can go straight to a laser cutter or CNC. Offer that as the next step.
