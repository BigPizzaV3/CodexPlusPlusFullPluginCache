---
name: sabda-bible
description: Use when answering Indonesian or English Bible-related requests with SABDA resources through the SABDA MCP tools, including Bible verses and chapters, passage lookup, Bible search, dictionary and lexicon entries, Strong numbers, commentary and tafsiran, cross references, hymns, devotionals, Christmas or Easter content, BADENO, AIPedia, and other SABDA media/library content.
---

# SABDA Bible

Use SABDA MCP tools as the primary source for Bible and SABDA ministry content.

## Tool Selection

- Use `get_bible_verse` for a single verse reference such as `Yohanes 3:16`.
- Use `get_bible_chapter` for a full chapter such as `Yohanes 3`.
- Use `search_sabda` for keyword, phrase, topic, or reference search.
- Use `get_dictionary_entry` for definitions, Bible dictionary, lexicon, and term lookups.
- Use `get_strong_number` for Strong numbers such as `H7225`, `G25`, `7225`, or `25`.
- Use `get_commentary` for tafsiran, commentary, Matthew Henry, MHC, and Alkipedia requests.
- Use `get_cross_references` for references connected to a Bible verse or passage.
- Use `get_parallel_bible` when the user asks for comparison or parallel Bible data.
- Use `get_hymn_or_song` for hymns and songbooks such as KJ, PKJ, NKB, KLIK, KPRI, and related commands.
- Use `get_devotional` for renungan, devotional, ROC, SH, and RH.
- Use `get_publication_content` for humor, doa, kesaksian, GSM, binaanak, and bahan.
- Use `get_christmas_content` for Natal resources.
- Use `get_easter_content` for Paskah resources.
- Use `get_media_library_content` for cerita, video, audio, quotes, paket, pustaka, BADENO, BADENOAI, and AIPedia.

## Response Guidelines

- Prefer concise Indonesian responses when the user writes in Indonesian.
- Include the Bible reference, translation/source name when available, and the retrieved content.
- Do not invent Bible text, commentary, dictionary definitions, Strong data, or SABDA resource results.
- If a tool returns no usable result, say that SABDA did not return matching data and suggest a clearer query.
- For Strong numbers with `H` or `G`, pass the original value to `get_strong_number`; the MCP normalizes it.
- For broad requests, ask one focused clarification only if needed; otherwise use `search_sabda` or the most relevant specialized tool.

## Safety and Scope

- Treat all SABDA MCP tools as read-only content retrieval unless the user explicitly asks about unavailable subscription actions.
- Do not use subscribe, unsubscribe, or account-changing commands.
- When presenting devotional, commentary, or study material, distinguish it from the Bible text itself.
