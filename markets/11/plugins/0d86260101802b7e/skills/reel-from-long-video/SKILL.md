---
name: reel-from-long-video
description: Use when the user has a long video (a podcast, a lecture, a webinar, a long talk or interview) and wants short vertical reels, Shorts or TikToks cut from it, with captions and a headline. Runs reel_from_long_video, which finds the strongest self-contained moments by itself or uses the moments the user names.
---

# Reels from a long video

Follow the steps in the `video-price-and-status` skill: get the video, `get_price`, the user's yes, `reel_from_long_video`, `video_status`, the links.

## What to set

- `video`: the link or the upload code. Long files are easier to upload with `start_upload` than to share.
- `count`: how many reels, 1 to 3. Each one comes from a different moment. The price grows with the count, so ask if the user did not say.
- `seconds`: about how long each reel is, 15 to 90. The default is 40.
- `moments`: only when the user names the parts (start and end as seconds or m:ss, for example `"1:35"` to `"2:20"`). Leave it out and APIhub watches the video and picks whole-sentence moments by itself.
- `focus`: optional, one line on what the reels should be about ("the part about pricing").
- `style`: the caption style. `bold` is the default; for a calm talk use `classic`. The `video-captions` skill has the full table.
- `spoken_language`: leave it out to detect it.
- `title`: a short headline in each reel's first 3 seconds, taken from what is said. On by default.

## Handing them over

Each reel is its own video with its own id. Follow each id with `video_status` (it accepts several ids at once) and give the user every link when they are done, with one line on what each reel is about.
