# Research Notes — Imago

Research date: 2026-09-23

## Product identity

Keep the name **Imago**.

Imago already exists as a public custom GPT and has a clear product identity: an image-first visual studio rather than an image-prompt generator.

Public GPT:
https://chatgpt.com/g/g-69e7de729cb48191a6aa83ec3af8a6cb-imago

The original public write-up described the core philosophy as image-first execution with minimal chatter and emphasized direct creation, reference consistency, factual data integrity, and fast iteration.

## Recommended plugin architecture

Use a **skills-only plugin** for v0.1.

Why:
- current ChatGPT already provides native image generation/editing;
- the plugin's differentiation is behavior and workflow, not an external image API;
- the skill can teach the host when to create, edit, inspect references, research facts, preserve details, and validate data;
- adding MCP would duplicate capability and introduce unnecessary authentication/tool complexity.

A future MCP server would only make sense for external creative systems such as DAM/CMS asset storage, brand libraries, design-system repositories, or publishing workflows.

## Current ChatGPT Images research

OpenAI's current ChatGPT Images documentation says the product can:
- generate new images;
- edit uploaded or generated images;
- make localized edits;
- select/regenerate aspect ratios;
- use templates;
- use sketches on supported mobile clients;
- add text/details;
- create transparent backgrounds.

The current help page also states that GPTs with Image Generation enabled can use the current ChatGPT image-generation model.

Source:
https://help.openai.com/en/articles/11084440

## Current prompting guidance

OpenAI Academy's current image-generation guidance emphasizes:
- clear concise prompts rather than unnecessary verbosity;
- explicit purpose, subject, action, setting, and style;
- specific spatial/layout instructions;
- clear constraints for edits;
- changing one element at a time to reduce drift;
- explicit text instructions;
- clear roles when multiple reference images are supplied.

Source:
https://openai.com/academy/image-generation/

These principles fit Imago's visual-first behavior, but the skill should not become a prompt-writing assistant. It should use these principles internally and then generate/edit the image.

## Current API capabilities

Current OpenAI image-generation API documentation describes:
- generations from text;
- edits of existing images;
- reference-image generation;
- mask-guided edits;
- Responses API image generation;
- multi-turn image editing.

Source:
https://developers.openai.com/api/docs/guides/image-generation

Imago's plugin should remain model-name agnostic because image model names and routing change over time.

## Plugin submission

Current OpenAI public-directory limits include:
- display name <= 30 chars;
- subtitle <= 30 chars;
- long description <= 4,000 chars;
- <= 20 capabilities, each <= 120 chars;
- <= 3 starter prompts, each <= 128 chars;
- supported category `Creativity`;
- verified developer/business identity;
- safety/security scans for bundled skills.

Skills-only ZIP uploads can omit remote-MCP URLs and do not need an MCP server.

Sources:
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Migration decision

Do not preserve stale model-specific wording from earlier Imago versions.

The plugin should preserve the durable behavior:
1. visual-first;
2. generate/edit directly;
3. inspect real references;
4. minimize unnecessary clarification;
5. choose a sensible format/aspect ratio;
6. preserve unaffected details during edits;
7. use exact user copy;
8. never fabricate factual/data values;
9. research current facts before factual visuals;
10. never return fake file paths or text prompts as a substitute for requested visual output.

## Branding note

No canonical Imago logo asset was found in the available file library during this packaging pass.

The bundle therefore contains a neutral temporary square SVG icon. Replace it with the current Imago production icon before public submission if you have the original asset.
