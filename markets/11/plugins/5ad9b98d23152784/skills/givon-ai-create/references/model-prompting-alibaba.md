# Alibaba Model Prompting

Sources:

- https://wan.video/
- https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777
- https://www.alibabacloud.com/help/en/model-studio/legacy-image-to-video-api-reference/
- https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes
- https://morphic.com/resources/how-to/happy-horse-1-0-complete-guide-prompts-features-tips
- https://fal.ai/learn/tools/prompting-happy-horse

## Wan Image

- Use a clear scene brief with subject, action or pose, environment, framing and style.
- Keep instruction edits surgical: target, requested change and preserved target.
- Name what each reference contributes.

## Wan Video

- Match the prompt to the schema-backed mode: text, start image, first/last frame, reference or
  edit.
- For start-image video, describe motion arc, camera path and continuity from the source.
- For first/last frames, describe the transition as one event.
- Keep edit instructions focused and multi-event stories aligned with available multi-shot
  controls.

## HappyHorse

- Use a concise director brief: subject, action, setting and one useful cinematography cue.
- Add dialogue, audio or shot structure only when the request needs them and the schema supports
  them.
- Keep spoken text clean for lip-sync or dialogue work.
