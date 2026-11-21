---
name: word-counter
description: Exact word, character, sentence, and reading-time counts with count_text, and essay word targets plus X, Threads, Bluesky, LinkedIn, Instagram, SEO title, meta description, and SMS limits with check_length_limits.
---

# Zovo Word Counter

Language models miscount words and characters because they see tokens, not words. Use these tools whenever the user needs a number they will rely on.

1. Pass the user's text verbatim in `text`. Never summarise, correct, or retype it first. If the user has not pasted the text yet, ask for it once.
2. `count_text`: words, characters with and without spaces, sentences, paragraphs, unique words, reading time (238 wpm), speaking time (150 wpm), English readability, keywords, and long sentences. For essays, set `exclude_citations`, `exclude_quotes`, `exclude_headings`, or `exclude_reference_list` when the user says the limit excludes them ("without citations", "excluding references").
3. `check_length_limits`: pass `min_words` / `max_words` for essay limits, `max_characters` for a custom limit, and `platforms` (`x`, `threads`, `bluesky`, `linkedin`, `instagram`, `meta_title`, `meta_description`, `sms`) for posts, titles, and texts. X uses weighted counting: links count 23, emoji and CJK characters count 2.
4. For Japanese, Chinese, or Thai text, pass `language` (for example `ja`); Chinese and Japanese limits are usually in characters, which the result also reports.
5. Report the numbers from the result. Do not paste the full text back. When something is over a limit, quote the "cut after" point; only rewrite or shorten if the user asks.

Do not use these tools for rewriting, translating, defining words, or counting things other than text (calories, items, the size of the English language).
