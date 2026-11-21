# Prompt Engineering

## Basics

Media.io models reward concrete, sensory prompts.

- **Subject + setting + style**: "a red fox curled in a snowy pine forest, golden hour, cinematic"
- **Camera**: lens (35mm, 85mm), angle (low, overhead), motion (dolly in, tracking shot)
- **Lighting**: rim light, neon glow, moody backlight
- **Style/medium**: oil painting, watercolor, photograph, anime, 3D render

Keep it under ~200 tokens. Models distort with very long prompts.

## Image-to-image

When an image parameter is supplied, the prompt should describe what changes, not redescribe the input.

Bad: "a man with brown hair in a leather jacket holding coffee, made into anime"
Good: "transform into anime style, vibrant colors, soft cel shading"

## Image-to-video

A start-frame parameter anchors the first frame. The prompt describes motion.

- Verbs: zooms in, dollies left, sweeping pan, slow push, fast whip
- Subject motion: "the dancer spins", "smoke rises slowly"
- Don't redescribe the static frame — model already has it.

## Negative phrasing

Most models don't expose a `negative_prompt`. Phrase positively:
- Instead of "no blur" → "tack sharp"
- Instead of "no people" → "uninhabited landscape"

## Output size

Treat aspect ratio, pixel size and resolution tier as generation settings. Extract them even when embedded in a prompt, screenshot or earlier request. Prompt wording such as "wide composition, 21:9" describes the scene but does not configure output dimensions.

Read the selected model's section in the generated [model parameters](model-parameters.md). The tool's field descriptions and this reference share the same reviewed mappings. Depending on the model, sizing can use `size`, `ratio`, `dimensions`, `aspect_ratio`, `resolution`, or a field such as `mode` whose UI meaning is resolution. Match the requested ratio and resolution to the declared value rather than inferring a field from its name. A `dimensions` value is a `WIDTHxHEIGHT` string, never an array. Preserve coupled option branches. Defaults apply only to settings the user left unspecified.

UI label context may name a resolution tier even when no `resolution` option exists: in that case select the mapped size and send only the declared field. Nominal ratio presets can use rounded dimensions. An exact pixel request must match an allowed value. If the selected model cannot satisfy a requested size or the requirements conflict, explain the available choices and resolve the requirement before submitting. Keep an explicitly selected model unless the user authorizes a change.

## Safety

Models reject prompts with `nsfw` or `ip_detected` terminal status. Avoid:
- Real public figures
- Sexual content
- Trademarks / branded characters
