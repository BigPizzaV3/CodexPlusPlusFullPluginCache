---
name: publora-publishing
description: >
  Publish or schedule a post to connected social accounts through Publora —
  LinkedIn, X, Instagram, Threads, TikTok, YouTube, Facebook, Bluesky,
  Mastodon, Telegram. Use for drafting, scheduling, editing the queue and
  checking what is already queued. Not for analytics; Publora does not
  expose metrics here.
---

# Publishing with Publora

One post, several networks, one set of rules. This skill covers the whole
publishing path: read what is connected, respect each network's limits, save a
draft or schedule, then confirm what actually happened.

Publishing is public and effectively irreversible. Show the user the exact text
and the exact accounts before anything goes out, and never publish on a guess.

## Always start with the connections

```
list_connections
```

Copy each target's `platformId` **verbatim** into the next call. Never invent,
shorten or guess an id — a wrong id is the most common reason a post silently
goes nowhere. If the network the user asked for is not in the list, say so and
stop: connecting an account is done by the user in the Publora dashboard, not
by a tool.

Pinterest can be connected but cannot be published to.

## Draft, schedule or publish

`create_post` does all three, and the difference is one field:

| Intent | Call |
|---|---|
| Draft, to finish later | `create_post` **without** `scheduledTime` |
| Scheduled | `create_post` with `scheduledTime` |
| Right now | `create_post` with a `scheduledTime` a few minutes ahead |

Times are ISO 8601 in UTC, for example `2026-08-12T09:00:00Z`. When the user
says "tomorrow at 9", convert from their timezone and state the conversion back
to them. Read the `scheduledTime` in the response rather than repeating the
requested one: the server may adjust it and explain why in `warnings`.

Default to a draft when the request is ambiguous. A draft that needed to be a
post costs one click; a post that needed to be a draft cannot be recalled.

## Per-network limits

Publora validates these, but knowing them avoids a failed call:

| Network | Caption limit | Media |
|---|---|---|
| X | 280 | optional |
| Threads, Mastodon | 500 | optional |
| Instagram, TikTok | 2200 | **required** |
| YouTube | 5000 | **required** |
| LinkedIn | 3000 | optional |
| Facebook, Bluesky, Telegram | generous | optional |

When one post targets several networks, the strictest limit wins. If the text
is too long for one of them, offer to shorten it or to drop that network —
do not silently truncate.

Instagram, TikTok and YouTube reject a text-only post. Attach media or leave
them out; see the `publora-media` skill for how.

Network-specific options — YouTube title and tags, TikTok privacy, Instagram
cover, Telegram flags, Threads reply control, LinkedIn scheduled repost — go in
`platformSettings`, never inside the caption.

## After the call

`create_post` returns a `postGroupId`. Give it to the user together with the
stored time and the resolved account names. That id is how anything is changed
later.

- `list_posts` — what is queued, filtered by status, network or date range.
- `get_post` — one post group in full, including per-network state.
- `update_post` — edit content, targets, status, time or settings in place.
  It overwrites, so state what will change before calling it. Removing a
  network from the target list drops that network's post.
- `delete_post` — permanent, for one post group at a time. Ask first, and
  never run it across a list because the user said "clear my queue".

## Retries

Every write accepts an `idempotencyKey`. Reuse the same key when retrying the
same post so a network hiccup cannot produce two identical posts. Change the
key only when the content changes.

## Test without publishing

`publora-playground` is a reserved target: a post sent there is acknowledged
and discarded, and nothing reaches a real account. Use it to prove the
connection works before touching a live account — especially on a first run.
It must be the only entry in `platforms` when used.

## Never

- Publish or delete without the user seeing the exact text and targets.
- Invent a `platformId`, an account, or a time the user did not confirm.
- Answer "which accounts do I have" from memory. Call `list_connections`.
- Present a draft as published, or a scheduled post as already live.
