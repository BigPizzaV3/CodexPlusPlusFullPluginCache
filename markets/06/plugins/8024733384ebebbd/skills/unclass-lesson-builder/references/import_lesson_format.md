# Lesson import Markdown, version 1

This document defines the lesson import format. Tutors import it with "Import lesson" on the courses index. Imported content maps to the current Unclass lesson editor and renderers.

HTML comments in this reference are instructions for AI, not lesson content or format syntax. In a lesson document, both HTML comments and plain prose outside blocks are commentary and are skipped on import. Reference headings and field tables are documentation, not lesson content. To import a section-only example, add a lesson header and a preceding `page` block.

A complete lesson can be pasted inside one outer backtick wrapper labelled `markdown`, `md`, or empty. Unclass removes the wrapper automatically when the first and last nonblank lines are its opening and closing fences, with the same number of backticks (at least three). Four backticks let the wrapper contain the lesson's three-backtick blocks.

<!-- AI: Return one lesson document. If the chat requires a code wrapper, use four backticks around the entire document; Unclass removes this wrapper automatically. Do not include explanations before or after the lesson. -->

## Complete example

Import [A day at the zoo](lesson-import-example.md) into an English-language course. Expected results:

- 6 draft pages and 26 sections, with no document validation errors.
- 4 downloads after confirmation: three images (the elephant is imported twice) and one audio file.
- 3 preview warnings for the final page's empty image, audio, and YouTube blocks, provided the other YouTube URL resolves. A resolution failure adds a warning and leaves that video section empty.
- The outside-block "Import check" sentence is not included in the lesson.

The final page's empty exercise is intentional and does not produce a warning. Check external media availability and permission separately; preview does not download the image or audio files.

## Document structure

A document contains:

1. One YAML front matter header at the start of the document for lesson metadata.
2. One or more `page` blocks.
3. Explicit section blocks, including `text` blocks, after each page block.

A `page` block starts a page and ends the previous page. It is a structural marker, not a section. Subsequent section blocks belong to that page until the next `page` block or end of file. Empty pages are allowed. A section block before the first page is an error; unblocked commentary after the header and before the first page is skipped.

Page boundaries and text sections are always explicit. Markdown headings, including `##`, are lesson content only inside a text or teacher-note block; outside blocks they are skipped, not turned into pages or sections.

<!-- AI: Repeat page blocks as needed. The order of pages, sections, questions, options, and pairs in the document is their authoring order. Do not generate IDs or position numbers. -->

````markdown
---
format: unclass/1
title: Ordering at a café
language: en
description: Practise ordering drinks politely.
---

```page
title: Warm-up
description: Talk about your favourite café.
```

```text
content: |-
  ### Discussion

  What do you usually order? Explain your choice.
```

```image
alt: A customer ordering at a café counter
```

```page
title: Listening
```

```text
content: Listen and identify the customer's order.
```

```audio
```
````

### Lesson header

| Field | Type | Required / default | Meaning |
| --- | --- | --- | --- |
| `format` | String | Required; exactly `unclass/1` | Format version. |
| `title` | String | Required; nonblank | Lesson title. |
| `language` | String | Optional; defaults to the destination course's language | Language being taught, using a supported lowercase code. |
| `description` | String | Optional; empty | Plain-text lesson description. Use `|-` for multiple lines. |

Supported language codes are `en` (English), `es` (Spanish), `fr` (French), `de` (German), `it` (Italian), `pt` (Portuguese), and `ru` (Russian), as defined by `Languages::SUPPORTED`. A supplied `language` must be one of these codes; blank values, null, language names, and regional variants such as `en-US` are invalid.

The tutor selects the destination course in Unclass. A supplied `language` must match that course's language; otherwise, stop import and ask the tutor to select a matching course or correct the header. When omitted, use the course's language. Lessons currently inherit language from their course, so this field validates the destination rather than setting a separate lesson attribute or changing the course. It does not translate the content or change the interface language.

<!-- AI: Set language to the language being taught, not the tutor's or student's native language. Use a supported code such as en, not a language name. -->

Course IDs, school IDs, level, duration, objectives, and publication status are not header fields. Level, duration, and objectives can guide generation; put any information that students should see into the description or a text section.

The importer creates a new draft lesson with draft pages. Readiness, archiving, and replacement of existing content are editor operations, not instructions from AI.

### Page block

| Field | Type | Required / default | Meaning |
| --- | --- | --- | --- |
| `title` | String | Optional; `Page N` when absent or blank | Page title, where N is its one-based document position. |
| `description` | String | Optional; empty | Plain-text description displayed below the page title. |

A bare `page` block is valid and starts a page with its default title.

## Block syntax and shared rules

A block is a fenced code block whose exact, lowercase label identifies its type. The body is one YAML document containing a mapping; extra YAML documents separated by `---` are not allowed. An empty body or `{}` is an empty mapping. A block ends at its closing fence; blocks do not nest.

| Fence label | Creates |
| --- | --- |
| `page` | A page boundary, not a section |
| `text` | Text section |
| `teacher_note` | Teacher-only Markdown section |
| `image` | Image section with zero, one, or two images |
| `youtube` | YouTube embed section |
| `audio` | Audio section |
| `wordlist` | Wordlist section |
| `exercise` | Empty exercise section with the editor's type chooser |
| `fill_gaps` | Exercise section, type `fill_gaps` |
| `multiple_choice` | Exercise section, type `multiple_choice` |
| `matching` | Exercise section, type `matching` |

- Only the lesson header and `page` blocks accept `title`; these have editable title fields in the UI. No section type has a title input, so `title` is an unknown field on every section block. Use Markdown headings inside text or teacher-note content, or the editable exercise `instruction`, for visible headings. YouTube video titles and audio filenames are derived from their sources, not authored titles.
- Absent optional strings default to empty; absent optional lists default to `[]`. A supplied value must have its declared type. Explicit YAML `null` is allowed only for `url` and a question's `correct`, as specified below.
- Use UTF-8 and spaces, not tabs, for YAML indentation. Quote values as described in [Quoting plain-text values](#quoting-plain-text-values). Do not rely on YAML converting numbers, booleans, or dates into strings.
- Use `|-` for multiline content. It preserves line breaks without adding a final newline. YAML `|` is also valid and retains that final newline; `>` folds line breaks into spaces.
- YAML keys must be unique. Custom tags, anchors, aliases, and merge keys are not supported. Each mapping accepts only the fields documented for it.
- Use backtick fences with at least three backticks, starting at column zero with no indentation. The closing fence must also start at column zero, use the same number of backticks as its opener, and contain nothing else except optional trailing whitespace. Indented opening fences are not recognized as blocks. Tilde fences (`~~~`) are not supported. If content contains a fence, use a longer outer fence.
- Apart from the opening lesson header, only explicit blocks supply imported content. Unblocked prose, headings, lists, blockquotes, and HTML comments are skipped before, between, and after blocks. They create no sections, are not saved as teacher notes, and do not trigger media downloads. HTML comments outside blocks are skipped in full, including any apparent block syntax inside them.
- Skipping commentary applies only outside blocks. Unknown top-level fence labels, malformed block YAML, and unclosed fences remain errors, not comments to ignore. To show a literal fenced code sample to students, put it inside `text.content`.
- Empty section blocks are retained, not discarded. The tutor can complete them in the editor. Student rendering may show the existing unavailable or incomplete message.

### Quoting plain-text values

Most values need no quotes. Wrap the whole value in double quotes, or write it as a `|-` block, when it:

- contains a colon followed by a space, as in `dice: `, `Ejemplo: `, or `Nota: `;
- contains ` #`;
- starts with `-`, `?`, `:`, `,`, `[`, `]`, `{`, `}`, `#`, `&`, `*`, `!`, `|`, `>`, `'`, `"`, `%`, `@`, or a backtick;
- is `yes`, `no`, `true`, `false`, `null`, `~`, a number, or a date, but must stay text.

An embedded colon is the most common import failure. Unquoted, YAML reads the second `: ` as another mapping and reports `mapping values are not allowed in this context`:

````markdown
```multiple_choice
questions:
  - text: Una persona dice: Me llamo Marta.      # Wrong
  - text: "Una persona dice: Me llamo Marta."    # Right
  - text: |-                                     # Also right
      Una persona dice: Me llamo Marta.
```
````

This applies to every authored string, including `instruction`, question `text`, `options`, `explanation`, fill-gap `text`, `left`, `right`, `distractors`, and `words`. Inside double quotes, write `\"` for a literal quote character and `\\` for a literal backslash; a `|-` block needs no escaping. Question marks, inverted marks, accents, and apostrophes are safe unquoted.

<!-- AI: Always put lesson text in an explicit text block using content. Unblocked explanations are skipped on import, so never leave student instructions there. A teacher_note is actual teacher content, not response commentary. Do not invent fields or include generation prompts or model metadata. -->

## Text

Every text section requires an explicit `text` block. Write Markdown in `content`, including headings, paragraphs, lists, tables, and literal code examples. Put headings inside `content`, not in a separate title field. One block creates one section; blank lines within its content do not split it. Unblocked Markdown is commentary and is skipped.

| Field | Type | Default |
| --- | --- | --- |
| `content` | String, Markdown | Empty |

````markdown
```text
content: |-
  ### At the café

  **Maya:** I'd like a coffee, please.

  **Barista:** Would you like milk?

  - Read the dialogue.
  - Practise it with a partner.

  | Expression | Purpose |
  | --- | --- |
  | I'd like… | Making a polite request |
```
````

Supported Markdown includes headings, same-page heading links, paragraphs, line breaks, emphasis, bold, strikethrough, lists, links, autolinks, blockquotes, horizontal rules, code, and tables. Raw HTML, task-list controls, shortcodes, and syntax highlighting are not supported by the lesson renderer.

Markdown image syntax (`![alt](url)`) inside text or teacher-note content is not an image import instruction. The importer removes it from the saved content, shows a warning, and continues the import. Image syntax inside code spans or code blocks stays as literal code. Use an `image` block for actual images. Links inside text remain links; the importer does not download their targets. Images and links in unblocked commentary are skipped along with that commentary.

## Teacher note

| Field | Type | Default |
| --- | --- | --- |
| `content` | String, Markdown | Empty |

````markdown
```teacher_note
content: |-
  Allow two minutes for discussion.

  **Follow-up:** Ask the student to explain why they chose that drink.
```
````

Uses the same Markdown rules as text. The complete section is omitted server-side from student and guest views. It remains available in teacher preview and to the classroom's owning teacher.

<!-- AI: Put teaching guidance or a listening transcript here only when requested. An audio block does not have a script field, and an image block does not have a generation-prompt field. -->

## Images

| Field | Type | Default / meaning |
| --- | --- | --- |
| `url` | String or null | Optional single direct image URL. Missing, null, empty, or whitespace-only means no image. |
| `urls` | List of strings | Optional alternative to `url`, for up to two images. Empty or whitespace-only entries are removed. |
| `alt` | String | Optional shared image description; empty by default. |

Use either `url` or `urls`, never both, even if one is empty. More than two nonblank URLs is an error, not an instruction to truncate the list. An absent URL creates a normal empty image section with upload controls.

<!-- AI: The URLs below demonstrate syntax only and are not real media. Use only actual accessible file URLs supplied by the tutor or verified with your tools. If none is available, omit url; do not invent a URL. -->

````markdown
```image
url: https://media.example.org/cafe.webp
alt: A customer ordering at a café counter
```

```image
urls:
  - https://media.example.org/cafe-inside.jpg
  - https://media.example.org/cafe-terrace.jpg
alt: Two café settings to compare
```

```image
alt: A customer ordering at a café counter
```

```image
```
````

One image renders full width; two render side by side in the listed order. There is one shared alt-text field, not per-image alt text. For two images, the renderer adds each image's number to nonblank alt text. A visible caption belongs in a neighbouring text section, not in `alt`.

The current image editor has no alt-text control. `alt` is retained as import-only accessibility metadata used by the renderer, not as a section title or visible heading. The existing model stores it in the section's `title` column; that internal detail does not make `title` an accepted import field.

Supported files: PNG, JPEG, GIF, and WebP, up to 10 MB per file. See [Media import behaviour](#media-import-behaviour).

## Audio

| Field | Type | Default / meaning |
| --- | --- | --- |
| `url` | String or null | Optional direct audio file URL. Missing, null, empty, or whitespace-only creates an empty audio section. |

<!-- AI: Audio URLs must point to files, not to pages with an audio player. If you cannot provide a real file URL, leave the block empty for the tutor to upload a file. -->

````markdown
```audio
url: https://media.example.org/cafe-dialogue.mp3
```

```audio
```
````

Supported files: MP3, M4A/MP4 audio, WAV, and OGG, up to 50 MB per file. Unclass obtains filename, byte size, and playable duration from the imported file; AI must not supply these values. There are no import options for autoplay, looping, playback speed, clipping, transcript, voice, or audio generation.

## YouTube

| Field | Type | Default / meaning |
| --- | --- | --- |
| `url` | String or null | Optional YouTube URL. Missing, null, empty, or whitespace-only creates an empty YouTube section. |

<!-- AI: Choose a relevant real video only if you have its URL. This example illustrates a supported URL shape and start offset, not a recommended lesson video. -->

````markdown
```youtube
url: https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s
```
````

Supported links are `youtu.be` links and YouTube watch, Shorts, and embed links, including supported mobile/music hosts. The existing resolver accepts `t` or `start` offsets such as `30`, `30s`, or `1m30s`; `t` takes precedence when both are present. Keep the offset in the URL. There are no separate start, end, autoplay, or loop fields.

Unclass resolves the video title and thumbnail during preview and again when the tutor confirms import, using the existing privacy-enhanced embed on success. Resolution failure produces a warning, not an import error: the lesson imports with an empty YouTube section. The failed URL is not retained in the saved section; add a URL again in the editor. YouTube has no background download or retry state. Videos are embedded, not downloaded. Arbitrary uploaded videos and other video providers are not section types.

## Wordlist

| Field | Type | Default |
| --- | --- | --- |
| `words` | List of strings | `[]` |

````markdown
```wordlist
words:
  - coffee
  - a table for two
  - would like
  - takeaway
```
````

Each entry is one word or phrase. Entries are trimmed; blank entries and case-insensitive duplicates are removed, preserving the first spelling and order. Do not put commas, semicolons, or newlines inside one entry: the wordlist parser treats those as item separators, even inside a quoted YAML string. The importer does not reject or warn about these separators; the entry is split when the lesson's wordlist is read.

Definitions come from the existing dictionary in the course language. Translations, definitions, pronunciation, dictionary images, and dictionary audio are not authored fields in this block.

## Exercises

`fill_gaps`, `multiple_choice`, and `matching` all accept:

| Field | Type | Default / meaning |
| --- | --- | --- |
| `instruction` | String, plain text | Empty; the renderer uses its standard instruction when blank. |

Exercise content is plain text, not Markdown. An explanation is student-facing exercise content, not a teacher note. Answer keys are needed for interactive checking; do not put IDs, scores, saved responses, or exercise state into the document.

To create an exercise whose type the tutor will choose later, use an empty `exercise` block. It accepts no fields; use a concrete exercise label for instructions, questions, pairs, or gaps.

````markdown
```exercise
```
````

### Fill the gaps

| Field | Type | Default / meaning |
| --- | --- | --- |
| `text` | String | Empty; source text with `[[answer]]` gap markers. |
| `mode` | String | `typing`; one of `typing`, `word_bank`, or `choices`. |
| `gaps` | List of mappings | Optional per-gap options in marker order. |
| `distractors` | List of strings | `[]`; extra wrong options for `word_bank`. |

Each `gaps` entry accepts:

| Field | Type | Default / meaning |
| --- | --- | --- |
| `alternatives` | List of strings | `[]`; additional accepted answers in `typing`. |
| `prefill` | String | Empty; initially editable text in a `typing` gap. |
| `choices` | List of strings | `[]`; extra wrong options for this gap in `choices` mode. |

#### Gap markers

- Every `[[answer]]` marks one gap. The enclosed text is its primary answer. It may contain multiple words, but must be nonblank and must not start or end with whitespace.
- Repeated answers create separate gaps. Gap order is left to right through `text`, including subsequent lines.
- Omit `gaps` to use default options for every marker. If supplied, its length must equal the number of markers. Use `{}` for a gap with no overrides. `gaps: []` is valid only when there are no markers.
- After YAML decoding, `\[[` and `\]]` produce literal brackets and `\\` produces a literal backslash. Other backslashes remain literal. Use `|-` or single-quoted YAML when writing these escapes so YAML does not reinterpret them.
- Unescaped unmatched, empty, or nested gap markers are errors. The marker syntax has no special meaning in text or teacher-note content.
- The importer removes markers, preserves the primary answers in the source text, and computes each gap's ID and JavaScript UTF-16 `start`/`end` offsets. AI must not calculate offsets or send an `answer` field separately.

<!-- AI: Use typing for free answers, word_bank for a shared set of draggable words, and choices for a separate dropdown at each gap. A prefill is a starting value to edit, not an extra accepted answer. -->

#### Typing

````markdown
```fill_gaps
instruction: Complete the sentence. Correct any misspelled starting text.
mode: typing
text: We meet [[Friday]] at [[six]].
gaps:
  - alternatives: ["Friday afternoon"]
    prefill: Frday
  - alternatives: ["6", "six o'clock"]
```
````

Typing accepts the primary answer and its alternatives after case folding, trimming, collapsing whitespace, and removing trailing `. , ! ? ; :` punctuation. `prefill` is not automatically accepted or checked before the student edits it. Reset restores it. `choices` and shared `distractors` are inactive in this mode.

#### Word bank

````markdown
```fill_gaps
instruction: Drag the correct words into the gaps.
mode: word_bank
text: I [[would like]] a [[coffee]], please.
distractors:
  - tea
  - want to
```
````

The bank contains one primary answer per gap, plus shared distractors, shuffled by the renderer. Repeated primary answers produce separate bank items. Answers use exact matching. `alternatives`, `prefill`, and per-gap `choices` are inactive in this mode. Do not repeat correct answers in `distractors`.

#### Choices

````markdown
```fill_gaps
instruction: Choose the correct word for each gap.
mode: choices
text: She [[goes]] to work [[by]] bus.
gaps:
  - choices: ["go", "going"]
  - choices: ["on", "with"]
```
````

Each dropdown contains the primary answer plus that gap's `choices`. Values are trimmed, blank values and exact duplicates are removed, and the remaining options are shuffled. Answers use exact matching. Include at least one distinct nonblank wrong choice per gap for an answerable dropdown. Otherwise the gap remains incomplete and produces a warning. `alternatives`, `prefill`, and shared `distractors` are inactive in this mode.

Inactive fields may be retained so the tutor can change modes later, but AI should omit them unless requested. An empty `fill_gaps` block or text without markers creates an incomplete exercise, not an automatic exercise inferred from the prose.

### Multiple choice

| Field | Type | Default / meaning |
| --- | --- | --- |
| `questions` | List of mappings | `[]`; questions in display order. |

Each question accepts:

| Field | Type | Default / meaning |
| --- | --- | --- |
| `text` | String | Empty; question text. |
| `options` | List of strings | `[]`; options in display order. |
| `correct` | Integer or null | Optional; one-based index into `options`. Absent or null means no answer selected yet. |
| `explanation` | String | Empty; explanation available after a correct answer. |

<!-- AI: Each question has exactly one correct option when complete. Count options starting at 1. Prefer at least two distinct nonblank options; multiple-answer checkboxes are not supported. -->

````markdown
```multiple_choice
instruction: Choose the most polite request.
questions:
  - text: What would you say to the barista?
    options:
      - Give me coffee.
      - I'd like a coffee, please.
      - You must make coffee.
    correct: 2
    explanation: "I'd like… is a polite way to make a request."
  - text: "Maya says: I'd like a coffee. What is she doing?"
    options:
      - Making a polite request
      - Refusing an offer
    correct: 1
```
````

The importer generates question and option IDs and converts `correct` to the selected option's ID. An index below 1, outside the options list, or pointing at a blank option is an error. Do not use an answer string, option ID, boolean, or list of indices for `correct`.

Question and option order is preserved, not shuffled. Missing question text, options, or a correct selection produces an incomplete question with a warning; it does not cause AI or the importer to guess an answer. Blank option slots are retained during index conversion so removing a blank cannot shift the answer key. Explanations are plain text, not Markdown, and are shown only after a correct selection.

### Matching

| Field | Type | Default / meaning |
| --- | --- | --- |
| `pairs` | List of mappings | `[]`; pairs in left-column order. |
| `distractors` | List of strings | `[]`; extra wrong right-column options. |

Each pair accepts `left` and `right`, both plain-text strings defaulting to empty.

````markdown
```matching
instruction: Match each expression to its meaning.
pairs:
  - left: takeaway
    right: food or drink to consume elsewhere
  - left: eat in
    right: have your meal at the café
distractors:
  - reserve a table for tomorrow
```
````

The importer generates pair IDs. The renderer preserves left-column order and shuffles right-side answers with distractors. Matching is exact after trimming the authored pair values. Repeated right-side answers remain separate items; duplicate distractors and distractors exactly equal to an answer are omitted from the displayed choices. Incomplete pairs are retained and warned about, not silently dropped.

<!-- AI: Use clear, unambiguous pairs. Do not add matching explanations, pictures, accepted-answer alternatives, or left-side distractors: the current exercise does not support them. -->

## Media import behaviour

These are importer requirements, not additional document fields:

1. Preview does not download image or audio files; these downloads start in the background only after the tutor confirms import. YouTube metadata resolution does make network requests during preview, once the document is otherwise valid, and is repeated on confirmation.
2. A missing or blank image/audio URL creates a normal empty section immediately, with the existing upload controls. `urls: []` has the same meaning for images. No generation prompt, audio script, or new placeholder section kind is needed.
3. For supplied image/audio URLs, show a downloading state, download and validate the files, then store them with Active Storage. Use our stored paths in lesson content, not external hotlinks. Preserve image order regardless of download completion order. While any file in a section is pending, disable its media inputs and hide its upload controls. Download results update the editor without a reload.
4. On failure, retain the section, identify the failed file, and offer retry, replacement URL, or manual upload. Failed downloads are not retried automatically. Do not silently fall back to external playback or discard a successful image because its partner failed. Pending and failed states are authoring state, not playable media sources.
5. Allow direct public HTTPS files only. Do not accept local paths, private-network addresses, embedded credentials, `data:`, `blob:`, AI `sandbox:` links, or authenticated sharing pages. Apply SSRF protection to DNS resolution, connections, and every redirect, including IPv4 and IPv6 destinations. Prevent DNS rebinding; URL-string validation alone is insufficient.
6. Enforce download timeouts, a maximum of 3 redirects, streamed byte limits, and actual detected file types, not just extensions or response headers. Apply the existing 10 MB image and 50 MB audio limits. Obtain duration from playable audio, not AI metadata. The importer does not add account quotas or document-size limits.
7. Ask the tutor to confirm the right to copy the files before import and again when supplying a replacement URL. Retrying the same URL does not require renewed confirmation. A public URL is not proof of permission. Do not fetch ordinary text links or download YouTube videos.
8. Retain stored files while any source lesson or frozen `LessonCopy` references them. Current snapshots preserve media URLs without duplicating blobs; deleting source content must not break copied lessons.

Existing audio authoring can hotlink external files, but version 1 import deliberately stores its own copy. AI-generated files with private or expired URLs must be uploaded manually.

## Validation and current-model mapping

Malformed front matter/YAML, unsupported versions, unsupported or mismatched languages, unknown fields or block labels, wrong value types, invalid gap markers, mismatched gap-option counts, invalid answer indices, and excess images are errors. Report the page/block and source line where possible. Do not partially write a structurally invalid lesson or silently discard unknown content.

Empty sections and structurally valid incomplete exercises are allowed because the current editor supports them. Warnings identify missing or unresolved media, removed Markdown images, and the incomplete gap, question, or pair cases described above. An empty `exercise`, `multiple_choice`, or `matching` block does not itself produce a warning. Do not invent missing content or automatically mark the lesson ready. Remote-file failures are handled separately from document validation as described above.

| Import content | Existing destination |
| --- | --- |
| Header `title`, `description` | `Courses::Lesson` attributes |
| Header `language` | Validate against the destination `Course#language`; inherit it when omitted, without changing the course |
| `page` title/description and document order | `Courses::Page` attributes and `position` |
| Section document order | `Courses::Section#position` |
| `text.content` | `kind: text`, `content_md` |
| Unblocked text and HTML comments outside blocks | Skipped; no persisted content |
| `teacher_note.content` | `kind: teacher_note`, `content_md` |
| Image `alt` and successfully imported URLs | `kind: image`, `title`, `metadata.image_urls`; `content_md` remains nil |
| Successfully imported audio | `kind: audio`, stored path in `content_md`; derived `audio_name`, `audio_size`, `audio_duration` metadata |
| YouTube URL and resolver result | `kind: youtube`, `content_md`, derived `youtube_title` and `youtube_thumbnail_url` metadata |
| Wordlist `words` | `kind: wordlist`, newline-delimited `content_md` |
| Empty `exercise` | `kind: exercise`, no selected `exercise_type` |
| Concrete exercise label | `kind: exercise`, matching `metadata.exercise_type` |
| Exercise `instruction`, fill-gap `mode` | Corresponding metadata fields |
| Fill-gap `text` and `gaps` | Marker-free `content_md`; generated IDs, UTF-16 offsets, primary answers, and per-gap options in `metadata.gaps` |
| Exercise `distractors` | `metadata.distractors` |
| Multiple-choice `questions` | `metadata.questions` with generated IDs, option objects, and `correct_option_id` |
| Matching `pairs` | `metadata.pairs` with generated IDs |

Metadata is produced by the importer as native arrays/objects, not AI-authored JSON strings. The existing accessors accept that representation. Do not expose raw `metadata`, `content_md`, database IDs, attachment IDs, or derived media fields as import options.

Runtime controls such as shuffle behaviour, attempt limits, hints, answer reveal, scoring, and exercise synchronization are owned by the existing application. They are not configurable in version 1. This format imports authored lesson content, not classroom sessions, students, or saved exercise progress.

<!-- AI: Final check: one versioned lesson header; at least one page; all lesson text inside explicit blocks; supported blocks and fields only; valid YAML; correct answer keys; no fabricated media URLs, reference headings, or field tables. Commentary outside blocks is skipped. Use only the block types needed for the requested lesson, not every example in this reference. -->
