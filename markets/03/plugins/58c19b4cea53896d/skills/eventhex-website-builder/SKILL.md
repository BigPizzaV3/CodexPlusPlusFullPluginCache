---
name: eventhex-website-builder
description: Build or edit the event website — new-site pipeline vs live-site editing, drafts vs published, SEO, real URLs.
---

# Website — build & edit

## Decision rule (most common mistake)

- **NEW site** (none exists / full rebuild): `generate_website(eventId, vibePrompt)` → returns candidate specs → `apply_website(eventId, spec)` saves a DRAFT → `publish_website(eventId)` makes it live.
- **EDIT an existing live site** ("make it better", "change the colors", "rewrite the hero"): `improve_website(eventId, instruction[, sectionId])` — reads the live design, edits it with AI, and publishes in ONE step.
- `apply_website`, `refine_website` and `update_website_draft` only touch the DRAFT — changes will NOT show until `publish_website`.

## Supporting tools

- `get_website(eventId)` — current draft + published state; check this before deciding new-vs-edit.
- `generate_section(eventId, …)` — regenerate a single section's content.
- `generate_seo(eventId)` — title/description/meta.
- `get_event_domains(eventId)` — the real website URL, slug, all domains/subdomains.

## Reply rules

- After `publish_website` / `improve_website`, share the exact `url` the tool returned. NEVER construct a URL yourself.
- If the user reports "my change isn't visible", suspect an unpublished draft: `get_website` → `publish_website`.
- For precise design control (fonts, colors, layout variants, section structure) use the `design` guide instead of regenerating.
