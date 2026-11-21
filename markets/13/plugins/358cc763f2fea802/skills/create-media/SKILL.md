---
name: create-media
description: "Use when the user asks to generate or edit media with getimg, including images, videos, music, speech, sound effects, photo recipes, or reuse of their getimg library."
---

# Create media with getimg

Use the connected getimg MCP tools to carry out the user's request. Write the brand as `getimg`, always lowercase. Preserve the service's actual URLs.

## Choose the tool

Match the request to a tool in [Tool guide](references/tools.md). Prefer a dedicated recipe when one matches the request. For example, use `headshots` for professional profile photos and `photo_restoration` for damaged photos.

Use `generate_image`, `generate_video`, `generate_music`, `generate_speech`, or `generate_sound_effect` for requests without a matching recipe. Use the transform tools to upscale, resize, or remove a background from existing media.

Read the connected tools' current schemas before filling parameters. Omit `model` for automatic selection. Call `list_models` before specifying a model, and always before speech generation to obtain a supported `voice_id`. Discover current costs and capabilities there rather than assuming model names, prices, durations, or resolutions.

Act on a clear request with reasonable defaults. Ask for missing creative details only when they materially affect the result. The user's media request authorizes the requested credit-spending operation. Do not add a separate cost confirmation unless the user asks to approve costs first. Keep the number of outputs within the requested scope.

## Get the input media

- Reuse `media_id` values from earlier tool results. Use `list_media` to find media from earlier sessions or the getimg website.
- For a public HTTPS URL, use the tool's media input as `{ "url": "https://..." }`.
- When the host supports file attachments through the tool's `*_file` or `*_files` fields, use those fields as their schema requires.
- If the file is on the user's device and the host cannot pass it directly, call `upload_media` to show the server's upload widget. Reuse the returned `media_id`.
- If the client cannot display the upload widget, ask for a public HTTPS URL or reuse a library item. Do not promise that ordinary chat attachments are readable by the server.

Do not send a local filesystem path as a media URL. Keep imported media within the scope of the user's request.

## Submit and finish the request

Use one generation call for the requested work. For independent images sharing settings, `generate_image` supports up to six `prompts`. Recipe tools support `runs` for two to six independent runs. Use batching only when the user requests multiple outputs.

If the result is `processing`, reuse its `batch_id` or `batch_ids` with `get_generation_status`. Prefer `wait_seconds` between 30 and 60 and use the returned `next_tool` arguments when available. Never repeat the generation call because a result is still processing.

Inspect the returned status and outputs. Report failed outputs honestly when a batch partially succeeds. Read tool errors and explain the failure. Do not retry a failed generation automatically. Mention notable parameter adjustments reported in `adjustments`.

## Present the results

Follow the server's instructions for the current client's display mode. When its widget already shows results, describe the media briefly and avoid embedding the same images or repeating a gallery. If the user requests a link, provide the returned link.

When the client cannot display the widget, provide each result URL with a short description. Use returned native media content when the host displays it. Do not download media just to work around host display restrictions.

Describe media by its content. Keep `media_id`, `batch_id`, and `job_id` in tool calls unless the user asks for them. The returned public links expire after 24 hours, while the media remains in the user's getimg library. Mention expiration when it matters for saving or sharing.

## Account and connection

Use `get_account` for the connected team, subscription, or credit balance. Never spend credits to test a connection. Each connection belongs to the team chosen during OAuth consent. To switch teams, reconnect and choose the intended team.

If authentication fails, use the host's connection flow. The user signs in and approves OAuth in the provider UI. Never request passwords, access tokens, or client secrets in chat or write them into plugin files.
