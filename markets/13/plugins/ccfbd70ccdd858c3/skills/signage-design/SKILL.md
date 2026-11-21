---
name: signage-design
description: Design content for a digital signage screen, or decide what form it should take. Use when the user wants to create or redesign a slide, menu board (including menus that change daily), announcement, promotion, welcome sign, wayfinding sign, wait-time board, kiosk page or screen dashboard for a TV or display, or wants to put a dashboard, spreadsheet, website, Power BI report or live data on their screens, including from a document, calendar, chat channel or brand guide. Picks the right format (built-in app, slides, image or web page) and gets it ready for OptiSigns. Not for general design advice (font sizes, colors, layout tips) when the user isn't making content for their OptiSigns screens; answer that directly, without OptiSigns tools.
---

# Signage design

Design the way you normally would; this skill adds only what is specific to OptiSigns screens. Host
features ("the host's slides tool", "the host's image tool", "the host's web-page tool") are named for
this session in [references/host-tools.md](references/host-tools.md).

## 1. Pick the format, in this order

1. **A built-in OptiSigns app already does it** (weather, clock, news/RSS, Google Slides, calendar,
   Power BI, YouTube, social feeds, a live website) → recommend the app.
   [references/native-apps.md](references/native-apps.md)
2. **Static message** → the host's slides tool, 16:9, exported as **PDF** (PPTX only if the user will
   re-edit it). No slides tool, or a portrait screen, or exact rendering needed → one PNG per slide
   from the host's design or image tool. [references/slides.md](references/slides.md)
3. **Changes several times a week, live data, or interactive** → a hosted web page.
   [references/web-app.md](references/web-app.md), plus [references/kiosk.md](references/kiosk.md)
   when people touch it.

Match the screen: landscape is 1920×1080, portrait is 1080×1920. A 16:9 file on a portrait screen
plays letterboxed.

## 2. Screen facts the design must respect

- TVs crop the edges: keep text, logos and QR codes 5% inside every edge.
- Each slide stays on screen 8–15 s (default 10). Nothing scrolls.

## 3. Facts and brand

- Use only the user's facts. Hours, dates, prices, names, offer terms they didn't give: leave them off
  or show a visible placeholder like `[end date]`, and ask. List anything else you assumed.
- Brand: use what the user gives (colors, fonts, logo, a file to extract from).
  [references/brand.md](references/brand.md)

## 4. Before anything goes live

1. Show the design and get the user's OK. Nothing is uploaded or published before it.
2. On OK, run [references/preflight.md](references/preflight.md), write the "Ready to publish" block
   from [references/handoff.md](references/handoff.md), and hand off to `optisigns-operate`.
3. Live writes need approval: the user approves on the card if the tool shows one. If it returns a confirm
   text instead, show it, wait for yes, then re-call with `confirmed: true`.

## Rules

- House rules: [references/house-rules.md](references/house-rules.md) (voice, truth, disclosure, escalation).
- Never quote OptiSigns prices or plans; link https://www.optisigns.com/pricing.
- Never build a fake screen, record or brand the user doesn't own.
- Don't hardcode upload limits; the upload tools return them at runtime.
