---
name: feeder-daily-brief
description: Brief the user on what is new across their Feeder feeds; use when they ask what's new, want a morning brief, or want to catch up on their subscriptions.
metadata:
  short-description: Catch up on your feeds with a structured brief
---

# Daily Brief

Turn the user's unread feeds into a short, structured brief they can act on.

## Tool-call guardrails

- Feeder tools require a connected Feeder account on a Plus plan or higher. If a tool call returns an upgrade message, relay it briefly and stop; do not retry.
- If a Feeder tool returns `Tool <name> not found`, treat Feeder as unavailable for this task and ask the user to connect the Feeder app, then retry.
- Post lists can be long. Work folder by folder rather than fetching everything at once.

## Workflow

### 1) Map the reading landscape
1. Call `Feeder:list_folders` and `Feeder:list_feeds` to see the user's structure and unread counts.
2. If the user asked about a specific area ("my crypto feeds"), narrow to the matching folder or feeds.

### 2) Gather what is new
1. For each folder or feed with unread posts, call `Feeder:get_posts` for the recent window (default: last 24 hours; use the user's requested window if given).
2. Prioritize by unread count and recency. Skip feeds with nothing new.
3. Only call `Feeder:expand_post` when a summary is too thin to describe a story the brief highlights.

### 3) Write the brief
- Lead with the 3 to 5 stories that matter most across all feeds, one line each with the source name.
- Then a short section per folder (or feed, if unfoldered): what changed, in 1 to 3 bullets.
- Note volume ("12 new posts in Design, mostly about X") instead of listing everything.
- End with anything time-sensitive spotted (deadlines, releases, breaking items).

### 4) Offer cleanup
- Ask before marking anything read. If the user agrees, use `Feeder:mark_folder_read` or `Feeder:mark_feed_read` for the sections they confirm. Use `Feeder:mark_all_read` only when the user explicitly asks for everything.
- If a story should be kept, offer to save it with `Feeder:add_to_collection` (list options with `Feeder:list_collections` first).
