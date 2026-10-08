# Identity method

## 1. Establish the brand — four questions, asked once, together
Name · what it does · who it's for · one word for how it should feel.

## 2. Palette — 5 to 6 colours with stated roles
Never a list of pretty swatches. Every colour gets a job:

| Role | What it does |
|---|---|
| Ground | The dominant background |
| Surface | Cards, panels, raised areas |
| Ink | Primary text |
| Muted | Secondary text, captions |
| Accent | The one colour that carries the brand |
| Semantic | Success / warning / error, separate from the accent |

Give hex values. Then **show them applied** — `generate_image` a sample surface using
those exact hexes in the prompt. Swatches alone prove nothing.

Neutrals should carry a slight hue bias toward the accent. A pure mid-grey reads as
unconsidered.

## 3. Typography — two faces, both real
A display face used with restraint, and a body face that complements it. Name real,
available faces. Say what each one is doing and why they work together — contrast in
weight, width, or era.

## 4. Logo — three directions
`generate_logo`. Then `generate_3d_logo_animation` once one is chosen.

## 5. Applications — prove it works
Show the identity applied to at least three real surfaces, reusing the other skills' tools:
- A social post (`generate_instagram_post`)
- A product or hero shot (`generate_image`)
- The animated logo reveal

Every one of these prompts carries the palette hexes explicitly.

## What to say about exports
Palette and typography are delivered as structured text. There is no brandbook file export
yet. State this once, plainly, rather than implying a download that isn't coming.
