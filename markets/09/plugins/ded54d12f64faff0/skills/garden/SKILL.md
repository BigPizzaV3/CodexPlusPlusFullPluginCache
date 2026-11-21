---
name: garden
description: "Garden Design with MeltFlex. Use when the user wants to landscape a garden, backyard, front yard, patio or terrace, or types /garden."
---

# Garden Design

MeltFlex's garden design tool, with the same garden styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the garden or yard if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "garden"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "garden"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Garden styles

- `modern`: Modern
- `tropical`: Tropical
- `minimalistic`: Minimalistic
- `bohemian`: Bohemian
- `rustic`: Rustic
- `vintage`: Vintage
- `baroque`: Baroque
- `mediterranean`: Mediterranean
- `desert`: Desert
- `japanese`: Japanese Zen
- `cottage`: English Cottage
- `coastal`: Coastal
- `prairie`: Prairie

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
