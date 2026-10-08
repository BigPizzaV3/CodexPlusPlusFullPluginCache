---
name: hypernatural
description: Use when the user wants a video made or edited — "make me a video", a promo, ad, UGC clip, explainer, product or launch video, turning a script, blog post, or images into video — even when no tool is named, and whenever Hypernatural or its MCP server is mentioned.
---

# Creating videos with Hypernatural

## What Hypernatural is

Hypernatural (https://hypernatural.ai) is a **subagent** that builds a _composition_: a timeline of still images, animated clips, music, and TTS narration that together constitute a video. You direct it over MCP server `https://api.hypernatural.ai/mcp` (streamable HTTP; your client handles OAuth).

The division of labor: **you decide the creative structure; Hypernatural renders it.** It is a strong executor and a weak reasoner. It accepts open-ended prompts, but it works far better when you specify the exact shots you want — the shot-list format in [references/shot-writing.md](references/shot-writing.md) — and address everything precisely: library entities by exact `@Name`, shots by position ("shot 2"). You are better than it is at working out which shot or entity the user means, so resolve that yourself, then name it.

Every creative call is asynchronous — it queues background work and returns immediately, and you poll for the result. Only the `list_*` / `get_*` reads answer straight away.

## Glossary

**Composition** — the video itself: a timeline of shots plus independent audio tracks. Created once with `create_composition`, then changed by conversation. Has an id, a shareable `url`, a `title`, and a `render_size` (`landscape` / `portrait` / `square`) fixed at creation. The `url` opens the website editor; it is **not** a video file.

**Shot** — one entry on the timeline: a still image generated from its description (using its `@`-mentioned references), an optional animation (a short video clip derived from that still), and optional animation instructions.

**Animation instructions** — the motion for a single shot. They can also bake **dialogue (lip-synced) or sound effects** into that one shot's clip; quoted speech here is voiced _in the clip_, not as a separate voiceover.

**Voiceover track** — TTS narration: independent audio that plays across the timeline alongside the shots. It is not part of any shot, and is added, moved, and replaced separately.

**Music track** — a background score across the timeline, added / moved / resized by asking in chat.

**Captions** — on-screen text auto-generated from the narration. Captions and voiceover are different concepts: "hide the captions" is a visibility change, never a voiceover removal. Captions are the only text _overlay_ over MCP — there are no separate title or end-card elements. Words can also be generated directly into a shot's still image (a title card, a sign, an end-card); the rules for that are in [references/shot-writing.md](references/shot-writing.md).

**Reference** — a named, reusable, team-scoped library entity that you mention as `@Name` in shot text. Three kinds, routed by what the image _depicts_, not by how you want it used (all three end up in the video):

| The image is                                                     | Create it with                                                              | Then                                                                                        |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| A recurring on-screen person (spokesperson, presenter, founder)  | `create_character` — one image, or a text `bio` with no image               | `@Name` in shots                                                                            |
| One specific product or logo that must look identical every time | `create_reference_object` (`kind: product` / `logo`) — an image is required | `@Name` in shots                                                                            |
| A scene, location, background, mood, or style — the common case  | `create_asset`                                                              | pass `{asset_id, name}` in `static_image_references` **and** use that `@Name` in the prompt |

**Job** — one unit of background work, identified by a `job_id`. Poll `get_job` until `complete` or `failed`. Composition turns are the exception: they poll `get_composition` instead.

**`next_action`** — the single computed instruction `get_composition` returns for the composition's current state. It is the state machine, not a suggestion: always obey `next_action.guidance`.

**Credits** — the team's generation budget. A composition can pause mid-plan on `top_up_credits`.

## The tools

| Purpose                 | Tools                                                         |
| ----------------------- | ------------------------------------------------------------- |
| Get images in           | `get_image_upload_urls`, `upload_file_from_remote_url`         |
| Build the library       | `create_asset`, `create_reference_object`, `create_character` |
| Read the library        | `list_assets`, `list_characters`, `list_reference_objects`    |
| Create and read a video | `create_composition`, `get_composition`, `list_compositions`  |
| Change a video          | `send_chat_message`                                           |
| Track background work   | `get_job`, `list_jobs`                                        |

Each tool's own description defines its arguments; this skill defines the workflow and the UX.

## Building a video

### 1. Decide the references first, and ask the user about them

Before writing any shot text, decide which characters, products, logos, and scene images the video needs — and **ask the user**. The video should show _their_ spokesperson, product, and business; do not invent a stand-in for something the user owns.

References are team-scoped and reusable across compositions, so check the library first (`list_characters`, `list_reference_objects`, `list_assets`) and reuse existing entities rather than creating duplicates.

Every new image needs an `upload_key` first. Pick the path by **where the bytes already are**:

| Bytes are                        | Call                                                                       |
| -------------------------------- | -------------------------------------------------------------------------- |
| On local disk, and you can `PUT` | `get_image_upload_urls([filenames])`, then PUT each file's bytes to its url |
| A native attachment (`file`, ChatGPT only) | `upload_file_from_remote_url(file=…)`                           |
| Already at a public HTTPS URL    | `upload_file_from_remote_url(url=…)` — never download it locally first     |

Upload only the files you were given, never a whole directory. `upload_file_from_remote_url` takes exactly one source — whichever of `file` / `url` your client's schema offers — and returns its `upload_key` immediately, with no job to poll. If a PUT fails, switch to `upload_file_from_remote_url` instead of retrying it. Never invent a `url` for a local file — when neither path is available, say so and ask the user for a public URL or an attachment, rather than building the video without an image they asked for.

### 2. Create a reference for each image, routed by what it depicts

Route each image with the table in the glossary, then **poll each returned `job_id` with `get_job` until `complete`**. The entity does not exist before that, so never use a new `@Name` in the same turn as its `create_*` call — a `create_composition` or `send_chat_message` that mentions an unresolved `@Name` fails. A `complete` job can still carry per-file failures: check `error_message` and `result.errors`; failed files are absent from `result.assets`.

Creating a reference from material the user handed you with stated intent ("this is our founder", "here is the logo") is setup, not speculation — do it now; it is reusable library work either way. A reference that was _your_ idea, for a subject the user never raised, belongs to your draft and waits for approval in step 4.

### 3. Write the shot list that uses those references

Each `Shot 1: …` entry becomes exactly one shot; the planner preserves your count, order, and intent while filling in generation detail. Give every shot a **Visual** (subjects, placement, exact `@Name`s) and an **Animation** (motion, camera, any quoted on-screen speech first). Shots are generated with no memory of each other, so every appearance of an entity is its exact `@Name` — in every shot, every time.

Read [references/shot-writing.md](references/shot-writing.md) before drafting: Visual vs Animation, standalone shots, `@Name` discipline, quoted speech, in-shot text, pacing, and a worked example.

### 4. Get approval for anything you wrote

- **The user supplied the shots:** preserve their wording, weave in the required `@Name`s, and create immediately. Those `@Name` edits are a binding requirement, not a rewrite — they are the only change you make without approval.
- **You wrote or expanded any shot beyond those `@Name` edits** — from prose, a brief, a vague idea, or by filling in detail the user did not give: show the drafted shot list and get approval **before any `create_*` call**; an unapproved plan makes those entities wasted work. Label the draft `Shot 1:`, `Shot 2:` … so the approved text becomes the prompt verbatim. An explicit waiver ("just make it, I trust you") counts: show the list, then proceed without waiting.

### 5. Call `create_composition` once

One composition per video: every later change is a `send_chat_message`, never a second `create_composition`. Pass the approved shot list as `prompt`, every scene image as a `static_image_references` entry whose name appears as `@Name` in that prompt, and the `render_size` the user wants.

### 6. Follow `next_action` until `done`

Poll `get_composition` (not `get_job`) and do exactly what `next_action` says. While work is in flight, say generation is _kicked off_, never _ready_, until polling confirms it — and close each turn in one brief sentence.

| `state`                          | Do this                                                                                                                                                                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wait`                           | Wait `retry_after_seconds`, then poll again. Send no message and no unsolicited progress update; answer a direct status question if the user asks one.                                                                                    |
| `answer_question`                | Ask the user `question.question`, then send **only** their answer. A labeled recommendation of your own is fine; answering for them is not. Send nothing else — an unrelated message cancels the question.                                |
| `pick_references`                | Planning paused on a subject you did not `@`-tag. Show every question with its candidates, then send all choices in one message: `Use @Name for <subject>.` or `Use any <kind> for <subject>.` Create and poll a missing reference first. |
| `top_up_credits`                 | Relay the shortfall and the composition `url`.                                                                                                                                                                                            |
| `open_in_app` / `report_failure` | Relay the guidance with the `url`, then stop polling.                                                                                                                                                                                     |
| `done`                           | Relay `assistant_reply`; add `actions` if the user wants the change details.                                                                                                                                                              |

### 7. Edit by conversation, then hand off the `url`

Send one intent per `send_chat_message`, in plain language, with exact `@Name`s. Refer to shots by position ("shot 2", "shots 3–5") and pick the shot yourself rather than describing it. Music, captions, voiceover placement, and volume are all chat edits: describe what you want.

- Ask for pacing in words ("quick cuts", "let it linger") rather than per-shot seconds, unless the user needs exact timing.
- Quote the durations `get_composition` reports, never the ones you requested — narration refits timing. Do not send a follow-up message to correct drift the user never raised.

Finish by giving the user the composition's `url` — review, rendering, and export all happen in the Hypernatural app, not over MCP. Hand over the `url`, never a bare id.

## Common errors

| Mistake                                                     | Instead                                                                                       |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `create_composition` straight from a vague ask              | Draft the shot list, show it, get approval                                                    |
| Deciding the references yourself                            | Ask the user which spokesperson / product / logo images the video should use                  |
| Using an `@Name` in the same turn as its `create_*`         | Poll `get_job` to `complete` first — the entity does not exist yet                            |
| Writing "your logo", "the same barista", or "she" in a shot | The exact `@Name`, in every shot, every appearance                                            |
| A `static_image_references` name that is not in `prompt`    | Every name there must appear as `@Name` in the prompt, or the call is rejected                |
| Uploading a product photo as a plain asset                  | Products and logos are reference objects, people are characters, scenes and styles are assets |
| Downloading a remote image locally to re-upload it          | `upload_file_from_remote_url(url=…)` — the server fetches it for you                           |
| Answering a `next_action` question yourself                 | Forward the user's own answer                                                                 |
| Messaging while `next_action` is `wait`                     | Wait `retry_after_seconds`, then poll again                                                   |
| A second `create_composition` to change something           | One composition per video; every later change is `send_chat_message`                          |
| Vague in-shot text ("a sign with the company name")         | Text in shots is fine used sparingly — quote the exact words and specify style and placement  |
| Treating a `complete` job as fully successful               | Check `error_message` and `result.errors`                                                     |
| Handing over a composition id                               | Hand over the `url`                                                                           |

When something does fail:

- Follow the recovery instructions in the error text and any `guidance` field before improvising.
- After an ambiguous `create_composition` failure (timeout, server error), call `list_compositions` **before** retrying. The composition may already exist, and a blind retry creates a duplicate.
- Never loop on identical failures. On `report_failure`, relay the guidance with the composition `url` and stop — the user can continue in the app.
