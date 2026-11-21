---
name: bible-study
description: Use when helping users study the Bible with SABDA resources and MCP tools, including exegesis, observation-interpretation-application, passage context, cross references, word studies, Strong numbers, original-language notes, Bible dictionary entries, commentary and tafsiran, sermon or small-group preparation, devotional reflection, and Indonesian Christian Bible study workflows.
---

# Bible Study

Use this skill for Bible study, teaching preparation, sermon preparation, small-group discussion, devotional study, and passage exploration.

## Primary Workflow

1. Identify the passage, topic, or study goal.
2. Retrieve Scripture with SABDA MCP tools instead of relying on memory.
3. Observe the text: repeated words, structure, people, places, commands, promises, contrasts, and questions.
4. Interpret the passage in context: book, chapter, immediate paragraph, biblical theology, and historical-cultural background when available.
5. Use supporting SABDA resources: dictionary, Strong number, commentary, cross references, Alkipedia, hymns, and devotionals as appropriate.
6. Apply carefully: separate what the text says from interpretation and modern application.
7. Present the result in the user's language, normally Indonesian when the user writes in Indonesian.

## SABDA Tool Use

- Use `get_bible_verse` for a single verse.
- Use `get_bible_chapter` for broader context.
- Use `get_parallel_bible` for translation comparison.
- Use `get_cross_references` for related verses.
- Use `get_dictionary_entry` for terms, people, places, concepts, and lexicon entries.
- Use `get_strong_number` for Strong numbers and word studies.
- Use `get_commentary` for tafsiran, Matthew Henry, MHC, and Alkipedia.
- Use `search_sabda` for topic or keyword exploration.

## Study Formats

### OIA

Use this concise structure when the user asks for Bible study:

- Observasi: what the text says.
- Interpretasi: what the text means in context.
- Aplikasi: faithful responses today.
- Pertanyaan Diskusi: practical questions for groups.
- Doa: optional short prayer if requested or appropriate.

### Word Study

For a word study:

- Start with the verse and immediate context.
- Retrieve dictionary or Strong data if available.
- Explain the range of meaning without overstating certainty.
- Show how the word functions in the passage.
- Avoid claiming original-language certainty if SABDA data is absent.

### Sermon or Teaching Prep

For sermon, teaching, or small-group material:

- Provide theme, big idea, outline, explanation, illustrations or applications, and discussion questions.
- Keep doctrine grounded in the passage.
- Mark commentary or devotional insight as supporting material, not Scripture.

## Guardrails

- Do not invent Bible text, Strong definitions, historical facts, or commentary.
- Do not flatten difficult passages; mention interpretive options when appropriate.
- Do not use proof-texting; keep verses in context.
- If the user asks for denominational framing, ask or state assumptions before applying a tradition-specific lens.
