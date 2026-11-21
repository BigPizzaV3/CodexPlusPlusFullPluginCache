---
name: wignet-visuals
description: Design images for a Écran Papier colour e-paper frame (Spectra 6 panel) that print cleanly - choose from its six inks, pick a harmonious palette and fonts that stay sharp, size text for a panel read across a room, check the file before pushing it, and convert photos so their colours stay true. Use when composing a picture, poster, dashboard, card or illustration for a Écran Papier frame, or when a pushed image looks dotted, dull or muddy.
---

# Visuals for a Écran Papier colour frame

A Spectra 6 panel has six inks and nothing else: black, white, red, yellow,
green, blue. Every pixel is one of them. Any other colour is faked by
scattering dots of several inks (dithering), which looks grainy and dull
up close. Images that look good on the panel are mostly **solid inks**, drawn
in exact values, with mixes used on purpose. This skill covers designing for
that. Sending the image, the frame link and the verify loop are the `wignet`
skill; its `references/eink-design.md` has the sizes and reading distances.

## 1. Know the frame

- `get_capabilities` → `screen.display_profile`: this skill is for
  `spectra6`. On `mono1` (black and white) follow the `wignet` skill.
- `get_orientation` → compose at `logical_width × logical_height` exactly
  (800×480, or 480×800 in portrait), and push with its `orientation`.

## 2. The six inks

| Ink | Draw with (exact RGB) | Looks like on the panel | Lightness |
|---|---|---|---|
| black | `#000000` | `#000000` | 0 |
| white | `#FFFFFF` | `#FFFFFF` | 100 |
| red | `#FF0000` | `#A02020` brick red | 35 |
| yellow | `#FFFF00` | `#F0E050` warm yellow | 88 |
| green | `#00FF00` | `#608050` sage green | 50 |
| blue | `#0000FF` | `#5080B8` steel blue | 53 |

**Draw with the left column, think with the right one.** The converter
matches pixels against the pure values: `#00FF00` prints as solid green
ink, while `#608050`, the way that ink actually looks, is rebuilt from dots
of five inks. `scripts/inks.py palette` prints this table; in Python,
`from inks import INK` gives the draw-with values by name.

## 3. Rules that keep an image clean

1. **Only exact ink values** for text, lines, shapes and flat areas.
2. **No anti-aliasing.** Smoothed edges are in-between colours, which the
   converter dithers into a fuzzy halo. Pillow: `draw.fontmode = "1"`
   before drawing text; shapes are already crisp. No blur, no shadows, no
   gradients, no transparency over colour.
3. **Draw at the final size.** Resizing a finished design blends pixels
   into new colours. If you must, resize with `Image.NEAREST`.
4. **Send it as PNG**, never JPEG: compression shifts the exact values.
5. **Check before pushing:** `python3 scripts/inks.py check design.png`
   reports how much of the image is exact ink, what would be dithered and
   why, and writes the preview of what the panel will show.

## 4. Colour choices

- **Every mark informs** (Tufte): no purely decorative elements (swatch
  rows, frames, boxes, rules, ornaments). **Colour carries meaning**, one
  colour per meaning, the same everywhere on the screen (the alarm red in
  the headline and on the chart); anything without a meaning is black on
  white. Label data directly, not through a legend.
- **2–3 colours plus black and white** per screen. Roughly 60 % background,
  30 % one main colour, 10 % accent.
- Six palettes and styles that work, with example layouts, in
  `references/palettes.md`: *ink & accent* (white, black, a touch of red:
  dashboards), *primaries* (red, yellow, blue blocks with black lines),
  *warm morning* (cream, red, black: alarms, agenda), *cool calm* (white,
  blue, green, teal: weather, sea), *earth* (cream, green, brown, red:
  nature), *informative* (Tufte: one big figure, a sentence and a small
  chart as evidence, colour only for meaning, direct labels: schedules,
  forecasts).
- **Text** (contrast ratios; 4.5+ for body text):
  black on white 21, black on yellow 15.5, white on red 7.7 → any size.
  Black on blue 5.1, black on green 4.7 → headings only.
  **Never** white on yellow (1.4), black on red (2.7), or green against
  blue (almost the same lightness: edges vanish).
- Don't carry meaning by red versus green alone: common colour blindness,
  and the two are close in lightness.

## 5. Text

Judged on the panel; details and the reasons in `references/typography.md`.

1. **Crisp, never smoothed:** `draw.fontmode = "1"`. Smoothed edges are
   grey, and grey becomes a dotted halo.
2. **The font decides whether crisp text looks clean.** Judged on the
   panel: Arial, Verdana and Tahoma on macOS and Windows; Lucida Grande,
   Geneva and San Francisco on macOS; and **Bitstream Vera**, the best open font,
   **shipped in `fonts/`** so every sandbox has it. Ubuntu and PT Sans are
   good too. **Archivo Black** (shipped) for big numbers. Never Pillow's
   default font: it has no "à". `pick_font("text", 24)` in
   `scripts/inks.py` picks the best available; `inks.py fonts` lists them.
3. **Sizes (recommended):** 16 px minimum (`pick_font` warns below it).
   24 px is comfortable at 1 m, 48 px at 2–3 m; the one thing read at a
   glance 64 px and up (96 across a room).
4. **At most three sizes, one headline, about 40 words.** Left-align
   blocks; a number with its unit smaller beside it (`21°`). Normal letter
   spacing: never spaces between letters.
5. **Text that is mostly words** (a note, a reminder): send it as
   `push_content` `text`, and the platform sets it.

## 6. Layout on a grid

A Müller-Brockmann grid (details in `references/grid.md`, helpers in
`scripts/layout.py`):

- **The module is a 30 px line.** Body text 24 px on one line, larger sizes
  on whole lines. **Every baseline sits on a line**: text between lines
  floats.
- **Landscape: 6 columns** (40 px sides, the default: halves and thirds,
  several elements) **or 5 columns** (30 px sides, 124 px columns: a 2 + 3
  split, one dominant element). 30 px top and bottom, 3 rows of 4 lines.
  Portrait: 3 columns of 120, 5 rows.
- **Near** (1 m, default): labels 20, text 24, headings 48 px. **Far**
  (2–3 m): the same grid, the type doubled.
- **Loop:** lay out with `layout.py` (it writes the PNG and an editable
  `.json`), `layout.py lint screen.json`, look at `layout.py overlay` and
  `inks.py check`'s `.real.png` with a critic's eye, then fix: shorter text
  first, then a smaller step, then another layout.

## 7. Mixing inks, on purpose

A pixel holds one ink; a mix alternates two inks in a fine pattern the eye
blends. Mixes of inks of close lightness look smooth; a big lightness gap
shows as grain. Details and the full table: `references/mixing.md`.

- **Smooth, use freely for large areas:** teal (green + blue), cream
  (white + yellow), brown (red + green), plum (red + blue, the only purple).
- **Grainy, large areas seen from across the room only:** orange
  (red + yellow), pink (red + white), light blue (blue + white).
- **Avoid:** any mix with black (dark and grainy), and text over a mix.
- Draw mixes as exact patterns, not by picking an in-between colour:
  `fill_mix(image, box, "green", "blue", 8)` in `scripts/inks.py` (8 = 8/16
  of the second ink). An in-between colour gets random, noisier dithering.

## 8. Photos

The platform's converter matches photos against the pure ink values, so
greens and blues come out muddy and grainy. Convert the photo yourself:

```
python3 scripts/inks.py photo photo.jpg -o photo.png --width 800 --height 480 --fit cover
```

It matches against how the inks really look and writes only exact ink
values, which the platform then leaves untouched. Push the PNG as is (it is
larger than a JPEG: prefer `image_url` or `image_file` over `image_base64`
when you can). Photos with big simple shapes and strong colours work best;
fine detail and skin tones suffer most.

## 9. Deliver and look

Push with `push_content` (the `wignet` skill, §5): the PNG at the logical
size, the frame's `orientation`, `fit: contain`. If the owner can look at the
frame, ask: the panel is the only real preview. `inks.py check` also writes
`<name>.real.png`, the image as the panel shows its inks, for everyone else.
