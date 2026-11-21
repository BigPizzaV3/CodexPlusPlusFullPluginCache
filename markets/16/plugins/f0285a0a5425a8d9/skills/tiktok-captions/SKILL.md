---
name: tiktok-captions
description: Write TikTok captions, the text under a video, with a clear first line and up to five relevant hashtags. Use when the user asks for a TikTok caption, a video description for TikTok, a rewrite of a caption, or hashtags to go with a caption. Follows a three-part formula and can match the style of the creator's own better videos. Not for subtitles or on-screen text, and it never promises reach.
---

Use this skill when the user wants the caption (description) for a TikTok video. If they mean subtitles of the spoken words, say this skill writes the text under the video and ask which they need.

## The formula

1. **Line one: what the video gives.** Everyday words, one sentence, no hashtags. Viewers see the start of a caption and tap to read the rest, so the first line does the job.
2. **Line two (optional): one detail or a question** that gives a viewer a reason to comment.
3. **Last line: up to five hashtags** that say what the video is.

## Steps

1. Ask what the video shows if the user has not said. The caption must describe the same topic as the video.
2. If the user gives a TikTok username and wants the caption in their own style, call `get_tiktok_script_and_hook_inputs` once and read the captions of `top_videos` for tone, length and the hashtags in `hashtags_used`. Otherwise skip this.
3. For hashtags, start with what the video is: one or two tags that name its topic in plain words. If the user names their niche (or it is clear from the video), call `get_tiktok_trending_hashtags` once with it and add a tag from its `hashtags` only if it truly fits the video. Say those counts come from a stored weekly sample of public posts, not TikTok's own trending list.
4. Write 3 caption options unless the user asked for another number. Keep each short.
5. If a tool was called, end with the plain link from its result, once.

## Rules

- At most five hashtags. Do not add #fyp, #foryou or #foryoupage: TikTok says they work just like all other hashtags.
- Never write a caption that is only hashtags, and never one about a different topic than the video.
- No promise of reach or views.
- Use the phrase a viewer would search for, in plain words, if it fits naturally. Do not stuff keywords.
- Keep the creator's language and tone.
- Explicit instructions from the user come before these guidelines.
