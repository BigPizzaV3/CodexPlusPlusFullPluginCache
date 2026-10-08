# create_project options

Full parameter reference for `create_project`. `type` is always required; the rest depends
on which branch you are on.

## type (required)

| Value | Effect | Cost |
| --- | --- | --- |
| `clipping` | Generates multiple short clips from the source with AI | 1 credit / minute |
| `captions` | Adds captions to the video with AI | 2 credits / minute |
| `editor` | Creates an editable project with no AI, from the user's own uploads or blank | free at creation; billed at render |

The two AI branches require `video_url` + `language`. The editor branch refuses `language`
and accepts `video_urls`, `video_titles` and `title` instead.

## video_url

Public source URL (YouTube and similar). Max 2000 characters.

- `clipping` / `captions`: **required**, any public URL.
- `editor`: the user's own `uploads.vdclip.com` URL, or omit for a blank project.

## video_urls (editor only)

One to five own `uploads.vdclip.com` URLs. Each becomes an independent editable result in
the same project. Takes precedence over `video_url`.

## video_titles (editor only)

Display title per upload, aligned by index with `video_urls`. Max 5 entries.

## title (editor only)

Project title, 1–500 characters. Defaults to a generic name when omitted.

## language (clipping / captions — required)

Transcription and caption language — must match the **spoken audio**, not the chat language.
Passing it with `type: "editor"` is rejected, not ignored.

`en` `pt` `es` `fr` `de` `it` `nl` `ru` `ar` `hi` `ja` `ko` `id` `pl` `uk` `sv` `no` `da`
`fi` `cs` `ro` `ca`

There is no tool to re-transcribe an existing project into another language. If the user
picked wrong, create a new project.

## category (optional, ask the user)

Helps the AI choose better cuts. Omitting it means `other`.

`comedy` `podcast` `motivational_speech` `how_to` `music` `tech` `fitness_health`
`tutorial` `gaming` `interview` `product_review` `fashion_beauty` `commentary`
`challenge` `listicle` `marketing` `vlog` `sports_commentary` `movies` `series` `qa`
`webinar` `recipes` `academic` `news` `unboxing` `travel_vlogs` `church` `politics`
`kids` `other`

## aspect_ratio (optional)

`9:16` (default, vertical — TikTok/Reels/Shorts) · `16:9` (horizontal, YouTube) ·
`1:1` (square, feed) · `auto` (keep the source)

## clip_durations (optional, clipping only)

Array of length buckets, max 20 entries. Omit for `auto`.

`auto` `<30s` `30s-60s` `60s-90s` `90s-3m` `5m-10m` `15m-30m`

## preset_id (optional)

Caption/style preset. Call `list_templates` first — it returns saved templates with
`id`, `name`, `is_default` and a `style` summary. Pass the chosen `id` here. Omitting it
uses the account's default preset.

## Output

`create_project` returns:

- `project_id` — poll with `get_project_status`, then `list_clips`
- `credits_consumed` — what this job cost
- `credits_remaining` — balance after the job
- `plan_tier` — plan the project was created under
