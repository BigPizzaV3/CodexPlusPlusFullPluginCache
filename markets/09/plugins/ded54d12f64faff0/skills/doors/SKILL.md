---
name: doors
description: "Doors Design with MeltFlex. Use when the user wants to redesign a front door or interior doors, or types /doors."
---

# Doors Design

MeltFlex's doors design tool, with the same door styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the door if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "doors"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "doors"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Door styles

- `modern-flush`: Modern Flush
- `shaker`: Shaker
- `panelled`: Classic Panelled
- `french-glass`: French Glass
- `black-crittall`: Black Crittall
- `barn`: Sliding Barn
- `pivot`: Pivot
- `arched`: Arched

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
