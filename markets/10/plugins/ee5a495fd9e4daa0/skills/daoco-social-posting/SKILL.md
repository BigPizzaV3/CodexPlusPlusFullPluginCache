---
name: daoco-social-posting
description: Save a social post the app already wrote to the brand's connected accounts in Daoco, then publish it now or schedule it, edit or cancel it, and read how it went out. Also connects a missing social account. Use when the person has the exact post and wants it posted or scheduled, not written by Daoco.
---

# Post to social accounts through Daoco

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for brand selection and tool boundaries.

These tools write the post exactly as given, with no Daoco thread and no model, so they use no workspace tokens. When the person wants Daoco to write the post, plan a batch, or make its images or video, use `start_work` through `daoco-content-and-creative` instead. Daoco's drafts from that work appear in `list_work` with `view: "drafts"`, and their `postId` works with the tools below.

## Pick the accounts

Call `list_channels` for the brand's connected accounts. Each has a `channelId`, its platform, whether it is ready to post, and the platform's limits: caption length, whether media is required, media kinds, image count, video length, and story support. Write to those limits instead of discovering them from a refusal. Use only the accounts the person named or confirmed.

If an account is missing or needs reconnecting, call `get_connect_link` with the platform as `target` and give the person the link. They open it, sign in to Daoco, confirm, and connect at the platform. The app never connects an account itself, and the link works for 24 hours. Then call `list_channels` with `waitSeconds` to see the account land. The same tool takes an integration id (such as `hubspot`) or `browser` for a signed-in browser profile.

## Save the post

`create_post` saves a draft: `text`, `channelIds`, and optionally `channelText` (different text per channel; channels on one platform share it), `files` (up to 20 images as a carousel where supported, or one video, in order), `cover` for a video, `postFormat: "story"`, `plannedDate` (a calendar date that does not schedule), `link` (a LinkedIn link card, shown only without media), and `platformOptions`. Use a `clientRequestId` so a retry does not save a second post. Attach local media through `upload_file` as the shared workflow describes. When the post makes an idea from `list_content_ideas`, pass its `ideaId`: the idea is claimed for this app and measured once the post goes out. If the reply says someone else holds the idea, do not save a second post for it.

Some platforms need settings before publishing, in `platformOptions`: TikTok `privacy` (do not pick a privacy level for the person; ask), a YouTube Shorts `title`, a Pinterest `title` and `boardId`, a Reddit `title` and `subreddit`. Instagram reels can be trial reels. The result lists `blockingIssues`, anything that stops the post going out now. Fix them with `update_post`, or ask the person for what only they can decide.

Write the person's post, not an improved one. If you draft the text yourself, call `get_brief` for the task and channel first, show the draft before saving, and keep the person's wording where they gave it. Never invent claims, prices, results, testimonials, or personal stories.

## Brand check

Daoco checks a saved, unpublished post a few seconds after each save: hook, audience, brand voice, clarity, claims against the brand's documents, images, and resemblance to the account's past posts. `brandCheck` is `checking` at first; `get_post` with `waitSeconds` returns when it finishes. Report findings marked `attention` in plain words and let the person decide. The check never blocks or changes the post; an `outdated` check predates the latest edit.

## Publish or schedule

Publish or schedule only when the person asked for it, for those posts and that time. `schedule_post` with `postId` publishes now; `publishAt` (ISO 8601 with an offset, two minutes to a year away) schedules. Confirm the time zone when the person gave a local time.

The brand's approval settings in Daoco decide what happens. When they allow it, a schedule is set at once and a publish starts at once (`publishing`; `get_post` gives each channel's link once live). Otherwise the status is `awaiting_approval` with a Daoco link, and the person is asked in Daoco and on their personal assistant. Share that link and say the post goes out only after they approve. Several posts asked about together share one approval page. Never treat an approval as given, and never ask the person to approve in chat for the app to pass on.

`approval: "skip"` applies only when a workspace owner or admin turned on "Let this app publish without asking" for this app. Pass it only when the person asked this post to go out without approval. Deletes, email, and connections set to always ask still need a person; when the setting is off, skip is ignored and the result says approval was needed.

## Follow

`get_post` reads status (`draft`, `awaiting_approval`, `scheduled`, `publishing`, `published`, `partly_published`, `failed`), each channel's link or error, and `lastApproval` (approved or rejected, whether the person edited the text while approving, and why an approved post did not go out). With `waitSeconds` it returns on a change. Report a partial or failed publish per channel; do not call it a success.

## Results

Once a post has been out three days, `get_results` says how it did against the account's usual engagement (`above`, `usual`, `below`, or `unknown`) and who made it; `madeByThisApp` keeps this app's own. Report the verdict as given; a post with too few views is `unknown`, not bad.

## Edit or cancel

`update_post` changes only the fields given; `files` replaces all media. It is refused while the post is scheduled, waiting on any approval, publishing, or published. `cancel_post` returns a scheduled post, or one waiting on an approval this app asked for, to a draft; then edit and schedule again. A published post cannot be called back from Daoco.
