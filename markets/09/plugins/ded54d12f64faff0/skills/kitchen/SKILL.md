---
name: kitchen
description: "Kitchen Design with MeltFlex. Use when the user wants to redesign a kitchen: cabinets, worktops, splashback, island or a whole new look, or types /kitchen."
---

# Kitchen Design

MeltFlex's kitchen design tool, with the same kitchen styles and the same design brief as meltflexai.com.

## Steps

1. Ask for a photo of the kitchen if the user has not shared one. Never invent the space.
2. If the user has not named a look, call `browse_presets` with `tool: "kitchen"` so they can pick from the gallery. Skip it when they already said what they want.
3. Call `generate_interior` with `image`, `tool: "kitchen"`, the chosen `style` id, and `prompt` holding only the user's extra wishes (for example "keep the window seat"), or an empty string.
4. Offer one next step: another style side by side (`variations: 2`), a walkthrough video, or placing a specific product the user likes.

## Kitchen styles

- `modern-handleless`: Modern Handleless
- `scandinavian`: Scandinavian
- `shaker-sage`: Sage Shaker
- `farmhouse`: Farmhouse
- `industrial`: Industrial
- `warm-minimal`: Warm Minimal
- `two-tone`: Two-Tone
- `timeless-white`: Timeless White

If the user describes a look that matches none of these, leave `style` out and put their description in `prompt`.
