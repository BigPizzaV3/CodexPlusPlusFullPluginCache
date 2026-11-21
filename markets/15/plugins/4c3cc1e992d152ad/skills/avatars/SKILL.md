---
name: avatars
description: Use when adding or replacing character portraits or choosing the default, manually active, or automated avatar.
---

# Character avatars

Find the character with `list_characters`, then call `list_portraits`. A character may have several named portraits. For a new JPEG, PNG, GIF or WebP, use `import_upload` and pass its signed ID as `avatar` to `add_portrait`. The first portrait automatically becomes the default. An additional portrait can be saved for later.

For a shapechanger, keep its everyday portrait as the default and add the wolf portrait with a distinct name. Use `list_portraits` on that character to obtain the wolf portrait’s ID. Pass the portrait ID to `update_portrait` to rename or replace the image, set `default: true` for the fallback, or set `active: true` to show that portrait now. Clear the manual selection with `active: false` on the active portrait when the user wants rules to choose again.

A manually active portrait takes priority over automation. Among matching avatar rules the later one wins, followed by the default when none match. For “show the wounded portrait when Poisoned,” use the Automations skill and the portrait ID returned for that member. A saved default or active change can affect an open game screen immediately.
