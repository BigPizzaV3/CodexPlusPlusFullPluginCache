# The prompt

Short, one paragraph per clause, nothing hedged. Length is not what makes
a grid come out right — the gaps are.

`COLS`×`ROWS` is the grid, `TOTAL` is COLS×ROWS, `AXIS` is what differs
between cells, `SUBJECT` is what the thing is.

## Transparent (the user asked for no background)

> Create a single square (1:1) transparent sheet: exactly TOTAL distinct
> images of SUBJECT arranged in a COLS×ROWS grid, each a different AXIS.
> Separate them with wide, fully transparent gaps. No two alike.
>
> Transparent background throughout — no backdrop, no shadows, nothing
> overlapping.
>
> Each subject has its own natural edges, with nothing added around it: no
> outline, no border, no keyline, no halo, no frame.

## With a background (the default)

> Create a single square (1:1) sheet: exactly TOTAL distinct images of
> SUBJECT arranged in a COLS×ROWS grid, each a different AXIS. Each
> image is complete in itself with its own background. No two alike.
>
> Separate them with wide, fully transparent gaps — the gaps carry no
> colour, no border and no frame.
>
> Nothing is added around a subject: no outline, no keyline, no halo.

## Why the gaps are the whole trick

They are not cosmetic. Gaps mean each image is its own island of
transparency, so the cutter **finds** the subjects instead of dividing a
grid — which is what makes it survive a layout that drifted, a canvas that
came back non-square, and gaps of uneven width. Ask for the gaps in both
modes, always, even when the subjects carry their own backgrounds.

The cost is resolution: at 1024 with wide gaps each subject is roughly
250px before it is scaled to 512. Worth it.

## AXIS — name it concretely

Abstract instructions ("vary widely") produce nine of the same thing.
Naming six or so real examples produces range. The count never appears
here — it lives in the layout clause only, or the model expands the grid
to fit the theme.

Each preset is written to read grammatically after *"each a different"* —
keep that shape when you write your own.

**meme / reaction** — the default for a set meant to be sent in chats

> exaggerated internet reaction — crying, confusion, shock, smugness,
> side-eye, deadpan disbelief — in awkward poses, with absurd humour

**emotion** — `emotion: delighted, furious, heartbroken, smug, exhausted, startled`
**outfit** — `outfit: winter coat, swimwear, black tie, tracksuit, armour, raincoat`
**job** — `job: chef, astronaut, mechanic, barista, surgeon, DJ`
**season** — `season: spring bloom, high summer, autumn leaves, deep snow, monsoon`
**art style** — `art style: flat vector, 3D render, hand-drawn, pixel, line art, painterly`
**colourway** — `colourway, one distinct palette per cell, same pose and framing`

If the user names an axis, use theirs, worded as concretely as these.

## SUBJECT — strip the format words out

SUBJECT is what the thing **is**, not what it is for. Take the user's words
and drop every word describing the output format; keep all the rest exactly
as written.

| the user asks | SUBJECT becomes |
|---|---|
| "a sticker pack of my dog" | `my dog` |
| "stickers of a furious little cactus" | `a furious little cactus` |
| "meme pack of a winking holographic blob" | `a winking holographic blob` |
| "cut-out images of my logo for WhatsApp" | `my logo` |

Never narrow what is left. "A furious little cactus" does not become "a
cactus".

**Never send these to image generation:** sticker, die-cut, vinyl, decal,
badge, cut-out, label. Say **image**. The word will be in what the *user*
wrote — that is fine. It must not be in what you send onward.

## Attachments

If the user attached an image, pass it as the input image and write the
subject as the character in the reference. The sheet is still one
generation, still one grid.
