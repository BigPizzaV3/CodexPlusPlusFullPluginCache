# Bold Typography

## Mandatory Brief Flow

When the user selects Bold Typography, present every composition character listed below, grouped as base, static support, and motion. Do not filter or silently select from the list. Ask the user to choose ehat they want before composing the design.

Before building a homepage or landing page, read [Hero](../hero.md) and reproduce the complete Markdown table under **Choose the Structure** in the user-facing question, including both headers and every row with its full `Choose it when` guidance. Do not shorten, paraphrase, flatten it into a list, rename, filter, merge, preselect, or omit anything. Ask the user to choose exactly one structure or delegate the choice.

## Required Related Skills

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

Resolve these dependencies through `get_alpy_skill` and the shared approval flow in [`AGENTS.md`](../AGENTS.md).

### UI Skill Coordination

Bold Typography owns focal display character: the narrow display exception, line-group composition, crop and overlap character, and the selected composition characters.

[Typography and Readability](../ui-design/typography-readability.md) owns type roles, family, weight, metrics, line formation, wrapping, and readability. [Visual Hierarchy](../ui-design/visual-hierarchy.md) owns perceptual rank; [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Rhythm and Space](../ui-design/rhythm-space.md), [Balance](../ui-design/balance.md), and [Gestalt](../ui-design/gestalt.md) own composition mechanics; [Scale and Proportion](../ui-design/scale-proportion.md) owns only non-type proportions.

[Color Discipline](../ui-design/color-discipline.md), [Border and Divider](../ui-design/border-divider.md), and [Elevation](../ui-design/elevation.md) own supporting color, boundaries, and layer relationships; [Motion and Transition](../ui-design/motion-transition.md) owns movement. [Hero](../hero.md), [User Experience](../user-experience.md), [Responsive Adaptation](../responsive-adaptation.md), and [Accessibility Audit](../accessibility-audit.md) own opening structure, content and behavior, transformation, and verification.

## Purpose

Make language the primary visual material. Bold Typography is a treatment: it changes display hierarchy and composition, not canonical components or product behavior.

The style requires unmistakably oversized live typography in its focal regions. If reducing the headline to an ordinary page title would leave the composition substantially unchanged, the treatment is not Bold Typography.

## Display Typography Exception

Bold Typography authorizes one narrow exception: short focal display statements may exceed canonical headline size and adjust line height and letter spacing. [Typography and Readability](../ui-design/typography-readability.md) resolves the complete treatment; ordinary headings, body copy, navigation, controls, labels, forms, and data remain canonical.

Keep the canonical headline family and weight unless the user explicitly confirms an alternative. Bold means visually dominant, not heaviest: let size create the impact while counters and words remain recognizable.

## Fluid Desktop Scale

Use final copy and two to five meaningful line groups. Let focal type grow continuously across desktop within bounded, zoom-respecting limits so the longest line fills most of its region without clipping while text-media balance and negative space remain stable. Check the smallest, middle, and largest widths for jumps or dead space.

### Headline Size Recommendation

| Display role | Desktop starting band | Use |
|---|---:|---|
| Primary focal statement | `12–16vw` | Lower for wider faces or longer lines; higher for condensed faces or short words. |
| Supporting display moment | `5–8vw` | Keep below the opening scale unless it forms a deliberate second climax. |

Rendered words decide; the bands are starting guidance, not fixed values.

[Typography and Readability](../ui-design/typography-readability.md) owns metrics and line formation, [Grid and Layout](../ui-design/grid-layout.md) the available region, [Balance](../ui-design/balance.md) and [Rhythm and Space](../ui-design/rhythm-space.md) the visual mass and negative space, [Scale and Proportion](../ui-design/scale-proportion.md) non-type proportions, and [Responsive Adaptation](../responsive-adaptation.md) transformations. Mobile may recompose the lines, but the live heading must remain one coherent statement in reading order.

## Composition

Apply [Hero](../hero.md) to the opening structure and [User Experience](../user-experience.md) to content and purpose. Apply [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Rhythm and Space](../ui-design/rhythm-space.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Balance](../ui-design/balance.md), and [Gestalt](../ui-design/gestalt.md) to the composition.

Use a typographic poster for the opening. Later focal sections may use a typographic poster or oversized index as their base. Add no more than one static support and one optional motion character. Repeat a small combination across the page instead of inventing a new trick for every section.

Select from the section's actual content and purpose. When several characters fit, use the simplest static option. Add motion only when it improves the relationship or sequence, not merely for spectacle.

| Section need | Select |
|---|---|
| One strong proposition | Typographic poster |
| Services, projects, or categories | Oversized index |
| Image should interrupt the phrase | Embedded media |
| Image and headline should share one focal plane | Layered media |
| Create scale without media | Edge crop |
| Attach proof, context, metric, or action | Attached microcopy |
| Repeat secondary names or capabilities | Traveling type |
| Keep a statement while supporting content changes | Pinned statement |
| Create depth between related text and media | Parallax relationship |
| Build emphasis through an existing sentence | Progressive reveal |

| Composition character | Role | Practical guidance |
|---|---|---|
| **Typographic poster** | Base | Let one short statement fill most of the region and act as its main image. Keep navigation, explanation, and actions clearly secondary. |
| **Oversized index** | Base | Use large service, category, or project names as full-width rows or section dividers when a list needs more presence than cards. |
| **Embedded media** | Static support | Insert one meaningful image between complete words or lines, or inside deliberate punctuation. Preserve the message and recognizable subject. |
| **Layered media** | Static support | Place one image over or behind the headline while every required word remains readable. Remove the overlap before weakening the message. |
| **Edge crop** | Static support | Let outer letterforms or decorative brand fragments leave the canvas to intensify scale. Never crop complete words or essential meaning. |
| **Attached microcopy** | Static support | Anchor an eyebrow, caption, metric, proof point, or primary action to the display mass instead of scattering small text around the canvas. |
| **Traveling type** | Motion | Move redundant names, capabilities, credits, or atmosphere through a strip. Never move the primary proposition, evidence, or action. |
| **Pinned statement** | Motion | Hold one short headline while related media or supporting copy passes through the section, then release it before the next content block. |
| **Parallax relationship** | Motion | Let headline, media, and supporting copy travel at different rates only when the changing relationship adds depth and reading order remains clear. |
| **Progressive reveal** | Motion | Reveal complete words or lines, or shift emphasis across an already complete sentence. The final message must remain available without motion. |

[Motion and Transition](../ui-design/motion-transition.md) is optional. Every composition must remain complete and intentional in its resting and reduced-motion states.

Only the motion character is optional; [Motion and Transition](../ui-design/motion-transition.md) remains the owner whenever traveling, pinned, parallax, or reveal treatment is selected.

Compose with final copy. Do not split words, position individual letters, manufacture filler language, or let media and effects become stronger than the statement.

## Focused Audit

Apply [Typography and Readability](../ui-design/typography-readability.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Responsive Adaptation](../responsive-adaptation.md), and [Accessibility Audit](../accessibility-audit.md) to the rendered verification.

Inspect the smallest, middle, and largest supported desktop widths plus mobile. The focal statement must remain unmistakable, fluid, fully readable, and compositionally dominant without clipping, abandoned space, or breakpoint jumps. Reject ordinary layouts with merely large headings or repeated oversized sections.
