---
name: comment-automations
description: Set up and monitor Instagram and Facebook Automations with the SocialAPI app. Comment-to-DM lead magnets ("comment LINK to get it"), follow-gated links, keyword auto-replies to comments and DMs, and FAQ answers, then check how each run went. Use when the user says "auto reply", "automation", "comment to DM", "send the link to everyone who comments", "keyword reply", "follow to unlock", "lead magnet", or wants replies to go out without them.
---

# Comment and DM Automations

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill's Automations section holds the full `create_automation` format: follow it for every call.

Automations work on Instagram and Facebook accounts only, up to 50 per account. On any other platform, say so and stop.

## 1. Goal

Get the trigger (a comment, or a DM), the keywords, what to send, which posts it covers, and whether each person gets it only once (`once_per_person`). Ask only for what is missing.

## 2. Account and posts

- `list_accounts` for the Instagram or Facebook account `id`.
- To limit it to some posts, `list_inbox_posts` for that account and use each post's `id` in `post_ids` (up to 100). Leave `post_ids` out to cover every post.

## 3. Build it

- Keyword filter: `{"type": "keyword", "keyword": {"keywords": [...], "match": "contains"}}`. It matches whole words and ignores case and accents.
- Comment trigger, `start` step: prefer `private_reply` (free) to send the link by DM. `reply_comment` costs 1 credit per run, `hide_comment` is free.
- DM trigger, `start` step: `send_dm`, 1 credit per run. It answers the same person at most 5 times an hour.
- Give 3 to 5 `texts` variants so replies do not all look identical. Up to 1000 characters each, or 640 when the step has buttons.
- Buttons: up to 3, titles up to 20 characters. A `postback` button leads to a later step, which may only send DMs. On Facebook, buttons on a `send_dm` step are not shown.
- "Follow to get the link" on Instagram: use `follow_gate` with `"steps": []`.

## 4. Confirm, then create

Show the Automation in plain words (when it fires, what it sends, what it costs per run) and the JSON. Call `create_automation` only after an explicit yes.

## 5. Test and monitor

- Ask the user to trigger it from another account (comment the keyword, or send the DM), then `list_automation_firings` to show each action's outcome and error code.
- `list_automations` shows fired, sent and failed counts. Pause with `update_automation` and `status: paused`, resume with `active`.
- Deleting an Automation also deletes its run history: confirm before `delete_automation`.
