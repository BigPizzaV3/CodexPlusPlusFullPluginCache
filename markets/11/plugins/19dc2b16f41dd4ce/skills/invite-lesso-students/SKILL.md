---
name: invite-lesso-students
description: Invite students by email to a published Lesso lesson or Talk room and list progress through its connected MCP server. Use when a teacher wants to assign work or check who finished.
---

# Invite students in Lesso

Use the Lesso MCP server and the connected user's account. Never ask for or store passwords, bearer tokens, or API keys. When sign-in is required, let the client show the Lesso OAuth flow.

1. Confirm lesson vs speaking room and collect real student emails. Do not invent emails.
2. Inspect tool schemas. Core tools: `invite_students_to_lesson`, `list_lesson_students`, `invite_students_to_talk_room`, `list_talk_room_students`, `list_lessons`, `list_talk_rooms`, `publish_lesson`, `publish_talk_room`. Resolve IDs with list or get tools.
3. Publish first only with explicit consent if needed. Invite only when emails are provided and the teacher asks.
4. For progress, use the list-students tools and summarize without inventing completion data.
5. Never claim invites were sent unless a tool confirmed it.

Example: Invite alex@school.edu and sam@school.edu to my published travel lesson and tell me who opened it.
