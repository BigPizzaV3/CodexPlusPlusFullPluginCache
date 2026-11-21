# Typography on a Écran Papier panel

What follows was judged on a real 7.3" Spectra 6 panel (800×480, 128 px per
inch, about 159 × 95 mm), through a series of test cards, in September 2026.
Where a rule is a model rather than an observation, it says so.

## 1. Draw text crisp

The panel has no grey. Anti-aliased (smoothed) text edges are grey pixels,
which the converter dithers into a fuzzy halo. Draw text with smoothing off:

```python
draw = ImageDraw.Draw(image)
draw.fontmode = "1"          # before any draw.text()
```

Crisp rendering is unforgiving: a vector font's strokes snap to whole pixels,
and a poorly hinted font comes out with a stem 1 px wide in one letter and
2 px in the next. The font decides whether that shows.

## 2. Fonts

Five families per board, Regular and Bold, 8 to 48 px, judged on the panel:

| Font | Verdict | Where it exists |
|---|---|---|
| **Arial** | best, every size | macOS, Windows; Linux with Microsoft's core fonts |
| **Verdana** | very good | same |
| **Tahoma** (Verdana's narrower sibling) | very good | macOS, Windows |
| **Lucida Grande** | very good | macOS |
| **Geneva** (regular only) | very good | macOS |
| **San Francisco** | very good | macOS |
| **Bitstream Vera** | the best open font; **shipped with this skill** | `fonts/` here, everywhere |
| Ubuntu, PT Sans | good | Linux (Ubuntu often preinstalled on Ubuntu images) |
| Open Sans | good from 16 px only | Google Fonts |
| **Archivo Black** | big numbers, 48 px and up; **shipped** | `fonts/` here |
| Trebuchet MS, Georgia, Helvetica, Helvetica Neue | visibly less clean | macOS, Windows |
| Selawik, DejaVu Sans, Liberation Sans, Arimo | less clean than Vera | |
| Pixel fonts (tested: TRMNL 12/16/21) | pixel-exact but unattractive at 2–3× | |
| Pillow's built-in default (Aileron) | **no accented letters**: "à" draws as a box | never |

The good ones share one trait: hand-tuned hinting for black-and-white
screens (the 1990s screen fonts, and Bitstream Vera, made for Linux desktops
of 2003). An automatic measure of stem widths did not predict the verdicts;
the panel did.

`python3 scripts/inks.py fonts` lists which of these this machine has and
checks that each draws accented letters. `from inks import pick_font`
returns the best one available for a role (and warns under 16 px):

```python
from inks import pick_font
face, name = pick_font("text", 24)        # Arial, Verdana, Tahoma... else Bitstream Vera
title, _ = pick_font("headline", 96)      # Archivo Black (shipped)
label, _ = pick_font("label", 16)         # Verdana, Tahoma, Geneva... else Bitstream Vera
```

Because Bitstream Vera ships with the skill, a sandbox without system fonts
still sets text well.

## 3. Sizes

Recommended, from the owner's review of the panel:

- **16 px minimum:** smaller is hard to read. `pick_font` warns below it.
- **24 px is comfortable at 1 m** (a desk, a bedside table).
- **48 px at 2–3 m** (across a room).

| Role | At 1 m | At 2–3 m |
|---|---|---|
| The one thing read at a glance (time, temperature) | 64 px and up | 96 px and up |
| Text | 24–32 px | 48 px |
| Details (source, date, unit), labels | 16–20 px | 24–32 px |

What fits on 800×480 with 30 px margins: 48 px ≈ 29 characters × 7 lines;
32 px ≈ 44 × 10; 24 px ≈ 59 × 14. Across a room a screen holds a headline
and a sentence or two; cut the text, not the size.

## 4. Hierarchy and layout

- At most three sizes per screen, each step about 1.5–2× the one below
  (e.g. 96 / 48 / 24).
- One headline. Left-align blocks of text; centre only single lines.
- Line spacing 1.1–1.25 × the size; lines of about 35 characters at most.
  On the grid (`references/grid.md`) it is 1.25: 24 px text on 30 px lines,
  every baseline on a line.
- **Normal letter spacing.** Never put spaces between letters ("R É V E I L"
  reads as separate letters, not a word); capitals, if any, only for a
  one-word label, at normal spacing. Sentence case reads best.
- A number is often the whole point: make it the headline and set its unit
  smaller beside it (`21°`, `1.2 m`).
- Margins of at least 30 px: the frame's mat covers the edges.

## 5. Colour of text

Contrast of the inks as they look (WCAG ratio; 4.5 and more for body text):

- **Any size:** black on white (21), black on yellow (15.5), white on red
  (7.7), white on black.
- **Headlines only (40 px and up):** red text on white (7.7, a good accent),
  black on green (4.7) or blue (5.1), blue text on white (4.1).
- **Never:** yellow text on white (1.4), black on red (2.7), green against
  blue, text over a mix or a photo (put a solid box behind it).

## 6. Before pushing

`python3 scripts/inks.py check design.png` flags grey text edges (a small
share of stray colours) among its other checks. Then look at the frame if
the owner can: previews and measurements both misled us during these tests;
the panel did not.
