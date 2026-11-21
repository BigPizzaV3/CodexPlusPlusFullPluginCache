# Slides and PNG

For a static message: an announcement, promo, welcome, menu, schedule, wayfinding sign.

## Export

- **PDF by default.** One page per slide. OptiSigns plays a PDF page by page and splits the item's
  duration evenly across the pages, so a 4-page PDF at 10 s a page is one item of 40 s. Say that in
  the hand-off. Keep images compressed; very large PDFs can stutter on players.
- **PPTX** only when the user wants to re-edit in PowerPoint later. The player may substitute fonts it
  doesn't have.
- **PNG per slide** for a portrait screen, exact brand fonts, or a hero image with text placed on it.
  Canvas exactly 1920×1080 or 1080×1920 (3840×2160 only if asked). PNG, not JPG, when there is text.
  Several PNGs on one screen become a playlist with a duration per image (optisigns-operate builds it).
- Transitions, animations, embedded video and speaker notes don't reach the screen.
- Name files the way the user will look for them: `Mother's Day brunch — 2026-05-03.pdf`.
- If the export lands only as a download for the user, say: "Download the file and drop it here, I'll
  upload it."

## No slides or design tool in this session

Write one self-contained HTML file per slide at the exact canvas size (`body` fixed to it,
`overflow: hidden`, no scripts) and show it. If a headless browser is available, render it to PNG or
PDF; otherwise give the user the file and say they can build it in PowerPoint or Google Slides and drop
the PDF here. A Google Slides deck they already have can also play live (native-apps.md).

## Upload (after the user's OK only)

optisigns-operate uploads, by the route in [host-tools.md](host-tools.md) → Export → upload. Keep each
returned `assetId`: the stored name may differ from the file name.
