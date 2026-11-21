---
name: full-edit-video
description: Use when the user wants a finished, edited video from their own footage — "edit this", "make it look great", "a full edit", "add AI shots / b-roll, music and effects", "make mine like this example". Lets the user pick the kind of edit and a look with choose_edit where that tool is available, then runs APIhub's video editor in one job (shots, music, sound effects, headline, captions, zooms and cuts) with full_edit_video after the price is approved.
---

# A full edit of the user's video

Follow the steps in the `video-price-and-status` skill: get the video, the price, the user's yes, `full_edit_video`, `video_status`, the link.

## What it makes

One finished vertical video from the user's footage: pauses and retakes cut, a headline in the first seconds, captions, and — by the kind of edit — shots cut in over the speech (real stock footage or AI-made), music with sound effects, punch-in zooms and flash cuts. Plus a title, a caption and hashtags for posting (nothing is posted).

## Let the user pick: `choose_edit`

When `choose_edit` is among your tools, start there whenever the user brings a video and wants it edited or is not specific about how ("edit this", "make it look good", "make a reel of it"). Call it with the video and nothing else. It only prices: the full edit three ways for this video, with four looks to see; nothing runs and nothing is charged.

- The three kinds: **edit + captions** (the pauses and retakes cut, a headline, captions; the cheapest), **stock footage + music** (that, plus real stock footage of what is said, music and sound effects), **AI shots + effects** (AI-made shots instead of stock, music, sound effects, zooms and flashes; the most expensive).
- The four looks: `clean`, `bold-lime`, `night`, `warm` — the colours and fonts of the captions and the headline, and the mood of the music.
- Where the app shows the card, the user taps a kind, a look and one button. The message that button sends ("Make my video: …, I approve up to N credits") carries `full_edit_video`'s exact arguments, the approval id included: use them as they are for the `full_edit_video` call.
- Where no card is shown (Claude Code, Cursor), tell the user the three kinds with their prices and the four looks in a few short lines (the preview links play), let them pick one of each, and after their OK send that pair's `call` from `choices` as it is. A kind the balance does not cover has no call.
- Do not ask about the style, the music or the shots in text first. A narrow ask goes straight to its own tool: "just captions" → `captions_for_video`, "reels from this podcast" → `reel_from_long_video`.

Without `choose_edit`, price with `get_price` and `task: full_edit_video`, show the price with the short list of what will be in the video, and wait for the yes.

## What to set

- `video`: a link or an upload code (in ChatGPT only, an attached file as `video_file`).
- `tier` and `look`: the kind of edit and the look the user picked in `choose_edit`, or named themselves.
- `example`: when the user picked a card in `show_examples` ("make mine like this"), that card's id — its look becomes this video's.
- `request`: the user's own words about the mood or what to stress, when they gave any.
- `shots`: `ai` (AI-made shots — the most striking, and most of the price), `stock` (real stock footage — much cheaper) or `none`. Offer `stock` when the price matters.
- `music`: `calm`, `warm`, `epic` or `none`.
- `length_seconds`: only when the user wants a set length (15–180). By default the whole clip up to 3 minutes, else about a minute of its strongest part.

Ask nothing more than you need: "make a great edit of this" plus the video is enough. If the finished plan needs more credits than approved, `video_status` says so with the real price: show it and ask again.
