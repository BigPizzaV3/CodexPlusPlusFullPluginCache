---
name: video-captions
description: Use when the user wants captions or subtitles burned into a video (Hebrew, English, Arabic, Russian or another language), wants a talking video turned into a captioned vertical clip, or asks which caption style fits their video. Picks a caption style by the kind of content and runs captions_for_video after the price is approved.
---

# Captions on a video

Follow the steps in the `video-price-and-status` skill: get the video, `get_price`, the user's yes, `captions_for_video`, `video_status`, the link.

## Which style

Pick by what the video is. Name the style you picked in a few words when you show the price, so the user can ask for another. When the user wants to see the styles, call `show_examples` with `kind: caption_styles` — each style plays as a short video with a "Use this style" button.

| The video | Start with | Also fits |
| --- | --- | --- |
| A calm talk, a lecture, a podcast, an interview, an explainer: long speech people read along with | `classic` | `news`, `quiet`, `typewriter`, `underline`, `elegant`, `cinema`, `bubble` |
| An energetic pitch, sales, a hype reel, a hook-driven short: the spoken word marked out | `bold` | `karaoke`, `one-word`, `marker`, `sticker`, `drama`, `scale` |
| Entertainment, humour, a playful or young brand: captions that move | `neon` or `pop` | `bounce`, `handwritten`, `comic`, `shadow`, `lime`, `retro`, `sport` |

If the user names a style, use it. If you can't tell what the video is, use `classic`.

## What to set

- `video`: the link or the upload code — or `video_file` when the user attached the video in the chat.
- `style`: from the table.
- `spoken_language`: leave it out to detect it, or set it when the user says (`he`, `en`, `ar`, `ru`…). Hebrew and Arabic captions are drawn right to left by themselves.
- `captions_language`: only when the user wants the captions in another language than the one spoken (they are translated line by line).
- `shape`: `vertical` (9:16, for Reels, TikTok and Shorts) is the default. Use `original` to keep the video's shape, or `square`, `portrait`, `landscape` when asked.
- `headline`: only when the user wants a short headline in the first 3 seconds (3 to 8 words, in the video's language).
- `cut_pauses`: `true` only when the user wants the silent pauses cut out.

Ask only what you can't infer. "Add Hebrew captions to my video" plus a link is enough to price it.
