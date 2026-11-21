---
name: post-performance
description: Report how the user's meeloop posts and stories are doing (likes, comments, reposts, quotes, views, bookmarks, story viewers). Use when the user asks about stats, reach, engagement or who saw a story on meeloop.
---

Explicit instructions from the user override this skill.

1. Identify the posts. If the user doesn't give an id, call `list_my_posts`
   and pick the posts they described (for example the newest, or one that
   mentions a topic). If it's ambiguous, ask.
2. Call `get_post_analytics` for each post. Report only numbers the tool
   returned. Don't estimate reach, rank or trends you can't see.
3. For several posts, show a compact table: caption snippet, posted date,
   likes, comments, reposts, quotes, views, bookmarks. Point out the one that
   did best and say which metric you used.
4. For stories, call `get_story_viewers` with the story id. Show the viewer
   count and, if the user wants them, the viewers' names and usernames.
   Expired stories (older than 24 hours) have no viewer list.

Only the user's own posts and stories have stats. Don't change any posts
while reporting.
