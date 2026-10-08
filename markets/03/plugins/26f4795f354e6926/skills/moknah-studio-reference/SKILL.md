---
name: moknah-studio-reference
description: Reference for operating Moknah Audio Studio - the Project/Chapter/Line data model, the tool call sequence, create_project options, batch editing, QA status codes, job polling, what costs credits, plan gating and hard limits. Use when you need the mechanics of a specific tool or option rather than a production workflow.
---

# Moknah Audio Studio reference

Mechanics and lookup tables. For workflows see `moknah-audiobook-production`;
for parameters see `moknah-voice-settings`.

## Data model

```
Project -> Chapters -> Lines
```

- A **line** is one spoken unit and one TTS request.
- A line is *converted* once it has rendered audio.
- `total_chars` on a line means **billed** characters and is `0` until the line
  renders. It is not the length of the text - never use it to estimate size.

Projects persist. After an interruption call `get_project` and continue; never
restart a book.

## Core call sequence

1. `create_project(filename, file_base64, options)` -> returns a `job_ref`
2. `get_job(job_ref)` every ~5 s until `is_terminal`; on failure read `error`
3. `get_project(project_id)` to inspect chapters and lines
4. `list_voices` -> `set_project_voice` (+ `set_line_voice_settings` for exceptions)
5. `estimate_project_generation` / `estimate_edits` -> show credits, get approval
6. `generate_audio(project_id, mode)` -> `job_ref` -> poll -> `get_job_result`

Use `get_project` for an overview (chapters + counts, no line text - safe on huge
books) and `get_chapter` only for chapters you actually need to read. Never
re-fetch what you already have.

## `create_project` options

| Option | Values / meaning |
|---|---|
| `chapter_style` | `None` / `Heading 1` / `Heading 2` / `Title` - Word chapter detection |
| `include_chapter_title` | keep the heading as the chapter title |
| `normalization` | `"0"` Basic (free) · `"2"` AI-Enhanced (1 credit/char, file only, **Standard Arabic only** - applies contextual tashkeel) |
| `enable_translation` | with `source_language` / `target_language` (file only; AI-Enhanced output is Arabic-only) |
| `line_split_mode` | `sentences` / `newline` / `custom` (+ `line_split_custom`) |
| `start_page` / `end_page` | PDF body range - skip cover, TOC, appendices |

Never use AI-Enhanced normalization on dialects or non-Arabic text.

## Standalone text-to-speech

`text_to_speech(text, voice_id, settings?, confirm_spend)` needs no project and
works on **every plan**, including free.

- `confirm_spend=false` (default) returns a **free estimate** and generates nothing
- `confirm_spend=true` starts a **background** render and returns a `job_ref` -
  poll `get_job` until `is_terminal`, then `get_job_result` for the public audio
  URL. Rendering runs on the worker, so the call never times out even for long
  text or the slower tashkeel / emotions settings.

## Inline audio player

`play_audio(audio_url= | job_ref=, title?)` renders an inline play button (the
`ui://moknah/audio-player` MCP Apps widget) in hosts that support MCP Apps -
e.g. ChatGPT. Pass the public audio URL from a finished render, or its `job_ref`
and it resolves the URL for you. **Only Moknah audio is accepted** - the URL host
must be `moknah.io` or `*.moknah.io`, so the player can't be pointed at an
external source. In hosts without MCP Apps (currently Claude) it returns the URL
instead of a rendered player.

Settings overrides: `temperature`, `similarity`, `speed`, `expressiveness`,
`emotions_mode`, `prerecording`. Omitted keys inherit the user's saved settings.

## Batch editing - prefer this

`update_lines` applies up to **200 edits in one request**. Each item is
`{line_id, text?, settings?, qa_status?}` in any combination; items apply
independently and the response reports per-item ok/error.

Use it for AI-QA corrections across a chapter, bulk revoicing, and QA sign-off.
Fall back to `update_line` / `set_line_voice_settings` only for a single line.
Never loop single-line calls when one batch call would do.

**Adding lines in bulk:** `add_lines(chapter_id, lines=[{text, position?, settings?,
qa_status?}])` creates up to 200 new lines in ONE call (FREE), with per-item
success/failure and the new line ids. Prefer it over looping `add_line`. To split
a text blob into lines automatically instead, use `add_chapter(text=...)` or
`create_project(text=...)`.

**Reading in bulk:** `get_chapter(chapter_id)` returns all of a chapter's lines;
`get_project(project_id, with_tree=true)` returns every line with text;
`get_line_audio(line_ids=[...])` returns many lines' audio at once. Never fetch
lines one at a time.

## QA status codes

| Code | Meaning |
|---|---|
| 1 | NotStarted |
| 2 | InitialOutputReady |
| 3 | UnderReview |
| 4 | RevisionsRequired |
| 5 | AwaitingReview |
| 6 | Finalized |

## Jobs

`job_ref` is `<kind>:<id>` - e.g. `project:1234`, `chapter:58210`,
`transcription:<uuid>`, `task:<uuid>`.

Poll `get_job` until `is_terminal` (`completed` / `failed` / `cancelled`), then
`get_job_result` for the artifact URL. `get_job_result` returns a URL, not bytes.

## What costs credits

**Free:** creating projects, editing text, reordering, voice settings, QA status,
`merge_chapters_audio`, `merge_chapters_subtitle`, and every `estimate_*` call.

**Billed:** generation (TTS), PDF OCR, AI-normalization, translation,
transcription, AI-QA.

Always call the matching `estimate_*` tool and show the number before a billable
action. Never spend credits the user did not explicitly approve.

### When credits run out

`INSUFFICIENT_CREDITS` reports the shortfall. Tell the user plainly how much is
missing, offer to **reduce scope** as a real option (rendering one chapter now is
a legitimate answer), and point them to their Moknah account to manage their plan.
Treat it as a next step, never a dead end.

## Access rules - absolute

- **Owner or team only.** Every tool re-checks permissions on each object. Other
  users' content is invisible and untouchable.
- **No admin.** Staff and superuser privileges are stripped over MCP. There is no
  tool for any admin page or feature and none will succeed. Never offer one.
- **Plan gate.** Studio tools raise `UPGRADE_REQUIRED` for plans without Audio
  Studio.

Tools that work on **every** plan, including free:
`text_to_speech`, `list_voices`, `play_voice_sample`, `estimate_text_to_speech`,
`check_credits`, `get_balance`, `get_job`, `get_job_result`, `download_result`.

## Hard limits

| Limit | Value |
|---|---|
| Lines per chapter | 200 |
| Characters per request, emotions ON | 3,000 |
| Characters per request, emotions OFF | 10,000 |
| Breaks per line | 20 |
| Total pause per line | 30 s |
| PDF upload | 50 MB |
| Batch edits per `update_lines` call | 200 |

Destructive tools (`delete_project`, `delete_chapter`, `delete_line`) require
`confirm=true`.
