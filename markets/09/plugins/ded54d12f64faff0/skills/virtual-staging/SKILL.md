---
name: virtual-staging
description: Furnish an empty or cluttered room for a property listing with MeltFlex. Use for real estate photos, new builds, rentals and before-and-after staging.
---

# Virtual staging

## Steps

1. Take the empty or cluttered room photo.
2. Ask who the listing is for if it is unclear (young professionals, a family, short-term rental); it decides the style.
3. Call `generate_interior` with a one-sentence prompt such as "Furnish this empty living room in a warm modern style for a young family, with a sofa, rug, coffee table and plants."
4. For a cluttered room, start the prompt with "Declutter and" so personal items are removed before staging.

## Listing guidance

- Keep staging realistic for the room size; mention "compact" pieces for small rooms.
- Use `design_level: pro` and `resolution: 2K` for photos that will be published.
- Remind the user that many listing sites require staged photos to be labelled as virtually staged.

## Staging presets

Use `tool: "staging"` with one of these `style` ids; put the room type, audience and any must-haves in `prompt` ("living room for a young family"). Call `browse_presets` with `tool: "staging"` to show them as a gallery.

- `modern`: Modern
- `scandinavian`: Scandinavian
- `luxury`: Luxury
- `midcentury`: Mid-Century
- `coastal`: Coastal
- `farmhouse`: Farmhouse
- `japandi`: Japandi
- `traditional`: Traditional
- `minimalist`: Minimalist
- `industrial`: Industrial
- `boho`: Boho
- `art-deco`: Art Deco
- `mediterranean`: Mediterranean
- `rustic`: Rustic
- `transitional`: Transitional
- `contemporary`: Contemporary
- `hamptons`: Hamptons
- `parisian`: Parisian
- `wabi-sabi`: Wabi-Sabi
- `organic-modern`: Organic Modern
- `hollywood-glam`: Hollywood Glam
- `french-country`: French Country
- `english-country`: English Country
- `tuscan`: Tuscan
- `moroccan`: Moroccan
- `tropical`: Tropical
- `desert-modern`: Desert Modern
- `mountain-lodge`: Mountain Lodge
- `urban-loft`: Urban Loft
- `shabby-chic`: Shabby Chic
- `eclectic`: Eclectic
- `maximalist`: Maximalist
- `retro-70s`: Retro 70s
- `neoclassical`: Neoclassical
- `zen`: Zen
- `cottagecore`: Cottagecore
- `dark-academia`: Dark Academia
- `quiet-luxury`: Quiet Luxury
- `biophilic`: Biophilic
- `monochrome`: Monochrome
