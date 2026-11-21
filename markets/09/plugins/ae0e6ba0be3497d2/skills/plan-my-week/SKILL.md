---
name: plan-my-week
description: Plan a week of social posts for the user's brand and put the ones they approve on the calendar. Use when the user asks to plan their week, fill their posting calendar, make a batch of posts for the next few days, or says yes to planning a week of posts.
---

# Plan my week

Use this skill to turn "plan my week" into five drafted posts the user reviews, changes and approves. Nothing is
posted without the user's yes. Explicit instructions from the user always take priority over this skill, including
the channels, days, times, number of posts and captions they name.

## Before you start
1. Call `get_brand`. If no brand is saved, ask for the website and set one up with `draft_brand` first.
2. Call `list_connectors`. If none of the channels the user wants is connected, say which one is needed and that it
   is connected in the Hermoso app under Connectors, in the sidebar. Never ask for a password or token in the
   chat. Planning still works without a connected channel; scheduling does not.

## Steps
1. Call `plan_week` without `confirm`, with the user's `timezone` if they gave one. It returns the price and whether
   the batch fits the account's posting allowance, and spends nothing. Tell the user the price in one line and ask
   whether to go ahead.
2. If they say yes, call `plan_week` with `confirm` set to true. If they say no, call it with `decline` set to true
   and stop.
3. Call `get_job` with the id it returned until the batch is done. It takes a few minutes; keep polling without
   asking the user to wait.
4. Show each draft: its picture, the caption, the channels and the suggested day and time. Number them 1 to 5.
5. Apply what the user asks to change with `run_post_refill` and `edit` (a new caption, a new time in `at`, other
   channels), or remove a draft with `discard`. Show the changed draft again.
6. When the user approves, call `run_post_refill` with `approve` set to the approved draft ids, or to all of them if
   they approve the whole week.
7. Call `list_scheduled` and report what is now queued, per post and per channel, from what it returns.

## Output
A numbered list of the week's posts with day, time, channels and caption, then a one-line note of what is
scheduled and what is still a draft. On TikTok, say that the posts land as drafts in the creator's TikTok inbox to
finish there.

## Do not
- Do not schedule a draft the user did not approve.
- Do not rewrite an approved caption. If a caption is too long for a channel, say so and ask how to shorten it.
- Do not say a post went out until `list_scheduled` shows it fired on that channel.
