---
name: Vacation Planner Pro
description: A calm, image-led trip decision desk for comparing and committing travel choices.
colors:
  harbor-ink: "#122d32"
  atlas-teal: "#0c6662"
  deep-teal: "#164d4d"
  seafoam-selection: "#dff2ec"
  quiet-mist: "#f2f7f5"
  paper: "#ffffff"
  soft-boundary: "#cadbd6"
  compass-gold: "#d99b2b"
  caution-clay: "#8f4a25"
typography:
  display:
    fontFamily: "Georgia, serif"
    fontSize: "clamp(30px, 5vw, 58px)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Georgia, serif"
    fontSize: "clamp(25px, 3vw, 36px)"
    fontWeight: 700
    lineHeight: 1.08
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  control: "10px"
  card: "16px"
  mast: "22px"
spacing:
  xs: "6px"
  sm: "10px"
  md: "16px"
  lg: "22px"
  xl: "34px"
components:
  button-primary:
    backgroundColor: "{colors.atlas-teal}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: "9px 13px"
    height: "42px"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.atlas-teal}"
    rounded: "{rounded.control}"
    padding: "9px 13px"
    height: "42px"
  decision-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.harbor-ink}"
    rounded: "{rounded.card}"
    padding: "16px"
---

# Design System: Vacation Planner Pro

## Overview

**Creative North Star: "The Traveling Decision Atlas"**

Vacation Planner Pro feels like a composed travel editor and a practical trip desk sharing the same surface. Destination photography supplies warmth and specificity; restrained teal structure keeps dense planning information trustworthy and navigable. The system is premium without becoming precious, and operational without feeling like a spreadsheet.

The interface favors one continuous story: orientation, current choices, itinerary, comparisons, budget, and evidence. It avoids promotional emptiness and keeps useful decision context on the card where a traveler needs it.

**Key Characteristics:**

- Image-led but evidence-conscious
- Calm, information-rich, and geographically grounded
- Strong selected states and transparent cost consequences
- Editorial headings paired with highly legible operational text

## Colors

The palette joins Atlantic teal and pale seafoam with white paper, dark harbor ink, and a scarce warm gold signal.

### Primary

- **Atlas Teal:** Primary actions, selected-card boundaries, and trusted links.
- **Deep Teal:** Hover states, secondary emphasis, and high-contrast supporting text.

### Secondary

- **Seafoam Selection:** Selected, ready, and helpful informational states.
- **Compass Gold:** Focus rings and short traveler-fit accents; it is a signal, not decoration.

### Neutral

- **Harbor Ink:** Primary text and deep tonal surfaces.
- **Quiet Mist:** Subtle data cells and low-priority grouping.
- **Paper:** Primary reading surfaces and cards.
- **Soft Boundary:** Dividers and card structure.

### Named Rules

**The Gold Means Look Rule.** Gold appears only where attention or traveler fit needs a deliberate cue.

**The Selection Must Read Twice Rule.** A selected choice uses both a stronger border and explicit text, never color alone.

## Typography

**Display Font:** Georgia (with serif fallback)  
**Body Font:** Inter (with system sans-serif fallbacks)

**Character:** Georgia introduces an editorial travel voice without external font dependencies. The sans-serif body remains compact and clear through comparison-heavy content.

### Hierarchy

- **Display:** Bold, responsive, tightly tracked; reserved for the trip title.
- **Headline:** Bold editorial serif; section orientation and major decision categories.
- **Title:** Bold editorial serif around 21px; individual hotels, experiences, restaurants, and transport options.
- **Body:** Regular 15px with generous 1.55 line height; descriptive and decision text.
- **Label:** Bold 12px; status, evidence, and compact data labels only.

### Named Rules

**The Editorial-Operational Pair Rule.** Serif type names the journey and the choices; sans-serif type explains, compares, and controls them.

## Layout

The page uses a centered container up to 1520px with a broad content column and a 300px sticky decision rail. Decision cards appear in two columns on desktop. At 1000px the rail drops below the content; at 680px all grids become one column and the section navigation scrolls horizontally. Spacing follows a compact 6/10/16/22/34px rhythm.

The first viewport holds the trip identity, four planning metrics, navigation, and a visual strip of current selections. The remaining categories form one continuous scroll rather than separate hidden tabs.

## Elevation & Depth

The system uses a restrained hybrid of boundaries and ambient shadow. Thin cool borders organize most surfaces; broad, low-opacity shadows lift only the masthead, panels, sticky rail, and hovered decision cards. Photography supplies the deepest visual layer.

### Shadow Vocabulary

- **Ambient panel:** `0 8px 22px rgba(0,0,0,.06)` separates reading surfaces from the mist ground.
- **Raised decision:** `0 15px 38px rgba(0,0,0,.12)` marks hover and focal containers.

### Named Rules

**The Border Before Shadow Rule.** Structure comes from boundaries first; shadow communicates hierarchy or interaction, not ornament.

## Shapes

Controls use gently rounded 10px corners, choice cards use 16px, and the trip masthead uses 22px. Pills are reserved for short statuses and tags. Media conforms to the card silhouette, while thumbnail buttons use tighter 7px corners. Shapes remain simple; the photographic content provides visual irregularity.

## Components

### Buttons

- **Shape:** Confident rounded rectangle with a 42px minimum height.
- **Primary:** Atlas teal with white text and compact 9px by 13px padding.
- **Hover / Focus:** Hover deepens to deep teal; keyboard focus uses a visible 3px compass-gold outline.
- **Secondary:** White with an atlas-teal border and text.

### Chips

- **Style:** Pale neutral or seafoam fill, compact bold text, and full pill geometry.
- **State:** Chips report status or attributes; they do not substitute for primary actions.

### Cards / Containers

- **Corner Style:** 16px choice cards and panels.
- **Background:** Paper over quiet-mist page ground.
- **Shadow Strategy:** Flat at rest for choices; ambient lift on hover and major containers.
- **Border:** One-pixel soft boundary; selected choices use a two-pixel atlas-teal boundary plus an explicit “Selected” action label.
- **Internal Padding:** 16px for decision cards and 24px for major panels.

### Inputs / Fields

- **Style:** Paper field, one-pixel soft boundary, and 8px corner radius.
- **Focus:** Shared compass-gold focus outline.
- **Behavior:** Numeric assumptions enforce their published minimum, maximum, and step.

### Navigation

The sticky section navigation is a white, bordered rail of compact text links. It scrolls horizontally on small screens and uses a seafoam hover surface. It contains destinations, never decorative icons.

### Image Gallery

Each decision card opens with 16:9 imagery, a quiet provenance link, and up to four image thumbnails. The selected thumbnail gains a gold boundary. Broken media produces a clear teal fallback naming the item; the fallback protects layout but does not replace pre-release media verification.

### Decision Rail

The rail keeps total, per-person cost, completion, current choices, research freshness, and reset within reach. It is sticky only where the viewport can support the two-column layout.

## Do's and Don'ts

### Do:

- **Do** give every decision candidate truthful, attributable imagery and visible practical detail.
- **Do** keep cost, tradeoffs, traveler fit, and evidence on the same card as the choice.
- **Do** use explicit labels alongside color for selection, readiness, and caution.
- **Do** preserve one continuous page with stable section anchors.

### Don't:

- **Don't** make external booking links the primary way to understand an option.
- **Don't** use unrelated stock imagery as if it depicted an exact property, venue, dish, vehicle, or tour.
- **Don't** turn the page into a uniform grid of generic icon cards or oversized empty marketing sections.
- **Don't** use decorative kickers, glyph icons, gradient text, or hard offset shadows.
