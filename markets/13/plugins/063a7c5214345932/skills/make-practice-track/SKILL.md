---
name: make-practice-track
description: Use StemConsole to turn an audio attachment, supported audio-file link, or song in the connected StemConsole library into a backing track for practice. Use for stem separation and practising with a recording, rather than music recommendations or generating a new composition.
---

Turn your recording into a backing track you can practise with inside ChatGPT.

Use the connected StemConsole tools for the source the user supplied:

- For an audio attachment, use split_song_file with the attachment reference supplied by ChatGPT. Do not invent attachment IDs or download addresses.
- For a supported audio-file URL, use split_songs. A streaming-service page is not an audio file; ask for a supported file or link when necessary.
- For an existing library song, use list_my_songs to find its ID, then open_player; avoid creating another split unnecessarily.

Choose the separation mode that fits the request: vocals for vocals and instrumental, fast for vocals/drums/bass/other, or full when separate guitar or piano stems are needed. Explain unavailable account entitlements neutrally, without offering a purchase or upgrade.

After starting a split, check get_split (or get_batch for a batch) until it finishes or fails. When processing remains in progress, report that state and use the existing job ID on subsequent checks. Do not start another split to retry a status check. If processing fails, explain the returned error and stop; do not automatically spend another allowance.

Open a completed song with open_player. The user can mute their part, balance stems, loop a passage, use the available speed/key controls, and export a practice mix. These controls run in the widget; do not claim to have changed a fader, saved a file, or measured key/BPM merely by opening it. Prepared downloads require the user to choose Prepare download and then Save file.

Act on the connected account only. Confirm the identified song and intent before permanent deletion; clarify ambiguous targets. Use song IDs returned by tools, not guessed IDs. Processing audio does not grant rights to the recording.
