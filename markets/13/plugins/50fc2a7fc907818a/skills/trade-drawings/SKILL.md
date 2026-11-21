---
name: trade-drawings
description: Make a trade-specific drawing from a photo with TechDraw AI: furniture shop drawings, garment technical flats for a tech pack, machined parts with tolerances, sheet metal with bend lines and a flat pattern, woodworking plans, or parts to 3D print. Use when the user names one of these trades or the photo clearly belongs to one.
---

# Drawings for a trade

`generate_technical_drawing` takes a `trade` that drafts to that trade's conventions. Pick it from the object, not from keywords.

| trade | Use for | What the drawing carries | Good next step |
| --- | --- | --- | --- |
| `furniture` | tables, chairs, cabinets, shelves | overall sizes, part sizes, joinery, material | DXF, render, 3D model |
| `clothes` | a garment laid flat | front and back flats, seams, topstitching, closures, measurement callouts | render |
| `machine-parts` | machined or cast parts | tolerances, hole and thread callouts, sections, finish | DXF, 3D model |
| `sheet-metal` | brackets, panels, enclosures | thickness, bend lines and radius, flat pattern | DXF for the laser or plasma table |
| `woodworking` | jigs, shelves, boxes, CNC projects | every board as thickness × width × length, joinery, screw positions | DXF for the CNC router |
| `3d-printing` | a printed part, or a part to remake | functional sizes, wall thickness, holes, bed face | 3D model (GLB and STL) |

## Steps

1. Get one clear photo of the object and, if the user knows it, one real measurement.
2. Call `generate_technical_drawing` with `image`, `trade` and any `measurements` (5 credits).
3. Offer the next step from the table; the card already has buttons for it. Keep the reply short.

## Notes

- Leave `trade` out for anything outside these six; the plain drawing is the right result then.
- A written description with sizes, not a photo, goes to `text_to_technical_drawing` instead.
