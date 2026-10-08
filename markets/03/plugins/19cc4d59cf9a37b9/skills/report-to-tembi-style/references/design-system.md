# Tembi design system reference

Mirrored from the EIP frontend, `ecom-new-frontend` (Nuxt 3 + Vuetify 3 + SCSS).
Source files if you need to re-derive anything:
- `ecom-new-frontend/assets/css/colors.scss` — color variables
- `ecom-new-frontend/assets/css/main.scss` — global overrides
- `ecom-new-frontend/plugins/vuetify.ts` — theme config
- `ecom-new-frontend/assets/logos/tembi.svg` — logo (bundled here as `assets/tembi-logo.svg`)

**Single light theme.** Vuetify config is `dark:false`; there is no dark mode. Every
restyle targets a light background.

## Color tokens

| Token | Hex | Use |
|-------|-----|-----|
| paper | `#FFFFFF` | page background |
| surface | `#F9FAFB` | inset / secondary surface, faint page bg |
| surface-2 | `#F2F4F7` | bar tracks, hatches, hover rows |
| card | `#FFFFFF` | card/panel background |
| ink | `#101828` | primary text, headings |
| ink-2 | `#1D2939` | slightly softer heading |
| muted | `#475467` | secondary/body text |
| faint | `#98A2B3` | labels, captions, axis text |
| line | `#EAECF0` | default borders, dividers |
| line-2 | `#D0D5DD` | stronger borders, input outlines |
| green | `#32D594` | primary brand accent, CTA, active |
| green-deep | `#12B775` | hover, positive, links, emphasis |
| green-ink | `#0A4F33` | text on green-wash backgrounds |
| green-wash | `#ECFDF6` | light green panel bg |
| green-100 | `#D1FAE8` | pill/badge bg |
| pos | `#12B775` | positive delta |
| neg | `#D92D20` | negative delta |
| warn / warn-bg / warn-ink | `#FDB022` / `#FFFAEB` / `#B54708` | warning |
| info / info-bg | `#155EEF` / `#EFF4FF` | info / neutral-blue accent |

The fuller brand green ramp (from `colors.scss`) if you need intermediate stops:
`#ECFDF6` 50 · `#D1FAE8` 100 · `#83ECC2` 300 · `#32D594` 400 · `#12B775` 500.

### Brand green is UI chrome, not data

Green colors the *product*: eyebrows, KPI accents, positive deltas, active tabs,
borders, CTAs, links. It must not color a data series — a carrier, a competitor, a
category. Data series use the canonical carrier map (`assets/carrier-colors.json`)
or, for non-carrier categories, a neutral categorical palette. Mixing the two makes
"is this the brand or is this a data point?" ambiguous, which is exactly the
confusion to avoid.

### Categorical (non-carrier) palette

When a report charts markets/regions/segments rather than carriers, you still need
several distinct series colors. Pick a triad/quad that stays clear of the brand
green and of carrier blue, e.g. info blue `#155EEF`, purple `#7839EE`, warm
`#E47649`, teal `#0E9384`. Reserve red `#D92D20` for "loss/negative" so it doesn't
double as a category.

## Typography

- **Inter** — body and headings. Weights 400/500/600/700/800. Headings 700–800 with
  `letter-spacing:-.02em`.
- **IBM Plex Mono** — numbers, KPI values, axis labels, eyebrows, table figures,
  provenance lines. Use `font-variant-numeric:tabular-nums` for aligned digits.
  (The live app is Inter-only, but reports lean on tabular numerals heavily, so a
  neutral mono earns its place.)

Google Fonts link:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

Heading scale (from the app): h1 30 / h2 24 / h3 20 / h4 18 (700); h5 16 / h6 14
(600). Reports can scale h1 up with `clamp()` for cover impact.

## Components

- **Card/panel:** `background:#fff; border:1px solid #EAECF0; border-radius:12px;
  box-shadow:0 1px 2px rgba(16,24,40,.04),0 8px 28px rgba(16,24,40,.05)`.
  (App uses 8px radius for compact UI; 12px reads better for large report panels.)
- **Pill/badge:** fully rounded (`999px`), mono, `#D1FAE8` bg / `#0A4F33` text for
  the affirmative variant; gray for neutral.
- **Table:** mono uppercase header in `#98A2B3` with a `#EAECF0` bottom border; row
  divider `#F2F4F7`; hover `#F2FBF7`; numeric cells mono + tabular.
- **Bars:** track `#F2F4F7`, fill in the series color (green for a brand metric,
  carrier color for a carrier), 6px radius, width transition for animation.
- **Buttons (in interactive dashboards):** white bg, `#12B775` text, `1px #D0D5DD`
  border, hover `#D1FAE8`.
- **Active tab:** `#12B775` text + green underline or green-tinted background.

## Logo

`assets/tembi-logo.svg` is the wordmark (72×18 viewBox, single path). Embed it
inline so it inherits no external dependency. Set the path `fill`:
- `#101828` on white/light header chrome
- `#12B775` on a muted footer
Pair with an 8px green dot (`#32D594`) and optionally a thin `#D0D5DD` divider before
a kicker/tagline. A lowercase "tembi" text wordmark in a source file should be
replaced with this SVG.
