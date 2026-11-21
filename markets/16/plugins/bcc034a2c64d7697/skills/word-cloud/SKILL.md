---
name: word-cloud
description: Draw a word cloud from text or from words with weights with make_word_cloud (SVG, PDF and CSV downloads, interactive view), and count word frequency in a text with count_words (CSV of all counted words).
---

# Zovo Word Cloud

Use `make_word_cloud` when the user wants a word cloud, word art or tag cloud.

1. Pass the user's text in `text` (up to 100,000 characters), or pass `words` as `[{"word":"growth","weight":12}]` when the user gives words with numbers. Give one of the two, not both. Turn "growth 12, pricing 7" into words with weights.
2. Options only when the user asks: `max_words` (10 to 200, default 100), `stop_words` (en default, es, fr, de, it, pt or none), `exclude_words`, `case` (fold or as_written), `min_length`, `include_numbers`, `shape` (rectangle or circle), `orientation` (horizontal or mixed), `palette` (classic, ocean, forest, sunset, mono), `min_font_size`, `max_font_size`, `seed`, `page_size` (letter or a4), `title`.
3. If the text is not English, set `stop_words` to its language when it is one of es, fr, de, it, pt; else use none.
4. After the tool returns, give the top words with counts, the rules line, any notes word for word (left-out words, skipped text), the layout and PDF checks, and the SVG, PDF and CSV links.

Use `count_words` when the user wants word counts or a frequency table without a picture. It uses the same word rules and returns the top words with percents and a CSV of all counted words.

Do not use this skill for reading text from images or files, sentiment scores, summaries, or charts of numbers.
