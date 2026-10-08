---
name: edit-gif
description: Change a GIF or animation already made in this conversation — speed it up or slow it down, loop it back and forth, boomerang or ping-pong it, remove or reorder frames, make the file smaller, or fix a visible seam or edge. Use for "make it slower", "speed that up", "make it bounce", "drop the last frame", "that one's too big", and anything else that adjusts an existing animation rather than creating a new one. Never regenerate the image for an edit: re-encode the sprite sheet that already exists.
---

Every one of these is a **re-encode of the sprite sheet that already
exists** in this conversation. Never generate a new image for an edit: it
costs a generation and, worse, comes back as different artwork — the user
asked to change the animation, not to replace it.

Find the sheet from the earlier turn and re-run the encoder from the
`make-gif` skill with different options:

```
python3 ../make-gif/scripts/sheet_to_gif.py SHEET --fps 10 --boomerang
```

| They say | You change |
|---|---|
| slower / faster | `--fps` (1–15, default 7) |
| back and forth, ping pong, bounce | add `--boomerang` |
| drop the third frame | `--skip 2` — indexes are 0-based |
| lose the last two | `--skip 14,15` on a 4x4 |
| reorder / swap frames | `--order 0,2,1,3,...` |
| smaller file, too big | lower `--size`, then `--colors` |
| edges look clipped | `--crop 0` (3% is trimmed by default) |
| thin seam or line flickering | raise `--crop` to 5 |
| colours look flat / banded | raise `--colors` toward 256 |
| file far too big | add `--no-dither` first, then lower `--size` |
| sharper, higher quality | raise `--size` (448 default), then `--colors` |

Keep every other option the same as the previous render, so one change is
one change. If they ask for two things, apply both in a single re-encode
rather than producing two files.

**The edit is not delivered until this block has been sent.** Write the
file somewhere fetchable, then emit exactly:

```
🎬 Done with the GIF
🎞️ [Download the separate frames](FRAMES_LINK)
📂 [Download the GIF](GIF_LINK)
Let's continue!
💡 Any new ideas or changes?

by [gifgen.ai](https://gifgen.ai)
```

Same fixed wording as `make-gif` — see
`../make-gif/references/output-message.md`. Drop the 🎞️ line unless the
frames were re-exported (`--frames`). Do not reword anything, do not add a
note about what changed, nothing before or after.

The grid is detected from the sheet, so there is nothing to keep in sync
between renders.

## When this does NOT apply

If they want a different subject, a different motion, or a different
style, that is a new animation — use `make-gif` to generate a fresh sheet,
or `animate-image` if they are pointing at an existing picture. The
dividing line is whether the artwork itself should change.
