---
name: reveals
description: Use for saving an image, video or sound as a reveal, showing saved media on the game screen, or clearing the active reveal.
---

# Reveals

For “show a reveal image of the Elder Red Dragon,” search `list_reveals` in the chosen campaign. Pick the matching image from the accessible results. If several match, use the returned names and media types to clarify which one the user means. When the requested image is missing, ask for the intended artwork or use an attachment the user already supplied.

To save new media, pass the actual file to `import_upload`, then call `create_reveal` with its signed ID as `file` and a recognizable name. Reveals support JPEG, PNG, GIF, WebP, MP4, WebM, Ogg video, MP3, Ogg audio and WAV. Saving adds it to the reveal pile. For “upload this and show it,” use the ID returned by `create_reveal` directly in `set_active_reveal`. For “save it for later,” finish after creation.

When asked to show it, call `set_active_reveal` with the campaign and returned reveal ID. To dismiss it, explicitly send `reveal_id: null`. Owners may show any reveal in the campaign. With player reveal activation enabled, a player can show their own uploads and dismiss the active reveal. Report which reveal was selected. `get_game_screen` reports whether a screen is connected.
