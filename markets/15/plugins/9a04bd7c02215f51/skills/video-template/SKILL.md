---
name: video-template
description: Make a launch video, promo, logo intro, title card, number counter or photo slideshow as an MP4 from one of Igly's fill-in video templates. Use when the user wants a real video file (MP4) with their own text, colors or logo, rather than an animation built as code in the chat.
---

# Video template

Igly's video templates are finished motion designs with text, color and image slots. Igly renders the filled-in template to a 1080p MP4 for free, and the user watches and downloads it in the board view.

## 1. Find a template
- `list_video_templates` with a `query` from the request ("product launch", "logo") and/or a `category` (logo-animation, text-animation, ai-product-demo, app-ui-animation, number-counter, photo-slideshow, product-promo, 3d-abstract, character-animation).
- It opens a picker with playing previews. If the user wants to browse, let them pick there; they can fill in the form and render it themselves.
- If they have not decided between a design, a video template and an animation, call `browse_igly` instead.

## 2. Fill it in
- `get_video_template` lists the slots: id, label, required or optional, length limit and a sample value.
- The samples are a demo brand. Write the user's own words into every required text slot; ask for what is missing (brand name, tagline, features) instead of keeping a sample.
- Colors are hex values like `#2f6bff`.
- Logos and photos are uploaded by the user in the template's form in the picker. If they want their own image in the video, open the picker for them.

## 3. Render
- `render_video_template` with `template_id` and `fields`. The board view shows progress, then the MP4 with a Download button.
- `get_video_render` with the `render_id` returns the status and, when done, the MP4 link to share.
- For a different text, render again: every render is a new video.
