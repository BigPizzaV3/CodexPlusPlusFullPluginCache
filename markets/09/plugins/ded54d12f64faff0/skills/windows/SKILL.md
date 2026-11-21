---
name: windows
description: "Windows Design with MeltFlex. Use when the user wants to redesign windows: frames, sills, glazing bars, curtains or blinds, or types /windows."
---

# Windows Design

MeltFlex's windows design tool, with the same window styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the window if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "windows"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "windows"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Window styles

- `black-frame`: Black Frame
- `crittall`: Crittall Steel
- `georgian`: Georgian Bars
- `picture`: Picture Window
- `wood-frame`: Wood Frame
- `arched`: Arched
- `bay`: Bay Window
- `floor-to-ceiling`: Floor-to-Ceiling

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
