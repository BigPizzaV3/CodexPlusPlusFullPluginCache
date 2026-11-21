---
name: artist-discovery
description: Look up a music artist on Spinn Radio and find radio stations that have been playing them, or Spinn playlists around a theme or artist. Use when the user asks about an artist together with radio ("who plays Burna Boy", "stations that play Fela Kuti"), or asks for a Spinn playlist.
---

Use this skill for artist and playlist questions.

- Artist on the radio: call `get_artist` with the artist's name.
  - Summarise in two or three sentences from the returned bio and genres.
  - If `airplay` is present, say how many times and on how many stations they were heard in the last 30 days, and in which countries. Offer to play one of `airplay.recentStations` with `play_station`.
  - If there is no airplay, say Spinn hasn't heard them on its stations in the last 30 days, and offer to find stations in their genre with `search_stations`.
- Playlists: call `search_playlists` with a theme, mood or artist, and share the titles with their links.

Only use facts returned by the tools. Link to the artist page with the returned `url`.
