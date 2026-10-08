---
name: eventhex-website-design
description: Precise website design control — set_design targets, section structure, typography, and authoring an original V3 template spec.
---

# Website design — precise control

All design tools publish live immediately (no draft step).

## Always start with `list_design_options(eventId)`

Returns valid fonts, presets, section types + variants, per-type `aiCustomDesign` knobs, header/footer options and the full V3 `specSkeleton` contract. Never guess enum values.

## One tool for everything: `set_design(eventId, target, …)`

| target | what it changes |
|---|---|
| `preset` | whole look at once (`preset` name) |
| `global` | `primaryColor`, `headingFont`, `bodyFont`, `radius`, `mode`, … |
| `section` | one section: `sectionId` + `variant`, OR `customDesign:{…}` for a NEW layout; also `background`, `align`, … |
| `typography` | one text element: `sectionId` + `field:'title'` + `font`, `size`, `transform`, … |
| `header` | `variant`, `tone`, `ctaText`, `menu` |
| `footer` | `variant`, `tone`, `tagline`, `links`, `footerDesign` |

Section ids come from `list_sections(eventId)`. Structure changes via `manage_sections(eventId, op:'add'|'remove'|'reorder'|'toggle', …)`.

## Authoring an ORIGINAL template (not a preset)

You can compose a full custom template yourself:

1. `list_design_options` → get `specSkeleton`, all enums, and `aiCustomDesign` knobs.
2. Compose a complete V3 spec object: `version:3`, `designSystem{palette, typography, shape, spacing, effects, mode}`, `header`, `footer`, `sections[]` — each section with `type` + `variant`, or `variant:'ai-custom'` + `design` for a unique layout.
3. `set_website_spec(eventId, spec)` — sanitizes/clamps and publishes live.

## Choosing between guides

- Content-level edit ("better headline") → `website` guide (`improve_website`).
- Visual/system-level edit ("brand color #FF5A00, rounder cards, different agenda layout") → this guide.
