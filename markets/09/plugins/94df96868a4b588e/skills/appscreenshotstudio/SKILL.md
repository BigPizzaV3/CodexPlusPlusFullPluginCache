---
name: appscreenshotstudio
description: Create App Store and Google Play screenshot sets with the AppScreenshotStudio tools, then refine and export them. Use when the user wants store screenshots, asks what their screenshots should show, or asks which screenshot sizes the stores need.
---

# AppScreenshotStudio in ChatGPT

Use the AppScreenshotStudio tools for store screenshots. Do not draw screenshots with image generation: the tools build real, editable sets at exact store sizes.

## Workflow

1. **Brief.** When the user asks what their screenshots should focus on, call `prepare-screenshot-brief` with the app's category (for example `fitness`, `finance`, `productivity`) and answer from its playbook.
2. **Generate.** When the user asks for screenshots, call `generate-screenshots` right away with what they told you: app name, a one-line description, and brand colour if given. Fill `codebase_context` from the conversation. Do not ask for app screenshots first: the set is built with empty device frames, and the user adds real screens later in the builder at the project URL.
3. **Wait for the design.** `generate-screenshots` returns status `generating` within seconds. Tell the user the set is being designed, then call `get-project` with the `project_id` about every 30 seconds until `status` is `ready` (usually 1 to 2 minutes). If it is `no_design`, show the `message` and answer it with `edit-screenshots`.
4. **Refine.** Apply changes the user describes with `edit-screenshots` (headlines, palette, layouts, device tilt, extra cards).
5. **Export.** `render-screenshots` returns PNG download links at exact store dimensions, valid for 7 days.

Sizes: call `list-devices` rather than quoting sizes from memory.
