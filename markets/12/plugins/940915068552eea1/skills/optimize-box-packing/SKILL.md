---
name: optimize-box-packing
description: Standardized multi-bin packing for items, pallets, and shipping containers.
---

# Optimal Packing Workflow

## When to use this skill
Use this skill whenever a user provides item dimensions (Length, Width, Height, Quantity) and asks how to pack them into containers, boxes, or pallets.

## Execution Steps
1. Parse the user's item list.
2. Call `pack_cuboid_items` with the parsed item dimensions and available bin sizes.
3. Extract the solution from the response payload.
4. Format the final output as a clear text manifest showing:
   - Total bins used and volume- and weight efficiency percentages.
   - Spatial placement (X, Y, Z coordinates) and notable rotation angles for each item.