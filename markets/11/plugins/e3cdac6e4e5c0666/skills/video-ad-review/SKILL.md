---
name: video-ad-review
description: Review a short vertical video ad (TikTok, Instagram Reels, YouTube Shorts, X, Snapchat, Facebook) by its public link with Quelta. Use when the user shares a link to a video ad and asks to analyze, score, review or improve it, wants fixes before launching it, or asks about their past Quelta analyses or remaining checks.
---

# Review a video ad with Quelta

Explicit user instructions take priority over these guidelines.

## Inputs

- **Link** (required): a public link to one video on TikTok, Instagram, YouTube Shorts, X, Snapchat or Facebook. If there is no link, ask for one. For a file or a private video, explain that Quelta works with public links and that the file can be uploaded at https://quelta.ai; it will then appear in `list_my_analyses`.
- **Platform**: where the ad will run. If the user does not say, leave it empty and Quelta guesses it from the link.
- **Market**: a two-letter country code such as US, GB, DE or FR. Use the market the user names. If none is named, use US and say so in the answer.
- **Audience**: `gen-z` (13–29), `millennials` (29–45), `gen-x` (45–61), `boomers` (61–80) or `any`. Map the user's words to one of these. If none is named, use `any`.
- **Language** of the report: the user's language when it is en, fr, es, de, kk or ru, otherwise en.

Do not ask for anything else. Do not ask questions when the defaults above are enough.

## Steps

1. Call `analyze_video_ad` with the inputs.
2. If the result has status `processing`, call `get_analysis` with its `analysis_id` until it is `done` or `failed`. Tell the user it takes about a minute.
3. Present the preliminary result:
   - the score range and what it means for this platform and market;
   - the first 3 seconds: what works and what fails;
   - the measured problems, most important first;
   - the link to the full report.
4. Offer the full check: the exact score, category scores, every issue with timecodes and prioritized fixes.

## Full check

`upgrade_to_full_review` uses one full check from the user's Quelta balance. Before calling it, tell the user this and wait for a clear yes in the current conversation. A request like "run the full check" counts as that yes. Calling it again for the same analysis does not use another check.

Present the full result in this order:
1. score and the weakest categories;
2. fixes in priority order, each with its timecode;
3. what already works, so the user keeps it.

If the balance is empty, say that the full check is unavailable for this account and that the preliminary check still works. Do not suggest purchases.

## Rules

- Report only what the tool returned. Do not invent scores, issues, timecodes or fixes, and do not guess at results from the title or link of the video.
- If a check fails, quote the reason from the tool and suggest the fix it gives, for example another public link.
- Quelta analyzes videos only. If the user asks to create, edit or publish a video, say that Quelta does not do this.
- To compare several ads, run one check per link, then compare the results side by side.
- For history, use `list_my_analyses`, then `get_analysis` for the one the user picks. For remaining checks, use `get_account`.
