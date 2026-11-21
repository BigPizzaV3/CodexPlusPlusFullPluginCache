---
name: videodb
description: Edit, clip, transcribe, subtitle, search, and visually analyse videos in the user's VideoDB account with the VideoDB tools. Use when the user wants to find moments in footage, make clips or highlight reels, get transcripts or captions, understand what happens on screen, process a video URL, generate media from a prompt, or monitor a live camera feed.
---

# VideoDB

Every tool acts on the connected VideoDB account only. IDs: videos `m-…`, audio `a-…`, images `img-…`, live streams `rts-…`, collections `c-…` (`default` always exists). Never guess an ID — list first.

## Find the media

1. `list_assets` with `asset_type` `collection`, then `list_assets` with `video` (or `audio` / `image`) in the right collection. There are no per-type list tools.
2. Details for one item → `get_asset` with the same `asset_type` and the ID.

## Ingest a URL

1. `upload_media` with the public URL (direct file link or YouTube). Local file paths are not supported — say so and suggest hosting the file or uploading in the VideoDB console.
2. It returns a job handle; poll `get_job_result` until the new media ID arrives.

## Make it searchable

1. `list_indexes` first; if the video already has a ready index, search it and skip the rest.
2. `understand_video` with analyzers: `spoken_words` for speech, `vlm` for what happens on screen (add `object_detection`, `ocr`, `activity_recognition` when the question needs them). Poll `get_understanding` until the analyzer is done.
3. `create_index` on each analyzer that finished.
4. For text only, `generate_transcript` is enough; read it back with `get_transcript`.

## Find moments and answer questions

- One video → `search_video`; a whole collection → `search_collection`.
- Answer content questions from the matches and the transcript; quote the supporting moments.
- Report timestamps as `mm:ss`, and give the clip link each match carries.

## Edit and deliver

- A segment → `generate_clip`. Several segments, or the best moments from a search → `compile_clips`.
- Captions → `add_subtitles`. Vertical or square → `reframe_video`. Overlays, text, audio tracks → `render_timeline`.
- Every `stream_url` has a `player_url` that opens in a browser; an MP4 of any stream → `download_stream`.

## Generate media

`generate_media` with `kind` `image`, `video`, `music`, `sound_effect` or `voice` and a prompt (for `voice`, the prompt is the text to speak). `duration` applies to video, music and sound effects; `aspect_ratio` to images; `voice_name` to voice. The result lands in the collection like any other asset.

## Live streams

`connect_rtstream` (RTSP/RTMP/HLS) → `index_rtstream_scenes` → `get_rtstream_scenes` to read what was seen. Alerts: `create_rtstream_alert` with the condition in plain language and the user's webhook URL; it creates the event itself.

## Long jobs

Uploads, transcription, understanding, clips, reels, reframes, renders, downloads and media generation return `{status: "processing", output_url}` at once. Poll `get_job_result(output_url)` about every 30 seconds, tell the user it is still processing, and never start the same job again while one is running.

## Credits

`{status: "insufficient_credit"}` means the account needs more VideoDB credits. Give the `console_url` as an "Add credits" link, say no subscription is required, and wait for the user to confirm before retrying. Do not mention plans or promotions.

## Safety

- Confirm with the user before any `delete_asset` call; name what will be removed and that it cannot be undone. Deleting a collection removes everything in it, and the `default` collection cannot be deleted. Never bulk-delete on a single request.
- Tools see only the connected account; decline requests about other people's accounts.
- Return only what the user asked for: media names, IDs, timestamps and links — not account metadata.
