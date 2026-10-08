---
name: moknah-text-preparation
description: Clean and prepare raw extracted text for narration in Moknah - strip page furniture, verbalize numbers, dates and abbreviations, build a proper-names dictionary, and segment into lines. Use after extracting text from a PDF/Word/EPUB and before creating a Moknah project or generating audio. Arabic-first but applies to any language.
---

# Preparing text for narration

Cleaning is **free**. Rendering is not. Every defect you leave in the text gets
paid for twice: once to render it wrong, once to render it again. Do this work
before any credit is spent.

Log every change you make. Silently deleting the author's text is the worst
failure mode in this whole workflow - always be able to show the user what you
removed and why.

## 1. Structural cleanup

Remove what belongs to the page, not to the book:

- Lines that are only a page number
- Running headers and footers that repeat across pages
- Footnote blocks, plus their in-text markers (`(1)`, `¹`) - **only** when a
  matching footnote actually exists
- Table-of-contents fragments that leaked into the body

Then repair the extraction:

- Merge lines broken mid-sentence (no terminal punctuation at the break)
- Rejoin hyphen-split words across line ends
- Collapse repeated spaces, blank lines and duplicated paragraphs

## 2. Symbols and punctuation

- Bullets and list markers -> rewrite as flowing sentences. A narrator cannot
  read a bullet.
- `/`, `\`, `_` -> a comma, or the word "or", whichever the sense requires
- Keep a single hyphen used as an aside; drop decorative dashes and rules
- `...` -> a period, unless the hesitation is deliberate
- Strip tatweel (ـــ)
- Keep `﴿ ﴾` around Qur'anic verses (confirm with the user - it affects delivery)
- Normalize curly/fancy quotes to a consistent pair

## 3. Verbalization - always yours to do

AI-Enhanced normalization applies **tashkeel only**. It does not turn symbols into
words. You must:

- **Numbers, dates, percentages, currency** -> written out in words, with correct
  i'rab for Arabic. `1995` -> `ألف وتسعمئة وخمسة وتسعين`, inflected to fit the
  sentence.
- **Abbreviations** -> expanded: `د.` -> `الدكتور`, `ﷺ` -> `صلى الله عليه وسلم`,
  `(رض)` -> `رضي الله عنه`
- **URLs and emails** -> drop them, or spell them out if the meaning depends on it
- **Foreign names** -> transliterate with the `پ / گ / چ` convention
  (`Google` -> `گوگل`) and record every one in a **proper-names dictionary**.

The names dictionary is the single most valuable artefact you produce. Keep it
consistent for the entire book - a character whose name is pronounced two
different ways in chapter 3 and chapter 9 is an obvious defect. Persist it and
reuse it across books by the same author or in the same series.

## 4. Structure

- Map TOC headings to chapter titles
- Subheadings: merge into the body, or keep as their own chapter. Ask in Full
  Control and Guided; merge silently in Express.
- Detect dialogue and build a speakers map - see `moknah-dialogue-and-pacing`

## 5. Segmentation into lines

A line is one spoken unit and one TTS request. Segment where a human reader would
breathe.

Rules:

- **Never split mid-sentence.**
- Merge consecutive lines belonging to the same speaker into one line (see the
  dialogue skill) - this is the most common cause of choppy audio.
- Max **200 lines per chapter**.
- Respect the per-request character ceiling: **3,000 with emotions on, 10,000
  off.**
- Prefer shorter lines where the text is risky (OCR'd, heavy with numbers or
  foreign names) - a bad line then costs one cheap single-line re-render instead
  of a whole chapter.
- Add missing punctuation, especially before conjunctions, so the engine knows
  where to breathe.

`line_split_mode` options at project creation: `sentences`, `newline`, or
`custom` (with `line_split_custom`).

## 6. OCR text needs stricter review

If the source was scanned and OCR'd, flag it (`ocr_source = true`) and review
harder. OCR reliably confuses:

- `ب / ت / ث / ن` - the dotted forms
- hamza placement (`أ / إ / ء / ئ`)
- `ة / ه` at word end

If more than ~5% of characters are unreadable, retry the extraction once, then
show the user a sample rather than pushing bad text forward.

## 7. Report before you proceed

Hand the user a cleaning report before creating the project:

- Counts per operation (lines merged, footnotes removed, numbers verbalized...)
- Before/after samples of the more aggressive edits
- The proper-names dictionary
- Verses or quotations detected
- The resulting chapter list

Get approval, then create the project. Corrections made now are free; the same
correction after rendering costs a full re-render.
