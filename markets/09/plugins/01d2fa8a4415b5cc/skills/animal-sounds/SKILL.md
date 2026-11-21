---
name: animal-sounds
description: Play real animal sounds, facts, loops, ambient sounds, dinosaur sounds, narrated animal tours and animal songs when the user asks. All content is free.
---

Use the focused Animal Sounds MCP tool for the user's request. `play_animal_sound`
without arguments plays a random animal. Each request opens or updates the player by itself.

Every playback tool shows the Animal Sounds player. `show_player` opens the player on its
menu without playing anything, which suits requests for the menu or help; `browse_animals`
returns catalog IDs as text. The player's own buttons handle stop, replay, next and video
settings. `animal_fact` and `browse_animals` never interrupt playback.
Animal and dinosaur sound results include a fun fact about the animal, shown on the player but not read aloud.

Answer fact questions ("how fast is a cheetah?", "what do pandas eat?") with
`animal_fact` and read the returned fact to the user. Use `animals_by_habitat` for
"what animals live on the farm/in the jungle". Tours, dinosaur tours and auto play
show their narration on screen; summarise briefly instead of repeating it all.

A successful tool call queues playback; it does not prove the browser played audio.
If needed, explain that the user must tap Enable sound. Do not promise playback after
the widget closes or the device sleeps. This plugin does not use a microphone and
cannot identify animals from recordings.

Everything is free. Do not offer purchases, subscriptions, Amazon account linking or
Alexa features.
