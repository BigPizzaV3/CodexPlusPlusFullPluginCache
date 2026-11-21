---
name: read-the-inbox
description: Look through the articles already saved in the user's Folio inbox — find one, summarise it, tidy the queue, or bundle a few into an issue and send them to a device.
---

Use this when the question is about reading the user already saved: "what's in my inbox?", "put this article on my Kindle", "did I save anything about heat pumps?", "clear out the stuff I'll never read".

- `list_articles` lists saved items. `status` is `inbox` for unread, `library` for archived, `failed` for what Folio could not fetch, `trashed` for deleted. It returns titles, sources and word counts, not the text.
- `get_article` returns one article's full text. Call it before summarising or quoting; never answer from the title alone.
- `search` finds saved articles by title or URL when the user half-remembers one.

To put saved articles on a device, bundle them rather than sending each on its own:

1. Pick the articles with the user, by title. Confirm the list if it is more than two or three.
2. Call `create_issue` with those `article_ids` and a short `title`. Rendering runs in the background; the articles move from the inbox to the library as part of this.
3. Call `list_targets`, then `send_file` with the returned `issue_id` and the target. Do not re-render an issue that already exists, and do not call `create_upload` — that is for files you generated yourself.

To tidy up, use `update_article`: `archive` moves a read item to the library, `trash` discards it, `restore` pulls one back, `set_category` files it. Act on one article at a time and say what you did in plain words.

Refer to articles by their title and devices by their label. Do not show ids, JSON or raw URLs unless the user asks.
