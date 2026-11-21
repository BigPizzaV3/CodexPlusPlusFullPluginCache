---
name: gilmos-screenwriting
description: "Write or revise a gilmOS screenplay, preserve structured cinematic paragraphs, or run Alfred's persistent long-screenplay and formatting workflows. Use for screenplay deliverables, not a shot list or a free media generation."
---

# Write a screenplay in gilmOS

Resolve the project with `gilmos_list_projects`/`gilmos_get_project` if needed. Read the selected screenplay and its exact current version through `gilmos_read_resources` when the context is incomplete. Use the existing brief, character voices, decisions and target duration; do not confuse a synopsis, treatment or scene outline with a complete screenplay.

## Choose the right writing operation

- A short creation or an explicitly requested complete new version uses `gilmos_create_screenplay`. Pass `screenplayId` to add a version to that screenplay; omit it only when creating a separate screenplay is intended.
- A long screenplay requiring planning, scene-by-scene writing, reviews and persisted progress uses `gilmos_write_long_screenplay`. Preserve the user's brief, language, duration and authorized token budget. This already delegates execution to Alfred's existing server workflow; do not call another model merely to restate the same request.
- Incorrect paragraph types in an existing screenplay use `gilmos_correct_screenplay_formatting` once, then `gilmos_get_alfred_workflow_status`. It corrects types while preserving text and saving a new version.

MCP does not expose Alfred's browser paragraph-edit tools. Do not claim to have edited the live editor draft. For a narrow requested correction, read the complete accessible version, preserve its unaffected content and explain that the exposed save operation creates a full version. If the content is incomplete or the request requires protected concurrent draft editing, stop before replacing anything and state that limitation.

## Typed cinematic content

For `gilmos_create_screenplay`, put actual arrays in `payload.blocks`, not `blocks_json` or JSON embedded in a string. Use:

| Type | Content |
| --- | --- |
| `scene_heading` | INT./EXT. PLACE - DAY/NIGHT; optional `sceneNumber` belongs here |
| `action` | Filmable visible/audible action at present tense, including action didascalies |
| `character` | Speaker name only, usually uppercase, optionally V.O./O.S./SUITE |
| `dialogue` | Spoken words only, without speaker name or acting notes |
| `parenthetical` | Brief acting instruction inside a speech, not a scene's action |
| `transition` | A cinematic transition |
| `cover_title`, `cover_credit`, `cover_author`, `cover_contact` | Title page fields |

Keep character and dialogue separate. Put long actions outside speeches; resume with a character block if needed. See [examples.json](references/examples.json) for a complete valid scene and workflow argument templates.

`syncScenes` defaults to true: saving the screenplay also synchronizes production scenes. Set `syncScenes=false` for a separate experiment or a revision that must preserve those scenes. Do not additionally create the same scenes manually after synchronization. Before a full-version save, reread the active version and avoid overwriting an unexpected concurrent change; MCP does not offer atomic expected-version enforcement for this operation.

## Persistent writing

Keep the `runId`/`screenplayId` returned by `gilmos_write_long_screenplay` and inspect `gilmos_get_screenplay_writing`. Use `gilmos_control_screenplay_writing` with `pause`, `resume` or `stop` when requested. An additional token allocation requires explicit user authorization beyond the previous budget.

If a submission result is uncertain, read writing status before starting a second run; reuse the same `requestKey` when retrying the same submission. A run can pause on a concurrent manual edit: preserve that edit and inspect the reported reason instead of forcing a restart. Follow the actual status, scenes written, review state and persisted versions. If still running, report that fact and its identifier; do not invent completion.

Finish by identifying the saved screenplay/version, what changed, and any ongoing job. Cite scene numbers when discussing actual scenes. The next step can be breakdown/storyboard, but do not launch that extra paid work without the user's request.
