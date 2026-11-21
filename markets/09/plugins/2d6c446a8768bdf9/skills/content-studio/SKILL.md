---
name: content-studio
description: Create and edit Cluelabs Content Studio storyboards and generate or retrieve narration, captions, graphics, sound effects, and music. Use for Content Studio project requests, including access errors and media delivery.
---

# Content Studio

Use the connected Content Studio MCP for live project data and operations. Explicit user instructions take precedence over workflow preferences; server authorization remains mandatory.

## Projects and authorization

- Content Studio projects are private to their account. Project sharing, invitations, and granting another account access are not supported. Never suggest those workflows, including after a permission error. Legacy tool wording about associated sharing data does not establish a sharing feature.
- Resolve a project name with `list_projects`. Clarify ambiguous names. Use an explicitly supplied project ID only for that requested project; never replace it with another project or guess IDs.
- On a project access denial, explain that the connected account cannot perform the requested operation and stop. Do not suggest sharing, ask an owner to grant access, switch accounts, retry through another mutation tool, or claim success. An explicitly authorized permission test may make its requested direct tool call; report which call actually ran and its returned result.
- Distinguish insufficient OAuth scope from project ownership denial. Read, write, and manage consent limits what the connection may do within the account; it does not grant access to another account's projects. Deletion requires manage permission and owner authorization.
- Preserve the exact requested project name. Audience, course topic, and instructions are separate from the name unless the user includes them in it.
- Map displayed slide numbers to persistent IDs using `get_slides`. Update only requested fields, then read back saved results. Storyboard activity notes describe implementation; they are not executable activities.
- For edits to existing slides, use `update_slide` or `update_slides_bulk`. If neither is callable, stop and report the missing editing capability. Do not substitute `create_slide`, deletion, or reordering: creating at an existing ID can preserve the original as an extra slide and change the storyboard structure.

## Saved media prompt identifiers

The host may omit JSON Schema pattern constraints from tool descriptions. Use these exact ID formats when saving new prompts. `N` is the displayed slide number resolved with `get_slides`, `T` is a numeric Unix timestamp in milliseconds, and `XXXXX` is exactly five ASCII letters or digits. Use a new stable ID for each intended prompt and reuse it when correcting a rejected save; preserve unrelated prompts.

| Media | Slide prompt (`type: generated`) | Custom prompt (`type: custom`) |
| --- | --- | --- |
| Graphics | `gp_N_T_XXXXX` | `cp_T_XXXXX` |
| Sound effect | `sp_N_T_XXXXX` | `sc_T_XXXXX` |
| Music | `mp_N_T_XXXXX` | `mc_T_XXXXX` |

For example, `gp_2_1792007200000_phish` is a valid generated graphics prompt ID for displayed slide 2. The `slide` object still uses the authoritative persistent `slideid` and displayed `slideno`. Custom prompts use `{slideid:0,slideno:0}`. Sound-effect and music prompt objects also require the nonnegative integer `timestamp` field; music requires `duration_seconds` and `vocal_mode`. Do not invent shorter ID variants after validation errors. Correct the rejected input before submitting generation, and never resubmit an already accepted generation job.

## Generation and completion

1. Read the saved source content and applicable voice or visual settings. Preserve unrelated settings and prompts.
2. Queue only the requested outputs. Report the actual returned chain/task identifier and queued state. Do not describe a queued job as a completed file.
3. Refresh the appropriate media listing to observe completion. Do not submit duplicate generation merely because work is pending. Report pending or failed work honestly.
4. Submitted prompt records are consumed after acceptance. Empty draft lists do not imply missing generated media. Use the generated media listing to retrieve completed outputs and their source prompts.
5. Audio `duration` metadata is rounded up to whole seconds. Identify it as rounded metadata; do not call it an exact playback measurement. A requested duration is distinct from the generated file's measured length.

## Deliver media without altering its URL

- Treat each returned media URL as an opaque string. Copy it exactly, including host, path, capitalization, percent encoding, credential, query parameters, and signature. Never reconstruct it from a filename, task ID, another URL, or memory; never decode/re-encode, shorten, repair, or normalize it.
- Prefer native media returned by the tool when the host exposes it. Otherwise use the exact returned URL as a Markdown link with a descriptive filename label. For images, use the exact returned URL in an image embed when supported, with a clickable fallback. Do not claim an inline preview works without evidence.
- When a link expires or fails, refresh the corresponding media listing once for a fresh returned URL. Never edit a signature or substitute a guessed URL. If the host blocks playback, state the limitation and provide the project's Content Studio location using the verified project ID so the user can open its media tab.
- Return SRT content exactly as supplied. Report which outputs are complete and which remain pending. Never invent caption URLs, completed files, preview success, or playback measurements.
