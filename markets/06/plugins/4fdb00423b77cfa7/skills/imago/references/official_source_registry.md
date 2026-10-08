# Official Source Registry

Research date: 2026-09-23

Use current primary documentation when product behavior, model capability, or plugin rules matter.

## ChatGPT Images
- Images in ChatGPT:
  https://help.openai.com/en/articles/11084440
- OpenAI Academy image-generation guidance:
  https://openai.com/academy/image-generation/

Current ChatGPT Images supports creating and editing images, reference-image workflows, aspect-ratio selection, templates, sketches on supported clients, transparent backgrounds, iterative editing, and text inside images.

## OpenAI image APIs
- Image generation guide:
  https://developers.openai.com/api/docs/guides/image-generation

Current API documentation describes:
- image generations;
- image edits;
- reference-image inputs;
- mask-guided editing;
- image generation in the Responses API;
- multi-turn image editing.

Do not freeze specific model IDs into Imago's skill instructions unless an implementation actually needs them. Model names and routing can change.

## Plugin packaging
- Plugins:
  https://developers.openai.com/plugins
- Build skills:
  https://developers.openai.com/plugins/build/skills
- Package plugins:
  https://developers.openai.com/plugins/build/plugins
- Submission:
  https://developers.openai.com/plugins/deploy/submission
- Submission validation:
  https://developers.openai.com/plugins/deploy/submission-errors

## Imago background
Public GPT:
https://chatgpt.com/g/g-69e7de729cb48191a6aa83ec3af8a6cb-imago

Original product write-up:
https://medium.com/javarevisited/i-built-imago-how-chatgpt-images-2-0-made-me-rethink-how-we-generate-visuals-dfe7d0211182

The original Imago philosophy is image-first execution with minimal conversational friction. Current instructions should target the current ChatGPT Images experience rather than preserve old model names or stale capability claims.
