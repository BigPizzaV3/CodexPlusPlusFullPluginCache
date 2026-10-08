# AAC image guidance

## Prompt contract

Build one prompt per card in this order:

1. State the single intended meaning and the concrete subject or action.
2. Place the primary subject centrally and make it visually dominant.
3. Apply `visual_style`, `visual_complexity`, `concept_range`, and `sensory_constraints` from the selected profile.
4. Use a minimal, low-distraction background unless context is necessary to understand the meaning.
5. Keep style, viewpoint, line weight, lighting, and color treatment consistent across the card set.
6. End with: `No text, letters, captions, labels, logos, borders, or watermark in the image.`

For an action, distinguish actor, action, and object. For an emotion, include only the expression, posture, and simple context needed for recognition. Use one stable visual rule for abstract concepts.

## Ambiguity rule

If a requested label has multiple likely meanings, ask one question before prompt generation. Example: for `쉬기`, ask whether it means resting or using the toilet. Preserve the user's original label in HTML after clarifying its visual meaning.

## Fallback

When image generation is unavailable or fails, return the complete prompt for each card and request an uploaded `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, or `.svg` image. Continue to JSON and HTML generation after the host supplies file references.
