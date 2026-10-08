---
name: schedule-content-week
description: Plan and schedule a week of social posts with PostSyncer. Drafts per-platform variants from a brief, shows the full week for approval, then schedules to the user's connected accounts. Trigger on "plan my week", "batch my posts", "schedule content", "fill my calendar", or any request to draft and schedule social posts ahead of time. Do not use for replying to or moderating comments, for pulling analytics, or for publishing a single post right now.
---

# Schedule a week of content

Turn a rough brief into a reviewed, scheduled week of posts across the user's connected
social accounts.

Publishing is public and hard to undo. The approval step below is not optional.

## 1. Establish context before drafting

Call `list-workspaces`, then `list-accounts`. Never guess or invent a `workspace_id` or
account ID — every ID must come from a tool response in this conversation.

Stop and tell the user if:

- **No accounts are connected.** They need to connect one in PostSyncer first.
- **An account has `has_expired: true`.** Say which one. Posts scheduled to an expired
  account will fail at publish time. Offer to schedule to the remaining accounts instead.

If the user has more than one workspace, ask which to use rather than assuming the first.

## 2. Get the brief

You need enough to write with. Ask only for what is missing, in one message:

- What the week is about (topics, launches, themes)
- How many posts, across which of the connected accounts
- Any dates or times that matter

If they say "you decide", pick a sensible cadence — roughly one post per weekday per
account — and say what you chose so they can correct it.

## 3. Draft per-platform variants

Write each post for the platform it will appear on. Do not paste one block of text across
every network. See `references/platform-notes.md` for per-platform guidance.

Never fabricate a statistic, quote, customer name, or result. If the brief implies a claim
you cannot source, write around it or ask.

To attach images or video, use IDs from `list-media`, or `upload-media-from-url` for a URL
the user supplied. Do not attach media the user did not ask for.

## 4. Show the whole week and wait for approval

Present every post as a table: date, time, account(s), and the full text. Ask for explicit
approval to schedule.

**Do not call `create-post` until the user has approved.** "Go ahead", "schedule it", or
"yes" is approval. Silence, a follow-up question, or a general expression of enthusiasm is
not. If they approve only part of the plan, schedule only that part.

## 5. Schedule the approved posts

One `create-post` call per post:

- `workspace_id` — from `list-workspaces`.
- `schedule_type` — `"schedule"`. Use `"draft"` if the user wants to review in the app
  first. Only use `"publish_now"` if they explicitly ask to post immediately.
- `schedule_for` — `{ date: "Y-m-d", time: "H:i", timezone }`. Times are interpreted in the
  workspace timezone unless you pass one.
- `content` — an array of thread items, each `{ text, media? }`. A single post is a
  one-item array. For an X/Twitter thread, use one item per tweet.
- `accounts` — `[{ id }]` using IDs from `list-accounts`. Omit only if the user wants the
  workspace default account.
- `labels` / `campaign_id` — optional, from `list-labels` / `list-campaigns`, when the user
  is organizing a campaign.

To put a link or CTA in a first comment rather than the caption, set `is_first_comment: true`
on a **separate** thread item, and keep at least one item that is not a first comment.
This applies to Instagram, Facebook, LinkedIn and YouTube only — TikTok and Threads will not
get it, so anything those platforms need belongs in the main caption. Never use it for an
X/Twitter thread.

If a call fails, report which post failed and why. Do not silently retry with different
content, and do not continue scheduling the rest as if nothing happened.

## 6. Confirm what landed

Call `list-posts` and summarize what is now on the calendar: how many posts, the date range,
and the accounts. If anything from the approved plan is missing, say so plainly.

## Rules

- Approval before publishing, every time. Scheduling to a real account is a public act.
- Confirm before anything destructive. `delete-post` is irreversible and removes the post
  from the social platform, losing its likes, comments and reach. `update-post` overwrites a
  live post in place with no version history.
- Never invent IDs. Workspace, account, media, label and campaign IDs come from tool calls.
- Do not report a post as scheduled unless a `create-post` call returned successfully.
