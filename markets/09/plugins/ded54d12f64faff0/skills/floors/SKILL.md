---
name: floors
description: "Floor Restyle with MeltFlex. Use when the user wants to change the flooring: parquet, herringbone, tiles, marble, stone, concrete or carpet, or types /floors."
---

# Floor Restyle

MeltFlex's floor restyle tool, with the same floor materials and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the room showing the floor if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "floors"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "floors"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Floor materials

- `oak-herringbone`: Oak Herringbone
- `white-marble`: White Marble
- `polished-concrete`: Polished Concrete
- `dark-walnut`: Dark Walnut
- `light-oak`: Light Oak
- `oak-chevron`: Oak Chevron
- `walnut-herringbone`: Walnut Herringbone
- `grey-oak`: Grey Oak
- `whitewashed-oak`: Whitewashed Oak
- `travertine`: Travertine
- `limestone-tile`: Limestone
- `black-marble`: Black Marble
- `microcement`: Microcement
- `black-slate`: Black Slate
- `terrazzo`: Terrazzo
- `checkerboard-marble`: Checkerboard Marble
- `terracotta-tile`: Terracotta Tile
- `patterned-tile`: Patterned Tile

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
