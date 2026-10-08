# Original card artwork

Generated with the built-in `image_gen` tool. Two independent generation calls; no input/reference images; no post-generation image edits. Generated PNGs copied into this project with alpha preserved.

## `astral-dragon.png`

Foreground celestial water dragon; transparent cutout. Generated at 1254 × 1254 pixels with alpha. Read-only Pillow inspection verified an alpha range of 0–255, including 642,629 fully transparent pixels.

Exact prompt:

```text
Use case: stylized-concept
Asset type: Foreground character layer for a premium original fantasy creature trading card with 3D parallax.
Primary request: Generate one original elegant celestial water dragon as a clean transparent PNG cutout with a genuine alpha channel.
Subject: A friendly but fierce collectible anime creature, pearly white and icy pale blue serpentine dragon body, navy and teal fin-like ears and wing fins, a long curling tail, glowing amber eyes, cyan crystal accents. Elegant expressive face, four small graceful clawed limbs, fantastical rather than realistic. Entire creature visible.
Style/medium: Luxurious Japanese fantasy trading card illustration, painterly rendering with fine ink contours and crystalline iridescence. Rich highly finished painted detail, collectible creature design.
Composition/framing: Centered square composition, dynamic S-shaped flying pose facing the viewer at a three-quarter angle. Head upper center, body arcs diagonally and tail curls around below, fins reach outward. Generous empty transparent margin around every wing tip and tail, absolutely no clipping.
Lighting/mood: Dramatic luminous cyan rim lighting and subtle warm gold highlights; white and pale-blue body remains clear against dark blue art.
Scene/backdrop: GENUINELY TRANSPARENT BACKGROUND. No ground, no shadow plane, no scenery, no colored background, no simulated checkerboard.
Constraints: Original creature; no existing franchise character; no text, letters, numbers, logos, card border, card frame, watermark, background, or extra creatures. Preserve real transparent alpha around and inside silhouette gaps. Single asset only.
```

## `astral-world.png`

Portrait celestial-ocean background. Generated at 1024 × 1536 pixels. The tool returned RGBA with partial alpha (range 7–246), so render it over a deep navy card base. The original alpha is preserved.

Exact prompt:

```text
Use case: stylized-concept
Asset type: Separate background artwork layer for an original premium fantasy creature trading card with 3D parallax.
Primary request: Portrait fantasy trading card background only, a moonlit celestial ocean with cobalt and teal waters, swirling blue clouds, distant small pale moon in the upper right, points of starlight and scattered gold dust. At the bottom, sea spray and luminous shimmering waves. Bright misty cyan opening through the center where a separate character will sit.
Style/medium: Rich detailed painterly Japanese fantasy trading card illustration, exquisite anime background painting, elegant atmospheric brushwork, sapphire and teal luminous water with gold sparks.
Composition/framing: Portrait 2:3 image, full-bleed environment filling the entire canvas. More contrast and detailed sweeping wave shapes at the edges, lighter misty cyan center, deep midnight blue at upper corners. A small moon high upper-right, no giant moon behind center. Clear flowing depth through layered distant clouds and near sparkling sea spray.
Lighting/mood: Moonlit magical cobalt night, radiant turquoise sea foam, flecks of warm gold, luxurious and cinematic.
Constraints: BACKGROUND ONLY. Absolutely no character, creature, dragon, person, animal, face, silhouette, card border, frame, text, letters, numbers, logos, or watermark. Single asset only.
```
