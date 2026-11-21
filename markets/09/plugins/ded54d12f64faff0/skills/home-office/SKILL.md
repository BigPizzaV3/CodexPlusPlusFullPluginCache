---
name: home-office
description: "Office Design with MeltFlex. Use when the user wants to turn a room or corner into a home office or redesign a workspace, or types /home-office."
---

# Office Design

MeltFlex's office design tool, with the same office styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the room if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "office"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "office"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Office styles

- `modern`: Modern
- `minimalist`: Minimalist
- `scandinavian`: Scandinavian
- `japandi`: Japandi
- `mid-century`: Mid-Century
- `executive`: Executive
- `dark-academia`: Dark Academia
- `industrial`: Industrial
- `boho`: Boho
- `coastal`: Coastal
- `biophilic`: Biophilic
- `gaming`: Gaming

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
