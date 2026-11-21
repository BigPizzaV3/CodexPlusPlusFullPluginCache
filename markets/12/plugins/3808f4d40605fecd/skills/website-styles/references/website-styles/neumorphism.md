# Neumorphism

## Mandatory Brief Flow

Neumorphism adds no style-specific choice group beyond the shared [Mandatory Brief](../AGENTS.md). Record Neumorphism in the final restatement; do not invent a subtype.

Before building a homepage or landing page, read [Hero](../hero.md) and reproduce the complete Markdown table under **Choose the Structure** in the user-facing question, including both headers and every row with its full `Choose it when` guidance. Do not shorten, paraphrase, flatten it into a list, rename, filter, merge, preselect, or omit anything. Ask the user to choose exactly one structure or delegate the choice.

## Required Related Skills

This file must declare every directly related Alpy skill and supporting resource by exact name and Markdown path.

The declared list must match the dependencies returned by `get_alpy_skill`.

Required direct skills:

- [User Experience](../user-experience.md) — `skills/user-experience.md`
- [Balance](../ui-design/balance.md) — `skills/ui-design/balance.md`
- [Gestalt](../ui-design/gestalt.md) — `skills/ui-design/gestalt.md`
- [Hero](../hero.md) — `skills/hero.md`
- [Accessibility Audit](../accessibility-audit.md) — `skills/accessibility-audit.md`
- [Responsive Adaptation](../responsive-adaptation.md) — `skills/responsive-adaptation.md`
- [Grid and Layout](../ui-design/grid-layout.md) — `skills/ui-design/grid-layout.md`
- [Alignment](../ui-design/alignment.md) — `skills/ui-design/alignment.md`
- [Scale and Proportion](../ui-design/scale-proportion.md) — `skills/ui-design/scale-proportion.md`
- [Rhythm and Space](../ui-design/rhythm-space.md) — `skills/ui-design/rhythm-space.md`
- [Motion and Transition](../ui-design/motion-transition.md) — `skills/ui-design/motion-transition.md`
- [Visual Hierarchy](../ui-design/visual-hierarchy.md) — `skills/ui-design/visual-hierarchy.md`
- [Color Discipline](../ui-design/color-discipline.md) — `skills/ui-design/color-discipline.md`
- [Typography and Readability](../ui-design/typography-readability.md) — `skills/ui-design/typography-readability.md`
- [Border and Divider](../ui-design/border-divider.md) — `skills/ui-design/border-divider.md`
- [Elevation](../ui-design/elevation.md) — `skills/ui-design/elevation.md`

Required supporting resources:

- [Agent Instructions](../AGENTS.md) — `AGENTS.md`

Before using this file, recursively resolve and disclose all declared dependencies through [Skill Resolution](../AGENTS.md) and its approval flow.

This file cannot be used alone when related skills are declared. If any required file is missing, unread, unregistered, or not approved by the user, stop the affected work.

### UI Skill Coordination

Neumorphism owns only the visible material language: surface continuity, light direction, dual-shadow polarity, relief character, soft shapes, accent restraint, and contrast-cue intent.

Use [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Scale and Proportion](../ui-design/scale-proportion.md), [Rhythm and Space](../ui-design/rhythm-space.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Balance](../ui-design/balance.md), and [Gestalt](../ui-design/gestalt.md) for structure, spacing, proportion, priority, weight, and grouping. Use [Typography and Readability](../ui-design/typography-readability.md) for type, [Color Discipline](../ui-design/color-discipline.md) for exact palette and contrast roles, [Border and Divider](../ui-design/border-divider.md) for boundaries and radius, [Elevation](../ui-design/elevation.md) for canonical shadow values, and [Motion and Transition](../ui-design/motion-transition.md) for transitions.

[Hero](../hero.md), [User Experience](../user-experience.md), [Responsive Adaptation](../responsive-adaptation.md), and [Accessibility Audit](../accessibility-audit.md) own opening structure, semantics, reflow, and verification. Do not restate or override those skills here.

## Art Direction and Atmosphere

Create one quiet matte field from which selected objects appear softly molded, raised, or pressed. Neumorphism is same-material construction shaped by light—not pale cards floating over a gray page.

- Use one restrained accent family and crisp foregrounds to puncture the low-contrast material.
- Avoid glass transparency, glossy highlights, clay-like inflation, realistic texture, hard bevels, harsh shadows, and unrelated card colors.

## Material Composition

Neumorphism defines relief distribution, not layout mechanics.

- Let one broad flat material field dominate instead of stacking contrast cards.
- Concentrate relief around one focal mass or one coherent group; keep surrounding content flatter.
- Give equivalent peers one shared material treatment. Prefer one relieved parent over raised boxes inside raised boxes.
- Preserve the same material and light logic wherever the style appears; variety should come from content, scale, and relief role.

## Surface, Color, Light, and Depth

Neumorphism defines the relationship; [Color Discipline](../ui-design/color-discipline.md) and [Elevation](../ui-design/elevation.md) resolve supported values.

1. Use one dominant surface family. Neutral relieved forms should match their receiving field rather than become contrast cards.
2. Use a mid-tone light or dark field with enough tonal room for both a bright cue and a dark cue. Pure extremes usually flatten one side of the effect.
3. Choose one light axis for the complete composition. Every raised, inset, concave, and convex form must agree with it.
4. Keep perceived height low and edges diffuse. The material should feel softly molded, not detached or carved.
5. Retune the material, foreground, highlight, and shadow relationships independently for light and dark modes; never mechanically invert them.

## Dual Shadow and Relief States

The opposing light-and-dark pair is the defining construction. A single drop shadow, uniform halo, border-only card, or generic blur is not Neumorphism.

| Relief | Visual construction | Practical use |
|---|---|---|
| Flat | No decorative relief | Reading, navigation, repeated content, dense information |
| Raised / extruded | Exterior bright cue toward the light and soft dark cue opposite it | Focal product shell, media frame, compact control base |
| Inset / pressed | The same opposing pair rendered inside the edge | Input well, track, pressed or selected region with another visible cue |
| Convex | The face brightens toward the light and darkens away, creating an outward swell | One focal dial, orb, or hardware-like object |
| Concave | The tonal bend reverses across the face, creating a shallow hollow | One focal well, dial bed, or sculpted background object |

- Keep both cues opposed, soft, and proportionate; do not create equal halos around every edge.
- Scale shadow breadth with the form while preserving shallow relief. Exact values remain canonical.
- Apply relief to opaque material forms, not text, icons, or transparent artwork.
- Keep rest stable; hover may clarify the same relief, while pressed may move raised to inset. Preserve the footprint and light axis; [Motion and Transition](../ui-design/motion-transition.md) owns the transition.

## Contrast Cues

Soft relief is deliberately subtle, so shadow must never carry essential meaning alone.

- Pair boundaries, focus, selection, pressed, validation, and status with a supported border, fill, icon, label, indicator, or focus treatment.
- Prefer a filled accent primary action over a same-color raised pillow when stronger recognition is needed.
- If stronger shadows make the material dirty or hard, restore softness and add a clearer non-shadow cue.
- Mentally remove every decorative shadow: controls, states, hierarchy, and boundaries must remain visually understandable.

## Rounded Corners and Soft Shapes

Neumorphism uses a coordinated molded-shape family; [Border and Divider](../ui-design/border-divider.md) owns the exact supported radii and boundaries.

- Favor rounded rectangles, circles, pill tracks, soft arcs, and cropped rings.
- Let larger focal forms carry broader curves and smaller controls use tighter related radii.
- Use full pills and circles only when the anatomy calls for them; do not round every rectangle into a capsule.
- Keep peer shapes consistent. Avoid arbitrary corner families, sharp cutouts, decorative notches, and clay-like blobs.

## Typography, Iconography, and Media Treatment

These rules define visual character only; the linked typography, color, scale, and component skills retain their normal ownership.

- Keep text crisp, planar, and high-contrast. Never emboss, deboss, blur, glow, or shadow it.
- Keep icons simple and consistent. The glyph stays flat even when a relevant control uses a raised, inset, or circular well.
- Let photography, illustration, and genuine product UI retain useful color and detail. Apply relief to the opaque frame or stage, not the media itself.
- Keep media lighting compatible with the page light axis; do not surround strongly directional imagery with contradictory shadows.

## Practical Website Applications

- **Product or media focal:** After [Hero](../hero.md) and [Visual Hierarchy](../ui-design/visual-hierarchy.md) establish the subject, place one genuine product view, illustration, or image in a broad raised shell; keep internal details flatter.
- **Feature or proof group:** Use one relieved parent around the group instead of raising every repeated card.
- **Input or interactive demo:** Use an inset well only when the canonical field keeps its label, boundary, value, focus, and state cues.
- **Hardware-like moment:** Use a circular raised, inset, convex, or concave form for a relevant dial, player, calculator, or device control—not as generic decoration.
- **Primary action:** Use a clear filled accent treatment when a same-material control would disappear into the field.

## Canonical Resolution

Do not copy literal colors, radii, offsets, blur, opacity, gradients, or shadows from references. This skill defines the visible relationships and character; the linked UI skills and canonical Alpy system supply supported components and values.

## Mandatory Visual Compliance Check

Approve the rendered style only when every condition is visible:

1. One continuous matte material family anchors the composition.
2. One coherent light axis controls every relieved form.
3. Raised and inset forms use an opposing dual-shadow relationship and read differently at a glance.
4. Flat space dominates; there is no grid of nested, equal-weight pillows.
5. Crisp foregrounds, restrained accent, boundaries, focus, and state cues remain clear without shadow; text, icons, and media stay planar.
6. Rounded rectangles, circles, tracks, and sculpted forms belong to one soft-shape family.
7. Light and dark modes each preserve the material rather than using mechanical inversion.
8. Wherever the style is applied, it remains recognizably Neumorphic without drifting into glass, clay, or realistic skeuomorphism.

If any condition fails, revise the art direction or do not use Neumorphism for that region.
