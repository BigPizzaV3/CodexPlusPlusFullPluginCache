---
name: create-lesso-speaking-room
description: Create and publish Lesso Teacher Talk speaking rooms through its connected MCP server. Use when a teacher asks ChatGPT to make a role-play, AI-teacher practice, or discussion room from a brief, lesson, or news link.
---

# Create a Lesso speaking room

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Capture requirements: teaching language, CEFR band (A2/B1/B2/C1), situation, student and partner roles, conversation vs AI-teacher (`teaching_phrase`), and any source lesson ID or news URL. Ask one short question only if a missing detail blocks a useful room.
2. Inspect tool schemas. Core tools: `create_talk_room`, `create_talk_room_from_lesson`, `create_talk_room_from_news`, `list_talk_rooms`, `publish_talk_room`, `unpublish_talk_room`, `invite_students_to_talk_room`, `get_credits_balance`. Never invent room IDs or share URLs.
3. Optionally call `get_credits_balance` before AI-teacher creates. Create with the matching tool for brief, lesson, or news.
4. Keep rooms private. Call `publish_talk_room` or invite tools only on explicit request.
5. Report title, format, lobby URL, and share URL only after publish succeeds. Never claim success unless a tool confirmed it.

Example: Create a B1 English speaking room where the student is a hotel guest and the AI is the receptionist, then publish a share link.
