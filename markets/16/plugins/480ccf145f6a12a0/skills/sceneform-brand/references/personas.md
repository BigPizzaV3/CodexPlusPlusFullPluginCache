# Persona descriptions

A Persona's portrait is the identity every later image and video copies.
Sceneform's portrait writer turns your `prompt` into the final image prompt
and decides the photo itself: framing, setting, light, and pose. Your
description decides who the person is. Write it as one short paragraph, most
important first.

## What to describe

1. **Who.** Adult age band, gender, and heritage, named plainly in the first
   words: "a South Asian woman in her early 30s". A trait mentioned only
   late gets dropped.
2. **Face.** One or two concrete features: a strong brow, a gap in the front
   teeth, freckles across the nose, a defined jaw.
3. **Hair.** Color, length, texture, and how it falls.
4. **Build.** In plain words, once.
5. **Style.** Their register in a few words ("quiet minimal, earth tones",
   "streetwear, bold sneakers") and their niche or job ("an outdoor cooking
   creator", "a skincare educator"). Name a complete outfit only when the
   user wants one exact look; otherwise Sceneform dresses them from its
   outfit library to fit the description.
6. **One signature element** at most: a hair color, a statement jacket, a
   septum ring. Two compete.

## Rules

- Leave products and props out by default, so later generations can place
  them freely; the product comes in through `product_ref`.
- Leave out camera, light, pose, and background: the portrait writer sets
  them for a consistent reference photo.
- Never describe a real, named person, a child, or an age-ambiguous person.
- With photos (`source_image_refs`), the photos carry the face; a `prompt`
  is not allowed alongside them.

## Several Personas

Each new Persona differs from the user's existing ones (`list_personas`) on
at least two of: age, hair (color or cut), and body type. Vary heritage and
style across a cast instead of repeating one default face.

## Example

"A Black man in his late 20s with a close-cropped fade, a short beard, and a
small scar through his left eyebrow. Lean build. Relaxed streetwear in rust
and cream; a home-barista creator who reviews coffee gear."
