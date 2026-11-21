---
name: competitor-watch
description: Track competitor and creator Instagram accounts with Hookest and report what changed for them in the last 7 days (new posts, follower changes). Use when the user wants to follow, track or watch a competitor or creator, asks what their competitors posted, or asks about their tracked accounts.
---

# Competitor watch with Hookest

Goal: keep a short, honest weekly picture of the accounts the user cares
about, and add new ones only with the user's say-so.

## Quota and consent

- `lookup_creator` and `search_creators` each spend one lookup from the user's
  daily quota. Search once and pick from the results instead of trying many
  terms. Call `get_account` if you are unsure how much is left.
- Tracking never starts on its own. Show the user what `lookup_creator`
  returned and call `track_creator` only after they confirm that exact account.
- `untrack_creator`, `set_creator_muted` and `set_creator_mail_prefs` change the
  user's settings. Call them only when the user asks for that change. Before
  `untrack_creator`, warn that tracking again starts from zero: earlier signals
  do not come back.

## What changed for my competitors

1. Call `get_creator_signals` without a creator to get every tracked account
   at once, or with a handle for one.
2. Report per account: new posts in the last 7 days and the follower change.
   Lead with the accounts that moved most. Link posts that are in the Hookest
   library to their Hookest page.
3. If nothing changed, say so in one line rather than padding the report.
4. After the user has read the report, offer to call `mark_signals_seen` with
   the `signal_ids` you showed (or `creator` for one account) so the same
   changes do not show up again. Call it only if they agree. Use `mark_all`
   only when they ask to clear everything.

## Track a new account

1. Have a handle or profile URL: call `lookup_creator`.
   No handle yet: call `search_creators` once with the brand or niche.
2. Show name, handle, followers and whether the account is verified.
3. After the user confirms, call `track_creator` with the returned id.
4. Call `list_tracked_creators` if slots may be full and tell the user how many
   are left. If tracking is not available with the user's plan, say so plainly.

## Be honest about the data

Signals cover the last 7 days and only accounts the user tracks. Hookest does
not report a competitor's ad spend, reach or engagement rate. Do not estimate
them.
