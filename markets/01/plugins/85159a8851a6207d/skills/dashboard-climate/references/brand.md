# MSCI Brand System (inlined — self-contained)

Everything needed to make a dashboard MSCI brand-compliant is here and in `assets/logos/`. This skill does not depend on any external brand skill.

## CSS variable block — paste into every dashboard `:root`

```css
:root{
  /* Brand */
  --msci-smokey-blue:#0626A9;  /* primary brand, headings, header gradient */
  --msci-primary-blue:#1A3FD6; /* subheads, links, accents, KPI numbers */
  --msci-daintree:#011B2B;     /* wordmark, primary text on light */
  --msci-turquoise:#00C4B3;    /* CTAs, primary buttons */
  --msci-sky-blue:#7188EF;     /* secondary accents, hover */
  --msci-powder-blue:#AEBAF0;  /* light accents, tag backgrounds */
  --msci-ice-blue:#F4F5FD;     /* section backgrounds, cards */
  /* Neutrals */
  --msci-black:#000000; --msci-charcoal:#4D4D4D; --msci-lead:#707070;
  --msci-flint:#999999; --msci-smoke:#CCCCCC; --msci-silver:#E6E6E6;
  --msci-dove:#F5F5F5; --msci-white:#FFFFFF;
  /* Values (financial up/down ONLY) */
  --msci-positive:#00A798; --msci-positive-strong:#118A5E;
  --msci-negative:#E02C1C; --msci-negative-mild:#FFC6B5;
  /* Type + shape */
  --msci-font:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;
  --msci-mono:'SFMono-Regular',Consolas,monospace;
  --msci-radius-sm:8px; --msci-radius-md:12px; --msci-radius-lg:16px; --msci-radius-xl:24px;
}
```

## Data-visualization palette

From the **MSCI Brand Visual Identity**, "Color palette — Data visualizations":
thirty colours forming a primary, secondary and tertiary palette "to be used in
all exhibits, charts and tables… in hierarchical order using 1 first and 30
last". Apply them in this order. Do not re-sort, and do not substitute another
palette.

```javascript
const MSCI_DATA_VIZ_COLORS = [
  // Primary 1–10
  '#16A3B6', // 1  Aqua
  '#D61A69', // 2  Raspberry
  '#561AD6', // 3  Violet
  '#F7620E', // 4  Orange
  '#1A7CD6', // 5  Azure
  '#529200', // 6  Lime
  '#831AD6', // 7  Amethyst
  '#DB7C00', // 8  Gold
  '#BC1AD6', // 9  Magenta
  '#D61A96', // 10 Fuchsia
  // Secondary 11–20
  '#107A88', // 11 Aquamarine
  '#A81452', // 12 Ruby
  '#4414A8', // 13 Dark Violet
  '#CA4D07', // 14 Burnt Orange
  '#1461A8', // 15 Sapphire
  '#366100', // 16 Evergreen
  '#6714A8', // 17 Purple
  '#A85F00', // 18 Mustard
  '#9414A8', // 19 Orchid
  '#A81476', // 20 Burgundy
  // Tertiary 21–30
  '#0B515B', // 21 Ocean
  '#7B0F3C', // 22 Plum
  '#310F7B', // 23 Indigo
  '#993A05', // 24 Copper
  '#0F477B', // 25 Cobalt
  '#1A2E00', // 26 Olive
  '#4B0F7B', // 27 Eggplant
  '#754200', // 28 Amber
  '#6C0F7B', // 29 Grape
  '#7B0F56', // 30 Raisin
];
```

**Tints.** Only the brand's own tints are permitted — never a computed opacity.
They exist for area fills and any fill sitting behind type; keep that type black.

```javascript
// 30% tints of the ten primaries, in the same slot order
const MSCI_TINT_30 = ['#B9E3E9','#F3BAD2','#CCBAF3','#FDD0B7','#BAD8F3',
                      '#CBDEB2','#DABAF3','#F4D8B2','#EBBAF3','#F3BADF'];
// 15% tints
const MSCI_TINT_15 = ['#DCF1F4','#F9DDE9','#E6DDF9','#FEE8DB','#DDEBF9',
                      '#E5EFD9','#ECDDF9','#FAEBD9','#F5DDF9','#F9DDEF'];
```

Two things follow from the hierarchy being fixed:

- Adjacent slots are **not** contrast-validated against each other; the order
  optimises for brand recognition, not pairwise separation.
- Tertiary (21–30) is deliberately dark and low-luminance. A chart deep enough
  to reach it should carry direct labels, or fold the tail into "Other".

Use the Values colours (`--msci-positive`, `--msci-negative`) for financial
up/down only — never for a categorical series.

## Typography

Load Inter: `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap`.

| Element | Weight | Size | Colour | Case |
|---|---|---|---|---|
| Page title | 600 | 30–32px | Daintree/black | Title Case |
| Section head | 600 | 20–24px | Primary Blue | Sentence case |
| Sub-heading | 600 | 16–18px | black | Sentence case |
| Body | 300 | 14–16px | black | Sentence case |
| Caption/label | 400 | 12–13px | Charcoal | Sentence case |
| KPI number | 600 | 36–48px | Primary Blue | — |

Product-name treatment: "MSCI" Semi-Bold ALL CAPS, product name Light Title Case (e.g. **MSCI** World).

## Logo

Inline the SVGs from `assets/logos/`: `msci-logo-rgb.svg` on light backgrounds, `msci-logo-white.svg` on dark/saturated (e.g. the header gradient). `view` the file, paste the `<svg>` inline, set a height (~28–34px in a header) and `width:auto`. Maintain clear space; never distort, recolour, or rearrange. Optional tagline "Clarity Drives Action" separated by a vertical rule.

## Component patterns

```css
.msci-card{background:var(--msci-white);border-radius:var(--msci-radius-md);padding:24px;
  box-shadow:0 1px 3px rgba(0,0,0,.08);border:1px solid var(--msci-silver);}
.msci-kpi{background:var(--msci-ice-blue);border:1px solid var(--msci-silver);
  border-left:4px solid var(--msci-primary-blue);border-radius:var(--msci-radius-md);padding:16px;}
.msci-kpi .num{color:var(--msci-primary-blue);font-weight:600;font-size:40px;line-height:1;}
.msci-btn{background:var(--msci-turquoise);color:#fff;border:0;border-radius:var(--msci-radius-xl);
  padding:10px 24px;font-weight:600;cursor:pointer;} /* pill CTA */
.msci-btn-secondary{background:transparent;border:1.5px solid var(--msci-primary-blue);
  color:var(--msci-primary-blue);border-radius:var(--msci-radius-xl);}
```

- **Header**: dark gradient `linear-gradient(135deg,var(--msci-daintree),var(--msci-smokey-blue))` with the white logo, title, sub-title, as-of stamp, and the Refresh pill top-right.
- **Tables**: alternating rows Dove `#F5F5F5` / White; header row Semi-Bold on Dove; cell padding ≥ 12px×16px; borders Silver or none. Rounded-corner container.
- **Cards / KPIs**: rounded corners, generous padding, coloured left border accent on KPI cards.
- **Rounded corners everywhere** (8–16px); circles for legend dots and accents. Generous white space (≥24px between sections).

## Responsive layout (prevent clipping)

Dashboards must not overflow horizontally on a narrow window. The common failure: a fixed multi-column KPI/metric row whose `1fr` tracks cannot shrink below their text, so when values widen (e.g. after refresh) the row blows out its container and clips the page.

- KPI / metric rows: `grid-template-columns:repeat(auto-fit,minmax(84px,1fr))` so they wrap by available space; never a fixed `repeat(N,1fr)` that can only break at a viewport media query. Add `min-width:0` to grid items and `overflow-wrap:anywhere` + a clamped font (e.g. `font-size:clamp(16px,3.4vw,21px)`) on large KPI numbers so they shrink instead of overflowing.
- Avoid breakpoint mismatches: do not let an inner row (KPIs) and its outer container (side-by-side cards) collapse at different widths — auto-fit on the inner row sidesteps this entirely.
- Wide tables: wrap in a container with `overflow-x:auto` (or set it on the card) so a table scrolls within its panel rather than widening the page.
- Header: `flex-wrap:wrap`; let long mono as-of lines `word-break:break-word`.
- Safety net: `body{overflow-x:hidden}` and `<meta name="viewport" content="width=device-width,initial-scale=1">`.
- Sanity-check the build at a narrow width (~380–700px), not just full screen.

## Chart rules

Charting library: **Highcharts**. Every rule below is from the MSCI Brand
Visual Identity, "Charts and graphs": *"Charts and graphs should be designed to
represent the information in the most simple and elegant way. Always adjust the
graphs to best fit the dimensions."*

**Colour.** Apply `MSCI_DATA_VIZ_COLORS` in hierarchical order, 1 first. Colour
follows the entity, never its rank — a filter that changes the series count
must not repaint the survivors. Where tints are needed, use `MSCI_TINT_30` /
`MSCI_TINT_15` only.

**Text.**
- Inter **Regular** and Inter **Semi bold**. No other family.
- Axis labels are semi bold and **1pt larger** than the rest of the values.
- Extra data points in semi bold.
- All text black; white only on a dark background.

**Lines and rules.**
- X- and Y-axis lines **0.5pt**, Silver `#E6E6E6`.
- The zero line is a **solid** `#707070`.
- Data lines **2pt**.
- Keep the charts as clean as possible — no per-point markers on a line. The
  brand's own reference chart draws ten series as bare strokes; identity comes
  from the legend.
- Never a dual-axis chart. Two measures of different scale get two panels
  sharing a category order, small multiples, or a common indexed base.

**Labels.**
- **Avoid Y-axis labels.** Put the unit in parentheses at the end of the chart
  title — "MSCI ACWI Performance (USD)", "Net Cash Flow (USD mn)".
- If X-axis labels don't fit, rotate them to **90°** — not 45°, which is
  Highcharts' default fallback and not a brand angle.
- Y-axis values: whole numbers. Integer + space + suffix for magnitudes
  (`25 M`), integer + `%` with no space for percentages, minus sign for
  negatives — never parentheses.

**Legend.**
- Centred under the chart, or to its right. Optimise for the space.
- **Circles** define the colour reference. Never squares or line segments —
  Highcharts cannot draw this natively, so render the swatch as HTML.
- Inter Regular, Title Case.

**Pie / donut.**
- Order slices largest → smallest, **clockwise**.
- Donut, not flat pie: a circular subtractive area in the centre.
- Label slices with name and value; leader lines for slices too small to hold
  a label.

**Tables.**
- Alternate row fills `#F5F5F5` (Dove) and `#FFFFFF`. Rounded-corner containers
  are preferred.
- Header row in Inter Semi bold on a Dove `#F5F5F5` background.
- Cell padding ≥ 12px × 16px; borders Silver or none.

**Source line.** Every chart and table carries its provenance beneath it — one
source per result, whichever tool produced the data.

## Accessibility & writing

- Text/background contrast ≥ 4.5:1 (≥3:1 for large text); clear heading hierarchy; descriptive labels; keyboard navigable.
- MSCI house style: American English, no serial commas, title case for page titles / sentence case elsewhere, spell out 1–9 / numerals for 10+, ISO currency before numerals (USD 20 billion), minimise abbreviations (spell out first use). Avoid em dashes.

## Do / Don't

DO: Inter only; Smokey/Primary Blue for headings; Turquoise CTAs; rounded corners + circles; the 30-colour palette in order; values colours for financial up/down only; inline SVG logo; let content breathe.
DON'T: colours outside the palette; non-Inter fonts; sharp corners on interactive elements; values colours for non-financial meaning; distort the logo; crowd the layout.
