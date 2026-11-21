# Designing for a Écran Papier panel

The panel is paper-like: no backlight, no grey on most units, read from
across a room, refreshed a few times an hour. What works on a phone often
fails here.

## Size and reading distance
- 800×480 on 7.5" ≈ 124 px per inch (128 on the 7.3" colour frame).
  Recommended: 16 px minimum; 24 px is comfortable at 1 m, 48 px at 2–3 m.
  `compose.py` warns when body text ends up small.
- Draw text crisp, in a font hinted for pixel screens (Arial, Verdana,
  Tahoma, or the open Bitstream Vera): on the panel they stay far cleaner
  than others (the `wignet-visuals` skill, `references/typography.md`).
- One idea per screen. If it needs scrolling on a phone, it is too much.
- Leave margins (≥ 1/16 of the short side): the frame's mat covers edges.

## Black and white (`mono1`)
- Only pure black and pure white exist. Grey is faked by dithering (a dot
  pattern): fine for photos, ugly on text and thin lines.
- Text, logos, QR codes, charts, icons → `mode: threshold`.
  Photos, gradients → `mode: dither`.
- Lines at least 2 px; avoid hairlines and light-grey fills (they vanish or
  turn to noise). Prefer solid black shapes and white space.
- Large black areas are fine: e-paper holds them without power.
- Charts: thick strokes, no gridlines, label directly instead of a legend,
  no colour-coded series (use patterns or labels).

## Six colours (`spectra6`)
- Inks: black, white, red, yellow, blue, green. Nothing in between: other
  colours are dithered from these.
- Use colour for one accent (a title, a warning), not for decoration.
- Pass `--profile spectra6` to `compose.py` and push without pre-reducing
  to black and white.
- For anything more designed than that (palettes, mixing inks, photos that
  keep their colours, checking a file before pushing), use the
  `wignet-visuals` skill (`read_skill` on the connector).

## Orientation
- Compose at `logical_width × logical_height` from `get_orientation`. The
  push inherits the frame's orientation, so it needs no `orientation` of its
  own (a different one is refused). A portrait frame is 480×800 logically.
- The orientation is the frame's, set once with `set_orientation`; services
  never carry their own.

## What the frame is not
- Not real-time: it wakes every `interval_seconds`. Don't display seconds,
  countdowns or "now playing".
- Not interactive: no touch, no buttons for the viewer.
- Not a notification screen: the owners chose a calm object. One image,
  changed on purpose.
