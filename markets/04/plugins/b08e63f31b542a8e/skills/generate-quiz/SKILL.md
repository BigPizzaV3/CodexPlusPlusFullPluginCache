---
name: generate-quiz
description: Build a daily vocabulary quiz for a Gordito learner from the words their spaced-repetition schedule says are due, using what you already know about them.
---

# Generate a quiz from due vocabulary

Gordito stores the record; you supply the judgement. The server decides **when** a word
comes back and you decide **what the question looks like**. Never invent a review
schedule, and never quiz a word the server did not return as due.

## The loop

1. `get_enrollments` — pick the enrollment. If there is none, the learner has not finished
   signing up: send them to the sign-up page to choose their language. You cannot create an
   enrollment yourself, and you should not try.
2. `get_vocabulary` with `dueOnly: true` — this is the entire pool of words you may quiz.
   If it returns nothing, say so and stop; do not invent words to pad a session.
3. `generate_quiz` — each question naming the `vocabularyIds` it tests.
4. Wait. The learner answers in the card and it submits for you.
5. `grade_questions` — one call for the whole quiz, scoring every word each question
   tested, honestly.

## Writing the questions

Write the prompt in the learner's **origin** language and ask them to produce the
**learning** language. Production is the point: recognition is what they can already do.

**Draw on what you know about them.** This is the reason Gordito is worth using instead
of a flashcard app. If they have been talking to you about Formula 1 all week, set the
sentence at a race. If they mentioned their in-laws are visiting, use that. A word met in
a sentence that matters to the learner is a word that sticks.

Vary the shape across a session so it does not read as a drill:

- **Translate a sentence** — the default. Embed the due word in a natural sentence.
- **Complete the gap** — give a sentence in the learning language with the word removed.
- **Answer a question** — ask something whose natural answer needs the word.

Rules that matter:

- **Name every due word the question tests** in `vocabularyIds`. A question without any is
  rejected: the review would not count and the word would stay due forever. One word per
  question is the usual shape and the easiest to grade honestly, but a sentence that genuinely
  exercises two due words may name both — each is scored separately afterwards, so you are not
  forced to average them. Never list a word the prompt does not actually test just because it
  is due.
- **Never put the answer in the prompt.** Do not write the learning-language word, and
  avoid a cognate so transparent that no recall is needed.
- **Keep prompts to one sentence.** You are testing one word, not reading comprehension.
- **Use the example sentence as a hint of register**, not as the prompt itself — quizzing
  the sentence they were taught tests memory of the card, not knowledge of the word.
- **Cap a session at 10–15 questions** even when more is due. A session someone finishes
  beats one they abandon; the rest stays due tomorrow.

## Grading

Score on the FSRS rating scale, and be strict — this feeds the scheduler directly:

| Score | Meaning |
| --- | --- |
| 1 Again | Wrong, blank, or the wrong word entirely. **Requires at least one recorded error.** |
| 2 Hard | Right, but laboured, hesitant, or awkwardly phrased. |
| 3 Good | Right. |
| 4 Easy | Right, immediate, and idiomatic. |

A generous grade is not kindness. Marking a shaky answer `3` tells the scheduler the
learner knows that word, and they will stop seeing it precisely when they most need to.
If the answer would not pass with a native speaker, it is not a 3.

**Mark the whole quiz in one call.** `grade_questions` takes every question you are
marking. The batch is written together or not at all, so if one grading is rejected nothing
lands — you fix it and resend, rather than discovering half the quiz is marked and half is not.

**Write the marking in the language being learned.** `correctionNote` and every error `rule`
go in the enrollment's learningLanguage, not in the learner's own language and not in English.
Reading the explanation is itself practice. Keep it short enough that a B1 learner gets it
first time — a plain sentence beats a precise one they have to decode.

**Score each word on its own evidence.** A question that tested two words takes two scores.
If the sentence got `manzana` wrong and `pan` right, that is a 1 and a 4, not a 2 for both.
Averaging is the one thing the split model exists to prevent.

**A blank answer is a 1, never skipped.** The question was tied to words the learner was
meant to produce; not producing them is not producing them. Grade it, record an error saying
nothing was written, and let the scheduler hear it.

When you record an error, reuse an existing `errorType` whenever the mistake is the same
kind — `noun_gender` twice is a pattern the learner can be shown, while `noun_gender` and
`wrong_gender` are two things that look rare. Snake_case, specific, and about the
*grammar*, not the word: `ser_vs_estar`, `subjunctive_after_doubt`, `preterite_vs_imperfect`.

### Quote the mistake, do not describe it

Every error carries `originalForm`: the exact text from the learner's answer that was wrong,
copied character for character. The app finds that text and strikes it in place, writing
`correctedForm` above it. This is the whole reason the learner can see where they went wrong,
so it has to match.

- **Copy, do not retype.** `originalForm` must appear verbatim in the response. Same accents,
  same spacing, same case. If it does not match, the mark cannot be drawn.
- **A missing word is a widened span, not an empty one.** For `"voy playa"` where the answer
  should be `"voy a la playa"`, quote `"voy playa"` → `"voy a la playa"`. Never quote `""`.
- **A spurious word is an empty correction.** For `"yo yo voy"`, quote `"yo "` → `""`.
- **Quote the smallest span that carries the mistake.** `"el manzana"` → `"la manzana"`, not
  the whole sentence. Two errors in one answer are two spans.
- **Do not overlap two spans.** Only the first is drawn; the second is listed separately.
- **Set `occurrence`** when the text you quoted appears more than once. `0` is the first.

`correctionNote` is for the one-line explanation — *"manzana is feminine"* — not for restating
the sentence. The marked-up sentence is drawn from the errors.

### Vocabulary you meet while marking

Grading is when a gap is most visible. If the answer reveals a word the learner clearly does
not have, pass it in `addVocabulary` and it joins the notebook, linked to the error that
exposed it. Check `get_vocabulary` first — an exact pair already saved is skipped and reported
back rather than duplicated, but a near-duplicate (`manzana` against `la manzana`) is not
caught for you. Add the word the learner would actually look up.

Accepted spelling variants, regional forms, and missing accents are judgement calls.
A missing accent that changes the word (`papa` / `papá`) is an error; one that does not
is worth a `2` with a note, not a `1`.

## After the session

Say what happened in one or two sentences: how many were right, and the one pattern worth
noticing. If the same `errorType` came up more than once, name it and offer to drill it
tomorrow. Do not list every answer back — they just did the quiz.
