---
name: tiktok-content-ideas
description: Suggest TikTok video ideas for a creator, based on which of their own recent public videos got the most views and how each compares with their usual. Use when the user asks what to post on TikTok, for content ideas, video ideas, a content plan for the week, or "what should I post next" for a named TikTok username. Also use when the user asks what is working or trending in their niche this week. Reads the account with get_tiktok_script_and_hook_inputs, or the niche with get_tiktok_niche_trends, and gives each idea with its reason, a hook and a format. Not for other platforms, and it never promises views.
---

Use this skill when the user wants ideas for what to post on TikTok.

## Steps

1. Get the creator's public TikTok username. If none is given, ask once. With no username, ask for their niche in a few words (for example skincare, gym, meal prep), call `get_tiktok_niche_trends` once with it, and say the ideas come from the niche, not from their account.
2. With a username, call `get_tiktok_script_and_hook_inputs` once. If its result has `niche_trends`, use those posts as the niche side. If it has none and the user names their niche, call `get_tiktok_niche_trends` once with it.
3. From `top_videos`, name the 2 or 3 topics or formats whose `times_typical` is above 1, with the real numbers (`views`, `times_typical`). From `lower_videos`, name what did worse. Only say what the data shows; with few videos, say the sample is small.
4. From the niche posts (`niche_trends`, or `top_posts` and `patterns` of `get_tiktok_niche_trends`): say which window they are from (`window_days`; `get_tiktok_niche_trends` also gives `window_note`), name 1 or 2 topics or formats the niche is posting now, and quote the counted patterns as counts (for example "6 of 40 posts open with a question"). Link each post you mention to its TikTok page. If the tool answers `unknown_niche`, `niche_needed` or `no_data`, say so with its `message` and carry on without the niche side.
5. Give the number of ideas asked for (5 if not said), in this shape:
   - **Idea:** one sentence on what the video is.
   - **Why:** which of the account's own videos it builds on, with that video's real views; or which niche post it builds on, with its link.
   - **Hook:** one opening line, with the hook type from `method.hook_types`.
   - **Format:** how to film it in a few words (talking to camera, voiceover, demo, list).
6. Mix the ideas: most build on what already did well on the account, and one or two take a topic or format from the niche posts. Label those as tests.
7. If the user asked for a plan, lay the ideas over the days using `posting_rhythm.posts_per_week` as the pace the account already keeps. Do not tell them to post more often than they do unless they ask.
8. Offer to turn any idea into a full script.
9. End with one plain link, once: the link from `get_tiktok_script_and_hook_inputs` when it was called, otherwise the link from `get_tiktok_niche_trends`.

## Rules

- Use only real numbers from the tool result. Never invent views or facts about the account.
- Never promise or predict views or growth. An idea is a suggestion to test.
- The tool reads captions and public view counts, not what was said in the videos, watch time or audience details.
- Niche posts belong to other creators and are a stored sample that is refreshed weekly, not TikTok's own trending list. Use the idea, never their words, and repeat the tool's note when it says the posts may come from an older list.
- If the tool cannot read the account, say so in one sentence using its `message` and continue from the niche the user describes.
- Explicit instructions from the user come before these guidelines.
