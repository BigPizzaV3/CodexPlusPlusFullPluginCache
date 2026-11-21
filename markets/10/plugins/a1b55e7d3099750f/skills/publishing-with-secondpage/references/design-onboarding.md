# Design onboarding notes

SecondPage's current publish contract is static files. Treat design preferences
as authoring context: ask only when useful, carry the answers into the HTML/CSS
files you generate, and do not claim that the preference was saved globally
unless a separate product surface has actually saved it.

## When to ask

Ask about taste only when the Page would benefit from a stronger visual
direction and the user's intent is not already clear. Do not block publishing.

Good prompts are short and concrete:

- "Should this feel more like a quiet memo, an editorial page, or a dense dashboard?"
- "Do you want this airy and premium, or compact and operational?"
- "Any hard no's: stock photos, gradients, loud colors, tiny text, heavy cards?"

## What to capture

Use these dimensions as private drafting guidance:

- **Character:** analytical, bold, calm and premium, editorial, playful, utilitarian, or whatever the user's own words suggest.
- **Density:** airy, balanced, compact.
- **Voice:** quiet factual labels, warm direct copy, energetic headings.
- **Exclusions:** stock imagery, decorative gradients, cluttered cards, marketing tone.
- **Use case:** report, itinerary, dashboard, comparison, guide, visual explainer.

Map the answer into the generated bundle:

```css
:root {
  /* Name the direction the user actually chose,
     e.g. quiet-editorial, playful-bold, or dense-operational. */
  --page-density: balanced;
  --page-tone: playful-bold;
}
```

## Link-based inspiration

If the owner gives public websites or images as examples, use them as inspiration
for the current Page only unless a separate saved-profile flow exists. Borrow
palette, spacing, density, typography feel, and layout cues. Do not copy logos,
proprietary text, exact hierarchy, brand names, or source imagery.

## After Edits

If the user repeatedly asks for the same design change, apply it to future
Pages you author in that organization context. Until the product has a live
profile persistence contract, keep that as agent-side context rather than a
stored SecondPage setting.
