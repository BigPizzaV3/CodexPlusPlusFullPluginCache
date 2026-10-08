---
name: report-to-tembi-style
description: >-
  Restyle an existing standalone HTML report, dashboard, or data visualization
  into Tembi's visual brand (the EIP / ecom-new-frontend look) while preserving
  all data, copy, and charts. Use this whenever the user wants to convert,
  transform, restyle, re-skin, "tembi-fy", or apply Tembi branding to one or
  more `.html` files — including phrases like "make this report look like
  Tembi", "convert these dashboards to our styling", "apply our brand to this
  HTML", or "restyle this with the frontend design system". Also use it when the
  user drops HTML report files and asks to "transform" or "convert" them with no
  other target named. Works for plain-CSS reports and for chart-library
  dashboards (Plotly, D3/topojson, inline SVG). Not for building a report from
  scratch (this restyles existing markup) and not for restyling the live
  ecom-new-frontend app itself.
---

# HTML → Tembi style

Convert an existing standalone HTML report/dashboard so it looks like it came out
of Tembi's product, **without touching the data or the narrative**. The data,
numbers, copy, and chart logic are the client's deliverable and must survive
verbatim — your job is purely presentation: palette, type, chrome, chart colors,
logo.

## The one rule that matters most

**Restyle, never recompute.** Don't change numbers, labels, copy, chart math, or
which data points are shown. If you find yourself editing a value inside a `DATA`
const or a `<td>`, stop — that's out of scope. You touch CSS, color literals, the
`<style>` block, fonts, and the header/footer chrome. Nothing else.

## Step 0 — Confirm three decisions before writing anything

These change the whole job, so ask up front (one `AskUserQuestion` with all three
is ideal) unless the user already answered:

1. **Output location** — new folder in the repo (e.g. `reports/`), beside the
   originals, or overwrite in place. Default: a new folder; never overwrite an
   original unless told to.
2. **Restyle depth** — *token swap* (keep each file's layout/structure, only swap
   colors/fonts/cards) vs *unify into one shared Tembi template* (normalize
   several files onto one header/card/chart style). Token swap is faster and
   lower-risk; unify is right when restyling a set that should look like siblings.
3. **Accent handling for data series** — if the report charts carriers/brands,
   confirm: carrier data series use the **canonical carrier color map**
   (`assets/carrier-colors.json`); Tembi green is UI chrome only (eyebrows,
   KPIs, positive deltas, borders, active tabs). For non-carrier categorical
   series (e.g. markets/regions), pick a distinct categorical triad that does
   **not** collide with the brand green or a carrier blue.

## Step 1 — Inspect before reading

Reports are often huge because of embedded data (geojson, a multi-MB `DATA`
const). Reading the whole file will blow your context. First profile it:

```bash
wc -c FILE; wc -l FILE
awk '{ if(length>2000) print NR": "length }' FILE   # find giant data lines
```

If one line is enormous, it's the data — **never read it**. Read only the template
(head/`<style>`/body/scripts) with `sed -n` ranges that skip the data line.

A file too big to `Read` is also too big to `Edit` (Edit requires a prior Read).
For those, transform with a **script** (Python is easiest) doing targeted
string/regex substitutions and writing the output to the new location. See
`references/frameworks.md` → "Large / minified files".

## Step 2 — Identify the framework

How a report draws its visuals decides what you restyle beyond the `<style>` block:

- **Plain CSS / inline SVG** — restyle the `<style>` block and any inline `fill=`
  / `stroke=` / `style="background:…"` color literals.
- **Plotly** — restyle the `<style>` block **and** the color literals scattered in
  the JS `layout`/`trace` objects (geo colors, `paper_bgcolor`, font color,
  colorbar tick color, `colorscale`, marker line). Replace named colorscales like
  `"YlGnBu"`/`"Blues"` with a Tembi green scale.
- **D3 / topojson** — usually CSS-variable-driven; remapping `:root` plus any
  hardcoded `.attr("fill", …)` literals is enough.

`references/frameworks.md` has the exact keys/patterns per framework.

## Step 3 — Apply the Tembi design system

The canonical tokens live in `assets/tembi-tokens.css` — copy that `:root` block in
(or map the file's existing variables onto these values). Full reference and the
"why" behind each token is in `references/design-system.md`. The essentials:

- **Light theme only.** White / `#F9FAFB` surfaces, `#101828` ink, `#475467`
  muted, `#98A2B3` faint, `#EAECF0` lines. If the source is dark-themed, this is
  the biggest change — flip every dark surface/text value.
- **Fonts:** Inter (body + headings, weights 400–800) + IBM Plex Mono (numbers,
  axis labels, eyebrows, tabular figures). Add the Google Fonts `<link>`. Source
  fonts (Space Grotesk, Fraunces, Nunito Sans, etc.) get replaced.
- **Green is chrome, not data.** `#32D594` / `#12B775` for accents, CTAs, positive
  deltas, active states, borders. Never recolor a rival's data series green.
- **Cards:** white, `1px #EAECF0` border, 12px radius, soft shadow
  `0 1px 2px rgba(16,24,40,.04),0 8px 28px rgba(16,24,40,.05)`.
- **Logo:** embed `assets/tembi-logo.svg` inline in the header (and footer if the
  source had a wordmark there). Recolor its `fill` to `#101828` on light chrome or
  `#12B775` on a muted footer. Pair with a small green dot.

## Step 4 — Carrier colors (only if the report charts carriers)

`assets/carrier-colors.json` is the source of truth for delivery-carrier brand
colors. Look carriers up **case-insensitively** (keys are mostly lowercase
snake_case; a few are capitalized, e.g. `Smartposti`). Some values are null —
fall back to a neutral gray for those.

The subject carrier of a report keeps its own canonical color too — it does **not**
become Tembi green. Green stays UI-only.

**Contrast:** some carrier colors are pale (e.g. `lietuvos_pastas #FFDD00`). On a
white background or inside a colored fill, give them a darker text color or a
subtle border so they stay legible.

## Step 5 — Verify in the browser

Static HTML still needs a server for the preview tools. Start one rooted at the
output folder and check each file:

```bash
python3 -m http.server 8848 --directory <output-folder>
```

Then with the preview MCP (or Playwright): load each page, check
`preview_console_logs` for **errors** (zero expected), and confirm charts rendered
by querying the DOM (count SVG paths / bars / map traces) and reading computed
styles (`preview_inspect`) to confirm colors resolved to Tembi tokens — screenshots
alone are unreliable for color. A screenshot is good for catching layout breaks.
Iterate on anything broken before reporting done.

## Step 6 — Stamp every output (required, last step)

The analytics reports endpoint **rejects any report that isn't a validated Tembi
restyle** (`POST /reports` → 422). So the final step on every file is to stamp it —
do this only after the restyle is complete and verified, and re-stamp after any
later edit:

```bash
python3 scripts/restyle_sig.py stamp <file.html>          # overwrite in place
python3 scripts/restyle_sig.py validate <file.html>       # exit 0 = will pass the server
```

The stamp is a `<meta name="tembi-restyle" content="v=1;ts=…;hash=…">` tag injected
into `<head>`. The `hash` is a SHA-256 over the file's content with the stamp tag
removed (no secret) — it binds the stamp to the exact markup. The server re-runs the
same check `scripts/restyle_sig.py validate` performs:

1. The Tembi fingerprint is present — Inter + IBM Plex Mono, the canonical `:root`
   tokens, the embedded logo, and no leftover source-theme markers.
2. The stamp's hash matches the current content.

Editing a stamped file (changing a number, copy, anything) breaks the hash, so a
file edited without re-running the skill is rejected. **If you edit after stamping,
re-run `stamp`.** The fingerprint the validator checks is
`assets/tembi-restyle-fingerprint.json` — the same values as `assets/tembi-tokens.css`.

## What "done" looks like

Each restyled file: Inter + mono fonts, white background, green chrome, Tembi logo,
canonical carrier colors on data series, all original numbers/copy/charts intact,
zero console errors, **and a valid `tembi-restyle` stamp** (`scripts/restyle_sig.py
validate` exits 0). If you unified several files, an `index.html` landing page
linking them is a nice touch. Tell the user exactly what changed (palette, fonts,
logo, chart recolor), explicitly that no data was altered, and that each file is
stamped and will pass the server's validation.

## References

- `references/design-system.md` — full Tembi token table, fonts, component specs,
  and where each value comes from in `ecom-new-frontend`.
- `references/frameworks.md` — per-framework restyle recipes (plain CSS, Plotly,
  D3) and the large/minified-file script-transform pattern.
- `assets/tembi-tokens.css` — drop-in `:root` + base component CSS.
- `assets/tembi-logo.svg` — the Tembi wordmark to embed inline.
- `assets/carrier-colors.json` — canonical carrier brand-color map.
- `assets/tembi-restyle-fingerprint.json` — markers the stamp + server validator
  check (fonts, tokens, logo signature, forbidden source markers). Source of truth;
  a vendored copy lives in `api-flexible-analytics` next to the server validator.
- `scripts/restyle_sig.py` — `stamp` / `validate` CLI + importable logic (Step 6).
