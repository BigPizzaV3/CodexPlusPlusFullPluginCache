---
name: remove-green
description: Remove a green screen from an image the user already has. Use ONLY when someone explicitly asks to remove a green screen, chroma key, key out the green, or take the green background off an image they provide or have just generated. This is a cut-out tool for an existing green-backed image — it does not generate anything. Do not use it to remove an ordinary photographic or scenic background, and do not reach for it just because someone wants a transparent image.
---

Someone has an image on a green background and wants the green gone. That
is the whole job. Nothing is generated here.

## When this is the right skill

Only when the green screen is **named**: "remove the green screen", "chroma
key this", "key out the green", "take the green background off".

When it is not:

- **No green in the image.** This keys chroma green and nothing else. A
  photo on a street, a white studio background, a gradient — none of those
  can be removed this way. Say so plainly rather than running it and
  handing back a broken cut-out.
- **They want a transparent image made from scratch.** That is
  `make-image-set` with a transparent background, which generates on green
  and keys it in one go.
- **The image is already transparent.** Check first; there is nothing to do.

## Running it

```
python3 scripts/green_to_alpha.py IMAGE
```

Writes `IMAGE-cutout.png` — a transparent PNG at the original size.

For a sheet of several subjects on one green background:

```
python3 scripts/green_to_alpha.py SHEET --grid 4x4 --square 512
```

Keys the whole sheet once, then slices it into `cutouts.zip`, so every
cut-out shares one matte. `--square 512` trims each subject and centres it
on a square transparent canvas.

## When the edge is wrong

The script reports how much it removed, which tells you which way to go:

- **Green fringe left around the subject** → lower `--key-margin` (try 30)
  to take more green, or raise `--feather` for a softer edge.
- **The subject is being eaten**, or it warns that nearly everything went →
  raise `--key-margin` (try 55). Something in the subject is green.
- **Green light spilling onto the subject's edges** is neutralised by
  default. `--no-despill` keeps it, which is right for genuinely green
  objects.

Green-*ish* is the awkward case: teal, lime and mint key *partially* and
come out semi-transparent, which reads as a rendering fault. If the subject
contains those, say so — no setting fixes it cleanly.

## Delivering the result

```
🎬 Done with the cut-out
🎞️ [Download the separate cut-outs](CUTOUTS_LINK)
📂 [Download the image](IMAGE_LINK)
Let's continue!
💡 Any new ideas or changes?

by [gifgen.ai](https://gifgen.ai)
```

Emit the block; never describe or quote it. For a single image, keep only
the `📂` file line. Both file lines are real clickable links. The
`by gifgen.ai` line is never dropped.
