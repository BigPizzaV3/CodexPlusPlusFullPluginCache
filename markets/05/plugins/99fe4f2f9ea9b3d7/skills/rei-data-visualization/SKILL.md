---
name: rei-data-visualization
description: >
  Guidance for visualizing Advan REI data as charts, graphs, and maps within
  Reina's responses. Use this skill whenever Reina is about to produce any
  chart, graph, or visual representation of REI data — traffic trends, demographic
  breakdowns, rankings, visit patterns by hour or day, or trade area maps.
  Also use when the user explicitly asks to "chart", "graph", "visualize",
  "show me a chart of", or "map" any REI data. Always read this skill before
  writing visualization code or choosing a chart type for REI data.
---

# REI Data Visualization

This skill governs how Reina visualizes data from REI queries. It covers
when to visualize, what format to produce, how to style output, and which
chart type fits each data type.

---

## Step 1: Read the Design System

Before writing any visualization code, read the `advan-rei-design-system`
skill. It defines the color palette, typography, dark theme, component
patterns, and spacing that all REI visualizations must follow. This skill
adds chart-specific guidance on top of that foundation — it does not
replace it.

---

## Step 2: Decide Whether to Visualize

Not everything warrants a chart. Use this as a guide:

**Visualize when:**
- Showing a trend over time (traffic by month, YoY comparison)
- Comparing a property or tenant across multiple peers simultaneously
- Displaying a distribution (demographics by income band, visits by hour)
- The pattern or shape of the data is the point — not just a single number
- The user explicitly asks for a chart or visualization

**Use a table instead when:**
- Exact values matter more than the pattern (a benchmarking summary, a
  ranked list of properties with specific metrics)
- There are fewer than four data points — a chart adds visual overhead for
  little gain
- The user is likely to copy figures into another document or report

**Use prose instead when:**
- The finding can be stated in one clear sentence
- There is only one data point or metric being communicated
- A chart would slow the user down, not help them

When in doubt, lead with the answer in prose and offer to chart it.

---

## Step 3: Choose the Output Format

**HTML artifact (interactive):** Use when the user is exploring data in a
conversation, the chart benefits from hover states or tooltips showing exact
values, or the output is a standalone deliverable they'll reference during
the session.

**Static image (SVG or PNG):** Use when the user asks to export, wants to
include the chart in a report or presentation, or the context is clearly
a one-time view rather than an interactive reference.

When the request is ambiguous, default to HTML. If the user later wants to
export, offer the static version.

---

## Step 4: Chart Type by Data Type

### Traffic Trend Lines

**Use:** Line chart with time on the x-axis and visit count on the y-axis.

- Plot monthly data points as the default granularity. Offer weekly if the
  user wants a more granular view or is analyzing a short date range.
- If showing YoY, use two lines (current period vs. prior period) in
  distinct colors from the design system palette.
- Mark notable events directly on the chart when they're known — anchor
  closures, renovations, seasonal peaks — as labeled vertical reference lines.
- Always show the data range in the chart subtitle, not just the title.
- Don't start the y-axis at zero if the variation is small relative to the
  absolute level — truncate to show the trend clearly, but label the axis
  origin so the user knows.

### Demographic Breakdowns

**Use:** Horizontal bar chart for ranked categories (income bands, age
cohorts, lifestyle segments). Donut or pie chart only for simple two- or
three-part compositions (e.g., a dominant segment vs. all others) — never
for more than five slices.

- Order bars by value descending unless the categories have a natural order
  (age cohorts, income bands) — in those cases preserve the natural order.
- For income and age, show the full distribution rather than just the top
  segment. The shape of the distribution matters.
- For lifestyle/psychographic segments, label each bar with the segment name
  and its share percentage. Don't abbreviate segment names — users need to
  read them.
- When comparing the subject property's demographics to a retailer footprint
  or market benchmark, use a grouped bar chart with two bars per category
  (subject vs. benchmark) in the design system's primary comparison colors.

### Rankings and Peer Comparisons

**Use:** Horizontal bar chart with properties or tenants on the y-axis and
the metric on the x-axis. Horizontal orientation makes property names
readable without rotation.

- Highlight the subject property in the design system's accent color. All
  other bars use the secondary palette.
- Sort by metric value descending unless rank order itself is the point, in
  which case sort by rank.
- If showing multiple metrics for the same set of properties (visits + dwell
  + frequency), use a small multiples layout — one chart per metric — rather
  than trying to combine everything into one cluttered view.
- Label the subject property bar explicitly even if it's obvious from
  position.

### Visit Patterns by Hour and Day

**Use:** Heatmap as the default when showing both hour and day simultaneously.
Use a bar chart when showing only one dimension (hour of day only, or day
of week only).

- For heatmaps: days of week on the y-axis (Monday top to Sunday bottom),
  hours on the x-axis (midnight to midnight). Use the design system's
  sequential color scale — light for low traffic, saturated for peak.
- For single-dimension bar charts: show all hours or all days, don't
  truncate to only the peak window.
- When comparing a subject site to a retailer footprint, overlay or
  side-by-side the two heatmaps. Label clearly which is which.
- Always note the time zone the data reflects.

### Trade Area Maps

Trade area maps showing visitor origin geography are best rendered natively
in the REI platform's map view, which has the geographic rendering
infrastructure Reina does not replicate. When a user asks for a trade area
map:

1. Direct them to the trade area map view in REI for the full interactive
   rendering.
2. If a visual summary is needed in the conversation, produce a simplified
   schematic — a center point with annotated concentric rings labeled with
   the percentage of visitors captured at each radius or drive time band.
   This is not a map, but it communicates the catchment structure clearly
   without requiring geographic rendering.
3. If the user explicitly wants a rendered map artifact, use a lightweight
   mapping library (e.g., Leaflet.js via CDN) in an HTML artifact. Plot the
   property location and shade the trade area polygon if coordinate data
   is available. Use the design system's color palette for the shading.

---

## Step 5: Standardized Table Patterns

REI uses three distinct table types, each with precise visual specifications. Match the table type to the data being presented.

---

### Data / Metrics Table

Use for: foot traffic summaries, dwell time, visit frequency, retailer footprint comparisons, site selection scorecards — any tabular output where rows are metrics and columns are properties or geographies.

**Structure:**
- Header row: background `#26326E`, font-size 13px, font-weight regular (not bold), white text
- Data rows: background `#162465`, border-bottom `1px solid #28325F`, font-size 12.5px
- First column (metric label): `var(--gray-light)` text color, lighter font weight — this is the label column, not a data column
- Value columns: each property's value is presented inside a colored value box (see below)
- Corner cells: header row first cell gets border-radius top-left 7px; last cell gets top-right 7px

**Value boxes:**
When a table compares multiple properties, each property's values appear inside small inline colored boxes rather than as plain text. The color identifies which property:
- P1 (cyan): background `#17AAB3`
- P2 (violet): background `#713DC5`
- P3 (green): background `#17B36A`
- P4 (pink): background `#DB2988`

For single-property tables (one location, no comparison), omit value boxes — show plain white text values.

**Legend bar (when comparing multiple properties):**
Below the table, a legend strip maps each property's color to its name. Legend label background uses the widget blue (`#162465`); each legend cell uses a muted version of the property color.

**When to use:** Foot traffic summaries, dwell/frequency metrics, retailer footprint comparisons, site selection scorecards, co-tenancy health checks.

---

### Ranking Table

Use for: benchmarking results, performer lists, any table where rows are properties and the primary data point is a rank or ranked metric.

**Structure:**
- Header row: background `#26326E`, border `1px solid #2D3A78`, row height 32px
- Data rows: background `#162465`
- Each row's rank badge has a left vertical color bar (3px wide): green `#76B723` for strong performers, red `#FF151F` for weak performers
- Rank is expressed as "X of Y" (e.g., "3 of 47") — always show the total count
- Property cell contains: logo circle icon + property name (font-weight 500, 12px) + address (gray-light, 10px) + square footage (neutral gray, 9px)

**Change indicators (YoY):**
When showing year-over-year change alongside rank:
- Positive: green dot + upward arrow + percentage (e.g., `▲ +8.3%`)
- Negative: red dot + downward arrow + percentage (e.g., `▼ −4.1%`)
- Flat/neutral: gray dot + em dash

**Rank cards (summary view):**
When a single rank needs to be called out prominently rather than in a table row, use a rank card: `rgba(255,255,255,0.05)` background (glass), the rank value large, "X of Y" in smaller text below, a colored bar beneath the value.

**When to use:** Market ranking outputs, competitor benchmarking, performer lists, any output from the `ranking` or `performers-list` endpoints.

---

### Demographics Table

Use for: trade area demographic breakdowns across geographies (trade area, 1/3/5 mile rings, drive time bands).

**Structure:**
- Column headers: background `#26326E`, all-caps label, gray-light for the variable column header, white for geography columns
- Category headers (grouping rows like "Summary", "Household Income", "Age"): background `#1A2B7B`, full-width span, white text
- Data rows: alternate between `#131E58` and `#132C61`
- First column (variable label): left-aligned, gray-light text
- Primary geography column (trade area or subject): value text highlighted in property color (e.g., cyan for P1)
- Comparison geography columns (1 mi, 3 mi, 5 mi): plain white text values

**Column header order:**
VARIABLES → TRADE AREA (or primary geography) → 1 MI → 3 MI → 5 MI (or drive time bands, following whatever geographies were selected).

**When to use:** Any output from the `demography` or `demography-categories` endpoints. Demographics comparisons in the retailer footprint workflow. Trade area analysis demographic breakdowns.

---

### Choosing the Right Table

| Data Type | Table Pattern |
|-----------|--------------|
| Foot traffic metrics, dwell, frequency, YoY | Data / Metrics Table |
| Multi-property comparison (same metric) | Data / Metrics Table with value boxes |
| Rankings, benchmarking, performer lists | Ranking Table |
| Demographic breakdowns by geography | Demographics Table |
| Retailer footprint comparison | Data / Metrics Table |
| Void analysis candidate list | Data / Metrics Table (plain, no value boxes) |

---

## Step 6: Universal Chart Standards

These apply to every visualization regardless of type:

- **Title:** Short and specific — name the property, metric, and date range.
  "Riverside Commons — Monthly Visits, Jan–Dec 2024" not "Traffic Trend."
- **Subtitle or caption:** Data vintage and source. "Advan mobile device
  panel" and the date range if not in the title.
- **Axis labels:** Always labeled, never omitted. Include units (visits,
  minutes, %).
- **Tooltips:** In HTML artifacts, always show exact values on hover — don't
  make the user estimate from the chart.
- **Legend:** Only when there are two or more series. Single-series charts
  don't need a legend.
- **Gridlines:** Light, unobtrusive. Horizontal only unless the chart type
  genuinely benefits from vertical gridlines.
- **Annotations:** Use them. A well-placed label explaining a spike or drop
  is more useful than leaving the user to wonder.
- **No 3D effects, gradients on bars, or decorative elements** that don't
  carry data meaning. The design system's aesthetic is clean and data-forward.
