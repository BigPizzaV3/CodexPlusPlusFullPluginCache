---
name: creation
description: "Read before creating lessons, quizzes or documents: gather the teaching brief, plan connected lessons, choose supported themes or recurring characters, resolve valid settings, and follow generation through to completion."
---

# Create lessons, quizzes and documents

Use this guide before calling `create_lessons` or `create_documents`. Use the named read tools below for live account and resource data. Read the references this guide links to from your installed skill files, or with `get_skill` and its `file` path when the skills are not installed.

## Gather a short teaching brief

Call `get_creation_context` for the teacher's country, language and plan, plus supported grades, languages, templates, themes and limits. Use details already supplied in the conversation. Ask only for missing information that changes what you will create, preferably in one short question with two or three parts.

- **What:** the topic and learning focus, or the existing Chalkie lesson/series to use as the source. Infer a teaching lesson, standalone quiz or printable document from the request; ask if the intended format is unclear.
- **Who:** the class year/grade or age range. Resolve a named year against the grades for the teacher's country. If the country or age-to-grade mapping remains ambiguous, ask which school system or class year they mean. Never guess an ID or ask the teacher to supply one.
- **Purpose and size:** for a broad topic, ask what pupils should learn. For slides, ask about slide count or lesson length when that would change the scope. For a vague document request, ask whether they want practice, a check of understanding, or another activity. Use specific instructions already given rather than asking again.

For example, if the teacher says only "Make a fractions lesson", ask "Which year group is this for, and should it introduce fractions or practise a particular skill?" If they already ask for a 6-slide Year 5 equivalent-fractions lesson and their account supplies an unambiguous school system and language, proceed without another questionnaire.

Use the account's country and language unless the teacher specifies otherwise; validate them against creation options. Ask for a missing language only if it cannot be inferred confidently. Do not make theme, image style, reading level, vocabulary, curriculum, or differentiation mandatory questions. Offer them when relevant to the brief, and otherwise leave optional settings unset so Chalkie applies its defaults. Do not claim browser-saved creation preferences are available through the account resource.

## Map the brief to supported inputs

### Slide lessons

Each `create_lessons.items[]` needs `topic`, `grade_id` and `language`. Match the grade label and country to the ID in creation options, and match language to its supported value. Put the learning goal, requested duration, prior knowledge, teaching approach and other requirements in `additional_instructions`.

Pass `slide_count` when the teacher requests a count; keep it within the returned plan limit. A duration is teaching context, not a slide count: do not silently treat 30 minutes as 30 slides. If a requested setting exceeds the plan or is unavailable, explain and agree on an alternative before changing that explicit requirement.

If one requested lesson exceeds the slide limit, offer a shorter lesson or a split into separate lessons, then **stop and wait for the teacher to choose**. Do not call a creation tool in that reply, even if their requested total could fit a batch. Saying "I'll split it" is not agreement from the teacher.

Use Chalkie's default theme unless the teacher requests a particular theme or custom look. For custom lesson designs, select Go Wild from `get_creation_context.options.lesson_themes` using `theme_id`, and put the teacher's visual preferences in `additional_instructions`. Do not add instructions to bypass the selected theme. Colour, readability or differentiation preferences alone do not require Go Wild. Go Wild applies to slide lessons; worksheets use the supported document themes.

Use `inclusions.activitySheet` only when an accompanying printable is requested, and select its template/difficulty levels from the supported options. Read `references/lesson-series.md` for connected lessons. Multiple lessons created by this tool are standalone resources, not a native series.

### Standalone quizzes

For an interactive quiz, use `create_lessons` with `type: "quiz"`, `question_count` and optional `question_types` from `options.quiz_question_types`. The count is questions only; Chalkie adds the cover. Respect `limits.max_questions_per_quiz` and ask before shortening or splitting an oversized request. Do not use `slide_count`, lesson frameworks, vocabulary or inclusions for a quiz. A printable paper quiz still uses `create_documents`.

A quiz can assess a topic or an owned lesson/series. For a saved source, resolve it with `search_resources`, read it with `get_resource`, and pass `source_lesson_id` or `source_series_id` (never both). This uses the real source and inherits its audience, language and curriculum. Do not create a new series.

Quizzes are saved as lesson resources: use `resource_type: "lesson"` for read, preview and recreation tools. Show `preview_resource` after creation. The card includes Teach, which opens Teach Mode; the image carousel itself does not run interactive questions.

### Recurring characters

For a recurring character, mascot or cast, read `references/consistent-characters.md`. It explains how to establish and reuse an original image within one lesson and the limits on cross-lesson reuse.

### Printable documents

Booklets and workbooks are the same native document format. Use `create_documents` with `type: "workbook"` for these, following the booklet steps below. Ordinary worksheets and posters use `type: "activity_sheet"` (the default). A workbook is not a worksheet template or a collection of difficulty variants.

Choose `source` from the actual brief:

- `topic`: provide the topic, grade ID and language.
- `lesson` or `series`: use `search_resources` to locate the intended source, then call `get_resource` with its type and ID. Ask the teacher to choose if several resources match. Provide the corresponding `lesson_id` or `series_id`; the source supplies its audience, language and content. Pass the source language. This source mode does not override the source's language or grade; if the teacher requests a different audience or language, explain that limit and offer a topic-based brief grounded in the source content.

Every document requires `language`; topic documents also require `grade_id`. For worksheets, pick a supported `template` that matches the requested activity, such as an exit slip or word problems. If the request is specific enough, choose the matching template without asking the teacher to name a template. Leave it unset when no specific format is needed. Use `difficulty_levels: ["core"]` unless differentiation is requested. Explain that support/core/challenge variants create multiple documents; do not add variants without a teaching reason or request.

For worksheets, each difficulty level is a separate saved worksheet. Write the shared `additional_instructions` for **one worksheet**, with the requested question count and answer page. Do not ask for both easier and harder sections in every worksheet: Chalkie applies the selected difficulty to each version separately. You can describe how support and challenge should differ. This also applies to `inclusions.activitySheet.prompt` on a lesson.

Only add new curriculum alignment when requested; documents based on lessons or series inherit the source's existing alignment. Resolve the curriculum from creation options, then use `search_curriculum_standards` for IDs. Never fabricate a standard or claim alignment without selected or inherited standards. Use only supported theme IDs.

### Booklets and workbooks

Use the same topic, lesson or series source rules as other documents. For a lesson or series, read its full content before planning; keep the booklet within that source's concepts and class level.

1. Establish the topic/source, class year and student-page target. `workbook.minPages` and `maxPages` count the cover but exclude answers. Respect `limits.max_pages_per_workbook`; null allows an open-ended `maxPages: null`. Numeric bounds must be 1–100. Page counts are targets, not exact layout guarantees. Ask before shortening or splitting an oversized request.
2. Draft a short ordered section outline in the conversation. Each section has `title`, `content` (concepts and activities) and `questionCount` (0–30 top-level questions). Use 1–30 sections. Budget for the cover, headings, teaching, diagrams and answer space: a short booklet usually needs only 1–2 top-level questions per remaining page. More pages add practice at the same level, not harder concepts. Show the outline and page range and wait for the teacher to approve, unless they already supplied or approved that outline.
3. Call `create_documents` with `type: "workbook"` and `workbook` containing the page bounds, approved `outline` and four booleans: `includeTeachingMaterial`, `includeObjectivesAndKeywords`, `includeSupport`, `includeChallenge`. Infer these from the brief; default teaching/objectives on and support/challenge off when unspecified. Support and challenge go inside the same booklet. Omit `template` and omit `difficulty_levels` or use `["core"]`. Do not invent section IDs; Chalkie assigns them.
4. Chalkie saves a native workbook outline and queues generation of one booklet with a cover and answer key. Preview it with `resource_type: "document"`, retain its saved ID, and follow the normal completion flow below. `document_type: "workbook"` identifies it in creation, search and read results.

The plugin creates booklets but does not yet recreate existing workbooks with Edit Prompt; use Chalkie for that action. Do not describe booklets as unsupported or substitute several worksheets. Folded-print imposition and binding controls are not exposed.

## Write additional instructions like a teacher briefing a colleague

Write `additional_instructions` in natural, conversational language. Explain what the class should learn and how the lesson or activity should unfold. Prefer concrete requests such as "Start with a quick recap, then work through one example together" over formal phrases such as "Facilitate retrieval activation and scaffold progressive mastery".

- Use short sentences and familiar words. Avoid repetitive "Ensure..." commands, inflated adjectives, generic claims about engagement, and labels such as "Pedagogical objective" when a sentence would be clearer.
- Keep the teacher's specific requirements, examples and constraints. Don't invent facts about their pupils or previous lessons, and don't add activities or differentiation just to make the brief sound thorough. Preserve wording they explicitly ask you to use.
- Format the text with short paragraphs separated by blank lines. Use a short Markdown heading when a longer brief needs sections, bullets for a set of requirements, and a numbered list when order matters. A short brief can simply be two paragraphs; don't force every request into a template.
- Put real line breaks in the instruction text. Normal JSON escaping during a tool call is fine, but the decoded field should contain readable text, not literal backslash-n sequences, HTML, or an enclosing code block.
- Before calling the tool, read the brief once: would a colleague understand what to teach, what to include and what to leave out? Remove filler while keeping the useful detail. Apply the same style to an accompanying activity sheet's `inclusions.activitySheet.prompt` when used.

### Example lesson brief

Help the class understand why two fractions can have the same value. Start with fraction strips so they can see that 1/2, 2/4 and 4/8 cover the same amount, then work through one example together.

Give pupils a few pairs to compare on their own. Ask them to explain one answer with a drawing, and finish with a quick question that checks whether they can spot equivalent fractions without the strips. Leave adding and subtracting fractions for another lesson.

### Example worksheet brief

Give pupils some practice finding equivalent fractions, starting with pictures and moving on to missing numbers. Keep the wording short and leave enough room to draw or show their working.

Include:

- One completed example using a fraction strip.
- Four questions with diagrams and four with missing numerators.
- A final question asking pupils to explain how they know two fractions are equivalent.

Put the answers on a separate page so the teacher can keep them back.

These examples illustrate tone and formatting. Adapt the content to the actual request; don't add their question counts, activities or answer-page requirement to unrelated briefs. For a connected sequence, keep the extra context required by its reference and write it in this same style.

## Create and report the result

Once the essentials are known and the teacher has asked for creation, briefly state the brief and call the appropriate tool. Do not add a separate confirmation step when nothing material remains unresolved. If they asked only for ideas or a plan, do not create resources yet.

Keep batches within the returned limit. Preserve every returned ID. If a batch stops with an error, do not recreate items that returned an ID; call `get_resource` with their types and IDs before deciding what still needs attention. Only retry items known not to have been created.

Generation runs in the background. Say it has started, then call `preview_resource` with the resource type and saved ID (`lesson` for lessons and quizzes; `document` for worksheets and booklets). The inline card checks generation progress, shows saved slides or document pages, and links to Chalkie. Completed lessons and quizzes also have a Teach button. Do not poll `get_resource` just to update the card. On clients without inline UI, use the returned status and link; only read full content when needed. Do not loop on validation, permission or unknown-resource errors. Report failures honestly. A completed document can still contain generating media; the card waits for those assets before showing its preview. Lesson series do not have a preview card.

For differentiated worksheets, `versions` contains every saved version, including the root. Show a preview for each requested version using its own ID. On a later request for the easier or harder worksheet, use `get_resource` to read `versions` and select the matching difficulty. Do not treat a later page in the root worksheet as a different saved version.

The preview images are for the teacher. This MCP does not return slide screenshots to the assistant, so do not claim to have visually inspected them.

## Download a resource

After creation, use the separate `export` skill when the teacher requests a download or Google Slides/Docs transfer. If it is not installed, read it with `get_skill` and `name: "export"`. Use the saved resource ID; do not create the content again to export it.
