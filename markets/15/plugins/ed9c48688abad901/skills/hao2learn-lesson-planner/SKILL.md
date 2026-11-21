---
name: hao2learn-lesson-planner
description: Plan and build Mandarin lessons, worksheets and homework with hao2Learn. Use when a teacher asks for a lesson, worksheet, homework, quiz or vocabulary test, wants to run a lesson live, or asks how students did.
---

# hao2Learn lesson planner

These are defaults. When the teacher asks for something specific (a different lesson shape, exercise, length or language), do what they ask.

## 1. Live lesson or homework? Ask if unclear
Every worksheet works both ways, but is built differently. If the teacher has not said, ask once, together with any missing basics (level, length, topic): "Is this for a live lesson you'll run in class, or homework students open from a link?"

- **Live lesson**: students join with a code or QR (`start_lesson`); the teacher moves the class through it section by section (each `#` heading starts one; each exercise is its own step). Exercises: `reveal: "on_teacher_reveal"`, retries 0. Short instructions; the teacher explains.
- **Homework**: share with `get_share_link`. Exercises: `reveal: "immediate"`, retries 1-2, self-explanatory instructions, AI feedback on for writing.
- Results for both: `get_lesson_results`. A live worksheet can later be shared as homework; then offer to switch reveal to immediate with `update_exercise`.

## 2. Shape of a good lesson
The following is just one example. Depending on the topic it might make sense to deviate and focus more on audio, dialogues, specific exercises, english explanations, and so on. Feel free to get creative.
1. Warm-up: activate what they know (picture + one multiple choice, or a 3-card vocabulary test).
2. Input: a short text or dialogue at the level (`insert_content`, `generate_speech` for audio, optionally `generate_picture`). At most about 8 new words.
3. Vocabulary: `create_vocabulary_test` on the new words.
4. Controlled practice on the same words and pattern: fill the gaps, re-arrange, multiple choice.
5. Freer practice: guided writing (one pattern), then free writing (open task).
6. Exit check: one short multiple choice or vocabulary test.

Recycle the input's words in every exercise, vary exercise kinds, stay at the stated level, and start each section with a `#` heading. Live: about one exercise per 5-8 minutes. Homework: 4-6 exercises.

## 3. Which exercise for what
- Vocabulary test: call `search_dictionary` with the hanzi first and pick the reading you mean (行 xíng is not 行 háng); never guess word_ids. Max 10 cards (words x modes): `definition` for new words, add `pinyin` or `writing` for review.
- Particle or collocation contrasts (在/着, 了/过, 的/得/地): fill the gaps, mode `choice`.
- Words in context: fill the gaps, mode `word_bank`.
- Word order (time-place-verb, 把, complements): re-arrange, tiles chunked by meaning (在超市, not 在 + 超市).
- One grammar pattern: guided writing. Open expression: free writing (`ai_feedback: false` when the teacher wants to mark it).
- Comprehension and quick checks: multiple choice.
- Changing an exercise: `read_document`, then `update_exercise`. Never delete and recreate: collected answers would be lost.

## 4. Writing Chinese
Write Chinese plainly; the server segments it and adds pinyin. No hand-written pinyin or spaces. Dialogue speakers go in the bubble's speaker/pinyin attributes, not in the text. Instructions in the teacher's language.

## 5. After the lesson
`get_lesson_results`, then `get_exercise_answers` on the weakest exercise, then offer follow-up homework built from those mistakes (for example a vocabulary test of the words rated Wrong or Hard).

## Don't
- Invent new exercise types that don't exist as given in the tools descriptions
- Start a live lesson unless asked.
- Describe the whole document back; the editor card shows it.
- Put answers in instruction text.

## If the hao2Learn tools are not available
Ask the teacher to connect hao2learn for Teachers and sign in with their hao2learn account, then try again. Never invent document ids, word ids, lesson results or student answers.
