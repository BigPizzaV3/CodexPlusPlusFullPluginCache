---
name: videogen-polish-and-export
description: >-
  Polish an existing VideoGen project (captions, transitions, animate stills,
  zoom) and export an MP4. Use when the user already has a projectId or a
  finished run. Do not start a new workflow.
---

# Polish and export

Remix and MP4 download for a project that already exists.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

They already have a `projectId`, a succeeded workflow in this chat, or they ask to add captions/motion and download.

## Steps

1. Resolve `projectId` from this chat or `list_projects`. Never invent one. If none exists, stop and say they need a generated project first (getting-started or a use-case skill).
2. Call `get_me` if this chat has not already confirmed a linked account.
3. If they want polish, `remix_project` with `projectId` and ordered `edits`. Use at least two when they want a finished-looking cut:

| Edit | Effect |
| --- | --- |
| `CAPTIONS` | Show captions |
| `TRANSITIONS` | Section and asset transitions |
| `ANIMATE_IMAGES` | Turn stills into short clips |
| `ZOOM` | Ken Burns zoom on stills |

Pass `saveAsNewProject: true` when they asked to keep the original.

4. Poll `list_project_remix_actions` until remix actions succeed before exporting if those edits must appear in the MP4.
5. `export_project` with `projectId`. If still running, poll `get_project_export` until `succeeded`. Share `downloadUrl`.
6. If they asked for an edit MCP cannot do (music file, logo file, translate), say so and offer `get_app_deep_link` into the VideoGen editor (`projectUrl` / navigate to the project). Do not pretend MCP applied that edit.

## Output

A remix status (if any) and an MP4 `downloadUrl`. Do not invent ids.

## Do not

- Start `script_to_video` or `storyboard_to_video` from this skill.
- Export before the workflow or remix has `succeeded`.
