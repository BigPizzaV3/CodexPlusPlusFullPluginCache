---
name: ringtone-maker
description: Make a personal sung ringtone or alarm with Ringoz when the user asks for one, and remix it in plain words. Not for questions about phone settings, existing songs or how ringtones work.
---

Use this only when the user wants a ringtone or alarm sound made, or wants to change one made in this chat.

1. Get the name or subject. If it's missing, ask once: who is it for?
2. Get the words. If the user gave a line, use it as written. If not, write one or two short lines with them, in their words and language, and use the one they pick. Lines stay under 120 characters and suit all ages. If they ask for ideas, write a few lines with them in chat; there's no tool for ideas.
3. Call create_ringtone alone in the turn, never after another tool, so the card shows. Defaults: 28 seconds, the user's language, purpose ringtone. Lengths run from 5 to 30 seconds. Pick the closest of the 12 styles; if the user named a style that isn't one of them, say which one you picked.
4. The card shows progress and plays the ringtone. Don't call get_ringtone in the same turn. Reply in one or two short lines; don't repeat what the card shows.
5. Changes like shorter, another style, other words, another language or an alarm instead go to remix_ringtone with the ringtone_id. There's no voice control; offer a style instead.
6. If a result says the studio is busy, tell the user in one line and don't call again in that turn.
7. If the user asks how to get it on their phone, say the card's Make it my ringtone button opens it on the phone. Say nothing about prices, plans or downloads.
8. Decline in one sentence, without calling a tool, when asked for an existing or commercial song, a voice change, or help with phone settings.
