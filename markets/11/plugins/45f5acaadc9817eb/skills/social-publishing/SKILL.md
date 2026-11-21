---
name: social-publishing
description: Plan a content calendar, write, picture, schedule, change and review social media posts, blog articles, marketing emails, ad copy and product listings with Skryvo. Use when the person asks to plan or write content for their brand, post or schedule to their connected social accounts or blogs, post their own video, move, change or cancel a scheduled post, approve a team post, or learn which posts, articles, channels and times perform best.
---

# Social publishing with Skryvo

Skryvo writes in the person's own brand voice and publishes through the accounts they connected in
Skryvo. Its tools come from the `skryvo` MCP server. The first call asks the person to sign in to
Skryvo and approve access.

## Start every task by reading the setup

1. Call `list_brands`. With several brands, ask which one the post is for unless the request names it.
   Use the brand marked default when the person says it doesn't matter.
2. Call `list_channels`. Use only channels that serve the chosen brand (`brand_ids` empty means every
   brand). A channel with `needs_reconnect: true` can't post: tell the person to reconnect it in Skryvo
   under Settings › Connected Accounts. A channel of kind `blog` takes articles, not posts.
3. Each channel's `can` says what it takes: its word limit, required media, video limits, thread length,
   polls, comments, how a link appears, its own `options` and what the person `must_choose`. Rely on it
   rather than on what you remember about a network.
4. If the platform they want has no channel, call `list_platforms`. Where `can_connect` is true, point them
   to Settings › Connected Accounts in Skryvo; otherwise say it isn't available yet. Don't schedule to
   another platform instead.

## Write

- Call `write_post` with the topic (up to 200 characters: the news, the offer, who it is for) and the
  platforms (up to four per call). The call uses one of the person's Skryvo generations for all of them.
- Pass only what the person said (platforms, tone, language, audience, call_to_action, hashtags, link,
  pictures). When platforms or pictures are left out, `write_post` first returns `status: "confirm"`:
  every setting with where it came from, the cost in generations and image credits, and what is left this
  month. Show it as one message, let the person turn anything on or off, then call again with their final
  values and `confirmed: true`. With pictures on, each post comes back with its picture in the brand's look.
- Show every draft in full, labelled by platform, before anything is scheduled. Edit on request; small
  wording changes don't need a new `write_post` call.
- If a platform comes back with an `error` (for example, the monthly limit), report it as it is and carry
  on with the others.

## Picture

- When the person wants a picture, call `design_picture` with the approved text and the platforms it goes
  to. It designs one picture in the brand's kept look and returns a copy sized for each platform
  (`image_url`, `width`, `height`), plus the Image Studio credits used and left. It takes about a minute.
- The picture carries the post's opening line; pass `headline` (up to nine words) for other words, and
  `direction` for what the person wants, in their words, e.g. "warmer" or "bolder". `photo_id` builds it
  around one of the brand's own photos.
- Where the person added their own design for that format under the brand, the picture follows its layout and
  style. Reference images for one piece are chosen in Skryvo under For this piece; don't promise them here.
- Show every picture before scheduling. If it comes back refused (no credits, or no kept look yet), pass
  the reason on; a brand with no kept look gets one through `brand_design` and `change_look`, with the
  person's yes before `keep`.

## Schedule

- Never schedule without the person's clear go-ahead on the exact text, channels and time.
- Pass times as ISO 8601 with the person's time zone offset, e.g. `2026-10-14T09:00:00-04:00`. Without
  `at`, the post goes out in about five minutes. Skryvo moves a time to its next quarter hour.
- One `schedule_post` call covers every channel. Pass pictures as `images`, `{channel_id: image_url}`,
  giving each channel the copy sized for its platform. `image_url` puts one picture on every channel.
- `by_channel`, `{channel_id: {...}}`, gives a channel what is its own: `text`, `image_url`, `video_id`,
  `title`, `options`, `thread` (the posts that follow), `numbered`, `poll`, `comments`, `tiktok`, `youtube`.
  Send only what that channel's `can` lists. Anything it can't take is refused and nothing is scheduled.
- On a channel whose link is a `destination`, `link` is where its button or pin points; `button` chooses
  a Google Business Profile button.
- Whatever `must_choose` names is the person's answer, never yours, such as a TikTok audience
  (`tiktok_privacy`) or whether a YouTube video is made for kids.
- Confirm afterwards with the returned date and time of each post.

## The person's own video

Skryvo never makes video; a post carries a clip the person already has. `list_videos` shows the ones ready.
To add one, `add_video` with its file name and size returns an `upload_url`; send the file there with an
HTTP PUT, then call `finish_video`. An agent that can't send files asks the person to upload it in Skryvo.
Schedule it with `by_channel.video_id`.

## Check and change

- `list_scheduled_posts` shows what is coming up and anything that failed to publish, with the reason.
- `change_post` moves a post that hasn't gone out, changes its words, or both. Confirm first.
- `cancel_post` removes a scheduled post. Confirm which post first; it can't be undone.
- `review_post` records the person's own decision on a team post waiting for approval. Asking for changes
  needs a note saying what should change. Never decide for them.
- `find_content` finds earlier work by kind, with the ids the other tools take.

## Plan a calendar

`plan_calendar` plans a week or a month of topics for a brand and adds nothing; it uses one generation.
Show the rows, let the person keep or change them, then `accept_plan` with those rows adds them to the
calendar as planned topics. Nothing is written or published by this.

## Learn what works

- `post_results` (7, 30 or 90 days, optionally one brand) gives reach, engagement and clicks per channel,
  the best posting times and the top posts. Use it to suggest when to post and which angles to repeat,
  and say how many days the numbers cover.
- Results arrive about an hour after a post goes live, so a brand-new post shows no numbers yet.

## Articles

1. `plan_article` with the topic and only what the person said. It is free and takes about a minute:
   headline options, the search phrase, the outline, sources and facts, the settings with where each came
   from, the cost, and up to three questions only the person can answer. Show it all as one message.
2. `write_article` with the plan id, the person's chosen headline and their answers in their own words.
   It writes in the background in about four minutes; check `article_status` about once a minute. A
   failed article is not charged.
3. Show the finished article, its score and each checked claim with its verdict and sources.
4. `article_seo` checks it for free. `improve_article` fixes what it found (goal `seo`), adds an FAQ that
   cites its sources (`geo_citations`) or rewrites only disputed sentences (`accuracy`), saved as a new
   version. The first improvement is free, each after costs one generation: ask first.
5. `publish_article` to a channel of kind `blog`, only after the person approves the article, the blog and
   the time; `as_draft: true` sends it there as a draft instead. An article read from a live address goes to a
   blog only as a draft or as an update of that post. `repurpose_article` turns it into one post per
   platform for `schedule_post`. `article_results` shows how it does once published.

The person's own article: `import_article` brings it in from text (markdown or HTML) or a public address,
free within the plan's monthly limit, once they say it is theirs to publish (`is_mine`). Ask first. Every
article tool then works on its id. A post the person wrote themselves needs no `write_post`: pass their words
to `schedule_post` as they are.

To turn a page, release note or transcript into a campaign, pass its address as a `plan_article` source,
then write, repurpose and schedule as above.

## Emails, ad copy and product listings

- `write_email` writes subject lines, a preheader, the body and a call to action. `write_listing` writes a
  title, description and bullets shaped for the marketplace. `write_ad` writes copy shaped for each ad
  platform. None of them sends, posts or runs anything.
- Left without a type or marketplace, the first call to the email and listing tools returns
  `status: "confirm"`; show it, then call again with the person's choices.

## A new brand

`add_brand` reads a brand's voice, kit and facts from its website in the background, using one of the
month's voice trainings. Ask first; it appears in `list_brands` when it is added and improves over a few
minutes.

## Balance and defaults

- `balance` says what this month still allows; check it before a large request.
- When a summary shows `differs_from_brand`, offer once to keep those choices, and call `keep_defaults`
  only after the person says yes.
