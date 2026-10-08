---
name: videogen-getting-started
description: >-
  Connect a VideoGen account, pick the right workflow, and make a first video.
  Use when the user is new, asks what VideoGen can do, or has not named a
  workflow. Do not use for a specific product ad, training lesson, news recap,
  film scene, or export-only request.
---

# Getting started with VideoGen

Teach ChatGPT how to go from a linked VideoGen account to a finished MP4.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

The user is new, asks what VideoGen can do, or wants a video without naming a workflow.

## Steps

1. Call `get_me`. If it fails, stop and ask the user to link VideoGen in ChatGPT.
2. Tell them generation takes several minutes for a full video, then pick a workflow. If they have not named one, give short pros/cons and wait:

| Prefer when | Tool | Inputs |
| --- | --- | --- |
| Narrated explainer, ad, or recap from **text**, especially about one minute or longer | `script_to_video` | `script`, optional `style`, `aspectRatio` `{ width, height }` |
| They have a voiceover audio file | `voiceover_to_video` | `fileId` from `open_uploader` |
| They have a PDF or PowerPoint | `slideshow_to_video` | `fileId` from `open_uploader` |
| Short shot list, frame-by-frame control | `storyboard_to_video` | `scenes` with a visual `prompt` each; **at most 3 scenes** unless they explicitly ask for more |
| One short clip (up to about 30s) as a project | `prompt_to_video_clip` | `prompt` |
| One still, clip, voice, or transform only | a `generate_*` media tool | per that tool |

Do not silently default to `storyboard_to_video`. Do not start a long storyboard for a one-minute explainer.

3. Start the workflow. If the result is still `pending` or `running`, poll `get_workflow_run` until terminal. Keep `projectId`.
4. Optionally `remix_project` with at least two of `CAPTIONS`, `TRANSITIONS`, `ANIMATE_IMAGES`, `ZOOM`.
5. Call `export_project`, poll `get_project_export` until `succeeded`, and share `downloadUrl`.

## Output

A real `projectId`, then an MP4 `downloadUrl`. Never invent ids.

## Do not

- Chain several `generate_*` tools to fake a full video.
- Name internal model vendors.
- Start work before `get_me` succeeds.
