---
name: schedule-social-posts
description: Schedule social media posts and attached videos or images, inspect queues, or cancel pending posts through a connected Hogmatix account on X, TikTok or YouTube.
---

Use Hogmatix's connected-account tools for the requested scheduling task. The server supports X posts and threads (optionally with one image or video), TikTok videos, and YouTube videos. Other platforms, published-post deletion, analytics and media generation are outside this tool surface.

Discover destination identifiers with `list_accounts`: X uses `profile`, TikTok uses `openId`, YouTube uses `channelId`. When the request is about one platform, pass `platform` to list only that platform's accounts. Sign-in and social account connection happen on Hogmatix through the host's OAuth flow. Do not ask for passwords, tokens or payment details in chat.

Preserve supplied post text, captions, titles and descriptions verbatim unless the user requests editing. When text exceeds a platform limit, explain the limit and ask how to proceed. Never silently shorten, reword or normalize it.

Resolve the destination account, exact content, calendar date and time zone before scheduling. Use ISO 8601 with an explicit offset for that date; Hogmatix requires at least ten minutes of lead time. Before each scheduling call, show the destination account, exact content, date and time with its time zone, and every label, and get the user's confirmation, even when the request already states them all. For multi-platform work, review each destination's content and options before its write.

Read queues with `list_scheduled_posts`. For X, supply a discovered profile. Report returned statuses and times faithfully. Scheduling success means queued; it does not establish platform publication. After a timeout or ambiguous failure, inspect the queue before retrying a non-idempotent scheduling operation.

For a file attached in the chat, call `import_attached_file` with that file and the destination's purpose: `x-media` (image or video) for X, `tiktok-video` for TikTok, `youtube-video` for YouTube. Import once per platform; each upload serves only its own purpose. An import holds one of the account's upload slots until it is scheduled, so import only for the platforms the user chose, and schedule each platform's post before importing for the next. While the import is `downloading` or `uploading`, call `get_import_status` until it is `ready`; never schedule before then. Schedule with the ready import's `uploadId`, and give `schedule_tiktok_video` its `durationSec`. If an import fails, relay its error; if the attachment link expired, ask the user to attach the file again. If the call fails because the file argument was missing, call `import_attached_file` again once with the attached file; if it is still missing, ask the user to attach the file again. If the attachment arrived as a placeholder instead of a file (this happens in the mobile apps), ask the user to attach it again in a web browser, or to upload and schedule it on hogmatix.com. Never invent upload or import IDs.

Use the manual upload only from a client that can send file bytes itself: `create_media_upload`, PUT each part's actual bytes, with its base64 SHA-256 checksum, to the URL and headers from `get_upload_part_url`, then `complete_media_upload`. Schedule once the upload is `promoted`.

For TikTok, call `get_tiktok_creator_info`, then show the creator what Hogmatix's composer shows:
- Posting as: `creator_nickname` (@`creator_username`).
- Who can see this: only the returned privacy options, named Everyone, Friends, Followers or Only me.
- Allow comments, Allow Duet, Allow Stitch; any the creator disabled in TikTok stay off.
- Disclose video content, if the video promotes a brand, product or service: Your Brand ("You are promoting yourself or your own business", labeled "Promotional content") and/or Branded Content ("You are promoting another brand or a third party", labeled "Paid partnership"). With disclosure on, at least one is required. Branded Content requires Everyone or Friends visibility.
- AI-generated content: "Yes, AI made or changed this video" (TikTok adds an "AI-generated" label; AI voices, music, people or scenes count) or "No AI-generated images, video, voice or music".
- The declaration, word for word: "By posting, you agree to TikTok's Music Usage Confirmation." With Branded Content: "By posting, you agree to TikTok's Branded Content Policy and Music Usage Confirmation." Link https://www.tiktok.com/legal/page/global/music-usage-confirmation/en and https://www.tiktok.com/legal/page/global/bc-policy/en.

Require the creator's explicit choice for privacy, each interaction, disclosure and the AI label; never default or guess one. Show these choices with the video's file name, caption and time, and get the creator's go-ahead before `schedule_tiktok_video`, even when the request already states every choice. If the account can't post now or the video exceeds `max_video_post_duration_sec`, explain and stop. If Hogmatix says the caption names the account's own brand, ask whether to turn on Your Brand. After scheduling, note that TikTok may take a few minutes to process the video once it posts.

For YouTube, resolve title, description, privacy (private, unlisted or public) and made-for-kids selection.

Cancel only the specifically authorized pending post with `cancel_scheduled_post`, using its returned ID and platform. Resolve ambiguous targets first, then verify the resulting queue status. Already-published posts cannot be recalled here.

Use `get_plan` to explain current account entitlement and posting allowance when relevant. Do not sell subscriptions, promote trials or upgrades, initiate billing, or supply transactional links through this plugin.
