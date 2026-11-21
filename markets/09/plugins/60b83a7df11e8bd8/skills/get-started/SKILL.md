---
name: get-started
description: How to use dots brain — a relationship-first second brain that keeps one record per person (nickname, how you met, closeness, groups, connections, and a dated history that stays up to date on its own).
---

# dots brain

Use dots brain when the user talks about a specific person in their life, wants to prepare for meeting someone, wants to find people they haven't talked to in a while, or tells you something that happened with someone.

## Reading

- Before answering about a person, call `search_brain` (the user may use a nickname like "Min" or a role like "my CEO"), then `get_person` for the full context, including their history (newest first) and `daysSinceLastContact`.
- For "who should I reach out to" or "who haven't I talked to", call `people_to_reconnect` once and explain why (days since last contact). Don't fetch every person one by one.
- Use `get_me` when the user's own profile matters (e.g. tone of a message they are writing).
- Groups can be nested (a team inside a company). `path` shows where a group sits, e.g. `["Kmong", "Enterprise team"]`.

## Keeping history up to date

- When the user tells you about something that **already happened** with someone — a meeting, a conversation, news about them, something new you learned — record it with `add_note` on your own, without waiting to be asked. Update their profile with `upsert_person` if details changed (new role, new company).
- Don't record plain questions or future plans ("I'm having lunch with Min tomorrow — what should I remember?") unless the user asks you to.
- Profile edits, group changes, and new relationships are added to the person's history **automatically** (entries of kind `change`). Don't add a separate note just to describe those edits.

## Writing safely

- Before creating a person, call `search_brain` to avoid duplicates. Then use `upsert_person` and `add_note`.
- `add_note` only appends. `upsert_person`, `upsert_me`, and `upsert_group` overwrite the fields you send — send only what the user actually said. Previous values stay visible in the person's history.
- For a team inside a company, pass `parent` to `upsert_group` (e.g. name "Enterprise team", parent "Kmong").
- `merge_people` cannot be undone. Only call it when the two records are clearly the same person **and** the user has confirmed. If the names look like different people, ask first.
- If a write call returns an error or is cancelled before it runs, assume nothing was saved: check with `get_person` or `search_brain` before telling the user, and don't silently retry a whole batch. Successful calls carry a `dots-brain/requestId` in `_meta` that matches the user's activity log.

## Boundaries

- Only the signed-in user's own brain is accessible. Never claim to read another user's data.
- Don't use these tools for unrelated requests (weather, general knowledge, etc.).
- Everything you read or write appears in the user's activity log in dots brain.
