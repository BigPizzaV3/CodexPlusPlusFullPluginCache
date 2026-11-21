# The page spec

`scripts/page.py` renders one JSON object into one HTML file. This is its format. The renderer computes no figure: it lays out the text and numbers it is given, checks that bridges tie, and formats chart values with thousands separators.

Every figure in a spec must come from a script's output or the calculator. Copy display text (tiles, table cells, summaries) exactly as the script printed it.

## Contents

- The page · Views · Tiles
- Blocks: bridge, line and bar, table, text
- What the page is · Errors

## The page

| Key | Type | Required | What it is |
| --- | --- | --- | --- |
| `title` | text | yes | The headline, in Finance plain: "September close: EBITDA up $28K on August" |
| `eyebrow` | text | no | The company or context above the title, shown with the Magnos mark |
| `summary` | text or list of texts | no | One short paragraph (a list makes several paragraphs) |
| `tiles` | list of tiles | no | Figure tiles under the summary; four fit one row |
| `blocks` | list of blocks | no | Charts, tables and text, in order |
| `views` | list of views | no | Several views and a switch between them (see Views) |
| `footer` | text | no | The source line: files, the skill, the date |
| `source` | object | no | Where the figures came from: `skill`, `files`, `run`; kept for people reading the spec. Used for the footer when `footer` is missing |

Unknown keys are ignored.

## Views

Each view is `{"label", "summary", "tiles", "blocks"}`. The labels become a segmented control under the title ("vs August", "vs budget"); the first view shows first. A view that leaves out `summary`, `tiles` or `blocks` uses the page's own. Without JavaScript, and in print, every view shows, one after the other, under its label.

## Tiles

```json
{"label": "Gross margin", "value": "61.6%", "change": "−0.2 pts", "direction": "down", "tone": "bad", "note": "vs August"}
```

- `label`, `value`: required text.
- `change`: the change as printed by the script, with its sign or unit ("+1.6%", "−0.2 pts", "−$70K").
- `direction`: `up`, `down` or `flat`; picks the arrow.
- `tone`: `good`, `bad` or `neutral`; picks the color. Default: up is good, down is bad. Set it for costs, where up is bad.
- `note`: a small line under the value, such as the period and baseline.

## Blocks

Every block takes `type`, and optionally `title`, `subtitle` (put the unit here: "$K"), `note` (a line under the block) and `wide` (span the full width; text blocks are wide by default). On a wide screen, blocks sit two to a row.

### bridge (also `waterfall`)

```json
{"type": "bridge", "title": "EBITDA, August to September", "subtitle": "$K",
 "bars": [
   {"label": "Aug", "value": 762, "total": true},
   {"label": "Revenue", "value": 80, "detail": "4000–4999 revenue accounts"},
   {"label": "Cost of revenue", "short": "Cost of rev.", "value": -40},
   {"label": "Sales and marketing", "short": "S&M", "value": -3},
   {"label": "R&D", "value": -6},
   {"label": "G&A", "value": -3},
   {"label": "Sep", "value": 790, "total": true}]}
```

- The first and last bars are totals (`"total": true`); a total in the middle is a subtotal.
- Steps are signed numbers in the subtitle's unit. Each total must equal the total before it plus the steps between them, exactly; the renderer stops with an error otherwise. When rounding to the unit breaks the tie, the script that made the figures puts the difference in the largest step and says so in `note` (the board-pack skill does this).
- `short` is used when the label does not fit under its bar; `detail` and the value show on hover.
- `display` overrides the value label ("+$80K"); by default totals show as "762" and steps as "+80" or "−40".
- Totals are navy, increases teal, decreases grey. When all levels sit in a narrow band far from zero, the axis starts near the lowest level, as finance bridges do.

### line and bar

```json
{"type": "line", "title": "Revenue by month", "subtitle": "$K",
 "x": ["Jan", "Feb", "Mar"],
 "series": [{"name": "Actual", "values": [4030, 4120, 4280]},
            {"name": "Budget v3", "values": [4150, 4250, 4350], "dashed": true}]}
```

- `x`: the categories. `series`: up to four, each with `name` and `values` (one per category; `null` for a gap). `dashed` draws a line series dashed.
- `bar` draws grouped bars from zero; with one series and at most 16 bars, each bar carries its value.
- `line` starts its axis at zero unless the values sit in a narrow band far from it; `"zero": true` forces zero.

### table

```json
{"type": "table", "title": "What moved",
 "columns": ["$K", "Aug", "Sep", {"label": "Effect on EBITDA", "tone": "sign"}],
 "rows": [
   {"cells": ["Revenue", "4,870", "4,950", "+80"], "role": "highlight"},
   {"cells": ["Cost of revenue", "1,861", "1,901", "−40"]},
   {"cells": ["EBITDA", "762", "790", "+28"], "role": "total"}]}
```

- `columns`: text, or `{"label", "tone", "align"}`. The first column is left-aligned, the rest right-aligned; `align` is `l` or `r`.
- `"tone": "sign"` colors that column's cells: "+80" and plain positive figures green, "−40" and "(610)" red; zero and empty cells keep the text color.
- `rows`: lists of cells, or `{"cells", "role"}`. A cell is text or `{"text", "tone"}` with `tone` `good`, `bad` or `neutral`.
- `role`: `total` (tinted and bold, with a rule above), `subtotal` (shaded and bold), `ratio` (italic and muted, for margins), `highlight` (tinted).
- The header row is Magnos navy. Wide tables scroll sideways inside their box at phone width.

### text

```json
{"type": "text", "title": "Next step", "body": "Ask the owner of sales and marketing which costs are above budget v3."}
```

`body` is text or a list of paragraphs; `items` is a list shown as bullets.

## What the page is

- One HTML file: inline CSS, inline SVG charts, and only when there are views, a few lines of plain JavaScript for the switch (arrow keys work).
- No network requests: no fonts, scripts, styles or images are fetched, and a Content-Security-Policy blocks any request. The fonts are the system's.
- Light and dark follow the reader's setting (`prefers-color-scheme`).
- At phone width the header stacks, tiles go two to a row, blocks go one to a row, and every chart swaps to a narrow drawing (bridges and bars turn horizontal).
- All text from the spec is escaped: a spec cannot add markup or scripts.
- The colors: Magnos navy `#021627` for table headers and totals, cyan `#00EAFF` only for the mark and the keyboard focus ring, green and red only for better and worse.

## Errors

The script exits with code 2 and one sentence when the spec file is missing, is not valid JSON, has no title, has a block of an unknown type, has a chart value that is not a number, a series whose length does not match `x`, a table row with the wrong number of cells, or a bridge that does not tie.
