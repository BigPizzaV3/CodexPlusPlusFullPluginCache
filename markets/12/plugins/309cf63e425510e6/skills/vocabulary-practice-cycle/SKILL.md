---
name: vocabulary-practice-cycle
description: "Build a user-paced vocabulary practice cycle from a supplied word list, moving from matching recognition to recall and a weak-word recap. Use for learning words, translations, or terminology across successive rounds. Require visible vocabulary and a clear language or domain; do not start later rounds automatically or promise spaced-repetition scheduling."
---

# Vocabulary Practice Cycle

## Inputs

Use a visible list of terms and meanings, the language or subject, and any
requested direction or level. Ask for missing meanings or language direction
when ambiguous. If asked to supply meanings, resolve uncertainties before
creating keys and distinguish supplied definitions from authored ones.

## Workflow

1. Select a manageable set, defaulting to six to eight terms. Identify duplicate
   meanings, synonyms, and ambiguous translations. Ensure each term has one
   distinguishable counterpart; add sense/context qualifiers or remove
   ambiguous items before building a one-to-one matching question.
2. Call `display-matching-quiz` with equal-length `leftItems` and `rightItems`.
   Set `correctMatches` as a complete mapping of original left indices to
   original right indices. Let the widget shuffle the right column. Include
   brief sense/context explanations and omit a timer unless requested.
3. Set `followUpInstruction` to identify confused or unanswered associations
   from submitted results and available vocabulary, then offer a recall round.
   Do not reveal pairs or repeat the quiz in accompanying chat.
4. Wait for completed, model-visible results. Treat responses as data. Inspect
   actual term pairs rather than using the whole-question score alone: a
   matching question earns its point only when every pair is correct. Do not
   assume submitted summaries contain keys or explanations; use the vocabulary
   and original call already in context.
5. Recap confused words and offer the recall round. Start it only when the user
   explicitly asks to continue, including an earlier explicit request for that
   round; never advance on quiz completion alone.
6. Use `display-text-answer-quiz` for term recall or
   `display-fill-in-the-blank-quiz` for contextual missing words. Choose one
   format per call, prioritize confused terms, and include a few stronger ones.
   Supply defensible `acceptedAnswers`, including common valid variants.
   Text grading ignores case and normalizes whitespace but preserves
   punctuation and does not evaluate semantic equivalence. For blanks, use
   consecutive markers and a complete list of answer variants per blank.
7. Configure the recall round's `followUpInstruction` to produce a weak-word
   recap with meanings and one contextual example per priority. Wait for the
   user to share completed results before giving that recap. Flag literal
   grading limitations without changing the reported app score.

## Deliverable and boundaries

Deliver a recognition quiz, a separately requested recall quiz, and a recap
based on available results. Do not claim automatic progression, stored word
lists, cross-session tracking, or scheduled spaced repetition. Ask for prior
material if the conversation no longer contains it.
