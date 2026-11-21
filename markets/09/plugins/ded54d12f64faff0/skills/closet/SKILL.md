---
name: closet
description: "Closet Design with MeltFlex. Use when the user wants to design a walk-in closet, fitted wardrobe or dressing room, or types /closet."
---

# Closet Design

MeltFlex's closet design tool, with the same closet styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the closet or wall if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "closet"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "closet"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Closet styles

- `modern`: Modern
- `boutique`: Boutique
- `luxury`: Luxury
- `minimalist`: Minimalist
- `scandinavian`: Scandinavian
- `japandi`: Japandi
- `warm-oak`: Warm Oak
- `traditional`: Traditional
- `art-deco`: Art Deco
- `industrial`: Industrial Open
- `boho`: Boho

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
