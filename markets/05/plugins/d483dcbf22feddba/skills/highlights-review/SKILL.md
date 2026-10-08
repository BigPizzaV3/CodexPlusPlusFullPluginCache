---
name: highlights-review
description: Gather and organize the passages the user highlighted in Saive. Use when the user asks what they highlighted or underlined, wants to review highlights on a topic, or wants study notes or a digest built from their highlights.
---

# Review the user's highlights

## Steps

1. Call `list_highlights`. Pass `query` to search the highlight text for a
   topic, and `tags` or `folder` when the user names them.
2. For a time range, pass `since`. It filters by when the page was saved, not
   when the user highlighted it, so say that in your answer.
3. Follow the cursor until you have every result or 100 highlights.
4. Group the highlights by the save they came from.

## Output

For each save: its title linked to its URL, then each highlight as a quote,
followed by the user's annotation when there is one.

When the user asks for study notes or a digest, add your synthesis after the
quotes under its own heading. Keep your words apart from theirs.

## Boundaries

- Quote highlights word for word. Never edit, merge, or paraphrase them inside
  the quotes.
- `query` matches the words inside each highlight, so highlights on a topic
  often miss it. When `list_highlights` returns nothing for a topic, call
  `search_saves` on the topic, then `get_save` on the top hits: each record
  carries every highlight on that save. Say nothing matched only when that
  finds none either.
