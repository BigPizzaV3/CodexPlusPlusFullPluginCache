---
name: watchlist
description: "Add movies and shows to the beckett watchlist and books to the reading list, and log finished ones with a rating. Use when the user mentions something they want to watch or read, something they finished, or asks what to watch or read next."
---

# Watchlist and reading list

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- Add a clear title with `beckett_add_media`. Map "watchlist" to `want_to_watch` and "reading list" to `want_to_read`. Something they just finished is `watched` or `read`, with their rating if they gave one.
- For an ambiguous title, search `beckett_search_media_catalog` first. For titles they've already saved, use `beckett_search_media_library`.
- For suggestions, read what they've loved or rated highest with `beckett_search_media_library` sorted by rating, find candidates with `beckett_search_media_catalog`, and add the ones they ask for.
