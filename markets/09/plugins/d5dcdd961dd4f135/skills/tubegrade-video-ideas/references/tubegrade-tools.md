# TubeGrade tool notes

Shared by every TubeGrade skill. Source of truth: `apps/plugin/shared/` —
`deploy/build_release.py` copies it into each skill's `references/`.

## Inputs
- Channel tools accept a channel id (`UC…`), an `@handle`, or a channel URL.
  Video tools accept an 11-character id or any YouTube video URL. Resolving a
  handle or URL is free and happens before any charge, so pass what the user gave.
- Link videos as `https://www.youtube.com/watch?v=<id>`. Channel results from
  `tubegrade_similar_channels` / `tubegrade_rankings` carry a `tubegrade_url`
  (the channel's public stats page) — use it when pointing at a channel.

## Credits
Every research call spends credits from the user's TubeGrade balance; the
cost is charged when the call runs, even if YouTube returns nothing.
`tubegrade_balance` is free — call it first when a plan needs more than
~40 credits, and say what a plan will cost before running it.

| Tool | Credits | What it gives |
|---|---|---|
| `tubegrade_balance` | 0 | Current balance |
| `tubegrade_expand_keywords` | 1 | YouTube autocomplete phrasings for a seed (no volumes) |
| `tubegrade_rankings` | 1 | Weekly fastest-growing / breakout / most-subscribed channels, worldwide or by country |
| `tubegrade_my_competitors` | 2 | The user's tracked competitors with 7/30-day growth |
| `tubegrade_channel_videos` | 3 | A channel's recent / popular / shorts uploads with views |
| `tubegrade_get_channel` | 5 | Channel stats, average views, plus `growth` history when tracked |
| `tubegrade_get_video` | 5 | Video stats, plus `growth` history when tracked |
| `tubegrade_search_videos` | 5 | Live YouTube search (filters: long/short, upload window, duration) with `outlierRatio` per result |
| `tubegrade_suggested_videos` | 5 | YouTube's own "up next" rail for a video |
| `tubegrade_get_comments` | 5 | Up to 100 top-level comments (top or newest) |
| `tubegrade_viral_formats` | 5 | Proven title or thumbnail FORMATS with examples and lifecycle state |
| `tubegrade_similar_channels` | 5 | Same-topic channels of similar size |
| `tubegrade_get_transcript` | 10 | One video's full `[MM:SS]` transcript |
| `tubegrade_get_channel_outliers` | 10 | One channel's videos that beat its own baseline |
| `tubegrade_find_outliers` | 10 | Semantic search over TubeGrade's breakout-video corpus |
| `tubegrade_find_similar_thumbnails` | 20 | Videos whose thumbnail + title look/read alike |
| `tubegrade_thumbnails` | 1 per video | Actual thumbnail images (≤10, any channels) |
| `tubegrade_channel_thumbnails` | 1 per image | One channel's thumbnails as images (≤30) |
| `tubegrade_channel_transcripts` | 10 per video | Bulk transcripts for one channel (≤50) |
| `tubegrade_bookmark`, `tubegrade_list_bookmarks`, `tubegrade_track_competitor`, `tubegrade_untrack_competitor` | 0 | Account actions — only when the user asks |

Bulk tools bill per item actually returned. Ask before any single call over
30 credits (e.g. more than 3 bulk transcripts).

**Stay inside the skill's budget.** Don't re-fetch what a result already
gave you: videos from search, outliers or channel lists already carry their
views and dates — never call `tubegrade_get_video` on them one by one. If the
work truly needs more than the stated budget, say what and why, and ask.

## What each tool returns
Field names as the server sends them (captured from the live server
2026-10-02). Naming differs between tools (`videoId` vs `video_id`) — read the
one the tool gives. Every paid tool also returns `credits_remaining`.

| Tool | Main fields |
|---|---|
| `tubegrade_get_channel` | `channel`: `title`, `handle`, `subscriber_count`, `view_count`, `video_count`, `avg_views`, `upload_frequency`, `avg_video_length`, `country`, `joined_date`, `description`, `categories`; optional `growth` |
| `tubegrade_get_video` | `video`: `title`, `channel_id`, `views`, `likes`, `comment_count`, `duration`, `published_at`, `tags`, `category`; optional `growth` |
| `growth` (both above) | `period`, `metrics`, `gained_note`, `series[]`: `period`, `metrics{}`, `gained{}` |
| `tubegrade_search_videos` | `results[]`: `videoId`, `title`, `views`, `duration`, `publishedTime`, `channelTitle`, `channelHandle`, `subscriberCount`, `subscriberCountText`, `channelAvgViews`, `outlierRatio`, `uploadFrequency` |
| `tubegrade_suggested_videos` | `results[]`: `videoId`, `title`, `viewCount`, `publishedTime`, `channel{}`, `subscriberCountText`, `channelAvgViews`, `outlierRatio` |
| `tubegrade_find_outliers` | `outliers[]`: `video_id`, `title`, `views`, `published_at`, `outlier_ratio`, `relevance` (0–1) |
| `tubegrade_get_channel_outliers` | `outliers[]`: `video_id`, `title`, `views`, `likes`, `comment_count`, `published_at`, `outlier_ratio` |
| `tubegrade_find_similar_thumbnails` | `results[]`: `videoId`, `title`, `channelTitle`, `viewsRaw`, `publishedAt`, `outlierScore`, `subscriberCount`, `avgViews`; or `status: "indexing"` |
| `tubegrade_channel_videos` | `videos[]`: `videoId`, `title`, `views`, `duration`, `publishedTime` |
| `tubegrade_get_transcript` | `transcript` — text, one `[MM:SS]` line per caption |
| `tubegrade_channel_transcripts` | `transcripts[]`: `video_id`, `title`, `transcript` or `error` |
| `tubegrade_get_comments` | `totalComments`, `comments[]`: `author` (display name), `isChannelOwner`, `text`, `likeCount`, `replyCount`, `publishedAt` |
| `tubegrade_expand_keywords` | `keywords[]` — phrases only |
| `tubegrade_viral_formats` | `formats[]`: `label`, `template`, `description`, `state`, `score`, `hit_rate`, `member_count`, `new_members_14d`, `examples[]`, `trend[]`; optional `note` |
| `tubegrade_similar_channels` | `channel{}` (the seed), `similar_channels[]`: `title`, `handle`, `subscribers`, `subscriberCountText`, `tubegrade_url` |
| `tubegrade_rankings` | `week_start`, `tracked_channels`, `entries[]`: `rank`, `previous_rank`, `title`, `handle`, `country`, `subscriberCountText`, `gained_30d_text`, `gained_pct`, `tubegrade_url`; `list_url` |
| `tubegrade_thumbnails`, `tubegrade_channel_thumbnails` | A summary, then per video a text line (id, title, URL) followed by the image |
| `tubegrade_my_competitors` | `competitors[]`: `title`, `handle`, `subscriber_count`, `avg_views`, `subs_delta_7d`, `subs_delta_30d`, `views_delta_7d`, `views_delta_30d` |
| `tubegrade_bookmark` | `add`/`remove` → result flags |
| `tubegrade_list_bookmarks` | `show: folders` → `folders[]`; `show: videos` → `videos[]` |
| `tubegrade_balance` | `credits_remaining` |

## Reading the numbers
- **Outlier ratio** = a video's views ÷ its channel's average views. 3.0 means
  three times what that channel usually gets. It is the core TubeGrade signal:
  prefer it over raw views when judging what "worked".
- Tiny channels make ratios jumpy — a 40x on a channel averaging 200 views is
  weak evidence. Weigh ratio together with views and channel size.
- In `tubegrade_suggested_videos`, the rail mixes in old catalog videos whose
  lifetime views are compared with recent averages, so ratios in the hundreds
  mean "back-catalog hit", not a fresh breakout. Check `publishedTime`.
- `tubegrade_find_outliers` searches TubeGrade's own corpus (tens of thousands
  of breakout videos, not all of YouTube) by meaning, not exact words. Use
  `days` for recency and `min_ratio` (e.g. 3) for only big breakouts. A thin
  result means thin coverage — fall back to `tubegrade_search_videos`, whose
  results also carry `outlierRatio`.
- `tubegrade_viral_formats` patterns are mined across all niches; omit
  `niche` and judge fit yourself. `state` (emerging / rising / peaking /
  declining) says where a format is in its life — rising formats are the
  better bet for a new video.
- **Growth blocks**: `gained` is the change per period; where readings are
  several periods apart it is the per-period average — multiply by the gap for
  a total. Channels and videos TubeGrade hasn't tracked have no `growth` key.
- Subscriber counts are YouTube's rounded public figures; quote
  `subscriberCountText` / `gained_30d_text` rather than inventing precision.
- `tubegrade_expand_keywords` has no search volumes or difficulty — never
  present its order as demand data.

## Images
- `tubegrade_thumbnails` / `tubegrade_channel_thumbnails` return the images
  plus each thumbnail's URL. **Some assistants don't pass tool images to the
  model.** Describe a thumbnail only if the picture is really in front of
  you: faces and expressions, on-image text word for word, colours, focal
  object, layout. If you only received text, say "I can't see the thumbnail
  image here" and give its link — never guess what is in an image.

## Errors
- "Not enough TubeGrade credits": say how many the call needed and the
  balance, then offer a smaller version (fewer items, a cheaper tool). Don't
  retry the same call.
- `tubegrade_find_similar_thumbnails` may answer `status: "indexing"` for a new
  video — wait ~15 seconds and call once more.
- `tubegrade_similar_channels` refuses (uncharged) for channels without a
  fingerprint yet; use `tubegrade_suggested_videos` on one of its videos instead.
- Competitor tracking is only available on accounts that include it; if
  `tubegrade_track_competitor` says so, carry on with the research tools.
- No captions → the transcript call errors; pick another video.

## Honesty rules
- Every number you state must come from a tool result in this conversation.
  Name the video or channel it belongs to.
- **Every video you cite is a link**: write it as
  `[title](https://www.youtube.com/watch?v=<id>)` using the id from the tool
  result. A cited video without a link is incomplete.
- Transcripts may be in another language. Quote the lines you rely on in
  English translation, keep their `[MM:SS]`, and say the original language.
- Write tight: lead with the answer, then the evidence. Aim for 400–700 words
  unless the user asks for more.
- Separate evidence ("this video did 6.2x its channel average") from your
  judgement ("the curiosity gap is likely why"). Label guesses as guesses.
- Say what you didn't check and where coverage was thin.
- Never present a competitor's video, title, script or thumbnail as something
  to copy. Extract the mechanism and make it the user's own.
- Contact details for channels are never available — don't look for them.

## Before you send — check every time
1. Every video title you wrote is a markdown link `[title](https://www.youtube.com/watch?v=<id>)` — including the user's own videos.
2. Every number came from a tool result in this conversation.
3. You stayed inside the skill's credit budget (or asked first).
4. You described no image you couldn't actually see.
