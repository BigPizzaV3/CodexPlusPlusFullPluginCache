---
name: get-started
description: Help a new JSON2Video user make their first video from ChatGPT, starting from a featured template or a short description of the video they want.
---

# Get started with JSON2Video

1. Ask what video the user wants: topic, format (vertical for Reels/Shorts/TikTok, horizontal for YouTube), length and any text, images or voiceover.
2. If a featured template fits, call `list_featured_templates`, then `get_template` to read its variables, fill them from the user's request and call `render_video` with the template id and variables.
3. Otherwise build a movie JSON: call `get_help` (and `get_example` for a close example), check it with `validate_movie`, then call `render_video`.
4. `render_video` returns the video URL when the render finishes. If it is still rendering, call `check_status` with the project id until it is done.
5. Share the video URL. Offer one change at a time (text, voice, music, length) and render again.

Use `get_account` when the user asks about their remaining credits. Do not invent media URLs: use URLs the user gives, files from `media_list`, or AI-generated images and voices described in the movie JSON.
