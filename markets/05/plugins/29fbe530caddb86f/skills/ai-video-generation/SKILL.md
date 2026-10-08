---
name: ai-video-generation
description: |
  Generate AI video clips through the doublespeed MCP: choose a model, submit text-to-video or image-to-video jobs, poll status, and hand the clips to a video draft. Use when the user asks for AI video, generated clips, image-to-video, or video from a prompt.
---

# AI Video Generation via doublespeed

## Setup

1. `whoami` to confirm the active product; `list_products` + `set_product` if wrong or missing.
2. Video generation costs credits and charges the ACTIVE product. On an insufficient-credits error, STOP and report it for the active product - never `set_product` to another product to chase credits. Suggest alternatives: existing collections (`browse_media`), cheaper models, or image-to-video from existing images.

## Workflow

1. **Pick a model.** `list_models` for available video models, parameters, and pricing. Cheaper models are fine for background/demo footage; spend on the hook.
2. **Choose the mode.** Text-to-video for generic scenes; image-to-video when you need a specific product, person, or look (generate or pick the source image first - `generate_image` with `image_url` references keeps a recurring character consistent).
3. **Generate.** `generate_video` per segment (async - returns a media file ID). Submit segments in parallel, then poll `check_generation_status`. Always 9:16, ~5s clips (shorter = better quality).
4. **Prompt for realism.** Candid phone-camera footage, real setting, natural light - not a glossy render. Never ask the model to render text; overlay text is added at the draft stage.
5. **Review every clip** before using it: artifacts, warped hands/faces, and dead first seconds are common. Regenerate rather than shipping a weak clip.
6. **Hand off.** Feed the clip URLs into the hook-demo workflow (`doublespeed://skills/hook-demo-videos`) for overlay text, preview, draft, and posting. For local post-processing (trims, speed ramps, concat via ffmpeg), upload results with `prepare_media_upload` → PUT → `commit_media_upload`.

## Notes

- `generate_image`/`generate_images` follow the same async + credits rules for still images.
- Store keeper images in a collection: `create_image_collection`.
- For research, strategy files, and the feedback loop, read `doublespeed://skills/content-creator`.
