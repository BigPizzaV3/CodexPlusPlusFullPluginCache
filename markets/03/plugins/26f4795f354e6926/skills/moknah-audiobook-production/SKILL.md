---
name: moknah-audiobook-production
description: End-to-end workflow for turning a document (PDF, EPUB, Word, TXT) into a finished audiobook with Moknah - production modes, intake, cost gates, sampling, rendering and delivery. Use when the user wants a book or long document narrated. Not needed for one-off text-to-speech of a short passage.
---

# Moknah audiobook production

Take a document and deliver a finished audiobook. The governing rule: **no credit
is ever spent without an estimate shown and an explicit approval given.**

## Mental model

```
Project -> Chapters -> Lines
```

One line = one spoken unit = one TTS request. A line is "converted" once it has
rendered audio. `total_chars` on a line means **billed** characters (0 until it
renders) - it is not the length of the text.

Projects persist. If a session is interrupted, call `get_project` and continue -
never restart a book from scratch.

## Step 1 - Always ask for a production mode first

- **Full Control** - confirm every decision and every stage.
- **Guided** *(recommended default)* - ask only the 7 key decisions below, decide
  everything else from these skills.
- **Express** - decide everything from the book itself. Only two touchpoints
  remain: spend confirmation and sample approval.

The 7 Guided decisions:

1. Cleaning - you do it, the user does it, or skip (warn that skipping hurts quality)
2. AI-Enhanced normalization (tashkeel, costs 2x) or Basic
3. Translate to another language?
4. Segmentation style (sentences / newline / custom)
5. Read chapter titles aloud? Include the title in the chapter text?
6. One voice for the whole book, or a voice per character?
7. Emotions on or off (warn that tone may vary between lines)

## Stage 0 - Intake

Accepts pdf, epub, doc, docx, txt, xlsx. PDFs must be under 50 MB - split or
supply a lighter copy if larger.

Determine:
- **PDF type** - has a text layer (use directly) or scanned (OCR; set
  `ocr_source = true` and review far more strictly)
- **Language** - fusha / dialect / non-Arabic / mixed
- **Structure** - TOC, front matter, appendices

**Gate 0:** page count, the proposed body range (skip cover, TOC and appendices
with `start_page` / `end_page`), any flags, and `estimate_book_cost`.

## Stage 1 - Extraction

Prefer extract -> clean -> `create_project(text=...)` over handing the raw file
over, because it lets you clean before anything is billed. For PDFs use
`create_project` with `start_page` / `end_page`.

## Stage 2 - Cleaning (free)

Follow the **`moknah-text-preparation`** skill. Produce a cleaning report.

**Gate 2:** the report - change counts, before/after samples, proper-names
dictionary, chapter list.

## Stage 3 - Language review

Review before any spend. Post-generation fixes cost double, because you pay to
render the mistake and again to render the correction. Be stricter when
`ocr_source` is set.

**Gate 3:** itemized in Full Control, a summary in Guided, silent in Express.

## Stage 4 - Create the project

- Name = the exact book title
- `chapter_style = Heading 1`, `include_chapter_title` per gate
- `line_split_mode` per gate
- **Normalization by language:**
  - fusha -> AI-Enhanced (2x credits, best result). If the user refuses the cost,
    use Basic and manually add tashkeel only to genuinely ambiguous words
  - dialect -> Basic, always
  - non-Arabic -> Basic
  - mixed -> split by language, or follow the dominant one
- Translation (100+ languages) - the user reviews the translation *before* any
  audio is generated

After creation, verify the chapters match your map. If headings were missed, fix
the source document and re-import rather than patching chapter by chapter.

## Stage 5 - Voices and settings

Follow **`moknah-voice-settings`** for parameters, and
**`moknah-dialogue-and-pacing`** for casting, line merging and pause placement.

**Gate 5a - casting approval, in every mode.** Express proposes and confirms once.
Use `play_voice_sample` so the user *hears* a voice before choosing it.

## Stage 6 - Sample, then generate

Render **one sample line per content type** - narration, dialogue, verse or
poetry, a line with converted numbers, a line with a foreign name. Pick
non-adjacent lines. With AI-Enhanced normalization, sample from the start, middle
and end to check tashkeel consistency.

**Gate 6 - the big spend gate, never skipped in any mode.** The user listens and
approves. On rejection, iterate in this order: settings -> voice -> text. Cap it
at 3 loops, then recommend human help rather than burning credits.

Then generate, chapter by chapter (better fault isolation) or whole book. If one
line comes out wrong, re-render only that line with `generate_lines` - never the
whole chapter. Log every re-render.

## Stage 7 - Review and delivery

- Spot-check the start, middle and end of each chapter (`get_chapter_audio`)
- Deliver per-chapter files (default) or one merged file via
  `merge_chapters_audio`
- Matching subtitles via `merge_chapters_subtitle` (`srt` or `vtt`)
- Both merges are **free**; omit `chapter_ids` to cover the whole book in order
- Naming: `{NN} - {chapter}.mp3`, zero-padded
- Final report: durations, credits spent, lines re-rendered

## Gate matrix

| Gate | Full Control | Guided | Express |
|---|---|---|---|
| 0 intake / page range | ask | ask | auto |
| 2 cleaning report | ask | ask if AI cleaned | on demand |
| 3 corrections | itemized | summary | auto |
| 4 project options | ask all | 7 questions | auto |
| 5a voice casting | ask | ask | propose + confirm once |
| 6 sample approval | ask | ask | **ask - never skip** |
| 7 merge / format | ask | ask | auto |
| **any credit spend** | ask | ask | **ask - never skip** |

## Money

**Free:** creating, editing text, reordering, voice settings, QA status, merging
audio, merging subtitles, and every `estimate_*` call.

**Billed:** generation (TTS), PDF OCR, AI-normalization, translation,
transcription, AI-QA.

Always call the matching `estimate_*` tool and show the number before a billable
action. If the balance is short, say so plainly, and offer to reduce scope -
rendering a single chapter now is a legitimate third option.

## Jobs

Long work returns a `job_ref` shaped `<kind>:<id>` (`project:1234`,
`chapter:58210`, `task:...`). Poll `get_job` roughly every 5 seconds until
`is_terminal`, then call `get_job_result` for the artifact URL.

## Hard limits

- 200 lines per chapter
- 3,000 characters per request with emotions on; 10,000 with emotions off
- 20 breaks and 30 s of total pause per line
- Destructive tools require `confirm=true`
- You can only ever touch the signed-in user's own content
