---
name: feeder-topic-monitor
description: Set up or run ongoing monitoring of a topic in Feeder; use when the user wants to follow a subject, company, or keyword over time, or asks what happened lately on a monitored topic.
metadata:
  short-description: Follow a topic across sources over time
---

# Topic Monitor

Build a durable monitoring setup for a topic in the user's Feeder account, or run a check against one that already exists.

## Tool-call guardrails

- Feeder tools require a connected Feeder account on a Plus plan or higher. If a tool call returns an upgrade message, relay it briefly and stop; do not retry.
- Adding feeds changes the user's account. Confirm the list of sources with the user before calling `Feeder:add_feed`.
- Prefer existing subscriptions: search the user's own feeds before proposing new sources.

## Workflow

### 1) Understand the topic
Clarify the topic if vague ("AI" is too broad; "EU AI regulation" is workable). Identify 2 to 5 search phrasings including synonyms and key entities.

### 2) Check what already exists
1. Call `Feeder:search_posts` with each phrasing to see how well the user's current subscriptions already cover the topic.
2. Call `Feeder:list_folders` to see whether a folder for this topic already exists.
3. If coverage and structure exist, skip to step 4.

### 3) Build the setup (with consent)
1. Find candidate sources with `Feeder:search_feeds` (site names, RSS URLs, topic keywords).
2. Show the user the candidates and let them pick.
3. Create a folder for the topic with `Feeder:create_folder` (a plain name like "EU AI Act").
4. Subscribe with `Feeder:add_feed`, then file each feed with `Feeder:add_feed_to_folder`.

### 4) Run a check
1. Pull recent posts for the topic: `Feeder:get_posts` scoped to the topic folder, plus `Feeder:search_posts` with the phrasings from step 1 to catch mentions outside the folder.
2. Summarize developments in chronological order: what happened, which source reported it, what changed since the last check.
3. Flag disagreements between sources explicitly; provenance is the point of monitoring.

### 5) Keep the trail
Offer to save key posts into a collection named after the topic (`Feeder:list_collections`, then `Feeder:add_to_collection`), so the next check can build on a curated record.
