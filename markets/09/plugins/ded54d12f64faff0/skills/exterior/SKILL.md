---
name: exterior
description: "Exterior Design with MeltFlex. Use when the user wants to restyle a house or building facade, roof, cladding or front of a home, or types /exterior."
---

# Exterior Design

MeltFlex's exterior design tool, with the same architectural styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the building from outside if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "exterior"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "exterior"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Architectural styles

- `art-deco`: Art Deco
- `brutalist`: Brutalist
- `chinese`: Chinese
- `cottage`: Cottage
- `farmhouse`: Farm House
- `french`: French
- `gothic`: Gothic
- `italianate`: Italianate
- `japanese`: Japanese
- `mediterranean`: Mediterranean
- `midcentury`: Midcentury
- `middle-eastern`: Middle Eastern
- `minimalistic`: Minimalistic
- `modern`: Modern
- `morocco`: Morocco
- `ski-chalet`: Ski Chalet
- `spanish`: Spanish

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
