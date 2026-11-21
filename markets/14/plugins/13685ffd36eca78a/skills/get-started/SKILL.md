---
name: get-started
description: Set up Lumadeos after installing it — confirm the connected account, show its processing minutes and recent videos, and suggest a first task.
---

# Get started with Lumadeos

Use this skill right after the Lumadeos plugin is installed, or when the user asks what Lumadeos can do with their account.

1. Call `my_limits` and tell the user which Lumadeos plan is connected and how many processing minutes are left this month.
2. Call `video_list_jobs` with `limit` 5. Summarize the most recent videos: title, status (completed, processing or failed) and duration. If there are none, say so.
3. Offer a first task that fits what you found:
   - no videos yet: process a recording from a link they share (a direct file link, Dropbox, or a Google Drive file shared with anyone who has the link);
   - a finished video: get download links, tighten the cut, burn in captions, blur private information, or cut vertical reels;
   - a failed video: look at the error in `video_get_job` and offer `video_retry_job`.
4. Mention two facts so there are no surprises: processing a new video uses minutes from the plan, while edits and reels don't; download links expire after 24 hours.

Don't start processing, edits or deletions during setup — wait until the user asks for a specific task.
