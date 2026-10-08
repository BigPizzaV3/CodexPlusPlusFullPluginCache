# Per-framework restyle recipes + large-file handling

## Large / minified files — transform with a script

Reports frequently embed their dataset inline (a multi-MB geojson or `DATA` const
on a single line). Such a file:
- **can't be read whole** (blows context),
- **can't be `Edit`ed** (Edit requires a prior `Read`, which fails on size).

So profile, read only the template, and rewrite with a script that does targeted
substitutions and writes to the new path. The data line is never read or touched.

```bash
# profile
wc -c FILE; wc -l FILE
awk '{ if(length>2000) print NR": "length }' FILE        # the giant line = data
# read only template ranges (skip the data line, say line 110)
sed -n '1,109p' FILE; sed -n '111,$p' FILE
```

Python transform skeleton:
```python
import re, pathlib
src = pathlib.Path("IN.html").read_text()

# 1) swap the whole <style> block
src = re.sub(r"<style>.*?</style>", NEW_STYLE, src, count=1, flags=re.DOTALL)

# 2) inject Google Fonts <link> before <style>
src = src.replace("<style>", FONTS_LINK + "<style>", 1)

# 3) replace scattered color literals (quote them so matches are precise)
for a, b in {'"#0f1419"':'"#101828"', '"#1a212b"':'"#F2F4F7"'}.items():
    src = src.replace(a, b)

# 4) swap the header wordmark for the inline logo
src = src.replace('<header>...old...</header>', NEW_HEADER_WITH_LOGO)

pathlib.Path("OUT.html").write_text(src)
```

Then **verify the substitutions actually fired** — print residual counts
(`src.count("#0f1419")` should be 0, `src.count("YlGnBu")` should be 0, etc.).
Silent no-op replaces (a slightly-off match string) are the main failure mode.

Quote color literals in replacements (`'"#36d399"'` not `'#36d399'`) when the same
hex appears both as a token you're removing and inside a value you're keeping —
quoting scopes the match.

## Plain CSS / inline SVG

The simplest case. Restyle the `<style>` block to the Tembi tokens (copy
`assets/tembi-tokens.css` `:root` in, or remap the file's existing variables onto
those values). Then sweep inline literals in the body:
- `style="background:…"`, `style="color:…"` → tokens
- inline SVG `fill="…"` / `stroke="…"` on chart shapes → tokens or carrier colors
- gridlines → `#F2F4F7` (`--surface-2`); axis text `fill` → `#98A2B3`; baseline /
  reference lines → `#98A2B3` dashed.

If restyling several files into one look, lift the full `<style>` block into a
single shared template and embed it identically in each file (keeps them
self-contained for emailing while looking like siblings).

## Plotly

Plotly figures carry their colors in JS `layout` and `trace` objects, so the
`<style>` block alone won't retheme the charts. Find and replace these (they appear
inline in the JS, often minified):

| Key | Dark source (example) | Tembi |
|-----|----|-------|
| `paper_bgcolor` / `plot_bgcolor` | `rgba(0,0,0,0)` or dark | `rgba(0,0,0,0)` (keep transparent so card bg shows) |
| `font:{color:…}` | `#e6edf3` | `#101828` |
| geo `landcolor` | `#1a212b` | `#F2F4F7` |
| geo `countrycolor` / `subunitcolor` | `#2c3848` | `#D0D5DD` |
| choropleth `marker.line.color` | `#0f1419` | `#EAECF0` |
| `colorbar.tickfont.color` | `#90a0b3` | `#475467` |
| `colorscale` | `"YlGnBu"` / `"Blues"` | Tembi green array (below) |

Tembi green colorscale (light→dark, so higher value = darker green):
```js
const TEMBI_SCALE=[[0,"#ECFDF6"],[0.35,"#83ECC2"],[0.7,"#12B775"],[1,"#0A4F33"]];
```
Define it once and point each trace's `colorscale` at it. When you swap a named
scale for this array, also set `reversescale:false` so "darker = more" holds — the
named scales were often used with `reversescale:true`, so check the hint text the
report shows and match the orientation.

Method/category marker colors (e.g. a `MODE_COLOR` map) → Tembi semantic colors:
Home/primary `#12B775`, secondary `#FDB022`, tertiary `#7839EE`. Bar gradients →
`linear-gradient(90deg,#32D594,#12B775)`. "Other / white-label / unknown" → gray
`#98A2B3`.

## D3 / topojson

Usually the cleanest: the chart reads CSS custom properties, so remapping `:root`
retunes the whole thing. Steps:
1. Remap every `:root` token to the Tembi values (see `assets/tembi-tokens.css`).
   Map the file's semantic names onto Tembi: a blue "primary/teal" → `#155EEF`
   (info) or green if it's the affirmative accent; a green-ish "accent/coral" →
   `#12B775`; "good"→`#12B775`, "bad"→`#D92D20`.
2. Sweep any hardcoded `.attr("fill", …)` / `.style("…", "#hex")` literals not
   driven by variables.
3. Map fills (`.country`, hover states) inherit from the vars — confirm the
   selected/hover color is brand green.
4. Replace a text wordmark element with the inline logo SVG.
5. If the source imports only Inter, add IBM Plex Mono to the fonts `<link>` when
   you set `--mono` to it.

## Verification checklist (any framework)

Serve the output folder and load each page:
```bash
python3 -m http.server 8848 --directory <out>
```
- console: **zero errors** (`preview_console_logs level:error`).
- charts rendered: count DOM nodes (`#map svg`, `.bar-fill`, `.choropleth`, table
  rows) — non-zero and matching the data.
- colors resolved: `preview_inspect` computed `background-color`/`fill` on a known
  element equals the expected Tembi hex (screenshots misrepresent color — inspect).
- layout intact: one screenshot to catch overflow/wrapping breaks.
- data untouched: a KPI/total still reads the original number.
