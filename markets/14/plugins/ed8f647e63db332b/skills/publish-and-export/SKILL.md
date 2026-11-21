---
name: publish-and-export
description: "Export the finished Donkey Cut video and set its publish caption and tags. Use when the user wants a file to download or post."
---

# Publish and export
set_publish edits the project's caption, tags, sound title and handle. These fields describe the intended post.
export_video renders the saved cloud project with one of these presets: original, tiktok, fast, light. Read its tool description for the preset choices. loudness masters the mix to a LUFS target for its destination, and stems adds a zip of one WAV per lane for mixing elsewhere. A returned export job is completed through get_export_status, and the card offers the finished download. render_preview and get_preview_status provide a playable preview for review. Only report a preview or export as ready when its result confirms completion.
