---
name: room-redesign
description: Restyle a room, facade or garden from a photo with MeltFlex. Use when the user wants a new style, colour scheme, floor, wall finish or furniture look while keeping the room's structure.
---

# Room redesign

## How to call it

Use `generate_interior` with:

- `image`: the user's room photo.
- `prompt`: **one sentence** naming the style and the two or three changes that matter most, e.g. "Redesign in warm Japandi style with light oak floors, a low linen sofa and paper lanterns."
- `variations`: 2 or 3 when the user is still deciding between looks (each image is charged).
- `design_level`: `pro` for a final, detailed render; `lite` for quick exploration.

## Good prompts

- Name the style first, then materials, then the hero piece of furniture.
- Say what must stay if the user cares ("keep the fireplace and the window seat").
- Do not describe the camera or the room layout; MeltFlex keeps both from the photo.

## After the render

Offer one follow-up, not a list: try another style, swap one element ("same room, green velvet sofa"), make a walkthrough video, or place a real product the user owns or wants to buy.

## Region edits

To change only one area, the user paints it solid red in the photo and you pass `mask: true`. The prompt then applies only to the red region.

## Style presets

For a named style, use the preset instead of writing the brief yourself: `tool: "interior"` with one of these `style` ids, and `prompt` holding only extra wishes. Call `browse_presets` with `tool: "interior"` to let the user pick from thumbnails. For a kitchen, bathroom, exterior, garden, walls or floors, use that tool instead (see browse_presets).

- `scandinavian`: Scandinavian
- `modern`: Modern
- `coastal`: Coastal
- `minimalist`: Minimalist
- `japandi`: Japandi
- `mid-century`: Mid-Century
- `industrial`: Industrial
- `bohemian`: Bohemian
- `farmhouse`: Farmhouse
- `rustic`: Rustic
- `mediterranean`: Mediterranean
- `traditional`: Traditional
- `transitional`: Transitional
- `luxury`: Luxury
- `art-deco`: Art Deco
- `neoclassical`: Neoclassical
- `bauhaus`: Bauhaus
- `brutalist`: Brutalist
- `wabi-sabi`: Wabi-Sabi
- `maximalist`: Maximalist
- `memphis`: Memphis
- `dark-academia`: Dark Academia
- `moroccan`: Moroccan
- `environmental`: Environmental
