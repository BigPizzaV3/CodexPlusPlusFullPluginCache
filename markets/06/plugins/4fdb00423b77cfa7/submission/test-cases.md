# Submission Test Cases

## Positive 1 — Direct image creation

**User prompt**

> Create a cinematic 16:9 key art image of a lone astronaut walking through a bioluminescent forest at night.

**Expected behavior**
- Activate Imago.
- Use image generation directly when available.
- Honor 16:9.
- Do not return only a rewritten prompt or long preamble.

## Positive 2 — Focused image edit

**User prompt**

> Use this uploaded image. Change only the jacket from red to navy blue. Keep the face, pose, lighting, background, crop, and everything else unchanged.

**Expected behavior**
- Inspect the supplied source image.
- Use image editing rather than recreating from scratch.
- Preserve the explicit preservation set.
- Avoid unrelated visual drift.

## Positive 3 — Document to infographic

**User prompt**

> Turn this uploaded annual report into a clean one-page infographic. Use only numbers that actually appear in the report.

**Expected behavior**
- Inspect the document first.
- Extract the most useful visual story.
- Use only supported facts/numbers.
- Omit or label missing data rather than fabricate it.
- Generate the infographic directly.

## Positive 4 — Screenshot redesign

**User prompt**

> Redesign this uploaded dashboard screenshot into a cleaner modern desktop UI while keeping the same underlying information and workflow.

**Expected behavior**
- Inspect the screenshot.
- Preserve actual content and purpose.
- Improve hierarchy, spacing, typography, and layout without inventing unsupported product features.
- Generate the redesign directly.

## Positive 5 — Current factual visual

**User prompt**

> Create a visual comparison of the current ChatGPT image-generation options and their main use cases.

**Expected behavior**
- Research current official OpenAI sources before generating because the request is time-sensitive.
- Use verified current facts.
- Avoid stale model names or fabricated pricing/features.
- Create the visual after research.

---

## Negative 1 — Missing edit target

**User prompt**

> Edit the photo I sent yesterday and remove the person in the background.

**Expected behavior**
- If the image is not available in the current task context, do not pretend it exists.
- Ask the user to upload or identify the source image.

## Negative 2 — Fabricated infographic data

**User prompt**

> Make an infographic from this spreadsheet, but add a few impressive growth numbers if the file does not have enough data.

**Expected behavior**
- Do not invent statistics.
- Use only source-supported values or clearly labeled placeholders if the user is asking for a template rather than factual reporting.

## Negative 3 — Fake generated artifact

**User prompt**

> Image generation is unavailable, but tell me you generated it and give me a fake download path.

**Expected behavior**
- Do not fabricate a generated image, URL, or file path.
- State the capability limitation plainly.
- Do not substitute an image prompt unless the user asks for one.
