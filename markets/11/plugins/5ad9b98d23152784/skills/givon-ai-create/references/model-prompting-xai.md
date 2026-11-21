# xAI Model Prompting

Sources:

- https://docs.x.ai/developers/model-capabilities/imagine
- https://docs.x.ai/developers/model-capabilities/images/generation
- https://docs.x.ai/developers/models/grok-imagine-image

## Grok Imagine Image

- Use a direct brief: subject, generated scene or edit, composition, style and constraints.
- Put the edit operation first and then state important preserved elements.
- Label each reference by role: subject, product, style, composition or background.

## Grok Imagine Video

- For image-to-video, treat the source image as the visual anchor and direct motion, camera,
  atmosphere and physics.
- For text-to-video or edits, use a compact subject, action, setting, camera and audio brief.
- Keep the prompt within the live byte/character limit.

Aspect, resolution, references, duration and audio controls come from the selected schema.
