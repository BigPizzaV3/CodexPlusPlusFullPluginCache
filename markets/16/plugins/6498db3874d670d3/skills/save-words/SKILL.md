---
name: save-words
description: Save words and phrases to the user's Blindspot vocabulary with translation, meanings, collocations, synonyms and usage examples, optionally grouped into a topic. Use when the user asks to save, remember or add words, wants to collect vocabulary from a text, or has opted into automatic word capture for this chat.
---

# Save words to Blindspot

Explicit instructions from the user always take priority over this skill.

Only save when the user asked to, or has explicitly opted into automatic
capture in this chat. Translating or explaining a word does not by itself mean
the user wants it saved.

## 1. Decide what to save

- Use the dictionary form for single words (`went` → `go`), but keep phrasal
  verbs, idioms and fixed phrases whole (`run out of`, `on second thought`).
- When extracting from a text, prefer words that are new or useful for the
  user. Skip names, numbers and very basic words unless the user asks.
- If more than 15 candidates come up, show the list first and ask which to
  save.

## 2. Determine the languages

`add_word` needs `target_language` (the language being learned) and
`native_language` (the translation language) as ISO 639-1 codes. Take them
from what the user said, or from existing words returned by
`list_vocabulary`. If they are still unclear, ask once. Do not guess.

## 3. Check for existing entries

For each item, call `list_vocabulary` with `search` set to the word.

- Not found: save it with `add_word`.
- Found: tell the user it is already saved. Update it only if the user wants
  a correction or more detail. Use `update_word` with the `word_id` returned
  by `list_vocabulary`. Never invent a `word_id`.

`add_word` on an existing word merges into the existing entry rather than
creating a duplicate, so a repeated save is safe. Still, check first, so you
can tell the user what was new and what was updated.

## 4. Fill in the entry

Write the enrichment yourself; Blindspot stores exactly what you send.

- `native_value`: a short, dictionary-style translation, not a sentence.
- `meanings`: one item per sense actually relevant to the user, each with
  `part_of_speech`, a plain `definition` in the target language, and a
  `translation`.
- `usage_examples`: two or three natural sentences with translations. If the
  word came from the user's text, base one example on that context.
- `collocations` and `synonyms`: include them when they are genuinely common;
  leave them out rather than pad.
- `topic`: set it only if the user named a topic, or agreed to one you
  suggested. The topic is created if it does not exist. Call `list_topics` to
  reuse an existing topic name exactly instead of creating a near-duplicate.

Prefer the structured fields above over the legacy `context` and `examples`.

## 5. Report

After saving, give a compact table: word, translation, topic, and whether it
was new or updated. Mention anything you skipped and why. Do not claim a word
was saved unless the tool call succeeded.

## Organizing existing words

- Move or group saved words with `add_word_to_topic` and
  `remove_word_from_topic`, using ids from `list_vocabulary`.
- Removing a word from a topic, or deleting a topic with `delete_topic`, keeps
  the words themselves.
- `delete_word` permanently removes a word. Use it only when the user clearly
  asks to delete that specific word, and confirm first if the request is
  ambiguous or covers many words.
