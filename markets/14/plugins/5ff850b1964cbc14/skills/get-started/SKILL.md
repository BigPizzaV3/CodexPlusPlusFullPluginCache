---
name: get-started
description: Use when someone starts using Davnai in ChatGPT, asks what Davnai can do, or wants to turn a video into posts, Shorts or edits.
---

# Getting started with Davnai

Davnai turns one video into finished edits, Shorts and social posts, and schedules them. Every tool acts for the one signed-in person and follows their Davnai plan.

## First steps

1. Call `list_videos` to see what the person already has. If they have none, explain they can upload a video at https://davnai.com/library, or call `upload_link` to give them an upload link.
2. Call `list_accounts` to see which social accounts are connected. If none are, tell them to connect accounts at https://davnai.com/social before scheduling posts.
3. Ask what they want to do with a video, then pick a tool:
   - Plan a full edit: `ask_director`, then `get_director_plan`. The person approves the plan with `approve_director_plan`.
   - Shorts: `list_short_moments`, then `make_shorts` (or `find_shorts` to look for more).
   - Posts in their voice: `write_posts`. To put them on the calendar: `create_posts`.
   - Captions, resizing or joining: `add_captions`, `resize_video`, `join_videos`.
   - Results and comments: `get_results`, `list_comments`.

## Rules

- Never say a post was published. Posts added from ChatGPT wait in Davnai until the person approves them; say so plainly.
- Before any tool that schedules, approves, cancels, replies or changes a setting, confirm the details with the person.
- When a plan limit is reached, the tool says what ran out and when it resets. Tell the person and don't retry.
- Long jobs (Shorts, edits, drawings) run in the background. Use `job_status` to check on them instead of starting them again.
- Write "Davnai", never "Davnai AI".
