---
name: use-my-media
description: Bring the user's own image into RTST (rtst.ai) — a photo attached in the chat, a local file, or a public image URL — and get the hosted URL that image editing, image-to-video, reference images and motion transfer need. Use when the user wants to edit, animate or reference their own picture with RTST, and when the RTST upload card reports an uploaded image.
---

# Use the user's own image with RTST

Tools: `media_upload`, `media_upload_widget`, `media_import_url`.

RTST tools take images only as hosted https URLs. Pick the route by where the image is:

| The image is… | Do this |
|---|---|
| attached to the chat in ChatGPT | `media_upload` with the attachment as `file` |
| on the user's computer, in ChatGPT or claude.ai | `media_upload_widget`, then wait for the user to pick it |
| a local file, in Codex or Claude Code | run `rtst upload <file> --json` (the rtst CLI) and use the URL it prints; without the CLI, ask for a web URL or the chat app |
| already on the web | `media_import_url` with its https URL |
| already in the user's RTST library | use its URL from `list_images` as-is |

- The user mentions their photo ("my photo", "this picture") but nothing is attached, in
  ChatGPT or claude.ai: call `media_upload_widget` right away, in that same turn and before
  choosing a model or quoting. Never ask them in text to upload or attach it.
- Each new request for "my photo" opens the uploader again, even if the user uploaded
  one earlier in the chat. Reuse an earlier upload only when they point to it ("the same
  photo", "that image").
- After `media_upload_widget`, wait: the card uploads the file and reports the hosted
  URL. Do not also call `media_upload`.
- Images only, up to 15 MB. RTST cannot take a video through this plugin.
- Do not try to pass a real photo through `media_upload`'s `data_base64` yourself: you
  cannot reliably write out megabytes of base64. It is for the upload card and tiny images.
- The result's `url` is what goes into `generate_image` `image`, `generate_video`
  `first_frame` / `last_frame` / `reference_images`, or `motion_transfer`
  `character_image_url`. Continue the task the user started; do not stop at the upload.

## Messages sent by the RTST upload card

- "I uploaded an image to rtst.ai (hosted URL: …). Continue with it." → carry on with
  what the user wanted the image for; ask only if that is unclear.
- "Animate this image into a short video with rtst.ai: …" → `create-video`, with the URL
  as `first_frame`.
