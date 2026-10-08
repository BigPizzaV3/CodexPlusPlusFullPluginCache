# Product prompt library

Weave the real product into these; they are templates, not literals.

## /white-bg — marketplace main image
`{product} centred on a pure white seamless background, even soft box lighting from both
sides, no shadows on the backdrop, sharp focus edge to edge, product fills 85 percent of
the frame, commercial e-commerce photography, no props, no text`
- `1:1` · **two steps:** `remove_background` first (returns transparency), then
  `generate_image` with that cutout as `image_url` and this prompt. A transparent PNG is
  not a compliant marketplace main image.

## /product-shot — clean studio hero
`{product} on a smooth neutral surface, single soft key light from upper left, gentle
falloff, subtle contact shadow, shallow depth of field, 85mm lens look, premium commercial
product photography`
- `1:1` or `4:5`

## /lifestyle — in context
`{product} in a lived-in {setting}, natural window light, shallow depth of field, casual
styling with real props around it, warm and inviting, editorial lifestyle photography`
- `4:5` for social, `16:9` for banners

## /giant — monumental
`{product} rendered at enormous scale in {environment}, dramatic low angle looking up,
cinematic lighting, sense of awe and mass, photoreal, wide establishing shot`
- `16:9` · `generate_giant_product_showcase`

## /jewelry — macro motion
`extreme macro of {piece}, slow rotation, light sweeping across the metal and stone,
controlled specular highlights, deep black background, jewellery commercial, razor sharp
detail on the setting`
- `9:16` social / `1:1` product page · `seedance-2.0` · duration `5` · resolution `1080p`
- fallback: `ltx-2.3` (duration `6`, resolution `1080p`)

## /a-plus — story panels
Pass the **topic** to `generate_carousel`, not a per-slide prompt — upstream plans each
slide. 5 slides default. Example topic: `why {product} solves {problem}, benefits and
materials, sizing and care`

## Secondaries checklist
Cover these five angles, one image each:
1. Three-quarter hero on white
2. Detail / texture macro
3. Scale reference (in hand, beside a known object)
4. In use, real setting
5. What's in the box / included parts
