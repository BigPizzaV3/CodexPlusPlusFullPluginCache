---
name: image-prompt-craft
description: "For a generation-ready image prompt: turn the visual goal and the chosen model's contract into a standalone prompt with subject, composition and light. Not needed for video, audio or answers without a prompt."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Professional image prompt preparation

Your task is not to retell the request but to turn it into a controllable visual brief for the
exact chosen model. The finished prompt has to make sense to the generator without the chat
history and carry enough decisions to produce a coherent frame. Length by itself is neither a
virtue nor a flaw.

## 1. First establish the actual result

Determine what exactly the user wants to get:

- a new image from scratch;
- a change to an attached image;
- a new frame that keeps a character, product, logo or other object;
- a transfer of only the style, composition, background or palette from a reference;
- an advertising key visual, a product card, a poster, a portrait, an illustration, a UI or an
  infographic;
- a series of consistent images.

The user's explicit facts (subject, action, properties, relations, text, style, prohibitions)
are fixed. Do not turn everything else into a questionnaire: choose consistent non-essential
details yourself when they help the task. Ask a question only when, without the answer, the
result itself cannot be understood or a compatible input cannot be chosen.

## 2. Read images as evidence, not as decoration

Give each attached image one or more precise roles:

- `source` — the image to be changed;
- `identity / character` — the appearance and stable traits of a person or character;
- `product / object` — the product's shape, color, material, packaging and markings;
- `style` — artistic language, texture, palette, processing;
- `composition` — placement of objects, shot size, perspective;
- `background / location` — the surroundings;
- `logo / text` — exact graphics or lettering.

Look at the available pixels and use only the properties that belong to the declared role. A file
name and an earlier prompt are auxiliary metadata, not a substitute for the visual content.
If the user sent a screenshot of an interface, separate the target object from the buttons, frames
and interface text: the interface does not become part of the result unless the user asked for it.

Do not mix roles. A camera-motion reference does not set a character's appearance; a style
reference does not change the product; a source image does not mean that absolutely everything
must be kept.

## 3. Follow the chosen model's contract

Use only the confirmed inputs and capabilities of the chosen model. Do not guess them from the
brand, the name or a memory of the catalog. The chosen model's current prompting guidance owns model-specific syntax;
its live contract owns available fields.

For product references, exact lettering and local edits, read `references/product-and-text.md`
when needed. It holds general craft, checked against the official GPT Image 2 and Seedream 5 Pro
guides. Do not load it for a simple task where the current context is already enough.

Pass the aspect ratio, size, quality mode, number of results and other execution controls in the
typed settings. Repeat them in the prompt only when the value is itself part of the composition,
for example "a vertical poster with room for a headline at the top".

## 4. Build an internal visual brief

Before writing the prompt, sort the decisions into four groups in your head:

1. `keep` — all of the user's explicit facts and the invariants of the references;
2. `change / create` — the observable result;
3. `professional choices` — the angle, composition, setting, light, palette, material, texture
   and depth of field that you choose;
4. `do not add` — new characters, products, story facts, advertising promises, logos, lettering
   or decor that change the meaning of the task.

Professional choices are needed when they make the result specific. They must not contradict
explicit values. Do not add empty boosters such as `masterpiece`, `best quality`, `8K`, `HDR` or
a random lens unless they express the required look.

## 5. Architecture of a finished prompt

Do not copy this list mechanically and do not output empty sections. For an ordinary generation,
assemble a natural, coherent brief in this order:

1. **Purpose and main frame** — what is being created and for what, if that affects the
   composition.
2. **Subject** — who or what is in the frame, and its important visible traits.
3. **Action / pose / relations** — what the subject does and how the objects are placed relative
   to each other.
4. **Composition** — shot size, angle, perspective, focal point, negative space.
5. **Scene** — the environment, the background and only the details that carry meaning.
6. **Light and color** — source, direction, hardness, temperature, contrast, palette.
7. **Material and texture** — how the surfaces look and how light behaves on them.
8. **Visual language** — photography, CGI, anime, graphics, collage, and its specific traits.
9. **Text and invariants** — verbatim lettering, logo, geometry or identity, when needed.

### Creating a new image

Describe the final frame, not the agent's working process. Do not write "generate", "use the
model" or "choose the settings" inside the prompt. One paragraph is fine if it stays readable; a
complex commercial frame can be split into short blocks of meaning.

### Editing a source image

Use a clear logic:

```text
SOURCE: [which asset is being edited]
CHANGE: [one or more specific changes]
KEEP: [only the properties that truly must not change]
LOOK: [what the final visual look should be]
CONSTRAINTS: [side changes that are not allowed]
```

Do not list the whole image in `KEEP`. Pin down what the model can actually break by accident:
identity, geometry, angle, product color, logo, background or lighting.

### Person, avatar or character

If a new look is needed without an identity reference, describe the age group, visible features,
hair, clothing, expression, pose, gaze and light only as far as the task needs. If there is an
identity reference, do not replace it with a long invented description: state the reference's
role and pin down only the critical traits and the allowed change.

### Product and advertising

The product stays the visual anchor. Fix its shape, color, material, packaging and logo from the
reference, then choose a commercially meaningful composition, setting, light, contact with the
surface, shadows and room for copy. Do not invent product properties or marketing claims.

### Lettering and infographics

Pass the user's text verbatim in quotes. State the hierarchy, placement, typeface character,
color, contrast and free area. Do not correct the brand, spelling or letter case unless asked.
If the chosen model's contract does not confirm the text accuracy you need, do not promise it and
state the limitation plainly.

### Image series

First fix a shared style or identity anchor, then write a self-contained prompt for each frame.
Change only the given axes (scene, pose, angle or the product point a frame shows) and keep the
shared traits. Do not use phrases like "as in the previous frame" without an available reference
asset.

## 6. Full examples

### A bad retelling

Task from the user: «сделай белую Ferrari в мультяшном стиле (аниме)».

Not acceptable:

```text
A white Ferrari in a cartoon anime style.
```

This is a caption, not a finished prompt.

### A finished image prompt

```text
A white Ferrari is the main and only subject of the frame, seen from a low front three-quarter
angle, the whole car fitting inside the frame. A crisp, recognizable sports-car silhouette, glossy
white paint with neat cool highlights, dark wheels and clean reflections without distorted
details. The car stands on a wide city street after light rain; the background is simplified and
slightly blurred so that it does not compete with the car. The visual language of a modern
feature-length anime: expressive outlines, controlled cel shading, soft gradients in the sky,
dynamic diagonal composition, saturated but not neon accents. Evening side light brings out the
shape of the body, with a natural contact shadow under the car. No people, no text, no logos in
the surroundings and no extra cars; keep the geometry of the body and wheels correct.
```

This is one acceptable professional option. If the user set a different street, angle, time of
day or anime style, their values fully replace the ones chosen here.

### Editing a building from a source

```text
SOURCE: @Image1 — the original building and its camera angle.
CHANGE: move the surroundings into an open sandy desert; remove the neighboring buildings, roads,
cars, vegetation and urban elements.
KEEP: the building itself, its facade, proportions, the number of visible floors, the camera
position and the vertical composition.
LOOK: realistic dry daylight, pale sand to the horizon, a light atmospheric haze, natural contact
shadows at the base of the building.
CONSTRAINTS: do not change the architecture or the facade materials; do not add people, signs or
new objects around the building.
```

## 7. Final self-check

Before delivering the result, check that:

- every explicit fact from the user is kept;
- the prompt cannot be mistaken for a caption or a retelling;
- the attached images have explicit roles;
- missing non-essential decisions are made, not turned into questions;
- there is no new meaning-carrying object, text or claim;
- typed settings are not duplicated as filler prose;
- the structure fits the exact chosen model;
- the prompt is ready to use on its own, without the chat history.

Reference aliases apply only when the chosen model declares inline-reference support.
Bind them to actual reference order and roles; for dedicated source/start/end fields,
use the slot role instead of inventing an alias.
