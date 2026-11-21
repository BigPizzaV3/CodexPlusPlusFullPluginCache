---
name: mymemory
description: Use when the user wants to search, recall, summarize, save, organize or remove their own saved notes, bookmarks, X (Twitter) bookmarks, Instagram or Reddit saved posts, web pages, YouTube videos, podcasts, PDFs, Notion pages or documents, for example "what did I save about X", "find my notes on Y", "remember this", or "add this to my memory" in their MyMemory account.
---

# MyMemory

MyMemory is the user's personal knowledge base (second brain). Use the tools only for the user's own saved material.

- To answer a question from saved material ("what did I save about...", "find my notes on..."), call `search_memories` (or `ask_memories` for a written answer with sources), then `get_memory_by_id` if you need the full text. Say where the answer came from.
- To save something the user asks you to keep ("remember this", "save this note or link"), call `save_memory`.
- To organize, use the space, tag and reminder tools.
- Before deleting, call the delete tool without `confirm` to preview, show the user what would be removed, and call it again with `confirm: true` only after they agree.
- If the question is not about the user's saved material (weather, news, general knowledge), do not call the tools.
