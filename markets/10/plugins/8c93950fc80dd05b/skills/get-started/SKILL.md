---
name: get-started
description: How to brief AI Jingle Maker for a radio jingle, podcast intro, station ident or DJ drop, what is free and what uses account credits, and how to go from draft to clean MP3 and WAV.
---

# Get started with AI Jingle Maker

AI Jingle Maker makes short radio-style jingles (about 10 to 30 seconds): an intro sound, a music bed under a voice-over, and an outro, all from a licensed catalogue of about 970 sounds, plus a voice-over in one of 99 voices (up to 74 languages).

## A good brief

Say what the jingle is for and how it should feel. The more of these the better:

- the use: station ident, podcast intro, DJ drop, event promo, shop announcement
- the name to say: the station, show, event or business ("Big Sky Country Radio")
- the mood and genre: warm late-night jazz, upbeat pop, dark cinematic, country, lo-fi
- the length: about 10, 15, 20 or 30 seconds
- the voice: male or female, and the language if not English

Example: "Make a 10-second ident for my late-night jazz radio show, warm, male voice. The show is called Midnight Standards."

## What happens next

1. `compose_jingle` builds a draft: three sounds that fit, a script in your words (or written from the brief), and a voice. A card appears in the conversation.
2. Adjust it by talking ("faster bed", "darker outro", "something with piano", "shorter script", "female voice") or directly on the card (play each sound, swap with the arrows, edit the script, pick a voice).
3. `preview_jingle` plays a free, watermarked preview of the whole jingle on the card.
4. `render_jingle` produces the clean MP3 and WAV. This spends credits from the user's AI Jingle Maker account: 1 credit for a script up to 125 characters, 2 up to 500. Rendering the same draft again is free.

## Free versus credits

- Free, no account: drafting, swapping sounds, editing the script, choosing a voice, watermarked previews (a few per day).
- Needs a connected AI Jingle Maker account and credits: the clean MP3 and WAV. The first render asks the user to connect their account.
- Credits are bought and managed on aijinglemaker.com, never in the conversation. If the user has none, say that credits are managed on their account page; do not quote prices or point to a checkout.

## Do and don't

- Do write scripts that read aloud well: short sentences, no placeholders like [Station Name], numbers as words.
- Do quote what a vocal intro or outro says, so the user knows what plays before and after their own words.
- Don't call `render_jingle` unless the user clearly asked to render, finalise or download.
- Don't promise full songs, music licensing advice, or audio longer than about a minute; this plugin makes jingles.
