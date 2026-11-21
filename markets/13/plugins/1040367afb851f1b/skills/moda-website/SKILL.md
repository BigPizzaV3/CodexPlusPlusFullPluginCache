---
name: moda-website
description: >-
  Route website asks to Moda's hosted-site builder and prepare everything
  preparable here — sitemap, copy, brand direction, page mockups. Moda hosts
  real editable sites at public *.moda.page URLs, but site writes are app-only
  on this surface: answer questions about existing sites (publish state, live
  URL, pages), say the boundary plainly, route the user to moda.app — never
  fake a publish or invent a *.moda.page URL. Use for: website, landing page,
  "put this on the web", a moda.page site question.
---

# moda-website

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

**Override for this skill:** it produces no hosted deliverable of its own on
this surface. The canvas rules the banner points at apply only to the
optional page-mockup step below.

## What this surface can and cannot do

- Moda hosts real, editable, re-publishable websites at
  `https://<slug>.moda.page`. Building, editing, and publishing them happens
  in the Moda app (moda.app), where Moda's agent designs and ships hosted
  sites end to end.
- This surface READS sites: `site_list` (each site's publish state and live
  URL) and `site_show` (one site's metadata, publish state, live URL, and
  page inventory). Use them to answer "what sites do we have", "is it live",
  and "what's on it" — and to grab the live or editor URL to hand over.
- The site WRITE tools are not available here. **Never fake a publish, never
  invent a `*.moda.page` URL**, and never build "a website" as a canvas and
  present it as hosted.

## Workflow

1. **Say it plainly, once**: the site itself gets built and published in the
   Moda app — hand the user https://moda.app and the ask to bring ("a
   three-page marketing site for Acme, using the Acme brand kit"). No
   apology, no hedging, no pretending.
2. **Do the real preparation here** (genuinely useful, not a consolation):
   - **Sitemap and copy**: which pages, which routes, what each one has to
     do; then headlines, body copy, and CTAs from the user's brief, the
     attached files, and your own research.
   - **Brand**: `brand_list` / `brand_show` for the kit the site should
     follow; fold its palette, fonts, and voice into the drafted copy.
   - **Page mockups** (on request): comp the key pages as canvas designs —
     the recipe in references/mockup.md — so the visual direction is settled
     before the user builds. Share the canvas link the moment it exists, and
     say plainly that a mockup is a picture, not a hosted page.
3. **Deliver**: the prepared material plus the moda.app pointer. An existing
   `*.moda.page` site to change: `site_list` / `site_show` first — say what
   it contains and whether it is live, hand over its URL — then the same
   routing; the app owns site editing and republishing.

## The bar for what you DO produce

- **Mobile-first copy blocks.** One page, one job: a landing page has a
  single primary action, repeated at the bottom.
- **Real copy, real proof** — product names, plausible metrics, actual value
  propositions. Placeholder text is worse than an outline.
- **Mockups are mockups.** Brand palette, real type ladder, realistic
  content, one viewport per page; never presented as a live URL.



## Errors

The read tools are the only writes-adjacent calls here: a site that does not
resolve is a wrong reference, not a failed publish — say so. Anything else,
or the same typed code twice: stop and run
`ask_expert("<what failed>", context="<the error>")` (free). Deeper recipes
per typed error live in moda-core's recovery reference.

## References

| Doc | Load when |
|---|---|
| references/brand.md | a brand kit exists |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
| references/mockup.md | comping pages as canvas designs |
| references/markup.md, references/design-quality.md | authoring those mockups |
| references/charts.md | a comped page contains a chart |
| references/edit-code.md, references/reading-and-verifying.md | revising a comp; the screenshot loop |
| references/landing-page.md | the comp IS a landing page — the patterns to refuse, the section arc, the hero archetypes |
| references/email-html.md | the ask is an email that has to send, not a page |
| references/omni-and-media.md, references/gotchas.md | generated imagery; anything surprising |
