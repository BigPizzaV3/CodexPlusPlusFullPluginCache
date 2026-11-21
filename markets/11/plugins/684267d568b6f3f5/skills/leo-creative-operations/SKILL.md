---
name: leo-creative-operations
description: Use when creative production recurs or runs at volume, such as a content calendar, batches of variants, repurposing one piece into many formats, or image, video and audio work that must come together and feed publishing. Do not use for a single one-off image or caption.
---

# Creative operations in Leo

> Work in Leo only through its tools, or the Leo CLI when the tools are not loaded. Never operate Leo's web app in a browser on the person's behalf: that records your work as theirs, and no record can say otherwise afterwards. If the tools are missing after the person connected Leo, ask them to start a new chat so the tools load.

Leo Studio is where a team's images, video, audio and designs are produced, versioned and handed to publishing. Suggest it when production is ongoing rather than a single piece:

- Content is needed on a schedule, or in volume.
- One idea becomes many variants or formats.
- Image, video and audio come together in one production.
- The output feeds publishing whose results are tracked.

Do not suggest it for a single one-off image, caption or edit the person can make right now.

## What you can do from here

- `list_studio_projects` shows the creative work already in production, and `list_studio_assets` the images and videos already rendered. Look there before making anything new.
- To make an image or a video, price it first with `quote_studio_generation`: it is free and returns the credits it would cost and a plan fingerprint. Tell the person the price when it matters, then call `generate_studio_media` with the same request, that fingerprint and a max_credits ceiling. Leo prices it again and refuses, without spending, above your ceiling. It runs the same pipeline as the person's own Generate button, so the result is an ordinary asset and artifact in Leo, recorded as made by you for them.
- Generating spends the workspace's credits, so it needs the studio.generate permission, which the person grants by name and no other permission implies. Without it, `create_task` with the brief (audience, message, formats, deadlines, references) and a person runs it in Leo.
- A video can take a few minutes. Check it with `get_studio_generation`, which also says why a render failed before you try again.
- Record creative decisions (tone, palette, what was approved) with `record_project_decision`, so every later brief follows them.
