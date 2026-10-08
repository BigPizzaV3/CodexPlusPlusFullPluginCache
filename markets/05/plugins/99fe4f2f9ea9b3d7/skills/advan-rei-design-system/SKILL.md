---
name: advan-rei-design-system
description: >
  The authoritative design token reference for all Advan REI visual output —
  color palette, typography, spacing, border radius, widget structure, and
  component patterns. Read this skill before writing any HTML, CSS, or chart
  code for Reina. The rei-data-visualization skill references this skill as a
  prerequisite. Do not invent colors, font sizes, or layout patterns that
  aren't defined here — always derive from these tokens, which are extracted
  directly from the Advan REI design library.
---

# Advan REI Design System

This document defines every design token and structural pattern used in the
REI platform. All visual output Reina produces — charts, tables, widgets,
HTML artifacts — must conform to these specifications. All tokens are
extracted from the official Advan REI design library HTML.

---

## Foundation: Dark Theme

The REI interface is a dark navy application. Every visual artifact must use
this palette as its base — never white or light backgrounds.

| Token | Hex | Use |
|-------|-----|-----|
| `--bg-deepest` | `#0E1847` | Page / app background (outermost) |
| `--bg-deep` | `#101B4D` | Deep layer behind widgets, export drawers |
| `--bg-widget` | `#162465` | Widget body, data table cells |
| `--bg-section-hd` | `#1B2B7A` | Section heading rows within widgets |
| `--bg-table-hd` | `#26326E` | Table header rows |
| `--bg-subtle` | `#28325F` | Row dividers, subtle borders |

---

## Color Tokens

### Brand Blues (UI Structure)

| Token | Hex | Use |
|-------|-----|-----|
| `--blue-primary` | `#0061F3` | Interactive elements, modal nav, CTA buttons |
| `--blue-dark` | `#0F53C7` | Hover state for blue-primary |
| `--blue-light` | `#3F8CFD` | Highlighted button states |
| `--blue-lighter` | `#428AF5` | Secondary highlights |
| `--blue-ghost` | `#DBECFF` | Very subtle tint backgrounds |

### Extended Blues (Demographics / Panels)

| Token | Hex | Use |
|-------|-----|-----|
| `--bg-panel` | `#0B41AB` | Panel backgrounds |
| `--bg-panel-hd` | `#0E3894` | Panel header areas |
| `--bg-panel-deep` | `#112369` | Deep panel layers |
| `--bg-demo-cat` | `#1A2B7B` | Demographics category header rows |
| `--bg-demo-row` | `#131E58` | Demographics odd rows |
| `--bg-demo-alt` | `#132C61` | Demographics even rows (alternating) |

### Modal / Settings Shell

| Token | Hex | Use |
|-------|-----|-----|
| `--modal-nav` | `#0061F3` | Left nav column + right action column |
| `--modal-body` | `#0256D4` | Center content area |
| `--modal-btn` | `#3180F6` | Apply / Save / Reset buttons |

---

## Property Colors

Each property in a multi-property comparison is assigned one color track.
Always assign in order: P1 → cyan, P2 → violet, P3 → green, P4 → pink.
Never swap these assignments — cyan always means the first/primary property.

### Property 1 — Cyan

| Shade | Token | Hex |
|-------|-------|-----|
| Primary | `--cyan-primary` | `#17AAB3` |
| Dark | `--cyan-dark` | `#12888F` |
| Bright | `--cyan-bright` | `#00EEFA` |
| Muted | `--cyan-muted` | `#509EAA` |
| Bar / accent | `--cyan-bar` | `#46E2EF` |
| S1 (lightest) | `--cyan-s1` | `#A5F7FC` |
| S2 | `--cyan-s2` | `#39DBE3` |
| S3 | `--cyan-s3` | `#07A5AD` |
| S4 (darkest) | `--cyan-s4` | `#0B4D6D` |

Widget header background: `--cyan-primary` (`#17AAB3`), white text.
Value box background: `#17AAB3`.

### Property 2 — Violet

| Shade | Token | Hex |
|-------|-------|-----|
| Primary | `--violet-primary` | `#713DC5` |
| Dark | `--violet-dark` | `#4E2A89` |
| Bright | `--violet-bright` | `#AB7DF6` |
| Muted | `--violet-muted` | `#8240EA` |
| Bar / accent | `--violet-bar` | `#CAA8FF` |
| S1 | `--violet-s1` | `#D7C0FD` |
| S2 | `--violet-s2` | `#AB8AE1` |
| S3 | `--violet-s3` | `#8055C4` |
| S4 | `--violet-s4` | `#541FA8` |

### Property 3 — Green

| Shade | Token | Hex |
|-------|-------|-----|
| Primary | `--green-primary` | `#17B36A` |
| Dark | `--green-dark` | `#107D4A` |
| Bright | `--green-bright` | `#44E298` |
| Muted | `--green-muted` | `#15A15F` |
| S1 | `--green-s1` | `#B6F0D8` |
| S2 | `--green-s2` | `#7DC5A5` |
| S3 | `--green-s3` | `#459A73` |
| S4 | `--green-s4` | `#0C6F40` |

### Property 4 — Pink

| Shade | Token | Hex |
|-------|-------|-----|
| Primary | `--pink-primary` | `#DB2988` |
| Dark | `--pink-dark` | `#991D5F` |
| Bright | `--pink-bright` | `#E669AC` |
| Muted | `--pink-muted` | `#C5257A` |
| S1 | `--pink-s1` | `#FDC5E3` |
| S2 | `--pink-s2` | `#DC88B5` |
| S3 | `--pink-s3` | `#BB4B86` |
| S4 | `--pink-s4` | `#9A0E58` |

---

## Status Colors

Use for performance indicators, YoY change arrows, and rank badges only.
Never use these for property identity.

| Token | Hex | Use |
|-------|-----|-----|
| `--status-positive` | `#76B723` | Positive YoY, strong rank, green rank bar |
| `--status-negative` | `#FF151F` | Negative YoY, weak rank, red rank bar |
| `--status-neutral` | `#999999` | Flat / no change, neutral indicators |
| `--status-disabled` | `#707070` | Disabled or unavailable state |
| `--red-badge` | `#FE141E` | Alert badges |

---

## Neutrals

| Token | Hex | Use |
|-------|-----|-----|
| `--white` | `#FFFFFF` | Primary text on dark backgrounds |
| `--gray-light` | `#E4E4E4` | Secondary text, metric labels, address lines |

---

## Typography

**Font family:** `'Rubik', 'Google Sans Text', 'Roboto', sans-serif`
Import from Google Fonts: `Rubik:wght@300;400;500;600`

### Type Scale

| Token | Size | Common use |
|-------|------|------------|
| `--text-xs` | `8.75px` | Tertiary labels, badges, footnotes |
| `--text-sm` | `10.5px` | Addresses, supporting detail, pill buttons |
| `--text-base` | `12.25px` | Standard body, table cells, form fields |
| `--text-md` | `14px` | Default UI text, modal content, nav items |
| `--text-lg` | `15.75px` | Widget titles, section headings |
| `--text-xl` | `19.6px` | Section titles |
| `--text-2xl` | `22px` | Page-level headings |

### Font Weights

| Token | Value | Use |
|-------|-------|-----|
| `--fw-light` | `300` | Inactive nav items, secondary labels |
| `--fw-regular` | `400` | Body text, table cell values |
| `--fw-medium` | `500` | Active nav items, widget titles, button labels, property names |

---

## Spacing

| Token | Size |
|-------|------|
| `--gap-xs` | `4px` |
| `--gap-sm` | `8px` |
| `--gap-md` | `12px` |
| `--gap-lg` | `16px` |
| `--gap-xl` | `24px` |
| `--gap-2xl` | `32px` |

---

## Border Radius

| Token | Size | Use |
|-------|------|-----|
| `--r-none` | `0px` | Flush edges |
| `--r-xs` | `2px` | Micro elements, value boxes |
| `--r-sm` | `3.5px` | Buttons, pill segments, small chips |
| `--r-md` | `7px` | Cards, widgets, modals, table header corners |
| `--r-lg` | `17.5px` | Larger rounded panels |
| `--r-pill` | `26.25px` | Full pill shapes |
| `--r-full` | `50%` | Circles (logo marks, avatars) |

---

## Widget Structure

Every data widget follows this shell pattern:

```
┌─────────────────────────────────────────┐
│ WIDGET HEADER (property color bg)        │  ← colored per property P1–P4
│ Property name · metric · date range      │    font-size: 12–14px, fw-medium
├─────────────────────────────────────────┤
│                                         │
│  WIDGET BODY  (bg: #162465)             │  ← --bg-widget
│  Chart, table, or metric content        │
│                                         │
├─────────────────────────────────────────┤
│ LEGEND BAR (optional, multi-property)   │  ← --bg-widget, muted property colors
│ ● P1 Name   ● P2 Name                  │
└─────────────────────────────────────────┘
```

- **Outer border-radius:** `--r-md` (7px) on all corners
- **Header padding:** `12px 16px`
- **Body padding:** `12–16px`
- **Header background:** primary property color (`--cyan-primary` for P1). For multi-property or no-owner widgets, use `--bg-table-hd` (`#26326E`).

---

## Component Patterns

### Value Boxes

Small inline colored rectangles in data tables that tie a metric value to
its property color.

```css
background: var(--cyan-primary);   /* or violet / green / pink per property */
color: #FFFFFF;
border-radius: var(--r-xs);        /* 2px */
padding: 2px 6px;
font-size: var(--text-sm);         /* 10.5px */
font-weight: var(--fw-medium);     /* 500 */
display: inline-block;
```

Use value boxes when a table column belongs to a specific property. Omit them
for single-property tables — use plain white text instead.

### Rank Badges

Left vertical bar (3px wide, full cell height) + rank text "X of Y".

```css
/* Positive / strong performer */
border-left: 3px solid var(--status-positive);   /* #76B723 */

/* Negative / weak performer */
border-left: 3px solid var(--status-negative);   /* #FF151F */
```

Always format rank as `"X of Y"` — include the total count, never just the rank number.

### Change Indicators (YoY)

Shown alongside metric values in ranking tables.

- Positive: `▲ +8.3%` in `--status-positive` (`#76B723`)
- Negative: `▼ −4.1%` in `--status-negative` (`#FF151F`)
- Flat: `— ` in `--status-neutral` (`#999999`)

### Rank Cards

Standalone rank callouts (e.g., in a summary section):

```css
background: rgba(255, 255, 255, 0.05);   /* glass effect */
border-radius: var(--r-md);              /* 7px */
padding: var(--gap-md);                  /* 12px */
```

Value displayed large (14–16px, fw-medium), "X of Y" in smaller text below,
colored rank bar at bottom using the status color conventions.

### Pill / Segmented Buttons

```css
font-size: var(--text-sm);              /* 10.5px */
height: 26px;
padding: 0 8.75px;
border: 0.833px solid rgba(255, 255, 255, 0.15);
border-radius: 0;
background: transparent;
color: white;
font-family: var(--font-primary);

/* Active state */
background: rgba(255, 255, 255, 0.15);
border-color: rgba(255, 255, 255, 0.15);
```

First item in group: `border-radius: 3.5px 0 0 3.5px`
Last item in group: `border-radius: 0 3.5px 3.5px 0`

### Property Cell (Ranking Table Row)

Each row in a ranking table identifies the property with:
- Circular logo icon (50% border-radius)
- Property name: 12px, fw-medium (500), white
- Address: 10.5px, fw-light (300), `--gray-light`
- Square footage: 8.75px, neutral gray

---

## CSS Starter Block for HTML Artifacts

Include this in every `<head>` before any other styles:

```html
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600&display=swap" rel="stylesheet" />
```

Declare these tokens on `:root`:

```css
:root {
  --font-primary:   'Rubik', 'Google Sans Text', 'Roboto', sans-serif;

  /* Backgrounds */
  --bg-deepest:    #0E1847;
  --bg-deep:       #101B4D;
  --bg-widget:     #162465;
  --bg-section-hd: #1B2B7A;
  --bg-table-hd:   #26326E;
  --bg-subtle:     #28325F;
  --bg-demo-cat:   #1A2B7B;
  --bg-demo-row:   #131E58;
  --bg-demo-alt:   #132C61;

  /* Blues */
  --blue-primary:  #0061F3;
  --blue-dark:     #0F53C7;
  --modal-nav:     #0061F3;
  --modal-body:    #0256D4;
  --modal-btn:     #3180F6;

  /* Property colors */
  --cyan-primary:   #17AAB3;
  --cyan-bar:       #46E2EF;
  --cyan-muted:     #509EAA;
  --violet-primary: #713DC5;
  --violet-bar:     #CAA8FF;
  --green-primary:  #17B36A;
  --pink-primary:   #DB2988;

  /* Status */
  --status-positive: #76B723;
  --status-negative: #FF151F;
  --status-neutral:  #999999;
  --status-disabled: #707070;

  /* Neutrals */
  --white:         #FFFFFF;
  --gray-light:    #E4E4E4;

  /* Typography */
  --text-xs:    8.75px;
  --text-sm:    10.5px;
  --text-base:  12.25px;
  --text-md:    14px;
  --text-lg:    15.75px;
  --text-xl:    19.6px;
  --fw-light:   300;
  --fw-regular: 400;
  --fw-medium:  500;

  /* Spacing */
  --gap-xs:  4px;
  --gap-sm:  8px;
  --gap-md:  12px;
  --gap-lg:  16px;
  --gap-xl:  24px;
  --gap-2xl: 32px;

  /* Radius */
  --r-xs:   2px;
  --r-sm:   3.5px;
  --r-md:   7px;
  --r-lg:   17.5px;
  --r-pill: 26.25px;
  --r-full: 50%;
}

body {
  font-family: var(--font-primary);
  background: var(--bg-deepest);
  color: var(--white);
  font-size: var(--text-md);
  line-height: 1.5;
}
```

Chart libraries (Chart.js, etc.) may be loaded from `https://cdnjs.cloudflare.com`.
Chart canvas backgrounds must match `--bg-widget` or `--bg-deepest` — never white.
