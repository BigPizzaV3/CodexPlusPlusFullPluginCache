---
name: get-started
description: Start a MorphaReels video project, make bulk edits to it, and hand the person a link to finish it in the MorphaReels editor.
---

MorphaReels builds short vertical videos (Reels, TikToks, Shorts) from layers: text, shapes, images and video, animated on a timeline.

1. For a new video, call create_project. For an existing one, call list_projects, then open_project, then describe_video and inspect_layers before changing anything.
2. Refer to projects by their name, never by id.
3. Use the tools for work that would take many clicks by hand: many layers at once, staggered animation, versions of one video with different text.
4. Call save_version at the end of each set of changes.
5. Finish by giving the person the project's editorUrl. They can adjust anything by hand there and download the MP4.
