---
name: video-from-idea
description: Use when the user has only an idea, a topic or a script and no footage, and wants a short narrated video (a faceless reel with a voice-over, stock footage and captions). Writes the script with the user first, then runs video_from_idea after the words and the price are approved.
---

# A video from an idea

Follow the steps in the `video-price-and-status` skill for the price, the yes, `video_from_idea`, `video_status` and the link. There is no video to get: you write the words first.

## 1. Write the script with the user

- Write the exact words the voice will say: about 60 to 150 words for a 30 to 60 second video, in the language the video should be in.
- Open with a line that makes people stop scrolling, keep sentences short, end with one clear point.
- Show the script and ask for changes. Use only the version the user approved.

## 2. What to set

- `script`: the approved words.
- `voice`: `woman` (the default) or `man`.
- `language`: the script's language (`he`, `en`, `ru`…), or leave it out to detect it.
- `topic`: one line on what the video is about. It guides the choice of stock footage.
- `mood`: how the voice should sound, for example "warm and calm" or "energetic".
- `style`: the caption style; `bold` is the default. The `video-captions` skill has the full table.

## 3. Price, yes, run

Price it with `get_price`, show the price, wait for the yes, run it once, follow it to the end and give the link. If the user changes the script after the yes, price it again.
