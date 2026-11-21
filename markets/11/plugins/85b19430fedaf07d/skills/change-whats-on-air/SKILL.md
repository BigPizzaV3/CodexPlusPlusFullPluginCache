---
name: change-whats-on-air
description: Use when the user wants to skip, reorder, add or remove videos on a stream that is live right now, or play something once and go back to the loop.
---

# Change What's On Air

1. playout_get_state. What is playing is running.playlist.items, not the saved items. running.onAir says whether the loop or a play-once playlist is up.
2. Pick the tool for what the user wants:
   - Skip, reorder, add or remove videos on air: playout_edit_running_playlist with the full new list (copy rows you keep unchanged). Optionally jump to an item. A continuous stream follows its playlist, so this saves the new list to that playlist too.
   - Edit the saved playlist: playlist_get, then playlist_set_items. A running stream that plays it takes the new list within seconds.
   - Change what is on air but leave the saved playlist as it is: playlist_create with the new list, then playout_switch_playlist with switchType "loop".
   - Play another playlist once, then return: playout_switch_playlist with switchType "inline"; playout_cancel_inline ends it early.
   - Random order: playout_toggle_shuffle.
   - A scheduled stream refuses these while a calendar block is on air. Read the block with calendar_get and change it with calendar_update_entry, which takes effect on air straight away.
3. Say what viewers will see and when, and whether the saved playlist changes too. Confirm, then call the tool.
4. Check the result with playout_get_state.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
