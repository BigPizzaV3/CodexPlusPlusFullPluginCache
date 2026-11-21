# SocialAPI tool reference

Every tool name starts with `social_api_`, dropped below for readability. What each platform supports is in [platforms.md](platforms.md).

## Where each id comes from

| Value | Comes from | Goes to |
|---|---|---|
| account `id` | `list_accounts` | `account_id` of nearly every tool |
| brand `id` | `list_brands` | `brand_id` |
| page `id` | `list_account_pages` | `page_id` (Facebook, LinkedIn Page) |
| board `id` or `board_id` | `list_pinterest_boards` | `board_id` on every Pinterest target (either value works) |
| inbox post `id` (a platform post id) | `list_inbox_posts` | `inbox_post_id` of `list_post_comments`, `post_id` of every comment action |
| comment `platform_id` | `list_post_comments`, and `ID` of `get_comment_replies` | `comment_id` of `reply_to_comment`, `private_reply_to_comment`, `hide_comment`, `unhide_comment`, `like_comment`, `unlike_comment`, `delete_comment`, `get_comment_replies` |
| `sapi_cmt_...` id | webhook payloads, `comment_id` returned by `reply_to_comment` | `interaction_id` of `moderate_comment` |
| conversation `id` | `list_conversations` | `conversation_id` of every DM tool |
| review `ID` (`sapi_rev_...`) | `get_reviews` | `review_id` of `reply_to_review` |
| mention `id` (`sapi_mnt_...`) | `get_mentions` | `media_id` of `reply_to_mention` |
| post `id` (a UUID) | `list_posts`, `create_post` | `post_id` of the publishing tools and `get_post_analytics` |
| media id | `media_id` of `get_media_upload_url`, `ID` of `list_media` | media items with `source_type: media_id`, `verify_media_upload`, `delete_media` |
| Automation `id` (`aut_...`) | `list_automations`, `create_automation` | `automation_id` |

The two comment id forms only partly mix:
- `reply_to_comment`, `private_reply_to_comment`, `hide_comment`, `unhide_comment` and `get_comment_replies` accept either the raw `platform_id` or a `sapi_cmt_` id.
- `like_comment`, `unlike_comment` and `delete_comment` accept only the raw `platform_id`.
- `moderate_comment` accepts only a `sapi_cmt_` id.

`get_post` and `get_post_metrics` also accept a platform post id.

## Pagination and page sizes

`limit` takes a number. Pass a cursor back exactly as the previous page returned it and never build one yourself.

| Tool | Default | Max | Next page |
|---|---|---|---|
| `list_inbox_posts` | 25 | 100 | none, only `has_more`. Narrow with `since`, `account_id` or `platform`, or raise `limit` |
| `list_post_comments` | 25 | 100 | `next_cursor`, empty on the last page |
| `get_comment_replies` | 20 | 100 | none, first page only |
| `list_conversations` | 25 | 100 | `next_cursor`, empty on the last page |
| `list_messages` | 50 | 100 | none, only `has_more`. Newest first, so the latest messages are always on the first page |
| `get_reviews` | 20 | 50 | `next_cursor`, empty on the last page |
| `get_mentions` | 20 | 100 | `next_cursor`, absent on the last page |
| `list_instagram_stories` | 20 | 100 | `next_cursor`, absent on the last page |
| `list_posts` | 25 | 100 | `cursor`, null on the last page |
| `list_media` | 25 | 100 | `next_cursor`, absent on the last page |
| `list_events` | 50 | 100 | `next_cursor`, absent on the last page |
| `list_webhook_deliveries` | 50 | 100 | `next_cursor`, empty on the last page |
| `list_automation_firings` | 20 | 100 | `next_cursor`, empty on the last page |

`list_accounts`, `list_brands`, `list_account_pages`, `list_pinterest_boards`, `list_invites`, `list_keys`, `list_webhooks`, `list_automations` and `list_review_accounts` take no `limit` and return everything as `{data, count}`. `list_exports` returns the latest 50 as `{exports, count}`. `list_events` puts its rows under `events`, not `data`.

Timestamps are RFC3339 (`2026-10-12T18:00:00Z`). The analytics tools take days as `YYYY-MM-DD`.

## Response keys

Responses use snake_case keys, except these, which use capitalised keys:
- `list_review_accounts`: `AccountID`, `Name`, `Platform`, `Status` (`ok`, `reconnection_required` or `error`), `Summary`.
- `get_reviews` items: `ID`, `Rating` (1 to 5), `Text`, `Author`, `Reply` (null when unanswered), `CreatedAt`, `UpdatedAt`. Its top-level `summary` holds `AverageRating`, `TotalCount`, `LastReviewAt`.
- `get_comment_replies` items: `ID` (the reply's platform id), `Text`, `Author` (`Name`, `Username`, `IsOwner`), `LikeCount`, `HasReplies`, `IsHidden`, `ParentID`, `CreatedAt`.
- `list_media` items: `ID`, `Filename`, `ContentType`, `SizeBytes`, `Status`, `CreatedAt`. `get_storage_usage`: `UsedBytes`, `LimitBytes`, `Count`.
- `list_events` items: `ID`, `Category`, `Action`, `Status`, `Platform`, `AccountID`, `ResourceID`, `Summary`, `ErrorMessage`, `CreatedAt`.
- `profiles` of `list_pending_profiles`: `PlatformAccountID` (the `platform_account_id` that `select_pending_profile` takes), `DisplayName`, `Username`.

## Accounts, brands, profile

| Tool | Notes |
|---|---|
| `list_accounts` | Optional `brand_id`. `status` is `active` or needs reconnecting. |
| `connect_account` | `platform`, optional `brand_id` (a new brand is created when omitted). OAuth platforms return an `auth_url` for the user to open, and the account connects once they approve. Credential platforms connect immediately and return the `account_id`. |
| `list_pending_profiles`, `select_pending_profile` | Finish a `selection_required` connection: Google takes one `platform_account_id`, Facebook takes `page_ids`. Expires after 30 minutes, first selection wins. |
| `disconnect_account` | Irreversible. Scheduled posts aimed at the account will fail. |
| `get_creator_info` | TikTok only: the privacy levels and duet and stitch options this account may use. Read it before every TikTok post. |
| `list_brands`, `create_brand`, `update_brand`, `delete_brand` | A brand groups one account per platform for a business or client. The number of brands is plan-limited (`brand.limit_reached`). `update_brand` renames only. `delete_brand` disconnects all its accounts. |
| `list_account_pages`, `update_account_page` | Facebook Pages and LinkedIn organization Pages, with `is_default` and `is_active`. Pinterest accounts are refused. |
| `list_pinterest_boards` | `account_id` of a Pinterest account. Returns each board's `id`, `board_id` (Pinterest's own id), `name` and `privacy`. Other platforms return `account.boards_not_supported`. |
| `create_invite`, `list_invites`, `revoke_invite` | One-time link letting someone else connect their account to a brand. `expires_in_days` is 1, 3, 7 (default), 14 or 30. |
| `get_me`, `patch_me` | Plan tier, onboarding flag, `lock_accounts_to_brand`. |
| `get_usage` | Brands, posts and interactions used and allowed this period, with `period_end`. -1 means unlimited. |
| `get_account_limits` | The platform's own quotas for one account. See platforms.md for which platforms report them. |
| `list_keys`, `revoke_key` | API key metadata. No tool creates a key or deletes the user account: both are done in the dashboard. |
| `send_feedback` | `type` is `bug`, `feature_request` or `general`. |

## Inbox: comments

| Tool | Notes |
|---|---|
| `list_inbox_posts` | The accounts' posts with their comment counts, including posts with none: `min_comments: 1` keeps only commented posts. Filters `account_id`, `brand_id`, `page_id`, `platform`, `min_comments`, `since`. `since` and `sort_by: date` (default) both use the post's publish date, not its latest comment; `sort_by: comments` sorts by comment count. `sort_order` `desc` (default) or `asc`. Rows: `id`, `account_id`, `platform`, `content`, `permalink`, `comment_count`, `published_at`, `updated_at`. |
| `list_post_comments` | Needs `inbox_post_id` and `account_id`. The order depends on the platform. Rows: `platform_id`, `text`, `author_name`, `author_username`, `is_owner`, `like_count`, `reply_count`, `has_replies`, `is_hidden`, `parent_id`, `created_at`. |
| `get_comment_replies` | `account_id` and `comment_id`, optional `since`. |
| `reply_to_comment` | `account_id`, `post_id` (required), optional `comment_id` to answer that comment rather than the post, `text` up to 2200 characters. On Instagram, `comment_id` is required: a reply to the post itself is not supported there. Returns the new reply's `comment_id`. 1 interaction credit. |
| `private_reply_to_comment` | Answers the commenter by DM. `account_id`, `post_id`, `comment_id`, `text` up to 1000 characters, optional 1 to 3 `buttons`. Free. Once per comment, within 7 days of it. |
| `hide_comment`, `unhide_comment`, `like_comment`, `unlike_comment`, `delete_comment` | `account_id`, `post_id`, `comment_id`. Always pass `post_id`: on accounts with several Pages it selects the Page that acts. Free. |
| `moderate_comment` | `account_id`, `interaction_id` (`sapi_cmt_...`), `action` `hide`, `unhide` or `delete`. |

## Inbox: DMs

| Tool | Notes |
|---|---|
| `list_conversations` | Filters `account_id`, `brand_id`, `page_id`, `platform`, `status` (`active` default, or `archived`). Rows: `id`, `account_id`, `platform`, `participant_name`, `last_message`, `last_message_at`, `status`, `unread_count`. |
| `list_messages` | `conversation_id`. Newest first. Rows: `id`, `direction` (`incoming` or `outgoing`), `text`, `sender_name`, `attachment_type`, `attachment_url`, `created_at`, `status`. |
| `get_conversation`, `update_conversation`, `mark_conversation_read` | `update_conversation` sets `status` to `active` or `archived`. |
| `send_dm` | Replies in an existing conversation; it cannot start a new one. `account_id`, `conversation_id`, `text` up to 1000 characters. Optional `quick_replies` (up to 13, labels up to 20 characters) or `buttons` (1 to 3, `url` or `postback`, labels up to 20 characters); taps come back as `dm.postback` webhook events. `message_tag: HUMAN_AGENT` extends the Instagram 24 hour window to 7 days. 1 interaction credit. |

## Inbox: reviews, mentions, stories

| Tool | Notes |
|---|---|
| `list_review_accounts` | Accounts that have reviews, each with its rating summary and status. |
| `get_reviews` | `account_id`, `order` (`newest`, `rating_asc`, `rating_desc`). An account whose platform has no reviews returns `account.platform_unsupported`. |
| `reply_to_review` | `account_id`, `review_id`, `text` up to 2200 characters. Returns `reply_id` and `state` (`PENDING`, `APPROVED` or `REJECTED` on Google). On Google a review has one business reply, so replying again replaces it. 1 interaction credit. |
| `get_mentions` | Posts and comments by others that mention or tag the account. Optional `since`. Rows carry `id` (`sapi_mnt_...`), `author`, `content`, `permalink`, `received_at`. |
| `reply_to_mention` | `account_id`, `media_id` (the mention `id` or the post it is on), `comment_id` only when the mention is inside a comment, `text` (up to 2200 characters on Instagram and Facebook, the platform's post length on Threads and Bluesky). 1 interaction credit. |
| `list_instagram_stories` | The account's stories still live, each expiring about 24 hours after posting. |

## Publishing

| Tool | Notes |
|---|---|
| `list_posts` | Filters `status`, `platform`, `account_ids` (comma separated), `brand_id`, `page_id`, `from`, `to`, `search`, `sort` (`scheduled_asc` default, `scheduled_desc`, `created_asc`, `created_desc`), `hidden`. |
| `create_post` | See below. |
| `update_post` | Only `draft`, `scheduled` or `failed` posts. `targets` replaces the whole list. Free. |
| `publish_post` | Publishes a `draft` or `scheduled` post now. 1 post credit. |
| `delete_post` | Deletes a draft, scheduled or failed post entirely, or removes a published one from each platform. `results` reports each target as `deleted`, `not_supported` or `failed`. |
| `unpublish_post` | Removes the post from one platform (`account_id`) or all of them, keeping the record. |
| `retry_post` | `failed` or `partial` posts only, resends the failed targets. 1 post credit. |
| `get_post`, `get_post_metrics` | Delivery status per target, and the post's current engagement. |
| `validate_post`, `get_constraints` | Pre-flight check returning `{valid, errors, warnings}`, and the raw per-platform limits. |
| `get_media_upload_url`, `verify_media_upload`, `list_media`, `delete_media`, `get_storage_usage` | Media library. The free plan stores 100 MB, paid plans are unlimited. |

`create_post` fields:
- `text` is always sent; it may be `""` when every target sets its own. Also `title` (YouTube, Pinterest), `media`, `visibility`, `first_comment`.
- `publish_now: true` publishes, `scheduled_at` schedules, neither saves a draft.
- `targets[]`: `account_id`, plus `page_id` or `board_id` and per-target overrides of `text`, `title`, `media`, `first_comment`, `visibility`, `scheduled_at`, `platform_data`.
- `segments[]`: follow-up posts chained after the main one as an X thread.
- `platform_data` keyed by platform, for example `{"instagram": {"content_type": "reel"}}` or `{"tiktok": {"privacy_level": "PUBLIC_TO_EVERYONE"}}` (use a level `get_creator_info` lists). LinkedIn accepts `article_url`, `article_title`, `article_description`, `cta_label`, `cta_url`, `alt_text`, `media_title`, `disable_reshare`.
- The same content posted again within 24 hours is refused unless `skip_duplicate_check: true`.
- 1 post credit when it publishes or schedules, free as a draft.

Media items are `{source_type, source, type}`:
- `url` is a public http or https address.
- `media_id` is an item of the media library.
- `platform_attachment_id` is a media id already uploaded to the platform. It publishes on `instagram`, `threads`, `linkedin`, `linkedin_page` and `twitter` only, and needs `type` (`image`, `video`, `audio` or `file`).

Post status runs `draft` or `scheduled`, then `publishing`, then `published`, `partial` or `failed`.

Instagram cannot publish text alone, and `validate_post` does not flag a missing image or video: check that every Instagram target has one.

## Analytics

| Tool | Notes |
|---|---|
| `get_account_analytics` | `account_id`, optional `page_id`. |
| `get_brand_analytics` | `brand_id`: every account and page of the brand, summed per metric per day. |
| `get_post_analytics` | `post_id` (UUID). History starts when the post was first tracked. |
| `create_export`, `get_export`, `list_exports`, `get_export_videos` | Spreadsheet and report page for one account, built in the background. Poll `get_export`; its download link lasts 15 minutes. The free plan allows 2 a month, 7 days apart per account, 30 videos each, one export at a time. |

All three history tools take `from` and `to` as `YYYY-MM-DD` (default: the 30 days ending today, UTC, at most 400 days) and an optional `metrics` list. They return `{data: {from, to, series}}`, where each series has `metric`, `kind`, `day_tz` and `points` of `{day, value, subjects_counted}`.

How to read the series:
- A `gauge` is a level, such as followers: compare first and last values for growth.
- A `flow` is a per-day count, such as reach: sum it over the range.
- On a brand, a day with a lower `subjects_counted` had fewer accounts reporting. Its lower total is a gap in the data, not a decline.

## Automations

Automations answer matching comments or DMs automatically. They work on Instagram and Facebook accounts only, up to 50 per account (`automation.limit_reached`). Other platforms return `automation.platform_unsupported`.

| Tool | Notes |
|---|---|
| `list_automations` | Optional `account_id`. Each carries its trigger, steps, status and fired, sent and failed counts. |
| `get_automation`, `delete_automation` | `automation_id`. Deleting also deletes its run history. |
| `create_automation` | See below. |
| `update_automation` | Send only the fields to change. `status: paused` stops it, `active` resumes it. `steps` replaces the whole list. |
| `list_automation_firings` | Runs from the last 30 days, newest first, with each action's outcome and error code. |

`create_automation` takes `account_id`, `name` (1 to 100 characters), `trigger` (`comment` or `dm`), optional `once_per_person` and `post_ids` (comment trigger only; omitted means every post), and `steps`.
- Each step has a `key` (the entry step is `start`), optional `filters` (all must pass), `actions`, up to 3 `buttons` and an optional `fallthrough_step`.
- Filters: `{"type": "keyword", "keyword": {"keywords": [...], "match": "contains" or "exact"}}`, matching whole words, ignoring case and accents. `follows_account` exists on Instagram only and not on `start`.
- Actions on a comment trigger's `start` step: `hide_comment`, `reply_comment` (1 credit per run), `private_reply` (free). On a `dm` trigger's `start` step: `send_dm` (1 credit per run). Each text action holds `texts`, 1 to 10 variants of up to 1000 characters, or 640 when the step has buttons.
- Steps after `start` run when the person taps a `postback` button (`next_step`), and may only send DMs. A `url` button opens its `url`.
- A `dm` Automation answers the same person at most 5 times an hour.
- On Facebook, buttons on a `send_dm` step are not shown and the text is sent alone. Private replies keep their buttons on both platforms.

Example, private reply with a link to anyone commenting "link":

```json
{"account_id": "acc_...", "name": "Send the link", "trigger": "comment",
 "steps": [{"key": "start",
   "filters": [{"type": "keyword", "keyword": {"keywords": ["link"], "match": "contains"}}],
   "actions": [{"type": "private_reply", "private_reply": {"texts": ["Here you go: https://example.com"]}}]}]}
```

Instead of real steps, `follow_gate` (Instagram, comment trigger) builds a three-step gate; send it together with `"steps": []`, since `steps` must always be present. It sends a private reply with a button, then the link if the person follows the account, or a follow-first message with a retry button. Its fields are `keywords`, `opening_texts`, `button_title`, `link_texts`, `not_following_texts` and `retry_button_title`, with button titles up to 20 characters.

## Webhooks

`list_webhooks`, `create_webhook` (`url`, `events`), `get_webhook`, `update_webhook` (`url`, `events`, `is_active`), `delete_webhook`, `list_webhook_deliveries` (filter `status` `pending`, `delivered` or `failed`, and `event_type`), `get_webhook_delivery`, `retry_webhook_delivery`, `test_webhook` (`event_type`, `payload`).

The URL must be HTTPS. The HMAC-SHA256 signing secret is returned once at creation, then only a 4 character hint. To debug a failing endpoint, run `list_webhook_deliveries` with `status: failed`, then `get_webhook_delivery` for the request, the response and the error.

Every event `create_webhook` accepts:
- Posts: `post.scheduled`, `post.published`, `post.failed`, `post.partial`, `post.updated`, `post.deleted`, `post.unpublished`, `post.retried`
- Comments, reviews, mentions: `comment.received`, `review.received`, `review.updated`, `mention.received`
- DMs: `dm.received`, `dm.sent`, `dm.deleted`, `dm.referral`, `dm.postback`, `dm.status.sent`, `dm.status.delivered`, `dm.status.read`, `dm.status.failed`
- Accounts: `account.connected`, `account.disconnected`, `account.updated`, `page.removed`

## Activity log

`list_events` filters by `category` (`post`, `webhook`, `inbox`, `api`, `account`, comma separated), `status` (`success`, `failed`, `pending`, `skipped`), `platform`, `account_id`, `resource_id` and `action`. It returns `{events, count, retention_days, next_cursor}`, where `retention_days` is how far back the plan keeps events. `events_summary` counts events and failures by category over `from` and `to` (default: the last 24 hours).
