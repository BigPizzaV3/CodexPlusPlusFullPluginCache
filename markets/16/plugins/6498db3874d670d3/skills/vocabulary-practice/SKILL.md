---
name: vocabulary-practice
description: Quiz the user on words saved in Blindspot, focusing on the ones they know least, and update how well they know each word afterwards. Use when the user wants to practice, review, repeat or be tested on their saved vocabulary or on a specific Blindspot topic.
---

# Practice saved vocabulary

Explicit instructions from the user always take priority over this skill.

## 1. Pick the words

1. Call `list_vocabulary`. Pass `topic` if the user named one and
   `target_language` if they are learning more than one language. Use
   `limit: 200`; continue with `offset + count` while `has_more` is true, up
   to about 600 words.
2. If nothing comes back, say the vocabulary (or topic) is empty and offer to
   save words first. Stop.
3. Choose the words to practice. By default take 10 (or the number the user
   asked for), starting with the lowest `confidence`. Mix in a few random ones
   if many words share the same confidence.

## 2. Run the quiz

- Ask one question at a time and wait for the answer. Never show the answer
  in the same message as the question.
- Vary the format: translate into the target language, translate into the
  native language, fill the gap in a sentence, or use the word in a sentence
  of their own.
- Build questions from the saved translation, meanings and examples. Don't
  test a sense that isn't saved without saying so.
- After each answer, say whether it was right, give the correct form, and add
  one short tip or example when it was wrong. Accept close synonyms and small
  typos as correct, but point them out.

## 3. Wrap up

1. Summarize: how many correct, and which words to repeat.
2. Propose confidence updates on the 1–10 scale: about +1 for a correct
   answer (+2 if it was easy), −1 or −2 for a wrong one, kept between 1 and 10.
3. Apply them with `update_word` (the `confidence` field and the `word_id`
   from `list_vocabulary`) only after the user agrees, or if they asked up
   front to track progress. Report which words changed.

## Limits

- Don't change translations or enrichment during practice unless the user
  asks; if a saved translation looks wrong, point it out and offer to fix it.
- Practice does not delete words.
