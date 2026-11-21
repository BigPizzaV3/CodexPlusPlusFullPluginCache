---
name: anime-conversion
description: Turn an attached image or short video into anime with Anime Style. Use for anime restyling, manga conversion, cinematic anime, retro 90s anime, or chibi versions of existing media.
---

# Anime Style

Use this plugin's `anime_image` for images and `anime_video` for existing video clips. Do not animate a still image when the user asked to restyle a video.

Pass the user's attachment as the `image` or `video` file object, preserving its download_url and file_id. If the user provided a link, use image_url or video_url. Provide exactly one source. Never invent a file reference or ask for a public URL when an attachment is already available.

Choose the closest preset from the request: classic (default), cinematic, retro-90s, chibi, or manga. Pass extra art direction in prompt. Default to one image; request up to four variations only when the user wants alternatives. Preserve subject identity, clothing, scene, composition and, for videos, motion. These are editing instructions, not guarantees of exact reproduction.

Video conversion accepts MP4/MOV clips up to 10 seconds and 50 MB, and outputs 720p. If the video exceeds those limits, explain that it needs trimming or exporting before conversion. Do not silently replace, truncate, or switch models. Audio preservation is requested but not guaranteed.

Conversions spend Firemoon account credits. Video costs $0.10 per second of validated source footage. Images use Firemoon's Nano Banana Edit pricing. Use the host's normal Firemoon authentication flow; do not ask users to paste API keys into chat or include keys in prompts.

Display the returned interactive result. Use its media[].url and downloadUrl exactly as returned when providing links. Do not expose underlying storage URLs or invent output links. If a tool returns isError, report the actual error and a concrete next step. Do not automatically repeat paid requests after a timeout or uncertain outcome.

## Guest access and optional account linking

Start by calling the workflow tools directly. Do not request account linking before using the anonymous daily image/video allowance. Guests share 100 image/video outputs per host guest identity per UTC day; each image variation counts separately. Only offer account linking when the tool returns an authentication challenge or the user explicitly wants to use account credits. Never invent a guest identifier or bypass a quota response. Preserve existing attachment requirements and uncertain-job retry safeguards. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
