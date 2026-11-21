---
name: get-started
description: First steps with varg.ai — check the balance, make a first image or video, and find templates and voices.
---

# Getting started with varg.ai

varg.ai turns a brief into finished media: images, video, voiceover, music and full multi-scene ads.

1. Call `check_balance` to see how many credits the account has (1 credit = $0.01).
2. For a quick result, use `generate_image` or `generate_video` with a plain description.
3. Videos take 1–5 minutes: they return a `job_id`; call `get_job` until it is done.
4. For voiceover, find a voice with `search_voices`, then call `generate_speech`.
5. For a ready-made format, use `find_templates` → `use_template`, or `get_template` → edit → `render_video`.
6. For a specific model, use `list_models` → `get_tool` → `call_tool`.

Before an expensive request, `estimate_cost` prices it. If a call returns `insufficient_balance`, stop and tell the user.
