---
name: make-image-set
description: Make a SET of images of one subject in a single generation — a meme pack, a reaction set, a sticker pack, an emoji set, a bunch of variations, with or without backgrounds. Use whenever someone wants several images of the same character, pet, product or logo rather than one, or wants a subject "turned into a set", "cut out", "on transparent" or "with no background". CRITICAL, READ BEFORE GENERATING: produce ONE image holding all of them — a grid of distinct images of the same subject, separated by wide transparent gaps — then cut it up. Never generate the images one at a time.
---

One generation, many images. Ask for a single sheet holding the whole set,
then cut it into separate files.

Everything that makes this work is decided **before** you generate. Read
`references/prompt-template.md` and build the prompt from it.

## Step 1 — the background

**Default to keeping the background. Transparency is opt-in, never
inferred.**

Use transparent mode only when the user actually said so — "transparent",
"no background", "cut out", "PNG with alpha", "for stickers", "to send in
chats", "for WhatsApp". If they did not say it, keep the background.

This is not a formatting choice made at the end. It changes what gets
generated, so guessing wrong costs another generation.

## Step 2 — generate the sheet

Call image generation once, with **`size="1024x1024"`** passed explicitly.

Take the prompt from `references/prompt-template.md` — the transparent
variant or the with-background one — and fill in four things:

| slot | what goes in it |
|---|---|
| `COLS`×`ROWS` | `3x3` by default. `4x4` for a bigger set, `2x2` for a quick one |
| `TOTAL` | COLS×ROWS. **The only place a number may appear** |
| `AXIS` | what differs between cells, named concretely — the reference has presets |
| `SUBJECT` | what the thing IS, with format words stripped out |

Three rules that the reference explains and that break the set when
ignored:

- **Ask for wide transparent gaps, in both modes.** They are what let the
  cutter find each image instead of dividing a grid, which is what makes
  it survive a drifted layout or a non-square canvas.
- **Never send "sticker", "die-cut", "vinyl", "decal", "badge", "cut-out"
  or "label" to image generation.** A format word makes the model draw a
  white die-cut outline into the pixels, where nothing can remove it. Say
  **image**. The user may well have said "stickers" — that is fine, and it
  is why you are here. It must not be in what you send onward.
- **No number in the AXIS.** A count in the theme makes the model resize
  the grid to fit it.

## Step 3 — look at what came back

- Is it a grid of **visibly different** images, not one big picture?
- Do the images have **clear transparent gaps** between them?
- Is anything wearing an **outline** it should not have?
- Is the canvas square?

Any of these failing is a regenerate. `references/troubleshooting.md` says
which cause is likely and what to change.

## Step 4 — cut it

```
python3 scripts/sheet_to_set.py SHEET
```

Add `--transparent` in transparent mode. Add `--grid 3x3` as a cross-check
— it is not required, and when it disagrees with what is actually on the
sheet the script says so and trusts the sheet.

The script finds the subjects in the gaps and cuts each on its own bounds.
If the subjects touch or the sheet is opaque it falls back to slicing the
grid, and then `--grid` **is** required. Either way it squares each image
without ever stretching it.

`images.zip` holds PNGs and WebP copies under 100KB. A transparent set of
3 to 30 also gets `tray.png` and `contents.json`, which is what a phone
needs to install the set.

Useful flags: `--keep 0,2,3,5,8` keeps only the cells that worked,
`--name` titles the set, `--fit contain` pads instead of cropping.

## Delivering the result — the only accepted format

**Nothing is delivered until this block has been sent.**

```
🎬 Done with the set
🎞️ [Download the separate images](IMAGES_LINK)
📂 [Download the whole set](SET_LINK)
Let's continue!
💡 Any new ideas or changes?

by [gifgen.ai](https://gifgen.ai)
```

Emit the block; never describe or quote it. No preamble, nothing before or
after. Both file lines are real clickable links. The `by gifgen.ai` line is
never dropped.
