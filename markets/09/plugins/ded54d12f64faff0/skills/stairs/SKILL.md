---
name: stairs
description: "Staircase Design with MeltFlex. Use when the user wants to redesign a staircase: treads, balustrade, railing or a new stair style, or types /stairs."
---

# Staircase Design

MeltFlex's staircase design tool, with the same staircase styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the staircase if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "stairs"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "stairs"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Staircase styles

- `modern-oak`: Modern Oak
- `floating`: Floating
- `glass`: Glass Railing
- `farmhouse`: Farmhouse
- `industrial`: Industrial
- `spiral`: Spiral
- `traditional`: Traditional
- `scandinavian`: Scandinavian

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
