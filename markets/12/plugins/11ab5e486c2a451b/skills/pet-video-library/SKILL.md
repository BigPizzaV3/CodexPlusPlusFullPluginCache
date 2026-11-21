---
name: pet-video-library
description: Use when the user wants to find, check, save or delete the pet clips they made ('show my pet clips', 'is my clip ready?', 'delete my Boopreel clips'). Lists recent clips, their status and pages, and deletes them.
---

Boopreel keeps each person's clips for 30 days. Each ready clip has its own page, where the MP4 is saved or shared to TikTok, Instagram Reels or YouTube Shorts. The user's own instructions come first.

## Flow

1. `list_my_clips` returns the user's recent `clips` from the last 30 days.
2. `get_pet_clip` returns one clip's `status` and, once it is ready, its `watch_url`, the page where the clip is saved or shared.
3. `delete_pet_clips` deletes one clip (`clip_id`) or all of them (`all`), with their photos and pages, when the user asks.

## Scope

- Clips are AI-generated, carry a small "Boopreel · AI" mark and are deleted after 30 days.
