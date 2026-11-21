---
name: get-started
description: How to start a Mzelo watch party for a YouTube video and share it with friends.
---

# Watch YouTube with friends on Mzelo

Use the `create_watch_party` tool when someone wants to watch a YouTube video
together with other people online, at the same time.

- If they gave a YouTube link, pass it as `youtube_url`.
- Otherwise pass what they want to watch as `topic` (for example
  "lofi hip hop" or "a nature documentary"); one safe-search YouTube result
  is chosen.
- Call it once per request: every call creates a new room.

The tool returns a room link on mzelo.com. Tell the user to open it and share
it with the people they want to watch with. Anyone with the link can join from
a browser without an account, and the first person to open the room gets the
remote to play and pause for everyone.

Only YouTube is supported. Private, removed, age-restricted and embed-blocked
videos can't be used; if one is refused, ask for a different video.
