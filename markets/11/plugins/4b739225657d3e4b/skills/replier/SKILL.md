---
name: replier
description: Use Replier to create Instagram or Facebook post, story-reply and DM automations, including Follow Gate, opening message and email request gates, catch up on missed replies, read contacts, and inspect workspace, account or automation performance. Trigger for Replier, social post or story automation, comment or reply keywords, DMs, links, follower verification, collected emails, or Replier analytics.
---

# Replier

Use the Replier MCP tools for post or Instagram story automation, missed replies, contacts and performance questions.

## Workspace boundary

Call `list_workspaces` before using workspace-scoped tools unless a workspace ID was returned earlier in the same conversation.

When only one workspace is returned, use it. When multiple workspaces are returned and the user has not identified one, show the names and ask which workspace to use.

Use account, post, automation, and target IDs only with the workspace that returned them. Never infer that matching account names belong to the same workspace.

## Create an automation

Call `list_connected_accounts`. Use `list_posts` when the user needs a specific post, or `list_instagram_stories` when they need a specific active Instagram story.

Collect the automation name, one or more targets, keywords or any-interaction intent, public replies for post comments, DM message, up to three optional link buttons, optional gates and Follow Gate settings, and whether it should start enabled.

Use these target types:

- `post`: One post ID returned by `list_posts`.
- `next_post`: The next new post after activation; use a null `post_id`. Up to 10 automations can wait on one account, and each new post goes to the first one in line, paused or not, so a second `next_post` automation uses the post after next. `queue_position` in the output shows which upcoming post it will use; `list_next_post_queue` and `reorder_next_post_queue` read and change the order.
- `all_future_posts`: Every post published after activation; use a null `post_id`.
- `story`: One ID returned by `list_instagram_stories`; copy its timestamp to `published_at` when available.
- `next_story`: The first Instagram story published after activation; use a null `post_id`.
- `story_replies`: Every Instagram story; use a null `post_id`.
- `message`: Incoming DMs on the account; use a null `post_id`.

Prefer the `targets` array for new calls. It accepts up to 24 targets. Story target types are Instagram-only.

An empty keyword list means any eligible non-owner comment, story reply or message triggers the automation. A non-empty list means the interaction must contain a keyword. Story replies and messages are private, so those targets do not use the public reply.

### Keyword variants

A comment matches when its text contains a keyword, ignoring letter case, including inside longer words. People misspell and type the same word in different ways, so before saving, generate the variants yourself, as the Replier editor's keyword suggestions do:

- spacing and hyphen variants where a word joins two parts (bitplay → bit play, bit-play)
- common typos, keyboard slips and autocorrect misspellings (price → prcie)
- the whole word in the other Chinese script, as a Traditional or Simplified keyboard types it (連結 → 连结, never 連结 or 连結)
- full-width or half-width forms (ＧＵＩＤＥ, guide)

Only add spellings of the same word: no other words, word forms, synonyms, translations or romanizations. Never mix Traditional and Simplified characters in one variant, and never add spaces or punctuation inside Chinese or Japanese words. Leave out a variant that contains one of the keywords, since the keyword already matches it, and one that would also match comments meaning something else (lik is inside like, proce inside process, prise inside surprise). Keep at most 12 variants, most likely first. Show the final keyword list in the summary so the user can drop any.

### Gates

Runs go trigger, public reply, opening message, Follow Gate, email request, then the DM. Each gate is optional:

- `gates.opening`: the recipient must tap `button_text` before anything else is sent.
- `gates.email`: the recipient must reply with an email address. `retry_message` is sent when the reply is not an email. Replier checks the format only, and saves the address to contacts.
- Follow Gate is available when at least one target is on Instagram, including mixed Instagram/Facebook automations. Replier verifies Instagram follows before releasing the saved DM and links; Facebook targets send the saved DM and links without follow verification.

Text you leave out comes from the workspace's saved defaults (`get_message_defaults`). Without a saved default, ask the user for the gate text. On update, pass `null` to turn a gate off; a gate left out stays as it is.

Before calling `create_automation`, summarize the workspace, all targets, trigger keywords, public replies, gates, Follow Gate state, DM, and buttons so the user can verify the write. After creation, report the returned automation ID and workspace name.

## Saved defaults

`get_message_defaults` returns the workspace's saved opening message, email request, Follow Gate and public reply text. `update_message_defaults` replaces the sections you pass, as Save as default does in the editor; existing automations keep their own text.

## Catch up on missed replies

`list_catch_up` lists comments, story replies and messages that match an active automation but never got its reply, soonest to expire first. Meta accepts a reply within 7 days of a comment and 24 hours of a message or story reply. Show the items, including when each expires, and get explicit confirmation. Then call `send_catch_up` with `confirmed: true`, the confirmed items unchanged, and a new `idempotency_key`. Replies count toward the interaction allowance. Queued is not delivered: check `list_automation_activity`.

## Contacts

`list_contacts` lists people who interacted with the workspace's automations, with the email they gave an email request. Emails are personal data: share them only with the user who asked.

## Read performance

Use `get_workspace_performance` for the dashboard's numbers across the workspace, or one account with `channel` and `account_id`, including hourly activity and click locations. Use `get_account_performance` for one connected Instagram account or Facebook Page, and `get_automation_performance` for one automation. Use `list_automations` when the user asks to compare or discover automations.

When the user compares with the Replier dashboard, quote `interaction_metrics`: interactions, people reached, link click rate and completion rate, with the previous period. The dashboard's DMs sent is `messages_sent`, which counts every message of a flow; `performance.dms_sent` counts runs whose main DM was sent, and `performance` breaks those runs down by delivery outcome. Pass the user's IANA time zone, such as `Asia/Taipei`, for hourly activity.

State the reporting period. Distinguish recent period metrics from lifetime match and sent totals. Treat zero-volume click-through rates as zero, not as evidence of poor performance.
