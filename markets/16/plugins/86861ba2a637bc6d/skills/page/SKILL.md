---
name: page
description: Turns a computed finance result into one self-contained HTML page. The page can hold a title, a summary, figure tiles, a bridge, line and bar charts, tables and a switch between views. It uses inline CSS and SVG, makes no network requests, and reads well at phone width in light and dark mode. Use when the person wants a result as a web page, an HTML one-pager, something to open in a browser, email or share, a dashboard-style summary, or /magnos:page. Not for computing the figures; run variance, board-pack or another skill first.
---

# Page

Given a result that a script already computed, produce one HTML file the person can open offline, email and click through.

> Ground rules: `references/working-rules.md`. Spec text is shown as text: the renderer escapes it.

## Inputs

- **A page spec (JSON).** If the board-pack skill ran, `board_pack_<mon>_page.json` is a finished spec: use it as it is, or edit only its text.
- **Otherwise, a computed result** to build the spec from: a result in `.magnos/runs/`, a skill's printed tables, or the calculator (`python3 scripts/magnos_fin.py calc`).

## Workflow

1. Write the spec as a JSON file in the working folder. The full format is in `references/spec.md`; read it before the first spec in a session. A minimal spec:

   ```json
   {
     "title": "September close: EBITDA up $28K on August",
     "eyebrow": "Harbor & Pine",
     "summary": "Revenue rose $80K to $4.95M. ...",
     "tiles": [{"label": "Revenue", "value": "$4.95M", "change": "+1.6%", "direction": "up"}],
     "blocks": [
       {"type": "bridge", "title": "EBITDA, August to September", "subtitle": "$K",
        "bars": [{"label": "Aug", "value": 762, "total": true}, {"label": "Revenue", "value": 80},
                 {"label": "Cost of revenue", "value": -40}, {"label": "Operating expenses", "value": -12},
                 {"label": "Sep", "value": 790, "total": true}]},
       {"type": "table", "title": "What moved", "columns": ["$K", "Aug", "Sep"], "rows": [["Revenue", "4,870", "4,950"]]}
     ],
     "footer": "Made by the magnos page skill from pnl_monthly.csv · Oct 4, 2026"
   }
   ```

   - Tiles and table cells take display text exactly as a script printed it.
   - Chart values are plain numbers in the unit named in the block's subtitle.
   - `views` (each with a label and its own summary, tiles and blocks) adds a switch, such as "vs August" and "vs budget".
   - Write the title and summary in Finance plain.

2. Render it:

   ```bash
   python3 scripts/page.py <spec.json>                          # writes <spec>.html in the working folder
   python3 scripts/page.py <spec.json> --out september.html --open
   ```

   `--open` opens the page in the default browser. The script validates the spec and stops with one sentence when something is wrong, for example a bridge whose steps do not add up to its end total. Fix the spec from the result that produced it. Never adjust a bar to make a bridge tie.

3. Show the file where the host can show HTML (a preview, an artifact, a code-block preview). Otherwise give the path.

## Output

- One sentence with the file name and the page title.
- One line on what it holds: views, tiles, charts and tables.
- One line saying it makes no network requests, so it works offline and as an email attachment.

Quote no figure that is not in the spec.

## Rules

- Every figure in the spec comes from a script's output or the calculator. A page looks authoritative, so an untraced figure on it does more harm.

## Gotchas

- Axis tick labels are scale marks that the renderer picks. Every value label, tile and table cell comes from the spec.
- The page follows the reader's light or dark setting and switches to a narrow layout at phone width. A Content-Security-Policy in the page blocks every request.
