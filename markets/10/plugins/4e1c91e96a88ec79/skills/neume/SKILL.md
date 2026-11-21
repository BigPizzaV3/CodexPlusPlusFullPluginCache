---
name: neume
description: Make, play and change songs in the user's Neume account — writing lyrics, confirming before credits are used, and picking the right part when changing words.
---

# Making and changing songs with Neume

## Making a song (generate_song)
- Ask what the song is about and the sound they want if it isn't clear. Describe the sound in `style` with genre, mood, tempo, instruments and the kind of voice. Never name a real artist or ask for a real person's voice; describe the sound instead.
- Unless they gave their own words or want an instrumental, write the lyrics yourself with each part under a tag on its own line ([Verse], [Chorus], [Bridge]). Keep it to a normal song length (two verses and a chorus is plenty).
- Show them the title, style and lyrics, and make the song only once they're happy with them. Making a song uses credits from their Neume account.
- One call makes one song. The song card shows its progress and plays it when it's ready: don't poll, and don't paste audio links.

## Playing and finding songs
- get_my_songs lists their songs (newest first); get_song_details shows one song with its player and lyrics.

## Changing the words of one part (change_lyrics)
- Call get_song_parts first to see the song's parts (verse#1, chorus#2…) and the lines sung in each. Pick the part they mean; ask if it's unclear.
- Write the new lines with them. Pass every line sung in that part: the new lines where they change, the old ones word for word where they don't.
- Only call change_lyrics once they agree to the new lines. It makes a new song with that part sung again in the same voice; the original is kept.
- If the tool says the part is too short or too long, follow what it says (more lines, or a different part).

## A new style for a whole song (reimagine_song)
- Agree the new style with them first. It keeps the song's own words unless they want new ones, and makes a new song; the original is kept.

## Audio they attach (a hum, a voice memo, a song)
- Call add_audio with the file first. It returns an audioId, the length, and the words heard in it with its parts. It's free.
- To turn it into a song, call make_song_from_audio:
  - sing_again: their audio sung again by a singer in the new style. Best for a hum or a voice memo. A hum has no words, so write lyrics with them (about as many lines as its length allows) and pass them.
  - follow_melody: a new song that follows its tune. It needs lyrics.
  - take_sound: a new song with its sound and feel.
- To change some words of a song they uploaded, use get_audio_parts and then change_audio_lyrics, the same way as change_lyrics.
- Agree the title, style and words with them before making anything; it uses credits.

## When something can't be done
- If there aren't enough credits, say so plainly. Don't suggest buying anything or link to a purchase page.
- Neume can't delete songs, change account settings or buy credits from the chat; say so in one sentence.
