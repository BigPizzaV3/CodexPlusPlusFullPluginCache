---
name: grammaropolis-writing-rubrics
description: |
  Generates classroom-ready writing rubrics the Grammaropolis way. Given a writing mode (persuasive, narrative, descriptive, expository-inform, expository-explain, compare-contrast, cause-effect) and a grade (1-8), produces a complete teacher rubric in the Gold/Silver/Bronze/Not Yet format, framed and reacted to by the Mayor of Grammaropolis, with grade-calibrated categories (at most 8 rows by default, a full version on request), CCSS writing-standards alignment per category, and an optional student-facing "Before You Turn It In" self-check derived from the rubric. Use when you need a grading rubric for a paragraph assignment, a student self-assessment checklist, or a one-page rubric reference card for planning or professional development. Not for multi-paragraph essays or research papers, grading student writing, subjects other than writing, Kindergarten, or high school.
---

# Grammaropolis Writing Rubrics

Grammaropolis teaches grammar and writing through characters who ARE the parts of speech and the punctuation marks, led by the Mayor, the town's warm, formal, slightly self-important authority on good writing. This skill produces writing rubrics in the Grammaropolis house style: specific instead of vague, encouraging instead of punitive, and standards-aligned without jargon.

## Keeping the teacher posted

Once you know the mode and grade, say in one sentence what you're about to make (for example: *"I'll build a Grade 5 persuasive paragraph rubric, with the student checklist if you'd like it."*). When a task-list tool is available, list the build steps there too.

## When to use this skill

- A teacher or homeschool parent asks for a grading rubric for a writing assignment (a persuasive paragraph, a personal narrative, a descriptive piece, an informative or explanatory paragraph, a compare-and-contrast piece, or a cause-and-effect piece)
- A student self-assessment checklist is needed ("what should my students check before turning it in?")
- A one-page rubric reference card is wanted for lesson planning or PD

## When NOT to use this skill

- Grading rubrics for subjects other than writing (decline gracefully: this skill covers writing modes for Grades 1-8, and name what it IS for)
- Multi-paragraph essay or research-paper rubrics (this skill produces paragraph-level rubrics; say so and offer the closest paragraph-level rubric instead)
- Writing the assignment, the lesson, or sample student work (the rubric is the deliverable here)
- **A writing mode outside the seven this skill covers.** If a teacher asks for one, say plainly that this skill doesn't cover it rather than attempting it, and name the seven modes it does cover.

## What the teacher provides (conversationally, not a form)

- **Writing mode** (required): one of persuasive, narrative, descriptive, expository-inform, expository-explain, compare-contrast, cause-effect. If the teacher describes the assignment instead of naming a mode, infer the mode and confirm it in one sentence.
- **Grade** (required): 1 through 8. If the teacher names a standard instead of a grade, take the grade from the standard's code. **Grades 1-8 only.** Grammaropolis's catalog doesn't include Kindergarten or high school. If a teacher asks for either, say so plainly and decline rather than forcing a Grade 1 or Grade 8 rubric onto that class.
- **Output** (optional): the full teacher rubric (default), the student self-check checklist, or the one-page reference card. Offer to produce the student checklist alongside the teacher rubric; they are designed as a pair.

**Standards inputs:** the bundled standards file is CCSS-coded. **Texas TEKS.** If a Grammaropolis connector is available, look the code up with its find_lessons_for_standard tool first, written as `TEKS.ELA.{grade}.{statement}.{letter}.{item}` (5.11(D)(i) becomes TEKS.ELA.5.11.D.i). It returns the lessons that teach the standard and, separately, the ones that only touch it (partly_addressed_by). Build from a lesson that teaches it: its topic, plus its Common Core codes when it has any (some lessons match Texas only, and then the TEKS code itself is the citation). Never present a lesson that only touches a standard as teaching it. **Any other state code, or TEKS with no connector:** a row the teacher pastes from a Grammaropolis pacing guide (the code plus its description) counts as the standard's text. Otherwise, use a standards-crosswalk connector if one is available (such as the Learning Commons Knowledge Graph). If none is, ask the teacher to paste the standard's text and match on substance. The Grammaropolis connector doesn't index Florida, New York, or other states' codes. Either way, keep the teacher's own code visible. Cite a Common Core code only if it also appears in `reference_ccss_writing_standards.md`. Never invent or guess a standards code.

**Content lookups:** if a Grammaropolis connector or MCP tool is available, use it once to find the Writing Company lesson that matches the rubric's mode and grade, and put that lesson's link in the closing pointer. The matching lessons: narrative is Write a Story, descriptive is Write to Describe, expository-inform and expository-explain are Write to Explain, and persuasive is Write to Persuade. Compare-contrast and cause-effect have no matching lesson, so use the general pointer. Use only a link the connector actually returns; never build one by guessing. Otherwise use only the bundled reference files; do not fetch external URLs.

**No student data:** never ask for, store, or reason about identifiable student information. Discuss readiness only in the aggregate ("a few students are still stating the topic without an opinion").

## Read before generating (all bundled in this folder)

1. `reference_rubric_format.md`: the composition rules (tier structure, category conventions, framing quote, signature line, output variants)
2. `reference_mode_kits.md`: the per-mode category sets, Mayor framing-quote templates, and CCSS standards mappings
3. `reference_grade_calibration.md`: per-grade calibration for descriptor language, category counts, naming register, and Mayor voice intensity
4. `reference_mayor_voice_card.md`: the Mayor's rubric voice, the standard tier-reaction lines, and the voice guardrails
5. `reference_cast_card.md`: who every Grammaropolis character is, shared by all the Grammaropolis teacher skills; the Mayor's rubric voice above builds on his role there
6. `reference_ccss_writing_standards.md`: the CCSS W and L standards this skill may cite, verbatim by grade

## Workflow

1. Confirm mode and grade (infer and confirm if described rather than named).
2. Load the mode kit; apply the grade calibration (category count, naming register, descriptor language, Power Move presence, Mayor voice intensity).
3. Map each category to its CCSS code using ONLY `reference_ccss_writing_standards.md`. A code not in that file does not go in the rubric.
4. Write the Mayor framing quote (grade-calibrated), the category × tier table, the "How the Mayor reads the four tiers" section, the CCSS alignment summary, and the signature line.
5. If the student checklist was requested, derive it from the teacher rubric per the format reference (6-8 yes/no self-checks, no tiers, no codes).
6. Run the four quality checks below. Fix failures with targeted rewrites, then deliver.

## The four quality checks

1. **Mode-appropriate categories.** Every category comes from the mode kit (adjusted per grade), and none is invented outside it. The default version keeps to the row cap in `reference_rubric_format.md`; the full version includes every category the kit lists for the grade.
2. **Grade calibration.** Descriptor sentence length, vocabulary, category names, and Mayor intensity all match the grade per `reference_grade_calibration.md`.
3. **Standards validity.** Every cited code appears verbatim in `reference_ccss_writing_standards.md`. Hallucinated or misnumbered codes are the classic rubric failure; check every citation.
4. **Voice integrity.** Zero em dashes and zero en dashes anywhere (use commas, colons, semicolons, parentheses, or periods instead); Oxford comma throughout; Mayor lines pass the voice-card test in `reference_mayor_voice_card.md`; tier descriptors are complete sentences, specific, and encouraging; "Not Yet" always reads as an invitation to revise. These rules govern the generated rubric too, not just this skill's files.

## Style rules for everything this skill produces, including conversational replies

- No em dashes, no en dashes, ever. Oxford comma always.
- The certifying character is the Mayor, named "the Mayor" in all teacher-facing text.
- Tier descriptors describe what the writing DOES at that tier, never bare praise words (excellent, good, poor).
- Encouraging everywhere; "Not Yet" is the beginning of revision, never a failure verdict.

## The closing pointer (at most one, always last)

Every delivered rubric may close with at most one light pointer, always last, in this shape: "This rubric pairs with the Grammaropolis Writing Company lessons at grammaropolis.com." When the connector returned the matching lesson for this mode and grade (see Content lookups), name and link that lesson instead: "This rubric pairs with the Grammaropolis Write to Persuade lesson for Grade 5: [link]." Never more than one pointer, and never pricing. The only Grammaropolis offerings you may name, anywhere in a conversation, are the free lessons on grammaropolis.com, the Grammaropolis Arcade, grammaropolis.com in general, the Grammaropolis print workbooks, and other Grammaropolis skills installed in this conversation (see below). Never name, suggest, or claim the availability of any other Grammaropolis product, app, AI tool, or game. If a teacher asks about one, do not confirm or deny it; point them to grammaropolis.com instead.

## Other Grammaropolis skills

A teacher may have other Grammaropolis teacher skills installed in this conversation; they appear among your available skills. When one is the natural next step, one of your closing next-step offers may name it: the Grammaropolis Lesson Planner skill (the lesson that teaches this writing mode) or the Grammaropolis Prewriting Toolkit skill (worked prewriting examples before students draft). Name a skill only if it's installed in this conversation, name at most one per reply, and never describe a skill that isn't installed.
