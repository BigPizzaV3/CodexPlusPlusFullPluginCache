---
name: linkedin-outreach
description: Use when the user wants a LinkedIn outreach tool to prepare outreach, send approved LinkedIn messages, InMails, or connection requests, schedule paced outreach batches, check delivery results, or publish or schedule approved LinkedIn posts. Sending and scheduling require approval of the recipients and exact text. Outreach jobs cannot be canceled, paused, or resumed; scheduled posts can be canceled before they go out.
---

# LinkedIn outreach

Read [account access and limits](../../references/account-and-limits.md) before using tools.

## Prepare approved actions

Call `account_status` with the LinkedIn `account` (or `provider: "linkedin"` when only one LinkedIn account is connected). Every tool below takes the same optional `account`: act from the account the user chose, or the one the conversation came from. Resolve recipients to returned `person_id` or `chat_id` values. Show every recipient and the exact message or invitation note before sending or scheduling. Respect existing approval for that exact content and recipient list. If either changes, obtain approval for the changed action.

For an existing conversation, use `send_message` with `chat_id` and `text`. To contact a person, use `start_chat` with the `person_id` as `to` and `text`. New ordinary conversations require a first-degree connection. Set `inmail: true` only when the user requests InMail and the returned account and recipient information support it, since InMail needs Premium credits. Include the approved `subject` if needed.

Use `linkedin_send_invitation` with `person_id` and an optional `note`. Before inviting, or after an uncertain invitation result, check pending requests with `linkedin_list_invitations` (`direction: "sent"`) so nobody is invited twice. `direction: "received"` lists requests waiting for the user's answer. Free accounts, including accounts with unknown Premium status, allow notes up to 200 characters and about 15 notes a week. Confirmed Premium accounts allow up to 300 characters. Check daily, weekly, and note allowances from the server.

## Schedule a batch

Use `linkedin_schedule_outreach` for several approved messages or invitations. Explain before approval that the queue runs after the call and this plugin has no cancel, pause, or resume tool.

A batch runs from one LinkedIn account. With several, pass `account`: the server refuses items with a `chat_id` when the account is ambiguous, because a chat belongs to one account. Send 1 to 50 `items`. Each item contains `kind` and `text`. A message needs an existing `chat_id` or a `person_id` for a new ordinary conversation. An invitation needs `person_id`. Message text in a batch is limited to 3000 characters. Invitation text must satisfy the account's note limit. The batch tool does not support InMail subjects or publishing posts.

Use `min_gap_seconds` between 60 and 3600, with the server default of 120 unless the user chooses another supported gap. Actual timing also depends on randomized pacing, quotas, and cooldowns. A returned estimate is not a delivery guarantee.

Record the returned `job_id`. Use `linkedin_get_job` to report `done`, `failed`, `total`, and per-item `results`, matched by item index `i`. Scheduling is not delivery. A `status` of `done` can include failures or unattempted items. Claim complete delivery only when all approved items have successful results.

If the account disconnects, follow its reconnect guidance. After reconnecting, verify status and get the job's latest results. Only propose a new batch for failed or unattempted items, and obtain approval before rescheduling them. Do not resend successful items.

## Publish or schedule a post

Use `create_post` with the LinkedIn `account`, following [Social publishing](../social-publishing/SKILL.md). On LinkedIn the `text` is limited to 3000 characters, with at most one image (`image_urls` or `media_ids` from `upload_media`). A `link` is appended to the text and previewed when there is no image. `visibility` is `anyone` (the default) or `relations_only` (connections). Show the exact text, any link, any image, and the visibility before publishing, and publish only after approval of that content and audience. Add `publish_at` to schedule it instead. This plugin cannot edit or delete a published LinkedIn post. Report success and a post URL only when the tool returns them.
