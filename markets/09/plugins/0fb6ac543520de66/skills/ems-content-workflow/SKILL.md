---
name: ems-content-workflow
description: Work inside Engage Media Suite. Use when the user wants brand context, their media library, a Reel, a carousel, a render, or a schedule.
---

Engage Media Suite stores the brand, the footage, and the post. The model writes. Tool names and fields come from the connected server.

## Resolve the workspace

Call `list_brands` before any other EMS id. Use a returned `brand_id`. Do not guess one.

## Read the brand before writing

Call `get_brand` before substantive creative work. Use the voice, audiences, channel brief, preferred formats, and claims to avoid. Brand voice is the default. A channel brief overrides it for a post on that channel.

## Find media

Call `list_media` to browse. Call `search_media` when the user is looking for footage or images about a topic. `search_media` can record a small embedding charge. Use media ids the tools returned. Do not invent them.

Call `get_media` once with the `media_ids` you might use, up to 100, before choosing `start_sec` and `end_sec`. Do not call it once per file. Prefer a highlight. Use a segment when no highlight fits. Do not use the whole file duration unless the file is already a short clip. When the post aspect differs from the file, use that window's framing to keep the subject in the crop. Show those windows with the caption before saving.

## Read before editing

Call `list_projects`, `get_project`, and `get_post` before changing saved work. Do not guess project or post ids. Quick posts can be read. They cannot be created or scheduled.

## Create

Call `create_post` for one new Reel or carousel, after the user agrees to the caption and the media. A Reel uses ordered media, trim points, overlays, and a style that fits the brand. A carousel is a short sequence of slides with one job each. Show the plan before saving. Do not render or schedule as part of create.

## Edit

Call `update_post` with only the fields the user asked to change. Omitted fields stay. Sending `media` or `slides` replaces that whole list.

## Render

Call `render_post` only when the user asks for a render or export. Then call `get_render_status` with the returned `export_id`. Report the status. The status call does not return a download URL. Do not say the file is ready until the status says so.

## Schedule

Call `schedule_post` only after the user agrees to a channel and a time. `delivery` `remind` asks them to share from the app. `delivery` `api` can later post to Instagram, and it saves nothing when that channel cannot post. A failed schedule is not a saved schedule. Call `cancel_schedule` only when the user asks to remove a future schedule.

## Progress chip

`create_post` marks the project in progress. A saved schedule clears that chip. Do not call `set_ai_progress` unless the user wants the chip changed.

## When a call fails

Say what failed and the next step. Do not claim a brand, a file, a render, or a schedule that the tool did not return. If the response is `RATE_LIMITED`, wait and retry once.
