---
name: whats-playing
description: Tell the user what song is playing on a radio station right now, using Spinn Radio. Use when the user asks "what's playing on …", "what song is this" about a Spinn station, or "what's on" a named station.
---

Use this skill to answer "what's playing".

1. If the station is already in the conversation (a player or cards from Spinn), use its id.
   Otherwise find it with `search_stations` using the station name in `query`.
2. Call `get_now_playing` with the station id.
3. Answer with the artist and title. If the station does not broadcast song titles, say so plainly and offer to open the player so the user can listen.
4. If the user then wants to hear it, call `play_station`.

Never guess a song. Only report what `get_now_playing` returns.
