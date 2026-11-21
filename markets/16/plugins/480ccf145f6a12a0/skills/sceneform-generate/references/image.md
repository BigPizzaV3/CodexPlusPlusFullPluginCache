# Images

How to turn a brief into an image prompt that a model renders well. The
model's `prompt_guide` (from `query_generation_options` with `action: "get"`)
sets the shape: some models read labelled lines, others want one flowing
paragraph. This file sets the content.

## Pick the mode

The deliverable decides the mode, not the setting: a Pinterest pin of a
kitchen is a pin, and a banner showing a person outdoors is a banner.

| Mode | When | Default ratio |
| --- | --- | --- |
| Product shot | packshot, catalog, store listing, product on a plain or styled surface | 1:1 |
| Lifestyle | a product or person in a real place, in use | 4:5 |
| Portrait | a person is the subject | 4:5 |
| Close-up with person | a product held, worn, or applied; part of a face | 4:5 |
| Graphic with text | poster, banner, thumbnail, quote card, cover, slide | the destination's |
| Illustration | cartoon, mascot, sticker, icon, storybook art | 1:1 |
| Conceptual | surreal, floating, splash, sculptural, impossible scale | 1:1 |
| Edit | change part of an existing image | the source's |
| Restyle | the same subject and composition in a new look | the source's |

Restyle applies only when subject and composition stay. Anything that moves
the subject or reframes it is a new image that uses the old one as a
reference. Conceptual and surreal looks fight rustic, handmade, and budget
brands; give those a lifestyle or product shot instead.

## Build the prompt

Cover these in order, skipping any that the brief or a reference already
settles:

1. **Use.** What the image is for, in the first sentence: "A product
   photograph for a Shopify listing", "A YouTube thumbnail", "A candid
   phone snapshot". The stated use sets how polished the result looks, so
   name a premium or editorial use only when that look is wanted.
2. **Subject.** Who or what, with the detail that makes it this one and not
   a generic one: "navy blue tweed overcoat with horn buttons", not "a
   jacket".
3. **Setting.** Where it is and what sits close behind it.
4. **Composition.** Shot size, camera height, where the subject sits in the
   frame, how much of the frame it fills.
5. **Light.** Direction, quality, and color (vocabulary below).
6. **Materials.** Surfaces, textures, and the small real imperfections that
   make a photograph read as real: wear, dust, fabric weave, condensation.
7. **Palette.** Two or three named colors and one accent.
8. **Finish.** The medium and register: real photograph, 35mm film,
   flat vector, watercolor, 3D render.
9. **Constraints.** The few rules that must hold (text, identity, product
   fidelity), each written once.

A simple subject needs one or two sentences. A brief with several
requirements reads better as short labelled lines when the model guide
allows them.

### Words that carry no information

| Instead of | Write |
| --- | --- |
| good lighting | "one big soft light high on the left, neutral daylight, shadows that fade gently" |
| nice background | "warm grey seamless paper, slightly darker toward the top" |
| beautiful, stunning | the specific thing that makes it so |
| professional, high quality | the register: "catalog packshot, tack sharp, even exposure" |
| realistic | "real photograph" plus texture and one imperfection |
| modern | the palette, materials, and shapes that make it modern |

### Light

- Direction: key 45 degrees camera-left or right, frontal and flat (beauty,
  e-commerce), top-down, back rim for separation, low side light that rakes
  across texture, window light from one side.
- Quality: large softbox (soft edges), hard direct light (crisp shadows),
  dappled through leaves, bounced fill, a practical lamp visible in frame.
- Color: candlelight around 2000 to 2800K, tungsten interior around 3200K,
  neutral daylight around 5000 to 5500K, overcast around 6500K, shade and
  blue hour 7000K and up. A named source or a number beats "warm".
- Shadow: one coherent soft shadow grounding the product; a contact shadow
  only at the base; hard-edged shadows from a single source.
- Lens feel: wide and environmental, natural (35 to 50mm), portrait
  compression (85mm), macro detail, telephoto isolation; shallow focus with
  a soft background or deep focus with everything sharp. Exact focal lengths
  and f-stops help only on models whose guide welcomes them.

## Text in the image

Three cases, and exactly one applies:

1. **The user gave the words.** Put them in double quotes, verbatim, and say
   where they sit, how large, and the typeface in words ("bold condensed
   sans serif, white, top third"). Spell an unusual brand name letter by
   letter. Keep a headline to about seven words; long copy garbles.
2. **The user will add text later.** Ask for one calm, tonally even area
   that belongs to the scene: open sky, a blurred wall, a stretch of
   tabletop. The phrases "negative space" and "copy space" make models
   paint a flat color band or an empty rectangle.
3. **Nobody mentioned text.** Say nothing about text in the scene, and close
   with "no added text, watermarks, or logos". Text and logos printed on a
   referenced product stay, under the product rules below.

Thumbnails and covers: a headline of two to four words, high contrast,
placed away from the face. One face with a clear, readable emotion. The
whole idea must read at 120 pixels wide; if it does not, the composition is
wrong, not the resolution. Ask for "bold, punchy, high contrast", because
models drift toward a muted film look.

## People

- State the body framing, the gaze, and what the hands do: "waist up,
  looking down at the open book, both hands holding it".
- Name a moment instead of a pose: "caught mid-laugh, glancing off camera",
  "mid-sentence, eyebrows raised". "Poses" and "smiles at the camera"
  produce stock photos.
- Describe an adult as an adult with an age band ("a woman in her late
  30s"). Faces drift young; "defined jaw, adult proportions" holds them.
- For real skin: "visible pores, natural skin texture, soft natural
  catchlights, no retouching".
- To keep a face from a photo or a Persona, pass it as a reference and
  write an identity lock: "the same person as @{ref:<persona_ref>}, with
  the face shape, eyes, nose, mouth, jaw, hairline and skin tone kept exactly
  as they are; not beautified". A soft "keep the face" lets it drift.
- Never name a real person or a copyrighted character. Write "original
  character" for illustration.
- In a close-up with a product, the product fills 40 to 60 percent of the
  frame and the face shows only in part (lips, eyes, the nose down).
- Hands: say which hand, the grip, and where the fingers rest. More than two
  busy hands produces extra limbs.

## Products

- Pass the product as a reference (`product_ref` from `list_brand_kits`, or
  a photo) and lock it: "the product in @{ref:<product_ref>}: keep its exact
  shape, proportions, colors, materials, logo placement, and label text".
- Printed text: "reproduce every printed element exactly as in the
  reference; where a word cannot be read, copy its letterforms as shapes; invent no words".
- A reference shot from a tilted angle: "present the product level, in its
  natural upright orientation".
- Props only from the brief or the brand. A product alone on a seamless
  surface reads as a catalog image; two or three props from its category
  read as a lifestyle image.
- Without a photo, write the product once in full: shape, material, color,
  size against a hand plus centimetres ("palm-sized, about 15 cm"), how it
  opens or works, how the label looks, one honest imperfection. Reuse that
  sentence word for word in every prompt for that product.

## Edits and restyles

- Write the change, then what stays: "Change only the jacket to deep green
  corduroy. Keep the face, pose, lighting, camera angle, and background
  exactly as they are. Change nothing else."
- One change per edit. Several small edits beat one big rewrite.
- A restyle commits fully: name the palette, medium, surface, and light of
  the new look so none of the old one bleeds through.
- `upscale_image` and `remove_background` take the image in `reference_refs`
  and no prompt. `reframe_image` also needs `settings.aspect_ratio`, and
  extends the canvas to fit.

## Several references

Give each reference one job and name it where the prompt uses it as
`@{ref:<ref>}`, with the exact ref you pass: the subject, the product, the
style, the setting. Sceneform turns each mention into the token the model
reads. Say what must not carry over from it: "use only the jacket from
@{ref:media_abc123}, not its background or lighting". When a reference already shows
something exactly, refer to it and stop; describing the same face or
product again in words fights the image.

## Sets

- Write a visual system once (palette, surface, light direction and color,
  camera height, composition rule, finish) and paste it word for word into
  every prompt of the set. Vary only the subject, scene, or angle.
- When the subject has no reference image, generate the first image alone,
  wait for it, then pass its `asset_ref` as the reference for the rest.
- Number the outputs in your reply so the user can ask for "image 3, warmer".
- A carousel post with a caption belongs to sceneform-ad-studio's
  `generate_carousel`.

## Aspect ratio by destination

| Destination | Ratio |
| --- | --- |
| Instagram feed, Facebook feed ads | 4:5 |
| Stories, Reels, TikTok, Shorts covers | 9:16 |
| LinkedIn feed, store listings, profile images | 1:1 |
| Pinterest | 2:3 |
| Website hero, YouTube thumbnail, slides | 16:9 |
| Wide banner | 21:9 |
| Print poster | 2:3 or 3:4 |

Set `aspect_ratio` in `settings` only when the option lists that control.

## Checklist

- The first sentence names the use.
- The subject is specific enough to tell it apart from a stock image.
- Light has a direction, a quality, and a color.
- Every reference has one job and an `@{ref:…}` mention where it is used.
- Text follows exactly one of the three cases.
- People: framing, gaze, hands, an adult age band, real skin.
- A product: the fidelity lock and the printed-text rule.
- No word from the "carries no information" table.
- The length is near the `prompt_guide`'s target.

## Fixes

Each fix uses the latest output as the reference and starts: "Keep the
composition, subject, and framing exactly. Change only:"

| Observed | Change only |
| --- | --- |
| Flat lighting | a directional key from one side, a rim light on the other edge, a deeper contact shadow |
| Plastic or waxy surfaces | real micro-texture: pores, weave, grain; no retouching |
| Garbled text | the exact words in quotes, larger, fewer of them |
| Wrong hands or anatomy | the named body part, with its correct position |
| A face that drifted | regenerate from the original reference with a stronger identity lock, not from the drifted output |
| A flat color band | that area continues the real scene: sky, wall, surface |
| Stock-photo feel | one lived-in detail, some asymmetry, one specific story cue |
| Muted where punch was wanted | bold, high contrast, saturated poster grade |
| Looks too young | defined jaw, adult proportions, the stated age band |
| Product too small | the product fills 40 to 60 percent of the frame |
