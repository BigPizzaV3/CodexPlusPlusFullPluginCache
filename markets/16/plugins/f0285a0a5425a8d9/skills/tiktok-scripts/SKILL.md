---
name: tiktok-scripts
description: Write ready-to-film TikTok video scripts for a creator, built from what already worked on their own public TikTok account. Use when the user asks for a TikTok script, a video script for TikTok, a script "like my most-viewed videos", or wants a script written for a named TikTok username. Reads the account's recent public videos with get_tiktok_script_and_hook_inputs, adds what the creator's niche is posting this week when that is known, then writes each script with a hook, short beats, a payoff and a caption. Not for other platforms, and it never promises views.
---

Use this skill when the user wants one or more TikTok scripts.

## What you need

1. The creator's public TikTok username. If the user has not given one, ask for it once. If they do not want to share one, write from the topic they give and say the scripts are not based on their account.
2. What the next video is about, if they have a topic in mind. If they do not, pick topics from the account's better videos (step 2).

## Steps

1. Call `get_tiktok_script_and_hook_inputs` once with the username. Do not call it again for the same username in this conversation.
2. Read `top_videos` (the videos with the most views; `times_typical` shows how each compares with the account's `typical_views`) and `lower_videos`. Note for each top video: the topic, the opening line, and which of the hook types in `method.hook_types` it is closest to. Say in one or two lines what the top videos have in common that the lower ones do not. Only say what the data shows.
3. If the result has `niche_trends`: these are a few recent public posts from other creators in the same niche (a stored weekly sample). Name one topic or format from them that fits this account, and build at least one script on it. Say which post the idea came from, with its link, and say which window it is from (`window_days`). If `niche_trends` is missing, skip this step; if the user names their niche, you may call `get_tiktok_niche_trends` once with it.
4. Write the payoff first: one sentence on what the viewer gets by the end. The hook is a short promise of that payoff.
5. Write each script in this shape:
   - **Hook (0 to 3 seconds):** what is said, what the first frame shows, and the short on-screen text. All three make the same promise. One line that takes about three seconds or less to say. No greeting, no "hey guys", no name intro.
   - **Body:** 3 to 5 short beats that deliver the payoff, one idea per beat, in the creator's own words and tone as seen in their captions.
   - **Payoff:** keep the promise the hook made.
   - **Caption:** one plain sentence on what the video gives, then up to five hashtags that say what the video is.
6. Give two hook options per script, using two different hook types, and name the type next to each.
7. Unless the user asked for another number, write 3 scripts. Most build on the account's own top videos; one may build on a niche post from step 3, labelled as a test.
8. End with the plain link from the tool result, once. If two tools were called, show only the link from `get_tiktok_script_and_hook_inputs`.

## Rules

- Use only real numbers from the tool result. Never invent views, results or facts about the account.
- Never promise or predict views, followers or any result. Past videos doing well does not mean the next one will.
- The tool gives captions (the text under each video), not what was said inside the video. Do not claim to know what was said.
- Posts in `niche_trends` belong to other creators. Use the idea, never their words: do not copy a caption or opening line, and never present those posts as this account's own.
- The niche posts are a stored sample, not TikTok's own trending list. Say "a stored sample of public posts", and say when the window is wider than 7 days.
- If the tool answers `not_found`, `private`, `no_videos`, `rate_limited`, `paused`, `off`, `busy` or `unavailable`, tell the user in one plain sentence what happened, using the tool's `message`, and offer to write from a topic they describe instead. Do not make up account data.
- Keep the creator's language. If their captions are not in English, write the script in their language unless they ask otherwise.
- Explicit instructions from the user (length, tone, topic, number of scripts) come before these guidelines.
