---
name: social-publishing
description: Use when the user wants to write, publish, or schedule a post on LinkedIn, Instagram, Instagram Business, Facebook (as the profile or a Page), Threads, TikTok, YouTube, Pinterest, Google Business Profile, or WordPress - including images, carousels, videos, Reels, Stories, and articles - or to see, check, or cancel scheduled posts on the post calendar. Publishing and scheduling require user approval of the account, exact text, media, audience, and time.
---

# Social publishing

Read [account access and limits](../../references/account-and-limits.md) before using tools.

## Pick the account

Call `list_accounts` and use an account whose `can` includes `posts`. When several could post, ask which one, and pass its `account_id` as `account` to every tool below. If the network the user wants isn't connected, connect it as described in [Getting started](../getting-started/SKILL.md). Before a series of posts, check the remaining `posts` allowance with `account_status`.

Call `post_options` with the account before composing for an account you haven't posted to in this conversation. It returns the network's limits (characters, title, media) and fields, and the account's own choices: TikTok privacy levels and the interactions the creator allows, Pinterest boards and the default one, the WordPress site, YouTube visibilities, and Google Business Profile buttons. Use only values it lists.

## Compose

`create_post` takes `text` (the caption on Instagram, the description on YouTube and Pinterest, the article's HTML on WordPress) and the network's fields:

| Network | Text | Media | Also |
|---|---|---|---|
| LinkedIn | up to 3000 | one image, optional | `link` appended to the text and previewed when there's no image; `visibility` `anyone` or `relations_only` |
| Instagram (login) | caption up to 2200 | one photo, required | |
| Instagram Business | caption up to 2200 | up to 20 images or one video, required | one image is a feed post, several a carousel, a video a Reel; `story: true` makes a Story (one image, or a video up to 60 s); `share_to_feed`, `first_comment`, up to 3 `collaborators`, Reel cover `thumbnail_url` |
| Facebook | up to 10000 | one image, optional | `as_page` posts as a Page (`page_id` from `facebook_list_pages`); `visibility` `anyone` or `relations_only` (not for a Page); `share_post_id` shares a post, now only, with no image |
| Facebook Page (connected on its own) | long text; Facebook shows about 480 characters before "See more" | up to 10 images or one video, optional | posts as the Page; `reel: true` makes a vertical video (3 to 60 s) a Reel; `story: true` a Story (one image or video, no text shown); `first_comment` (not on Stories) |
| Threads | up to 500 | up to 10 images or one video | |
| TikTok | up to 2200 | up to 35 images or one video, required | `privacy_level`, `allow_comment`, and for a video `allow_duet` and `allow_stitch`, all required; `user_confirmed` |
| YouTube | description up to 5000 | one video, required | `title` (required, up to 100), `visibility` `public`, `private`, or `unlisted`, `tags`, `made_for_kids`, `thumbnail_url` |
| Pinterest | up to 800 | one image or one video, required | `board_id` (else the board picked at connect), optional `title` up to 100, `link` the pin opens, video cover `thumbnail_url` |
| Google Business Profile | up to 1500 | one image | `cta_type` and `cta_url` button; `event_title`, `event_start`, `event_end` for an event; with `coupon_code`, `offer_url`, `offer_terms` an offer |
| WordPress | article HTML up to 100000 | one image | `title` (up to 200), `excerpt`, `slug`, `tags` |

Write for the network's audience and stay within its limits. Keep facts, dates, offers, and claims grounded in what the user gave you.

`made_for_kids: true` turns a YouTube video's comments off for good: set it only when the user says the video is made for children.

## Media

Pass media in order as `media_ids` from `upload_media`, or as public `https` links in `image_urls` and `video_url`. Files attached in the chat can't reach Pluggzy: call `upload_media` once per file, give the user each link, and wait until they say the file is uploaded. If you made the file yourself and can run commands with internet access (a code sandbox, a terminal), upload it with the `upload_command` it returns and use the `media_id` once it answers `ok`. Images are JPEG, PNG, or WebP, at most 8 MB. Videos (MP4, MOV, or WebM) go only to publishing accounts, not to LinkedIn, Instagram (login), or Facebook. See [Getting started](../getting-started/SKILL.md) for upload limits.

## Confirm, then publish or schedule

Posts are public and can't be unpublished through this plugin. Before calling `create_post`, show the account and network, the identity (the profile or which Facebook Page), the exact text and title, every image or video in order, the audience or visibility, and for a scheduled post the time. Publish only after the user approves that exact post. If anything changes, get approval again.

To show the post before approval, call `create_post` with the same arguments and `preview: true`. It posts and schedules nothing. It checks the account, permission, time, length, and uploads, and where the app shows cards the user sees the post as a card: account, text, media, and time. The network checks the rest when the real call runs, so a preview is not a promise that the post will go through. Once the user approves, call `create_post` again without `preview`. If the preview has a `publish_at`, its card also has a Schedule button: when the user says they used it, the post is scheduled, so check `list_scheduled_posts` instead of calling `create_post` for it again. A post that is published or scheduled comes back as a card too, with a link to the calendar.

TikTok requires `user_confirmed: true`, meaning the user saw the final caption and media and agreed to publish them. It is TikTok's legal requirement: set it only after that explicit approval, never on your own.

Without `publish_at`, the post goes out now. With `publish_at`, an ISO 8601 date and time with a UTC offset (like `2026-11-03T09:30:00+01:00`), at least a minute and at most a year ahead, it is scheduled and the call returns a `scheduled_post_id`. Confirm the time in the user's time zone together with the content, and ask for the time zone if it is unknown. Links in `image_urls` or `video_url` must keep working until `publish_at`; uploads are kept with the post.

Scheduling is not publishing: the post goes out through the account's limits, so it can be a few minutes late, and it fails if those limits hold it back for more than six hours. Report success and a post URL only when the tool returns them. After an uncertain result, check `list_posts` or `list_scheduled_posts` before trying again: never post twice.

## Manage the calendar

`list_scheduled_posts` shows posts scheduled with `create_post` or on the Pluggzy dashboard's calendar: `status` `scheduled` (the default, soonest first), `publishing`, `published` (with the post `url`), `failed` (with `error`), `cancelled`, or `all`, optionally for one `account`. Each comes with its time, account, text, title, options, and media links. Posts scheduled before the calendar existed show only their length in `chars`.

`cancel_scheduled_post` with a `scheduled_post_id` cancels a post that hasn't gone out yet, or a draft saved on the calendar. Confirm which post first. To change a scheduled post, cancel it and schedule the approved new version, or the user can edit it on the calendar in the Pluggzy dashboard.

## After publishing

`list_posts` lists an account's posts, and `list_comments` and `comment` handle their comments. For Facebook post edits, shares, and reactions, use [Facebook](../facebook/SKILL.md). For Instagram Business comments and insights, use [Instagram Business](../instagram-business/SKILL.md).
