---
name: read-tooneru
description: Use when the user asks about manga works or episodes on トゥーンエル (toonERU, tooneru.com) — finding a work, reading or summarizing an episode, looking up a term in a work's glossary, or discussing what may happen next without spoilers.
---

# Read トゥーンエル works

トゥーンエル is a Japanese vertical-scroll manga media site. Its works are in Japanese. Use the トゥーンエル tools only for requests about its works, episodes and glossary terms.

1. Find the work with `search_works` (a keyword, a genre, or a job, money or procedure term from the request). Use the `id` from the result in later calls.
2. For a work's episodes, call `list_episodes`. For one episode, call `get_episode` (full text) or `get_context` (short summary of setting, characters, synopsis and terms).
3. For a term, call `get_glossary`. Say whether the entry is a rule of the story's world or a real-world fact, and show the source URL when there is one.
4. If the user says which episode they have read, pass it as `up_to_episode`, and do not reveal events from later episodes.
5. Cite the work title and the episode URL from the result.

Glossary entries are general explanations. They are not individual legal, tax or financial advice; for a personal case, suggest checking the cited source or a qualified professional.
