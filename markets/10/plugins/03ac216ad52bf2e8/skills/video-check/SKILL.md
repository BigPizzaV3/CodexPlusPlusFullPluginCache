---
name: video-check
description: Score the opening of the user's own video with the Hookest Virality Predictor before they post it, and explain what holds it back. Use when the user asks to score, rate, review or check their video, Reel, TikTok or Short, asks if it will go viral, or asks how to improve their first 3 seconds.
---

# Video check with the Hookest Virality Predictor

Goal: get the user an official Hookest score (0 to 100) for the opening of
their video, then turn the result into concrete fixes.

## What it can and cannot do

- It scores the OPENING of a video FILE against proven viral hooks. It does not
  estimate view counts. If asked for views, say so and offer the score.
- It needs a file, not a link. For an Instagram or TikTok link, ask the user to
  save the video and attach the file, or upload it on Hookest.
- `get_account` shows the plan and how many analyses are left. If the tool
  says the feature is not available with the current account, tell the user
  that plainly. Do not quote prices or offers.

## Steps

1. **Video attached in the chat, and you can read it with code.**
   Read its duration and size, then call `upload_prediction_video` with
   `duration_seconds`, `bytes` and the user's `language`. It reserves one
   analysis and returns a one-time upload URL on files.hookest.com and a ready
   `curl` command. Upload the attached file to that URL unchanged, then call
   `run_prediction` with the `prediction_id`.
   - The upload takes mp4 only, up to 32 seconds and 40 MB. Only the opening is
     scored, so a longer video can be trimmed to its first 30 seconds first.

2. **No attachment, the file cannot be read, or files.hookest.com cannot be
   reached.** Call `start_prediction` and give the user its `upload_url`, a
   Hookest page where they upload the video while signed in. When they say it
   is done, call `get_prediction`.

3. **Waiting.** If the status is `queued` or `running`, wait a few seconds and
   call `get_prediction` with the same id until it finishes.

## Output

- The score and its band, exactly as returned
- What holds the opening back, in the tool's own terms, then 2 or 3 concrete
  edits for the first seconds (cut, text on screen, first line, first visual)
- If it fits, 2 or 3 real library hooks from `find_hooks` in the same niche to
  borrow an opening from, with their Hookest links

If the user wants to compare with earlier videos, call `list_predictions` and
`get_prediction` with the ids they mean.
