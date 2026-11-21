---
name: feeder-research-collection
description: Research a question across the user's Feeder posts and build a cited collection; use when the user wants sourced research, a literature pass over their feeds, or a curated set of posts on a question.
metadata:
  short-description: Research your feeds and save a cited collection
---

# Research Collection

Answer a research question from the user's own subscriptions, with every claim traceable to a post, and leave behind a curated collection.

## Tool-call guardrails

- Feeder tools require a connected Feeder account on a Plus plan or higher. If a tool call returns an upgrade message, relay it briefly and stop; do not retry.
- `Feeder:expand_post` fetches full content for one post. Use it selectively on the posts that will carry the answer, not on every search hit.
- Cite by post title and source feed. Do not invent posts or attribute claims to posts you did not read.

## Workflow

### 1) Frame the question
Restate the research question and agree on scope with the user: time window, which feeds or folders count, and what the output should be (short answer, comparison, timeline).

### 2) Sweep
1. Run `Feeder:search_posts` with 3 to 6 phrasings: synonyms, key entities, and opposing terms. Scope to specific feeds or folders when the user named them.
2. Collect candidate posts and dedupe. Note which searches came up empty; that is a finding too.

### 3) Read
1. Rank candidates by relevance and recency.
2. Call `Feeder:expand_post` on the top posts (typically 5 to 10) to get full content.
3. Extract facts, numbers, dates, and quotes with their source post.

### 4) Synthesize
- Answer the question first, in a few sentences.
- Support with the evidence: one bullet per key fact, each ending with its source (post title, feed).
- State conflicts between sources plainly, and say what is unknown or not covered by the user's feeds.

### 5) Save the trail
1. Ask whether to save the curated set. List existing collections with `Feeder:list_collections`.
2. Save the load-bearing posts with `Feeder:add_to_collection` into the collection the user picks.
3. Close by telling the user what was saved and where.
