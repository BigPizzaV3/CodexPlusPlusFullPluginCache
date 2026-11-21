---
name: create-lesso-lesson
description: Create, generate, and optionally publish editable language lessons in Lesso through its connected MCP server. Use when a teacher asks ChatGPT to make a Lesso lesson from a topic, goal, curriculum topic, or student need.
---

# Create a Lesso lesson

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Capture requirements: teaching language, level, topic/outcome, duration, audience, and any curriculum topic. Ask one short question only if a missing detail blocks a useful lesson; otherwise choose reasonable defaults and disclose them.
2. Inspect tool schemas from the connected server. Core tools: `create_lesson_draft`, `generate_lesson`, `get_generation_status`, `get_lesson`, `publish_lesson`, `unpublish_lesson`, `list_lessons`, `get_credits_balance`, `list_curriculum_topics`. Never invent lesson IDs or URLs.
3. Optionally call `get_credits_balance` before generation. Use `create_lesson_draft` (pass `curriculumTopicId` when anchoring to catalog). Then, when the teacher wants full content, call `generate_lesson`.
4. Wait for generation with one `get_generation_status` call using `waitSeconds=60` (hard max). Do not poll in a loop. If `timedOut`, report that generation is still running and suggest checking `get_lesson` later. Only claim content is ready when `contentReady` is true.
5. Keep lessons private. Call `publish_lesson` only on explicit request. Use `unpublish_lesson` only on explicit request.
6. Report briefly: title, level, block outline or readiness, workspace URL if returned, public URL only after publish, and any credit notes. Never say a lesson was saved or published unless a tool confirmed it.

Example: Create a 50-minute B1 English lesson in Lesso about asking for help after a flat tire, generate the content, and give me the editor link.
