---
name: sceneform-publish
description: Schedule, publish, and manage images, videos, and carousels on the user's connected TikTok, Instagram, YouTube, LinkedIn, Facebook, or X accounts, plus text-only X posts. Use when the user wants to post, schedule, or share content, see what is scheduled or where a post went live, or reschedule, edit, cancel, publish now, or retry a post. NOT for making the asset (sceneform-generate), reading brand identity (sceneform-brand), or how posts perform (sceneform-research).
license: MIT
metadata:
  author: sceneform
  version: "0.11.0"
---

# Publish with Sceneform

`schedule_post` sends one finished asset or carousel to one connected social
account, either as soon as possible or at a set time. Posts go out through
the user's own account and appear on the Schedule page in the Sceneform
dashboard. The other tools here read the connected accounts and the
Schedule, and change posts that are already on it. For a text-only X post,
omit both media refs. X supports up to four images or one MP4 video (up to
512 MB in Sceneform), with up to 280 weighted characters; links count as 23
characters. The X account's audience settings apply. An X post can carry a
first comment: a reply from the same account posted right after it goes
live, the usual place for a link, since X shows posts without one to more
people. X analytics and threads are not supported. Each X post costs
Sceneform credits, more when its text has a link, and a first comment is
priced as a second post; the approval shows the exact cost. A post that
fails before X receives it is refunded, and so is a first comment X
refuses.

## Workflow

1. Get the asset. Use an `asset_ref` from a finished operation
   (`wait_operations` or `get_operation`, `status: "succeeded"`) or from
   `search_library`. The asset must be complete; a pending output cannot be
   scheduled. To post a whole carousel, pass its `carousel_ref` instead of
   `asset_ref` once `get_carousel` reports it `ready`: every slide goes out
   in order as one multi-image post. YouTube and Facebook take videos only,
   and each other platform caps the slide count; `schedule_post` names the
   limit when a carousel is too long. Skip this step for a text-only X post.
2. Read the account. `list_social_accounts` gives, for each connected
   account, `privacy_options` (who a post can be shown to: `public`,
   `followers`, `friends`, `private`), the TikTok `interactions` it can turn
   on (`comments`, `duet`, `stitch`), and for Facebook the `pages` it can
   post to.
3. Ask the user what only they decide. For TikTok, ask who can see the post
   (one of its `privacy_options`) and whether to allow comments, and duet and
   stitch for a video. TikTok requires the user's own choice: never pick a
   privacy for them, and leave every interaction off unless they turn it on.
   Ask once per conversation: when the user has already said, for example
   "public, comments on", reuse that for their later TikTok posts and say so
   with each quote, unless they change it. `private` makes a test post only
   the user sees, on TikTok and YouTube.
4. Write the caption in full, in the brand's voice (read the brand kit first
   with sceneform-brand when there is one). Add a short `title` only for
   platforms that show one, such as YouTube.
   - The first line carries the hook: feeds cut the caption after a line or
     two, so the reason to stop scrolling comes first.
   - One idea, then one call to action ("Link in bio", "Save this for
     later").
   - Three to five specific hashtags at the end on TikTok and Instagram;
     none or one or two on LinkedIn and Facebook.
   - Facts, prices, and claims only from the user or the BrandKit.
   - A paid partnership or a sponsored post says so in the caption.
5. Quote. Call `schedule_post` with `asset_ref` or `carousel_ref`,
   `platform` (`tiktok`, `instagram`, `youtube`, `linkedin`, `facebook`, `x`),
   `caption`, `privacy` (required for TikTok; defaults to `public`
   elsewhere), `interactions` and `ai_generated` for TikTok,
   `facebook_page_id` when a Facebook account has several Pages,
   `first_comment` for X when the post has a link to share, optional
   `title`, and optional `scheduled_for` as an ISO 8601 datetime with the
   user's timezone offset (`2026-09-10T09:00:00+02:00`), at most 30 days
   ahead. Omit `scheduled_for` to publish as soon as possible. The tool
   returns `status: "awaiting_confirmation"` with a `summary`, a
   `consequence`, the `details` (platform, Page, who can see it, the slide
   count for a carousel, when, title, and for TikTok the AI-generated label
   and interactions), the caption as `body`, and an `action_ref`. A
   `Daily limit` detail means the TikTok account is past TikTok's roughly 15
   posts a day: say so, since TikTok may refuse the post. A carousel edited
   after its quote is refused when confirmed; quote it again.
6. Confirm. Posting always asks, even where generation does not. Show the
   user the consequence, the details, and the caption, and only after they
   say yes call `confirm_actions` with the `action_ref` in `action_refs`.
   With `card_offered: true` the host was also given a card with Approve and
   Skip buttons; say they can approve there. Its
   `results[0].result` holds the `scheduled_post_ref`, the `platform`, and
   `scheduled_for`.

```sh
sceneform accounts
sceneform publish --asset ./out/1.mp4 --platform tiktok --caption "New drop this Friday" --privacy public --interactions comments --ai-generated yes --at 2026-11-06T09:00:00+01:00
sceneform confirm 3f2a7c1e-5b4d-4e8a-9c6f-0d1e2f3a4b5c
```

With `--yes` the CLI confirms on its own. `--asset` accepts a local path or
an `asset_ref`; `--carousel <carousel_ref>` posts a whole carousel instead.
For text-only X: `sceneform publish --platform x --caption "We shipped."`.
Add `--first-comment "Notes at https://example.com"` to reply with the link.

## Manage posts

- `list_social_accounts` lists each connected platform, whether it is
  `connected` or `disconnected`, `can_post`, and the options in step 2. A
  `disconnected` account is connected again on the Connections page.
- `list_scheduled_posts` lists posts in a window (default: the last 7 days
  through the next 30), filtered by `platform` or `statuses`. Each post has
  its `scheduled_post_ref`, `status` (`scheduled`, `publishing`, `posted`,
  `sent_as_draft`, `failed`, `cancelled`, `held`), time, caption,
  `media_type`, `privacy`, the `asset_ref` or `carousel_ref` it published,
  the `error` when it failed, and once posted its `post_url` (the live post
  on the platform, when the platform gives a link) and `metrics` (views,
  likes, comments). Use `statuses: ["failed"]` to find posts to retry. For
  how posts and accounts perform, load `sceneform-research`.
- `update_scheduled_post` moves a `scheduled` post to a new future time or
  replaces its caption or title. Pass only what changes.
- `cancel_scheduled_post` unschedules a `scheduled` or `held` post, or
  dismisses a `failed` or `sent_as_draft` one, or a `publishing` one that
  stalled. A post still publishing can't be cancelled, and a `posted` post
  is live; the user deletes it on the platform.
- `publish_scheduled_post_now` publishes a `scheduled` post now, or retries
  a `failed` one or a `publishing` one that stalled. A failure whose `error`
  says the post may already be live is refused: the user checks the
  platform first. It returns once publishing starts; check the outcome
  later with `list_scheduled_posts`.

```sh
sceneform posts --status failed
sceneform post-edit k57f2a9c1d3e4b5f6a7b8c9d0e1f2a3b --at 2026-11-07T09:00:00+01:00 --caption "New drop this Saturday" --yes
sceneform post-cancel k57f2a9c1d3e4b5f6a7b8c9d0e1f2a3b --yes
sceneform post-now k57f2a9c1d3e4b5f6a7b8c9d0e1f2a3b --yes
```

## Rules

- Never publish without an explicit yes on the exact summary. Do not infer
  consent from an earlier message.
- Ask for the timezone when the user names a time without one. Never guess it.
- For TikTok, ask the user who can see the post and which interactions to
  allow; never choose for them. Ask once and reuse their answer for later
  posts in the conversation.
- For TikTok, set `ai_generated` to whether AI made the asset: `true` for a
  Sceneform output, `false` for the user's own photo or video unless they say
  AI made it. Ask when you cannot tell. TikTok labels the post AI-generated
  when it is `true` or omitted. Other platforms ignore it.
- A platform with no connected account fails with a safe message. Point the
  user to the `connections_url` from `list_social_accounts` (Settings,
  Connections in the dashboard); there is no way to connect an account from
  here.
- Confirming the same `action_ref` twice is safe, and it is the way to retry
  a confirmation that timed out or failed: `sceneform confirm <action_ref>`
  in the CLI. Only when that answers `PLAN_STALE` (the post failed and was
  not made) quote it again; otherwise calling `schedule_post` again creates
  a second post once confirmed. To change a post, use `update_scheduled_post` instead of
  scheduling it again.
- Reschedule, edit, cancel, publish now, or retry a post only when the user
  asked for that post. State a new time or caption back to them.
