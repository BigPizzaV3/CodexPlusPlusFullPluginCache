---
name: failed-post-troubleshooting
description: Find out why a social media post failed or only partly published with the SocialAPI app, explain it in plain words, fix the cause and retry the platforms that failed. Use when the user says "my post failed", "didn't publish", "post not showing on Instagram", "scheduled post didn't go out", "partial", "publishing error", "retry my post", "why did it fail", or shares an error code.
---

# Failed post troubleshooting

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill holds the error code table, platform support and `create_post` fields: follow it for every call.

## 1. Find the post

- The user named it or gave an id: `get_post` with that `post_id`.
- Otherwise: `list_posts` with `status: failed`, then `status: partial`, with `sort: created_desc`. Narrow with `platform`, `from`, `to` or `search`. A scheduled post that never went out also shows here.
- Several candidates: list them (date, platforms, start of the text) and ask which one.

## 2. Read what happened

`get_post` returns one entry per platform in `targets`, each with its `platform`, `account_id`, `status` and, when it failed, an `error` with `code`, `message` and `caused_by`.

- `partial` means some platforms published and others failed: name both.
- `caused_by: user` means the content or the account needs a change. `platform` means the platform refused or was unavailable. `system` means a problem on SocialAPI's side: retry once, and if it fails again, tell the user to contact contact@social-api.ai with the post id.
- For more detail, `list_events` with `resource_id` set to the post id and `category: post` shows what each platform answered.

## 3. Explain and fix

Explain each failed platform in one plain sentence, then the fix. The usual causes:

| Cause | Fix |
|---|---|
| `account.reconnection_required`, `platform.<name>.auth`, `platform.<name>.insufficient_scope`, or the account's `status` in `list_accounts` is not `active` | Reconnect with `connect_account`, then retry. |
| Instagram post without image or video, or no `platform_data.instagram.content_type` | Add media and a content type. |
| TikTok `privacy_level` refused | `get_creator_info`, then use one of the levels it lists. |
| Pinterest target without `board_id` | `list_pinterest_boards`, then set the board. |
| Media URL refused or not reachable | Ask for a public `https` link to the file. |
| `validation.*` | The `message` and `field` say what to change. Run `validate_post` on the corrected content. |
| `publishing.velocity_limit`, `platform.<name>.rate_limit`, `platform.<name>.throttled` | Too many posts in a short time. Wait `retry_after_seconds` when given, then retry. |
| `resource.not_supported` | The platform cannot do this. Retrying never helps: offer another format or platform. |
| `validation.post_limit_exhausted` | Monthly plan limit reached. `get_usage` shows when it resets. |

When the content must change, `update_post` works on `failed` posts only (and on drafts and scheduled posts). A `partial` post cannot be edited: create a new post for the failed platforms instead, with `create_post` targeting only those accounts.

## 4. Retry

- Ask before retrying: `retry_post` costs 1 post credit. It resends only the failed platforms of a `failed` or `partial` post, never the ones already published.
- Then poll `get_post` until it reads `published`, `partial` or `failed`, and report each platform's result. Never say it worked before that.
- If the same error comes back, do not retry again in a loop: explain what is still wrong and what the user needs to do.
