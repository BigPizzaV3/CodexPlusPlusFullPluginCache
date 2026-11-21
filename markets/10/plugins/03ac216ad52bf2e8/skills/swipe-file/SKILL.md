---
name: swipe-file
description: Work with the user's saved Hookest hooks (their swipe file) - list them, save or remove hooks, find more like a saved one, download the hook clip or open it in the Hook Editor. Use when the user mentions their saved hooks, their list or swipe file, asks to save a hook, or wants the video file of a hook.
---

# Swipe file with Hookest

Goal: make the user's saved hooks useful: easy to review, easy to extend, and
ready to put in front of their own video.

## Review the swipe file

1. Call `list_saved_hooks` (`limit: 24`, page with `offset` if there are more).
2. Group the hooks by category and show account, views and the Hookest link
   for each. Mention which ones were added most recently.
3. Point out what the saved hooks have in common (category, length, format)
   based on the data that came back. Do not invent pattern labels.

## Save or remove

Call `set_hook_saved` only for hooks the user named in this conversation, with
`saved: true` to add and `false` to remove. Confirm what changed in one line.

## Grow it

For "more like this", call `find_similar_hooks` on the saved hook the user
picks (`exclude_same_account: true` keeps the results varied). Offer to save
the ones they like.

## Use a hook

- **Video file:** `get_hook_download` returns the hook clip (the opening
  seconds as mp4). It is not available on every plan and is the only way to give a video
  file. Never hand out thumbnail, source or Instagram URLs as a download. Only
  the hook clip exists, not the full reel.
- **Hook Editor:** every hook result has an `open_in_editor_url` that puts the
  hook in front of the user's own video on Hookest. Share that link.
- If an action is not available with the user's plan, say so plainly. Do not
  quote prices or offers.

To write new hooks from the saved ones, continue with the `write-hooks` skill.
