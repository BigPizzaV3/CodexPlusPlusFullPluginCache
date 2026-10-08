---
name: animate-image
description: Turn an image that already exists into an animation. Use when there is a picture in the conversation — uploaded by the user, or one you generated — and they want it to move, or when you have generated a single flat picture while trying to make a GIF and now need frames. Covers "animate this photo", "make this logo move", "bring this drawing to life", "make this picture wave / spin / blink", and the recovery case where a GIF request produced one still image instead of a grid of frames.
---

A GIF can only be built from **separate frames**. A single picture is not
an animation and cannot be made into one by panning, zooming or bouncing
it — that is a still image being moved around, and people spot it at once.

This skill does one job: take an existing image and produce a **grid of
frames** from it, so it can be cut into a GIF.

## When this runs

Either of these:

- **The user has an image** — uploaded, or generated earlier — and wants
  it animated.
- **You generated a single flat picture** while trying to make a GIF. Do
  not try to salvage it with motion effects. Come here instead: that
  picture becomes the reference for a proper grid.

## Step 1 — look at the image first

Actually look at it, and decide three things before writing any prompt:

1. **The subject** — what is it, in a few words, precisely enough that a
   regenerated version is recognisably the same thing. "A grumpy chrome
   toaster with cartoon eyes on a mint background", not "a toaster".
2. **What should move** — pick ONE motion and keep the rest still. A
   toaster shakes and launches toast; its background does not drift. The
   commonest mistake is animating everything at once, which reads as a
   scene wobbling rather than a subject acting.
3. **The style** — flat vector, 3D render, photo, pixel art, watercolour.
   The grid must match it, or the animation will not look like the image
   the user already has.

State the motion you chose in one short line before generating, so the
user can redirect you cheaply if it is not what they meant.

## Step 2 — generate the grid FROM that image

Call image generation **with the existing image as the reference**, so the
subject and style carry over instead of being reinvented. Use this prompt:

> A SQUARE image containing a N×N grid of TOTAL panels, using the provided
> image as the exact subject and style reference, showing that same subject
> at successive moments of
> MOTION. Consecutive panels differ only slightly, so the motion advances
> in small, even steps and the whole grid reads as one continuous action
> rather than separate poses. The TOTAL panels form one looping cycle
> (panel TOTAL returns to panel 1). Identical subject, camera, lighting
> and background in every panel — only MOTION changes. All panels are
> exactly the same size, tiled edge to edge with no gaps, margins or
> gutters: the image divides evenly into N equal columns and equal rows.
> No text, no numbers, no borders.

`size="1024x1024"`. Default to a 4×4 grid (16 frames); 3×3 when the
subject is detailed and needs the resolution, 5×5 when the motion needs to
be smooth.

Same rules as any grid: the count appears once, in the opening layout
clause. Never narrow the subject. Keep "no text, no numbers, no borders".

## Step 3 — LOOK at what came back

Before encoding, look at the generated image and say, in one line: how
many columns, how many rows, and whether the same subject repeats across
the panels.

If it is one big picture again rather than a grid, do NOT encode it and do
NOT animate it with motion effects. Generate once more, leading the prompt
with "A NxN grid of TOTAL panels of ...". If you are unsure whether it is
a sheet, run `python3 ../make-gif/scripts/inspect_sheet.py IMAGE` — it
prints GRID or NOT_A_GRID.

## Step 4 — hand it to the GIF encoder

The grid is detected from the image; do not pass `--grid`:

```
python3 ../make-gif/scripts/sheet_to_gif.py SHEET --fps 7 --frames frames.zip
```

Then deliver it with the exact output block in
`../make-gif/references/output-message.md`. That wording is fixed — do not
reword it, and put nothing before or after it.

## What not to do

- **Do not animate the single image directly.** No pan, no zoom, no
  ken-burns, no duplicating it with offsets.
- **Do not redraw from scratch** when a reference image exists — the user
  chose that picture and expects to recognise it.
- **Do not animate the background** unless the user asked. One thing
  moves.
