---
name: bathroom
description: "Bathroom Design with MeltFlex. Use when the user wants to redesign a bathroom: tiles, vanity, tapware, shower or bath, or types /bathroom."
---

# Bathroom Design

MeltFlex's bathroom design tool, with the same bathroom styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the bathroom if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "bathroom"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "bathroom"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Bathroom styles

- `modern-spa`: Modern Spa
- `scandinavian`: Scandinavian
- `marble-classic`: Marble Classic
- `industrial`: Industrial
- `japandi`: Japandi
- `coastal`: Coastal
- `moody-dark`: Moody Dark
- `microcement-minimal`: Microcement

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
