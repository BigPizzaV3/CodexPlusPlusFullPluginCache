---
name: live-quizzes-and-polls
description: Use when the user asks about interactive live streams on playout.video: live quizzes, polls or games viewers play on their phones or in chat, and the AI host voice.
---

# Live Quizzes and Polls

Quizzes and polls run from the Live Studio in the playout.video app. This skill explains how and helps plan them; it does not start one from ChatGPT.

1. docs_search with the user's topic ("live quiz", "live poll", "phone answers chat", "player limits", "AI host voice"), then docs_get the best match.
2. Explain the steps from the article: setting up the quiz or poll, how viewers join (QR code on their phones or answers in chat), and the limits that apply to their plan.
3. Help write the content if asked: questions, answer options, poll ideas that fit their channel.
4. For an on-air graphic to go with it (Channel plan and up), graphic_guide first, then graphic_write, and graphic_attach to a Live Studio scene after the user confirms.

Do not say a quiz or poll was started: the user starts it in the Live Studio.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
