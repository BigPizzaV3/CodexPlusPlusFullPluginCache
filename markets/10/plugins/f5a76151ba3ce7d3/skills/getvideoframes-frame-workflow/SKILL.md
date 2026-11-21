---
name: getvideoframes-frame-workflow
description: Extract still frames from public YouTube, Instagram, TikTok, Facebook, X, Vimeo, Google Drive, and direct video links with GetVideoFrames, then retrieve the resulting jobs. Use when a user asks to extract, preview, or review frames from a supported public video in their connected GetVideoFrames account.
---

# GetVideoFrames frame workflow

Use the connected GetVideoFrames account. Do not ask the user for an API key, password, health information, government identifier, or payment card data.

Follow an explicit user request when it names a mode, format, resolution, or time range. The limits in this skill still apply.

## Start a full extraction

1. Confirm the user supplied a public URL from YouTube, Instagram, TikTok, Facebook, X, Vimeo, Google Drive, or a direct MP4, MOV, or WebM link.
2. Call `getvideoframes_create_job` with that URL. Include `mode`, `every`, `count`, `timestamps`, `start`, `end`, `format`, `resolution`, or `output` only when the user asked for them.
3. The tool returns a job id and status `queued` or `processing`. It does not return frame URLs.
4. Call `getvideoframes_get_job` with that id. Pass `wait=true` to block up to 50 seconds while the job is still running. Repeat until the status is `completed`, `failed`, or `expired`.
5. When completed, report the frame URLs or ZIP URL from that response. Do not invent URLs.

A completed job uses the connected account. A failed job does not. Call `getvideoframes_get_usage` only when the user asks about their own usage. Do not describe offers or billing options.

## Preview

Use `getvideoframes_create_demo` only when the user asks for a short preview. It extracts 6 evenly spaced JPG frames, max 640px wide, from a public video up to 15 minutes. Then poll `getvideoframes_get_demo` with the returned id.

## Work with existing jobs

- Use `getvideoframes_list_jobs` to find jobs in this account. Those rows do not include frame URLs.
- Use `getvideoframes_get_job` to open one job by id.
- If the user asks about billing, say it is handled on the website. Do not list offers.

## Limits

- Stay inside the connected account. Do not query other users, databases, or billing records.
- Do not claim frames are ready while the job is queued or processing.
- If a URL is private or unsupported, say so and ask for a public URL from a supported platform.
- Do not delete jobs or collect a payment card.
