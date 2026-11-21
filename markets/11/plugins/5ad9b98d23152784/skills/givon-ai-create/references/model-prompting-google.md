# Google Model Prompting

Sources:

- https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- https://ai.google.dev/gemini-api/docs/image-generation
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide
- https://deepmind.google/models/veo/prompt-guide/
- https://deepmind.google/models/gemini-omni/prompt-guide/

## Nano Banana / Gemini Image

- Start with the operation: generate, edit, transform, place, localize or combine.
- For generation, describe subject, action, context, composition and style.
- For references, name what each image contributes and then describe the new scenario.
- Use concrete composition, lighting and camera language; quote exact rendered text.
- Keep iterative edits concise and coherent.

## Veo

- Describe subject, action over time, scene, camera, lighting, tone and pacing as relevant.
- Give audio direction in a separate sentence for audio-capable variants.
- Express exclusions as a concise list of unwanted elements when the model supports negative
  prompting.

## Gemini Omni Video

- Use concise transformation or videography direction for multimodal edits.
- Name reference roles such as source clip, style, product image or dialogue guide.
- State continuous-shot intent and camera state when they matter.

The live schema decides which reference and audio fields are available.
