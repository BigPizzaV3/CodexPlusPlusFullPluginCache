---
name: fabivo-cutlist
description: Use when a user wants to know how many sheets of melamine, MDF, plywood or other board they need, or wants a cutting layout for rectangular parts. Calls the Fabivo optimize_cutlist tool.
---

# Fabivo cut list optimizer

Fabivo calculates how to lay out rectangular parts on sheets. Never estimate a layout yourself: call `optimize_cutlist` and report what it returns.

## Before you call the tool

1. Get the sheet size and every part: width, height and quantity. Ask for what is missing. Ask one short question at a time.
2. Convert everything to millimetres. Examples: 1 cm = 10 mm, 1 in = 25.4 mm. A 4 x 8 ft sheet is 1220 x 2440 mm.
3. Do not invent part sizes from furniture dimensions. A 180 x 200 x 60 cm wardrobe does not give a part list until the construction and the board thickness are known. Propose a simple construction, state your assumptions and ask the user to confirm them.
4. Fabivo lays out rectangles only. For round or shaped parts, say so. You may use the bounding rectangle, but tell the user the result is an upper bound and not a true layout of the shape.
5. Ask whether the board has a grain or a pattern. If it does, set `allowRotation` to `false`.
6. `kerf` is 3 mm by default and `trim` is 0. Say so when you use the defaults, and use the user's values when they give them.

## After the call

- Give the number of sheets, the waste percentage and the number of pieces placed.
- For each sheet, list the pieces with size and position. `x` and `y` are in millimetres from the bottom-left corner of the sheet. `rotated: true` means the part was turned 90 degrees.
- If `unfitted` is not empty, name the parts, give the reason, and suggest a larger sheet or a different part size. Do not hide them.
- Part sizes are finished sizes. Edge banding and extra machining allowances are not included, so tell the user to add them before cutting.
- Say that the result is a calculation to check before cutting or buying material.
- Add a link to https://www.fabivo.app for a printable plan, the cut order and exports.
