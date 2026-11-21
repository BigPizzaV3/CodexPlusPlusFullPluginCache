# A typographic grid for the panel

After Josef Müller-Brockmann, *Grid Systems in Graphic Design* (1981): the
line of text is the module, and everything else is whole lines of it. Tried
on the panel in September 2026 with `scripts/layout.py`; these are
recommendations, not rules the tools enforce.

## The module

- **One line is 30 px** at 800×480. Body text is 24 px on one line; larger
  sizes take whole lines (48 px on two, 72 on three).
- **Every baseline sits on a line.** Descenders hang below it. Text centred
  between two lines looks as if it floats: the first thing the owner saw on
  the frame when the grid was drawn over a design.
- Margins, gutters, fields and gaps are whole lines too, so everything on
  the page lines up across columns: the baseline of a big figure with the
  third line of the sentence beside it.

## Two landscape grids (800×480)

Both have 30 px top and bottom, and 3 rows of 4 lines with a one-line gutter
(30 + 120 + 30 + 120 + 30 + 120 + 30 = 480).

| | 6 columns | 5 columns |
|---|---|---|
| Sides | 40 px | 30 px |
| Columns | 95 px, 30 px gutters | 124 px, 30 px gutters |
| Splits | halves (3 + 3), thirds (2 + 2 + 2) | 2 + 3, 3 + 2 |
| Use for | several elements of similar weight: dashboards, a figure and a sentence side by side, two or three data blocks | few, larger elements: a big figure beside a longer text, one chart with a caption column |
| Watch | a half is 345 px: short text lines, rewrite the text to fit | fewer ways to divide the page |

**The default is 6 columns**: the owner preferred it on the frame for the
alarm screen, by a small margin. Choose 5 when one element should dominate
and the text beside it needs longer lines.

**Portrait (480×800):** 30 px sides, 3 columns of 120 (or 2 of 195), 40 px
top and bottom, 5 rows of 4 lines.

## Reading distance: near and far

| Role | near (default, 1 m) | far (2–3 m) |
|---|---|---|
| Label, caption | 20 px, 1 line | 24 px, 1 line |
| Text | 24 px, 1 line | 48 px, 2 lines |
| Heading | 48 px, 2 lines | 72 px, 3 lines |
| The figure | cap height 3 lines (about 130 px) | 4 lines and up |

`far` keeps the geometry and doubles the type: the same grid holds half the
words. Cut the text, not the size.

## Placing things

- Hang the big figure from the top of its field: its capitals fill whole
  lines and its baseline lands on a line. Put its label **under** it, as a
  caption on the row's last line, rather than above, where the label's
  baseline would touch the figure's capitals.
- Text flush left, ragged right. Centre nothing but a lone short line.
- A chart takes whole fields; its labels also sit on the lines (tick labels
  on the field's last line), with a few pixels between the plotted data and
  a label line above it for descenders.
- Leave fields empty rather than filling them: the grid shows through white
  space.

## The loop: render, check, look, fix

Agents lay out best in a loop, not in one shot.

1. **Lay out with `layout.py`:** `Grid`, then `Layout` with `meaning()`,
   `text()`, `figure()`, `block()` and `graphic()`. `save()` writes the PNG
   and `<name>.json`, a description of every element (box, size, ink,
   baselines, overflow) that can be edited and re-rendered.
2. **Check:** `python3 scripts/layout.py lint screen.json` lists what breaks
   the recommendations: margins, off-grid boxes and baselines, colours with
   two meanings or none, text under 16 px, contrast by size, overflow,
   overlap, more than three sizes, colours that are not exact inks.
3. **Look:** `python3 scripts/layout.py overlay screen.png -o screen.grid.png`
   draws the grid over it, and `inks.py check` writes `<name>.real.png`, the
   inks as the panel shows them. Look at both as a critic: hierarchy, balance,
   what floats, what is crowded.
4. **Fix in this order:** rewrite the text shorter, then drop one size step,
   then change the layout (another split, the 5-column grid). Then go back
   to 2.

The panel is the final judge: if the owner can look at the frame, ask.

## The message board

The message board service follows the grid when its `vera` typeface is
chosen: flush left from the 40 px margin, baselines on the 30 px lines, body
and title sizes in whole lines (24/48, 48/72...), the largest that fits.
