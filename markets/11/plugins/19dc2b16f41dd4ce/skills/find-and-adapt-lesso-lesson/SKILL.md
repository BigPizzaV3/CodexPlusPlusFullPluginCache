---
name: find-and-adapt-lesso-lesson
description: Search Lesso Explore, copy a community lesson, or adapt a lesson for a new level or language through its connected MCP server. Use when a teacher wants something like an existing lesson to customize.
---

# Find and adapt a Lesso lesson

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Clarify whether to search Explore, copy a lesson, or adapt an existing lesson for a new level, language, or age.
2. Inspect tool schemas. Core tools: `search_explore`, `copy_explore_lesson`, `adapt_lesson`, `update_lesson`, `regenerate_block`, `generate_lesson`, `get_generation_status`, `get_lesson`, `list_lessons`, `get_credits_balance`. Never invent lesson IDs.
3. Search and shortlist results. Copy only on explicit request. Adapt with `adapt_lesson`, then generate if asked with one `get_generation_status` call using `waitSeconds=60`.
4. Keep results private until the teacher asks to publish. Report only URLs returned by tools.
5. Never claim success unless a tool confirmed it.

Example: Find a B1 cafe English lesson on Explore, copy it, and adapt it for A2 teens.
