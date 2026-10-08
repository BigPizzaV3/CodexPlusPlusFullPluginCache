---
name: schedule-social-posts
description: Use when publishing or scheduling a post to TikTok, Instagram, Facebook, YouTube or X through ViewPrinter, uploading media for one, editing or cancelling a queued post, or reading how published posts and connected accounts are performing. Covers the order the tools must be called in, the two-step media upload, and what to do when a tool refuses. Do not use for writing copy with no intent to post, or for platforms ViewPrinter does not connect to.
---

# Scheduling social posts with ViewPrinter

ViewPrinter queues posts to social accounts someone has connected. The tools
are ordered: several of them fail or do the wrong thing if called out of turn,
and one of them is not safe to retry. This is that order.

## Read the rules before composing

Call `platforms_list` before writing a caption or picking media. It returns
each platform's caption limit, the media kinds and counts it accepts, and its
per-platform options. Reading it costs one call; discovering the same rules by
being rejected costs the whole post.

A caption that fits X will be cut on Instagram. Check, do not assume.

## The order

1. `accounts_list` — get the account ids and see which workspace each is in.
2. `media_upload` → PUT the bytes → `media_confirm` — only if there is media.
3. `posts_schedule` — create the post and queue delivery.

`accounts_connect` comes before all of it if nothing is connected yet. It
returns a URL the person opens in their own browser; the sign-in happens on the
platform and cannot happen here. Call it again afterwards and it reports the
account that got connected.

**Every account on one post must be in the same workspace.** Mixing workspaces
is refused.

## Media is two steps, and the bytes never pass through you

`media_upload` reserves an id and returns a short-lived URL to PUT the file to.
The bytes go straight to storage — not through the tool, not through the
conversation. Then call `media_confirm` with the same id. **Nothing is recorded
until `media_confirm` succeeds**, so a file that was PUT but never confirmed
does not exist as far as scheduling is concerned.

`media_confirm` is safe to call again if the first response was lost; it reads
the size and type back from storage rather than taking them on trust.

A post is **either a video or a set of images, never both**.

## Scheduling

- Omit `scheduled_at` to send as soon as possible; pass it to queue for later.
- Pass `draft: true` to hold the post without sending anything. `posts_update`
  with `draft: false` is what later sends it — there is no separate publish
  tool.
- Name accounts by id from `accounts_list`, or name a group from `groups_list`,
  or both. A group is expanded **at schedule time**: it is shorthand for the
  accounts in it right now, not a live link, so adding a member to the group
  later does not add it to this post.

**`posts_schedule` is not idempotent.** There is no deduplication: the same
arguments twice queue the same caption to the same accounts twice. If a
response is lost and you need to retry, reuse the same `idempotency_key` — that
returns the original post instead of making a second one.

**Do not tell anyone their post is saved or scheduled until the tool has
returned successfully.** A queued post is a real thing that will appear in
public; saying it exists before it does is the one error here that cannot be
taken back with words.

## Changing or stopping a post

`posts_update` works only while every destination is still pending. Once any
destination has started publishing the post can no longer be edited — schedule
a new one instead. Changing the destination list replaces it rather than adding
to it.

`posts_cancel` stops destinations that have not started. Anything already
publishing cannot be recalled and comes back in `still_going` — report those
honestly as already gone rather than as cancelled.

## Reading performance

`accounts_performance` and `posts_performance` return figures collected by a
background sweep, not fetched live. Every row carries the time it was measured.

A delivery nobody has measured yet has **no metrics at all rather than zeroes**,
and sorts last. Do not report an unmeasured post as having zero views — say it
has not been measured yet.

## When a tool refuses

Relay the refusal as written and stop. The tools return plain sentences meant
to be read back to the person.

If a tool reports that publishing is not enabled on the account, say exactly
that. **Do not offer to sell anything, do not describe plans or prices, and do
not go looking for a signup or upgrade link.** Connecting accounts, uploading
media and every read stay available regardless, so keep working on the parts
that do function.
