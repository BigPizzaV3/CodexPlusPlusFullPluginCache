# VDClip: inspect a clip and hand off to the editor

You can read a clip's project and open it in the visual editor. You **cannot** change it
through the connector: chat-driven editing is paused.

## What is available

| Tool | Does |
| --- | --- |
| `get_project({ result_id })` | Opens the clip's project in the editor widget **and** returns its summary |
| `get_project_summary({ result_id })` | Returns the same summary without opening the widget |
| `get_transcript({ result_id, cursor? })` | Timed text of the project — see [transcript.md](transcript.md) |

## What is paused

`apply_edits`, `save_project` and `compose_scenes` are **not advertised in `tools/list`**.
If a model calls one from memory, the connector answers:

```
feature_paused — Chat-based editing is temporarily paused.
Open the full editor to keep editing: https://editor.vdclip.com/edit/<result_id>
```

Do not describe caption restyling, music, brand kits, cropping, trimming or timeline
changes as something you will do. Read the project, tell the user what is there, and hand
them the editor link.

## The summary

Both `get_project` and `get_project_summary` return a compact projection:

| Field | Meaning |
| --- | --- |
| `title` | Project title |
| `durationSeconds` | Total length |
| `aspectRatio`, `width`, `height` | Canvas format and pixel size |
| `fps` | Always `30` — the engine is pinned to it |
| `backgroundColor` | Canvas background |
| `version` | Version tag of the loaded project |
| `overlays[]` | Up to 40 items: `id`, `type`, `row`, `startSeconds`, `endSeconds`, `label`, `flags` |
| `truncated` | How many overlays were dropped from the list, when there are more than 40 |

All timing is in **seconds**. `EDITOR_FPS = 30` is fixed internal behaviour — never send
frame counts, and never offer to change the frame rate.

Overlay `label` is a short excerpt (24 characters) of the text content or the media
filename. It identifies an overlay for the user in conversation; it is not a full read of
the content. Use `get_transcript` when the user asks what is actually said.

## Workflow

1. `list_clips` (or `list_projects` → `list_clips`) to resolve the `result_id`.
2. `get_project` to open the editor widget and read the summary — or
   `get_project_summary` when the user only wants to know what is in there.
3. Describe what is on the timeline: duration, format, how many overlays and of what kind.
4. If the user wants a change, say plainly that edits happen in the editor and give them
   `https://editor.vdclip.com/edit/<result_id>`.
5. When they are done editing, come back for [rendering.md](rendering.md) and
   [publishing.md](publishing.md).

## Response style

Lead with what the clip is: length, format, and the notable overlays. Do not read out all
40 overlay ids. If the user asked for an edit, name the editor link in the same breath as
the limitation — never leave them without a next step.
