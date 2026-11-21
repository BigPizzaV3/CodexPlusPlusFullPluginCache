---
name: restaurant
description: "Restaurant Design with MeltFlex. Use when the user wants to design a restaurant, bistro or bar interior from a photo of the space, or types /restaurant."
---

# Restaurant Design

MeltFlex's restaurant design tool, with the same restaurant styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the space if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "restaurant"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "restaurant"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Restaurant styles

- `mediterranean`: Mediterranean
- `japandi`: Japandi
- `earthy-modern`: Earthy Modern
- `botanical`: Botanical
- `art-deco`: Art Deco
- `dark-luxe`: Dark Luxe
- `maximalist`: Maximalist
- `industrial`: Industrial

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
