---
name: unclass-lesson-builder
description: Create and revise useful language lessons in the Unclass `unclass/1` Markdown import format. Use when a tutor asks to build, adapt, or fix an importable Unclass lesson.
---

# Unclass Lesson Builder

Help tutors create useful language lessons in the `unclass/1` Markdown import format.

## Reference files

Use [references/import_lesson_format.md](references/import_lesson_format.md) as the authority for syntax, supported fields, defaults, and validation rules. Use [references/lesson-import-example.md](references/lesson-import-example.md) as a worked example, not as a lesson to copy. Consult the relevant reference sections before generating or revising a lesson. If the example and specification disagree, follow the specification. If you cannot access the specification, ask the tutor to attach it; do not invent a replacement format.

The example contains an intentional unblocked import-check sentence and empty sections. Do not reproduce that sentence or the example's media URLs in unrelated lessons. Do not include every block type unless requested.

GET THE LESSON BRIEF
Establish the language being taught, learner level, topic or learning goal, and approximate duration. Ask only for missing information, in one short group of questions. Use information already supplied. Interests, age group, and preferred activity types are optional. Do not request identifying student data.

The teaching language is not necessarily the language of the tutor's message or the student's native language. Supported codes are en, es, fr, de, it, pt, and ru. For an unsupported language, explain the limitation and ask for a supported choice. Do not silently substitute another language. If a stated destination course has a different language, ask the tutor to resolve the mismatch. Do not claim access to their courses.

Once the brief is sufficient, create the lesson without another approval question. Adapt vocabulary, activity difficulty, and approximate length to the brief. Keep teacher-only guidance in teacher_note blocks. Use clear student instructions and correct, unambiguous answer keys.

DOCUMENT RULES
Return one complete lesson document inside one Markdown code wrapper. Use four backticks for this outer wrapper and three backticks for the lesson's blocks. If a lesson block needs a longer fence for literal code, make the outer wrapper longer still. Put no introduction, conclusion, citations, or explanatory prose outside the wrapper when delivering a lesson.

The document inside the wrapper must start with YAML front matter delimited by --- lines. Its fields are format: unclass/1, a nonblank title, language when known, and optional description. Include the established teaching language as its lowercase code. Do not add level, duration, objectives, status, or words as header fields. Useful learner-facing details can go in description or a text block.

Create at least one explicit page block before any section block. Each block body is a YAML mapping. Only the lesson header and page blocks accept title. Pages also accept description. Section order and page order come from document order; never supply IDs or position fields.

All lesson prose must be inside explicit text or teacher_note blocks under content. Put Markdown headings, lists, tables, and paragraphs inside that content. Unblocked text and comments are skipped by the importer, so never put learning material there. Use content: |- for multiline Markdown. Use spaces for YAML indentation. Do not use YAML tags, anchors, aliases, or duplicate keys.

Quote every value that would otherwise break YAML. Wrap the whole value in double quotes, or write it as a |- block, when it contains a colon followed by a space (such as "El profesor dice: Buenos días."), contains a space then #, starts with - ? : , [ ] { } # & * ! | > ' " % @ or a backtick, or is yes, no, true, false, null, a number, or a date that must stay text. An unquoted embedded colon is the most common import error and reports "mapping values are not allowed in this context". This applies to every authored string, including instruction, question text, options, explanation, fill-gap text, pair left and right, distractors, and words.

SUPPORTED SECTION FIELDS
- text: content.
- teacher_note: content.
- image: url OR urls, plus optional alt. Never combine url and urls. Use at most two images in one block. alt describes the image for accessibility; it is not a title or caption.
- audio: url.
- youtube: url.
- wordlist: words, as a list of strings. Each item is one word or phrase. Do not put comma, semicolon, or newline separators inside an item. Do not add definitions or translations as extra fields.
- exercise: no fields. Use only when the tutor explicitly wants an unfinished exercise whose type they will choose later.
- fill_gaps: instruction, mode, text, gaps, distractors.
- multiple_choice: instruction, questions.
- matching: instruction, pairs, distractors.
Do not add section title, raw metadata, content_md, attachment identifiers, filenames, sizes, durations, or generated media metadata.

EXERCISES
For fill_gaps, use [[answer]] markers in text. Do not calculate offsets or send answer IDs. The modes are typing, word_bank, and choices. Per-gap options go in gaps, in marker order. If gaps is supplied, include exactly one mapping per marker; use {} when no options are needed. In typing mode, alternatives are extra accepted answers and prefill is starting text to edit. In word_bank mode, distractors are extra wrong bank options. In choices mode, each gap's choices are extra wrong options; the primary answer comes from its marker. Give each dropdown at least one distinct wrong option. Follow the specification for escaping markers.

For multiple_choice, each question has text, an options list, one correct index counted from 1, and an optional explanation. Use at least two distinct options for a complete activity. Do not send a correct answer string, an ID, or multiple correct indices.

For matching, each pair has left and right strings. Optional distractors are extra right-side choices. Exercise instructions, question text, options, explanations, and pair values are plain text, not Markdown.

Unless the tutor requests an unfinished activity, generate complete questions, pairs, and gap answers. Check that the answer keys agree with the lesson material.

MEDIA
Use only relevant source URLs supplied by the tutor. Image and audio sources must be direct public HTTPS file links. Do not invent URLs, copy documentation placeholder URLs, search for media, or claim to have verified a URL. Leave image, audio, or youtube blocks empty when a needed source is unavailable. An image may still have alt text. Empty media blocks are valid.

Do not embed images with Markdown image syntax. Do not add image prompts or audio scripts as media fields. If the tutor requests an original listening script, put it in teacher_note content. Do not invent facts about an unknown recording or video. YouTube is an embed, not a file download. Never use sandbox:, blob:, data:, or local file paths as media sources.

REVISIONS AND CHECKS
When asked to revise a lesson or fix validation errors, return the complete corrected document. Preserve unaffected content. Do not return only a patch or partial replacement unless the tutor specifically asks for a fragment.

Before delivery, review the header, language, page boundaries, block labels, allowed fields, YAML indentation, quoting of values containing a colon and space, gap-option counts, answer indices, and media rules. This is a self-check, not proof of parser validation. Do not claim that Unclass imported or validated the lesson, that media was downloaded, or that you ran tools you do not have.

If the tutor asks a setup or clarification question rather than requesting a lesson, answer briefly in ordinary prose. Keep those answers separate from delivered lesson documents.
