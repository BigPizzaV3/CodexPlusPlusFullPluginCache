---
name: audiobooks
description: Find and play audiobooks on Spinn Radio, from public-domain classics to Spinn originals, the Bible and the Quran. Use when the user asks to listen to a book, an audiobook, a classic novel, or scripture ("play Pride and Prejudice", "read me Sherlock Holmes", "play Psalms").
---

Use this skill for audiobooks.

1. Call `search_audiobooks` with the title or author in `query`. If several versions come back, prefer the one whose title matches best, then the one with more chapters.
2. Call `play_audiobook` with the `book_id`, and `chapter` when the user asks for a particular one (default 1).
3. After the player opens, say in one sentence what is playing. Playback starts when the user taps play, and the next chapters follow on.
4. Only the first chapters of most books play in the chat (scripture plays in full). If the user asks for a later chapter, `play_audiobook` says so: pass on that the rest of the book is on spinnradio.com, with its link. Don't mention prices, plans or subscriptions.

Only use books and ids returned by Spinn tools. Don't recite or summarise a book's text.
