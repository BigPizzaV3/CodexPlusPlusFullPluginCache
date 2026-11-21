---
name: learn-first
description: Answer what to learn first in Chinese. Use when the user asks which characters, words, sentence patterns or grammar to learn first, what is the most efficient way to start, what to learn at a given HSK level, or how many characters they need.
---

Answer with data, not guesses, then turn the answer into a conversation.

- Characters and how many: call `get_common_characters`. Give the coverage figures (how few characters cover half of real text, then 80%, 90%, 95%), then the top ten. Say the counts come from graded readings, so they describe learner-level text, not all of Chinese.
- Words to start with at a level: call `get_study_order` with the level (1 to 5) and present the first lessons in order.
- Sentence patterns: call `get_grammar_order` with the level (1 to 6), then `get_grammar_point` for any the user wants explained, including what to learn before it.
- Words for a situation: call `get_topic_words`, with no topic first to list the options.

Present at most ten items at a time with pinyin and meaning. Prefer the words that let the learner ask questions, such as 什么, 谁, 哪, 为什么, 吗, 呢, because those unlock the rest by conversation. Finish by offering to start a short conversation using only what you just listed, and ask which topic they want.

Do not invent frequencies, levels or orderings from memory. If a tool returns nothing for a level, say so.
