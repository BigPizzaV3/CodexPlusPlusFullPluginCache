---
name: slipa
description: Turn screen recordings or written documents into polished, re-voiced, branded demo videos in twenty-nine narration languages, and manage the resulting projects. Use when the user wants to create a product demo, walkthrough, tutorial or release video from a recording they have made, translate or re-voice an existing demo into another language, split a long recording into chapter videos, refine narration, or inspect and manage videos already in their Slipa workspace.
license: Proprietary
metadata:
  author: Salem Ventures
  version: "1.0"
---

# Slipa

Slipa turns a rough screen recording into a finished demo video. It transcribes the recording, rewrites what was said into a clean narration script, re-voices it with a synthetic narrator, and renders the result with the customer's logo, brand colours and captions. Narration language is independent of the recording language, so a user can record in one language and publish in another.

## Spending rules — read before generating anything

Four tools consume the workspace's monthly video quota and real text-to-speech budget: `slipa_process`, `slipa_split`, `slipa_create_video` and `slipa_create_from_doc`. Each refuses to run unless `confirmSpend` is set to exactly true.

Do not set `confirmSpend` on the user's behalf to satisfy a broad or ambiguous request. Set it only when the user has asked for that specific video, on that specific project, in this turn. A request like "make videos out of everything in my library" is not consent for each individual video — say what it would cost and ask.

`slipa_retry`, `slipa_regenerate` and `slipa_refine_script` also consume a quota slot. Say so before calling them.

## Preview before you spend

`slipa_plan_split` shows exactly what a split would produce — the output videos, their titles, the segments each keeps, and the projected quota consumption — while creating nothing and costing nothing.

Always call `slipa_plan_split` and show the user the plan before calling `slipa_split`. The inputs are the same minus `confirmSpend`. A user who sees the plan first can correct the grouping before paying for it.

## Choosing a language and voice

Call `slipa_list_languages` before generating narration in anything other than the project default. It returns each language's exact code, which must be passed verbatim as `language`, plus a `verified` flag. Verified means the full pipeline — script, speech and burned-in captions — has been confirmed end to end for that language. Unverified languages are offered and will render, but have not been quality-checked; mention this if the user picks one.

Call `slipa_list_voices` to resolve a narrator. Voices are fetched live from the speech provider, so do not cache or assume the catalogue.

The recording's own language and the narration language are separate fields. Setting `language` alone does not require re-recording.

## Typical workflows

Recording to video: `slipa_create_upload_url` to get a destination, the user uploads, then `slipa_process` with spend confirmed. Poll `slipa_get_video` for status.

Document to video, no recording needed: `slipa_create_from_doc`.

Long recording to chapters: `slipa_plan_split`, show the plan, then `slipa_split` once approved.

Improving an existing video: `slipa_refine_script` rewrites the narration and re-renders. `slipa_regenerate` re-renders from the saved script without rewriting it. Earlier generations are retained as variants rather than overwritten, so a user can compare.

Recovering a failure: `slipa_retry`, valid only when the project status is failed and its retry limit is not exhausted. It reuses the cached narration where possible rather than re-paying for speech.

Reading without spending: `slipa_list_videos`, `slipa_get_video`, `slipa_get_transcript`, `slipa_get_guide`, `slipa_upload_limits`, `slipa_list_brands`, `slipa_list_music`, `slipa_list_templates`.

## Deletion is permanent

`slipa_delete` removes the project, every retained variant of past generations, and every stored object it owns — the source recording, narration, renders, posters and screenshots. There is no undo. Call it only when the user has explicitly asked for that video to be deleted, and confirm which project first by title, not by identifier alone.

## Workspace scope

Every project operation is scoped to the workspace bound when the user connected Slipa. Projects belonging to any other workspace are not reachable and their existence should not be inferred or implied. If a user asks about another organisation's videos, say plainly that the connection is scoped to their own workspace.

## What Slipa does not do

Slipa is not a timeline video editor. It cannot remove or reorder arbitrary scenes, composite green screen, add overlays at chosen timestamps, or edit footage frame by frame. When asked for that, say so directly and offer what it can do instead: refine the narration script, re-voice in another language or voice, split into chapters, apply a brand kit, or regenerate.

Before uploading, check `slipa_upload_limits` — maximum file size and duration depend on the workspace's plan, and a recording that exceeds them will not be accepted.
