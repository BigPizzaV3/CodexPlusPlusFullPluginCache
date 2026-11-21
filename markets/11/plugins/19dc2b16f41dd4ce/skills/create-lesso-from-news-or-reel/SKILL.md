---
name: create-lesso-from-news-or-reel
description: Seed a Lesso lesson or speaking room from a news URL or short social video URL through its connected MCP server. Use when a teacher pastes a news or Reel/TikTok link.
---

# Create Lesso content from news or video

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Confirm news vs Reel/TikTok URL and whether the teacher wants a lesson or speaking room. Capture level and language when given.
2. Inspect tool schemas. Core tools: `create_lesson_from_news`, `create_lesson_from_reel`, `create_talk_room_from_news`, `generate_lesson`, `get_generation_status`, `get_credits_balance`, `publish_lesson`, `publish_talk_room`.
3. Optionally call `get_credits_balance` before Reel transcription or generation. If Reel returns pending, wait and call again with the same URL. Do not invent transcript text.
4. Generate lesson content only if asked, with one `get_generation_status` call using `waitSeconds=60`. Keep unpublished until asked.
5. Never claim success unless a tool confirmed it.

Example: Turn this news URL into a B1 English lesson draft in Lesso, then generate the content.
