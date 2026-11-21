---
name: plan-lesso-with-curriculum
description: Browse Lesso curriculum topics and create a lesson or speaking room anchored to a catalog topic through its connected MCP server. Use when a teacher plans from a CEFR course sequence.
---

# Plan with Lesso curriculum

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Ask for language and CEFR level if missing. Optionally narrow by keyword after listing.
2. Inspect tool schemas. Core tools: `list_curriculum_topics`, `get_curriculum_topic`, `create_lesson_draft`, `create_talk_room`, `generate_lesson`, `get_generation_status`, `get_credits_balance`. Never invent topic IDs.
3. List topics, then optionally fetch one for detail. Present a short pick list.
4. On choice, create a lesson or talk room with `curriculumTopicId`. Generate lesson content only if asked, with one `get_generation_status` call using `waitSeconds=60`.
5. Keep drafts private until asked to publish. Never claim success unless a tool confirmed it.

Example: Show B1 English curriculum topics about travel, then create a lesson from hotel check-in.
