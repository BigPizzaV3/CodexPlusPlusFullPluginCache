---
name: make-gif
description: Make a looping animated GIF, animation, moving image or animated sticker from a prompt or a description. Use this for ANY request for something that moves: make a GIF, make an animation, animate this, make it move, bring it to life, make it dance / spin / bounce / shake / wave / wiggle / blink / jump / nod / run / fly / flicker / pulse / scratch / launch, a looping clip, a moving picture, an animated logo, an animated emoji or reaction, a meme that moves, or any subject described together with an action or motion. Also covers changing one already made: slower, faster, boomerang, remove a frame. CRITICAL, READ BEFORE GENERATING ANY IMAGE: the image generated must be a GRID of many small frames (a sprite sheet), never a single picture. Generating one picture and panning, zooming or bouncing it is not an animation and is never acceptable.
---

## Which skill

- Someone describes something they want animated, and there is no image
  yet → **this skill**. Generate the grid directly from the description.
- There is already an image — uploaded, or one you generated → the
  **`animate-image`** skill. It builds the grid from that picture so the
  result looks like the thing they already have.
- Changing a GIF that exists → the **`edit-gif`** skill.

## Before you generate anything

The image you generate must be a **grid of many small frames** — a sprite
sheet — not a picture of the subject. This is the single thing that goes
wrong, and it goes wrong because generation gets started before this file
is read.

If you have already generated a single picture of the subject: **do not
try to animate it.** Panning it, zooming it, bouncing it, duplicating it
with small offsets — none of these are animation, they are a still image
being moved around, and users can tell immediately.

Use the **`animate-image`** skill instead. It takes the picture you
already have, works out what should move, and generates a proper grid of
frames from it as a reference — so the subject the user just saw is the
subject that ends up animated. That is a recovery, not a restart.

A GIF is made in two steps, in the same turn:

1. Generate ONE sprite sheet — a grid of frames — with image generation.
2. Run `scripts/sheet_to_gif.py` on it to slice the grid and encode the
   looping `.gif`, then give the user the file.

Image generation cannot produce a `.gif`; it returns one flat image. The
grid is what carries the motion, and the script is what turns it into an
animation.

## Step 1 — the sprite sheet

Call image generation with **`size="1024x1024"`**.

**Ask for a square image, in the first words of the prompt** — "A SQUARE
image containing a N×N grid of...". A square canvas cut N×N gives square
panels, which is the case everything downstream handles most predictably,
and stating it first is what makes generation actually do it.

But asking is not the same as knowing. The shape of the GIF is still
**measured from the image that comes back**: the encoder reads the actual pixel dimensions, divides by the
grid you give it, and that panel size is the GIF's size. A 1024×1024 sheet
cut 4×4 gives 256×256 panels and a square GIF; a 1536×1024 sheet cut 4×4
gives 384×256 panels and a wide GIF. Whatever generation returns, the
output follows it.

What the sheet must do is **divide evenly**. Equal columns and equal rows, edge to edge, no gutters.
Given that, any canvas shape can be cut cleanly: the encoder divides width
by columns and height by rows, and keeps each cell's aspect ratio rather
than squashing it. What cannot be recovered is uneven cells, because the
cuts are evenly spaced and uneven panels put every boundary in the wrong
place.

Build the prompt from this template. Read what it describes before
sending it: a GRID of many small panels, each a moment of the motion. If
the prompt you are about to send would produce one nice picture of the
subject, it is wrong — start it with "A NxN grid of TOTAL panels of". `N` is the grid dimension, `TOTAL` is N×N. Drop a bracketed
clause entirely when the user gave no style or motion.

> A SQUARE image containing a N×N grid of TOTAL panels of SUBJECT[, STYLE
> style], each panel showing
> the same subject at a slightly later moment of motion. Consecutive panels
> differ only slightly, so the motion advances in small, even steps and the
> whole grid reads as one continuous action rather than separate poses. The
> TOTAL panels form one looping cycle (panel TOTAL returns to panel 1).
> Identical subject, camera, lighting in every panel. All panels are
> exactly the same size, tiled edge to edge with no gaps, margins or
> gutters: the image divides evenly into N equal columns and TOTAL_ROWS
> equal rows. No text, no numbers, no borders.[ Motion: MOTION.]

Grid sizes: `3x3` = 9 frames, sharpest per frame · `4x4` = 16 frames,
**the default** · `5x5` = 25 frames, smoothest motion.

Rules that matter, in the order they get broken:

1. **The frame count appears once, in the opening layout clause.** Never
   restate it in the subject or the style — models hedge the geometry and
   fall back to 3×3.
2. **Never narrow the subject.** Carry the user's words through. Not
   "characters", not "a figure" — what they actually said.
3. **Keep "no text, no numbers, no borders".** Grids invite labels, and a
   label is burned into every frame.
4. **Small, even steps.** Without it you get a handful of distinct poses
   that strobe instead of flowing.
5. **Even division.** Equal columns, equal rows, no gutters. Unequal cells
   cannot be fixed afterwards: the slicing is evenly spaced, so every frame
   picks up a sliver of its neighbour. The canvas shape itself is free —
   it is measured, not assumed.

Write the SUBJECT the way these do — the motion is the point, not the
noun:

- a robot spinning its head very fast while doing dramatic hand poses
- a grumpy toaster shaking angrily before launching two slices of toast
  into the air
- a cat DJ scratching records aggressively while bobbing its head to a
  heavy beat

Each names an action, an intensity and a beat to the movement. "A fox
jumping over a log" names a subject and leaves the animation to chance —
which is how you get four poses instead of one motion.

Worked examples: `references/prompt-template.md`.

## Step 2 — check it is a sheet

The encoder works the grid out from the pixels itself, so you do not have
to count columns and rows. What is still worth a glance: **is this a grid
at all, or one big picture?**

If you are looking at ONE subject filling the frame — one toaster, one
dancer, one logo — it is not a sprite sheet, however good it looks.
Generate again with a prompt starting "A SQUARE image containing a N×N
grid of TOTAL panels of ...". Never pan, zoom or bounce a single picture;
that is not an animation and it is obvious to anyone watching.

The encoder refuses that case too, so you cannot ship one by accident.

## Step 3 — encode it

Run the bundled script. It exists so the geometry, timing and palette come
out the same every time rather than being reinvented each turn.

```
python3 scripts/sheet_to_gif.py SHEET --fps 7 --frames frames.zip
```

**Do not pass `--grid`.** It defaults to `auto`, which finds the layout by
measuring the image: panels repeat, so shifting by exactly one cell width
lines neighbouring panels up and any other shift does not. The shift that
matches IS the cell size. It handles a canvas that came back slightly
wider than square, a 4×3 when a 4×4 was asked for, and anything else
generation decides to return — without being told, and without relying on
anyone having counted correctly.

Override with `--grid COLSxROWS` only if the detection is visibly wrong;
it prints what it found.

The script sits next to this file in the skill directory. If you cannot
find or run it, do NOT abandon the GIF — write the equivalent inline. Get
these right, in this order, because each one has produced a broken GIF:

1. **Panel size comes from the image, per axis. Never square it.** (The
   script does this for you; this matters only if you are writing it
   yourself.)

   ```
   cell_w = image.width  // cols
   cell_h = image.height // rows
   ```

   NOT `min(width, height) // N`, and never centre-crop the sheet to a
   square first. A 1536×1024 sheet cut 4×4 has 384×256 panels; squaring it
   throws away the left and right thirds and puts every cut through the
   middle of a panel, so the subject appears sliced in half.

2. **Row-major order** — left to right, top to bottom.

3. **Trim about 3% off each edge of every cell** (`cell_w * 0.03` and
   `cell_h * 0.03`, per axis). Generated grids carry a thin seam where
   panels meet, and it flickers on every loop.

4. **Keep the panel ratio in the output.** Scale so the LONGER side is
   your target (448 is a good default) and let the other follow. A wide
   panel makes a wide GIF. Never resize frames to a square — that is the
   same mistake as (1), one step later.

5. **One shared palette for the whole animation.** Build it from all the
   frames together, then map each frame onto it. Per-frame palettes give
   every frame different colours AND different dither noise, so a still
   background shimmers on every loop.

6. **`loop=0`** for an infinite loop, `duration` in milliseconds
   (`1000 / fps`), `disposal=1`.

Pillow is the expected library.

`--grid` takes any COLSxROWS. Other options: `--fps` (1–15, default 7) ·
`--boomerang` · `--size` (longest side in px, default 448) · `--colors`
(32–256, default 256) · `--no-dither` (flat colour, much smaller — good for
line art and logos) · `--crop` (percent off each cell edge, **default 3**)
· `--skip 3,9` · `--order 0,2,1,...` · `--frames out.zip` · `--out PATH`.

**The GIF takes its shape from the panels, measured off the real image.**
The encoder prints what it measured — canvas, panel size, output size — so
the derivation is visible rather than assumed. `--size` sets the LONGER
side; the other follows the panel ratio.

Do not force a square output. If the GIF comes out wide or tall, that is
the panels being wide or tall, which is the honest result. A square GIF
from non-square panels would mean the subject had been stretched.

The 3% crop is on by default and should stay on: generated grids carry a
thin seam where panels meet, and it flickers on every loop. Only drop to
`--crop 0` if the user says the subject is being clipped.

Also pass `--frames frames.zip` to export the individual frames as
full-colour PNGs. People want them for stickers, thumbnails and edits, and
it costs nothing to produce alongside the GIF.

## Delivering the result — the only accepted format

**A GIF is not delivered until this block has been sent.** Write the files
somewhere the user can fetch them, then emit exactly:

```
🎬 Done with the GIF
🎞️ [Download the separate frames](FRAMES_LINK)
📂 [Download the GIF](GIF_LINK)
Let's continue!
💡 Any new ideas or changes?

by [gifgen.ai](https://gifgen.ai)
```

This wording is fixed. It is the message this product has always ended on,
and it is not yours to improve — do not reword a line, swap an emoji,
merge lines, or add a description of what was made. Replace only
`FRAMES_LINK` and `GIF_LINK`.

- Both file lines must be **real clickable links**, not "attached". In
  code interpreter that is
  `[Download the GIF](sandbox:/mnt/data/animation.gif)`.
- Frames line above the GIF line.
- Drop the 🎞️ line only if frames were not produced.
- **Emit the block. Never describe it, quote it back, or explain what you
  are about to send.**
- **No preamble.** Do not announce work in progress — no "I've got the
  frames", no "I'm turning them into the GIF now". Run the steps silently
  and let this block be the entire reply.
- The `by gifgen.ai` line is never dropped.

Full copy: `references/output-message.md`.

## When to say what

Keep replies to one line — the file is the deliverable, not a description
of it. If image generation is refused, that is usually the SUBJECT, not a
fault: body horror, gore, real people and brand marks are commonly
declined, and a milder rewording of the same idea normally passes. Offer
that rather than giving up.
