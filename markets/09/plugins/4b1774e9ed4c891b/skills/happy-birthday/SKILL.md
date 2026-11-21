---
name: happy-birthday
description: Sing Happy Birthday to someone by name, play birthday songs and styles, run birthday countdowns, and save birthdays. All content is free.
---

Use `sing_happy_birthday` to sing to a person by name, optionally in a style or after a
countdown (`delaySeconds`). Use `play_birthday_song` for a named song,
`set_song_order` / `play_song_order` for a saved one-to-three song order, and
`save_birthday`, `list_birthdays` and `delete_birthday` for saved birthdays. Each
playing or saving request opens or updates the player by itself. `list_birthdays`
and `browse_birthday_songs` only read: they open no player and never interrupt
playback. `save_birthday` never replaces a saved birthday; if that date or name is
already saved, ask the user before deleting the old entry with `delete_birthday`.
The player's own buttons handle stop, replay and next.

A successful tool call queues playback; it does not prove the browser played audio.
If needed, explain that the user must tap Enable sound. This plugin does not use a
microphone, cannot contact other people, and cannot order goods.

Everything is free. Do not offer purchases, subscriptions, Amazon account linking or
Alexa features.
