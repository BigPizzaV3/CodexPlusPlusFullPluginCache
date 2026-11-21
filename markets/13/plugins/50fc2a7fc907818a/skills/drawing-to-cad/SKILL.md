---
name: drawing-to-cad
description: Convert a drawing, sketch, scan or logo to DXF and DWG files with TechDraw AI. Use when the user wants a file for AutoCAD, Fusion, SolidWorks, Inkscape, a laser cutter or a CNC machine.
---

# Drawing to DXF and DWG

## Steps

1. Use the image the user shared, or the link of a TechDraw AI drawing made earlier in the chat.
2. Ask how wide the drawing should be in millimetres if size matters (laser, CNC), and pass it as `width_mm`.
3. Call `image_to_dxf` with the image (free). The card lists the DXF and DWG downloads.

## Tips

- Clean black lines on white trace best. For a faint scan, lower `threshold`; for white lines on black, set `invert: true`.
- The output is traced outlines. For an editable parametric model, the user still needs a CAD program.
