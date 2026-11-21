---
name: walls
description: "Wall Finishes with MeltFlex. Use when the user wants to change wall finishes: brick, stone, wood panelling, plaster, tiles or a paint colour, or types /walls."
---

# Wall Finishes

MeltFlex's wall finishes tool, with the same wall finishes and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the room if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "walls"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "walls"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Wall finishes

- `exposed-brick`: Exposed Brick
- `white-brick`: White Brick
- `natural-stone`: Natural Stone
- `wood-paneling`: Wood Paneling
- `concrete`: Concrete
- `subway-tile`: Subway Tile
- `limewash`: Limewash
- `venetian-plaster`: Venetian Plaster
- `microcement`: Microcement
- `roman-clay`: Roman Clay
- `wood-slats`: Wood Slats
- `fluted-panels`: Fluted Panels
- `marble-slab`: Marble Slab
- `terrazzo`: Terrazzo
- `board-and-batten`: Board & Batten
- `panel-moulding`: Panel Moulding
- `zellige-tile`: Zellige Tile
- `rough-stucco`: Rough Stucco

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
