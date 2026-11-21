---
name: muziek-maken
description: Make an original song with Muziek maken met AI from an idea or finished lyrics, after the user confirms the lyrics, style and the use of one song credit.
---

# Make a song with Muziek maken met AI

Use this when the user wants a new original song (birthday, retirement, wedding, a joke for friends, a song about a pet) or wants to hear a song they made earlier.

## Before making a song

1. Call `get_account` once to see the available song credits and saved voice profiles.
2. Agree on the content with the user. Either:
   - write original lyrics together (verses and chorus, optionally with tags like `[Verse]` and `[Chorus]`) plus a style such as "acoustic pop, upbeat, guitar", or
   - use a short description of the occasion, names and mood and let the service write the lyrics.
3. Show the title, style and lyrics or description, and say that one song uses 1 credit and returns two versions. Ask for confirmation.
4. Do not use lyrics from existing songs and do not ask for the voice or style of a named artist. The service rejects those requests.

## Making the song

Call `create_song` once, with `confirmed: true` and a new `idempotency_key`. When retrying the same request after an error, reuse the same key so no second credit is used. The player shows progress and plays both versions when they are ready; there is no need to call `get_song` repeatedly.

## Later

Use `list_songs` to find earlier songs and `get_song` to play one. Editing, extending or splitting songs into stems happens in the Studio on muziekmakenmetai.nl, not in this plugin.
