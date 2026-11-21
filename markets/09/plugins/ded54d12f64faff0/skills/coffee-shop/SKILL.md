---
name: coffee-shop
description: "Coffee Shop Design with MeltFlex. Use when the user wants to design a coffee shop or cafe interior from a photo of the space, or types /coffee-shop."
---

# Coffee Shop Design

MeltFlex's coffee shop design tool, with the same cafe styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the space if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "coffeeshop"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "coffeeshop"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Cafe styles

- `minimal`: Minimal
- `warm-walnut`: Warm Walnut
- `industrial`: Industrial
- `japandi`: Japandi
- `mediterranean`: Mediterranean
- `art-deco`: Art Deco
- `colour-pop`: Colour Pop
- `botanical`: Botanical

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
