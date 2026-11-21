---
name: image-to-video
description: 商品や人物の画像から短い動画を作り、動きや構図を修正して保存する。画像の動画化・短い商品動画に使う。
---

Preserve explicit user requirements. Establish the subject, desired motion, destination and duration from the conversation; ask only for missing consequential details. Do not invent product claims.

1. For a chat attachment use import_chat_images with medium video. For a generated image use the exact source messageId/index and conversationId from get_generation. Never infer image IDs or substitute another output.
2. Use list_video_models to choose an available image-capable model. Choose only supported aspect ratios, duration and audio options. Describe one feasible shot, camera motion and what must stay unchanged. Avoid promising lip sync or identity consistency beyond the model's results.
3. Call prepare_video with the reference and prompt. The user clicks the priced generation button. Poll/recover the same job with get_generation and never duplicate a pending request.
4. Review the resulting motion and preservation of the reference if the output is visible. Otherwise ask the user to assess it. Use the existing output's conversation and source for a supported edit; new generation requires another quote and priced click.
5. Deliver the video save action. If the user wants a cut or captions, use the widget's video-edit action and edit_video_project with actual imported clip IDs/durations. Finish with MP4 export; do not claim the saved file exists before rendering/download succeeds.

Template registration belongs in Studio. Do not initiate checkout.
