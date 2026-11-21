# Style control and meaningful iterations

A synthesis of the Givon owner materials (v2) and primary guides checked on 2026-09-07. These
are portable working methods: they do not prove that all models behave the same, and they do
not change the allowed inputs or settings.

## Express style through visible traits

Instead of a random set like "cinematic, masterpiece, 8K", choose coherent traits: palette,
light, contrast, texture, line character, grain or camera behaviour. Documentary footage,
catalogue product shots and stylized animation call for different decisions. Do not impose
smartphone realism when the user wants a glossy ad, and do not add a film look or camera shake
without a reason.

A style reference sets only the chosen style axes. Identity and product properties stay with
their own source. Stylization does not license importing a person, a prop, text or a plot from
the style sample.

## Fix the observed cause

1. Name the specific defect: face drift, an extra cut, wrong light, a halo around the hair, an
   altered logo or the wrong motion.
2. Check the source: motion blur, the direction of a pose, a raised foot, dust and other signs
   of motion can contradict the requested stillness. A blurry logo cannot be restored by
   confidently describing invented letters.
3. Change one cause and keep what worked. For drift, first check the reference and the action
   load; for extra cuts, the number of events and the duration; for a halo, the area of change,
   its edges and how the light matches.
4. If a new source or another operation is needed, explain why. Do not promise that adding
   "keep exact" will by itself fix the result.

When comparing variants where only the text changes, keep the model, the sources and the
settings the same. Do not run a new generation without the required permission. One lucky case
does not make a method guaranteed.

## Example of changing one axis

The original request keeps the product, action, camera and composition. Only the visual
treatment has to change:

```text
Replace only the look sentence with: restrained documentary treatment, muted
olive shadows, gentle highlight roll-off and fine film grain.
Keep the product's identity, geometry, action, camera path, composition and
light direction unchanged.
```

This is an editorial instruction for rebuilding a finished prompt. A user who asks for the
finished text gets the full updated version, not just the diff. A fixed length, the English
language, a negative block and timecodes are not universal rules: follow what the chosen model's
guide and the task call for.

## Sources

- Runway image-to-video guide: https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide
- Google video prompt guide: https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
- Adobe video prompting: https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/writing-effective-text-prompts-for-video-generation.html
- Luma Modify guide: https://lumalabs.ai/learning-hub/how-to-use-modify-video
