---
name: get-started
description: Introduce TechDraw AI and make a first technical drawing. Use when someone has just connected TechDraw AI, asks what it can do, or wants to try it without a specific plan.
---

# Get started with TechDraw AI

TechDraw AI turns a photo of a real product, or a written description with sizes, into a dimensioned technical drawing, and turns drawings into files for CAD, laser cutting and 3D printing.

## What to offer

- **Photo to drawing**: a product photo becomes front, side and top views on an ISO or ANSI sheet.
- **Description to drawing**: a part described in words with its sizes, drawn true to size.
- **Drawing to CAD**: DXF and DWG for AutoCAD, Fusion, SolidWorks, laser and CNC.
- **Line art to STL**: a logo or outline extruded into a 3D-printable STL.
- **Product render**: a photoreal studio image of the product in a drawing.
- **3D model**: a GLB and STL from a product photo or a drawing.

## First run

1. Ask for a photo of the product if none was shared, or for the part's sizes if they want it drawn from a description. Never invent a product.
2. Call `generate_technical_drawing` with the photo, or `text_to_technical_drawing` with the description. Pass any real measurements the user gave in `measurements`.
3. After the drawing, offer the natural next step: DXF/DWG for CAD, a photoreal render, or a 3D model. The card has buttons for all three.

## Credits

Drawings and renders cost 5 credits on the user's TechDraw AI account, 3D models 80 (Studio plan). DXF/DWG, STL and identifying a product are free. Call `get_credits` when the user asks what something costs, and before a 3D model. Failed 3D jobs are refunded automatically. Do not link to pricing or checkout pages in the chat.
