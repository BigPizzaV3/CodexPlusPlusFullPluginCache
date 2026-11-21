---
name: listen
description: Play faith radio, Christian or sacred music, hymns, gospel, DLM Faith's own songs, or a faith talk show or podcast episode. Use when the user wants to listen to faith music, a Christian station, hymns or a faith show.
---

Use this skill for music, radio and shows.

1. Music or radio: call `list_stations`, with `style` for what they asked ("sacred", "hymns", "instrumental", "gospel", "catholic", "kids", "spanish", "talk").
   - One clear fit: call `play_station` with its id.
   - Several good fits: call `show_cards` with kind "stations" and up to 6 ids, best first, and a short heading.
   - DLM Faith's own music has ids starting "music:" and plays as a shuffled radio of its songs.
2. Shows: call `list_shows`, then `get_show_episodes` for the show, then `play_episode` (without an episode id it plays the newest). Several shows to choose from: `show_cards` with kind "shows".
3. After the player opens, say in one sentence what you chose. Playback starts when the user taps play; don't claim it is already playing.

Only use ids returned by DLM Faith tools. Don't download or record audio.
