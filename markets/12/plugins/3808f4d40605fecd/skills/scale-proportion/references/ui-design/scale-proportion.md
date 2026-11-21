# Scale and Proportion

## Required Related Resources

- [Canonical Components](../canonical/components.md) — supported size variants, anatomy, properties, states, icons, media ratios, and behavior.
- [Foundations](../canonical/foundations.md) — canonical size and number mappings.

## Purpose

Make complete regions, groups, standalone content, and media appropriately sized for their role, content, and use.

Scale and Proportion owns sizing behavior, relative outer size, usable minimum and maximum bounds, [supported component size selection](../canonical/components.md), and meaningful media proportions. It receives importance from [User Experience](../user-experience.md), required prominence from [Visual Hierarchy](visual-hierarchy.md), regions and available space from [Grid and Layout](grid-layout.md), peer relationships from [Gestalt](gestalt.md), surrounding distance from [Rhythm and Space](rhythm-space.md), and text metrics from [Typography and Readability](typography-readability.md). [Balance](balance.md) evaluates the resulting distribution of visual weight.

It does not choose content priority, layout, text size, spacing, alignment, crop direction, [component anatomy](../canonical/components.md), or responsive transformation. A selected website style may influence size contrast and media shape only after the role is confirmed and only through [supported canonical options](../canonical/components.md). [Responsive Adaptation](../responsive-adaptation.md) owns transformations, and [Accessibility Audit](../accessibility-audit.md) verifies target size, zoom, text enlargement, reflow, and media resilience.

## Canonical Component Boundary

Treat every [canonical component](../canonical/components.md) as an indivisible unit. Select only [supported size variants, properties, states, icons, and media ratios](../canonical/components.md), and size compositions from component outer boundaries.

Never resize [internal text, icons, controls, targets, padding, or anatomy](../canonical/components.md); stretch, compress, or visually scale a [complete component](../canonical/components.md); or invent intermediate sizes. Resolve component number values through [canonical mappings](../canonical/foundations.md) and report unsupported size or proportion needs to the [canonical component system](../canonical/components.md).

## Core Rules

1. **Work outside in.** Judge frame → region → group → standalone content, then select [supported component sizes](../canonical/components.md). Never begin by resizing [component internals](../canonical/components.md).
2. **Choose behavior before dimensions.** Decide whether each subject is content-driven, fill, [fixed canonical](../canonical/components.md), bounded, or proportional before applying a width, height, or ratio.
3. **Let content determine growth.** Default to content-driven height. Fix a dimension only for a stable [canonical role](../canonical/components.md), a meaningful media shape, or a task that requires a persistent two-dimensional area.
4. **Make relative scale match confirmed roles.** Equal roles use equal scale; a larger treatment belongs only to a confirmed focal, selected, expanded, or task-critical subject. Use few clearly different levels.
5. **Bound for usability, not decoration.** Use minimum or maximum dimensions when reading, viewing, comparing, targeting, or manipulating becomes worse outside the bound. Do not enlarge content merely to fill a wide screen.
6. **Preserve meaningful proportions.** Use [supported media ratios](../canonical/components.md), keep repeated media comparable, and never distort content. A crop must preserve the approved subject and meaning.
7. **Transform before shrinking.** Do not scale down controls, content, or complete UI to repair insufficient space. Route changes in structure, stacking, visibility, or interaction to [Responsive Adaptation](../responsive-adaptation.md).
8. **Prove size with real conditions.** Test real copy, wrapping, dynamic data, loading, empty and error states, modes, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, input methods, and responsive results.

### Sizing Relationships

| Relationship | Decision |
|---|---|
| **Size** | Is the subject large enough for its content, purpose, and interaction? |
| **Scale** | Is its size appropriate beside peers, support, and the containing region? |
| **Proportion** | Do its dimensions preserve meaning, comparison, and intended shape? |

Judge all three in the rendered context. A subject may fit alone yet become too dominant, too weak, or distorted beside its neighbors.

### Sizing Behaviors

| Behavior | Use when |
|---|---|
| **Content-driven** | Text, forms, notices, cards, panels, or states need to grow with real content |
| **Fill available space** | A primary work area, media region, or collection benefits from its assigned [layout region](grid-layout.md) |
| **[Fixed canonical size](../canonical/components.md)** | A [component, icon, avatar, control, or target](../canonical/components.md) has a stable supported role |
| **Bounded** | A reading area, panel, chart, editor, map, or tool has a usable minimum or maximum |
| **Proportional** | An image, video, preview, diagram, or visualization has a meaningful shape |

Default to content-driven. Fix only the dimension that must remain stable; let the other follow content or available space. Never use scaling to conceal a layout or overflow problem.

### [Canonical Image Proportions](../canonical/components.md)

Use the [canonical Image component and its supported ratios](../canonical/components.md), selecting the proportion that best matches the content and its role.

| Shape | [Canonical ratios](../canonical/components.md) | Strong use |
|---|---|---|
| **Square** | `1:1` | Avatars, product thumbnails, and equal visual tiles |
| **Landscape** | `4:3`, `3:2` | General imagery, cards, and interface previews |
| **Wide** | `2:1`, `5:2`, `4:1` | Banners and wide feature media |
| **Video** | `16:9` | Video, demos, presentations, and product previews |
| **Portrait** | `4:5`, `3:4`, `2:3`, `1:2` | Portraits, posters, covers, and vertical editorial media |
| **Vertical video** | `9:16` | Mobile previews and vertical video |

Keep peer images consistent unless their content requires a different proportion. Never stretch media. Use an approved crop or alternate asset when a ratio would remove the subject; a placeholder may reserve the outer proportion but cannot replace essential content.

## How to Apply

### Scale and Proportion Pass

1. Receive confirmed importance, [prominence](visual-hierarchy.md), [regions](grid-layout.md), [peer relationships](gestalt.md), content, states, and [canonical support](../canonical/components.md).
2. Work frame → region → group → standalone content. Mark [complete components](../canonical/components.md), media, content-driven regions, and necessary bounds.
3. Select one sizing behavior per subject, compare it with peers and support, then choose the nearest [supported canonical variant](../canonical/components.md) or outer constraint.
4. Keep [component anatomy](../canonical/components.md) intact and route unresolved layout, type, spacing, crop direction, and responsive needs to their owners.
5. Test real conditions before [Responsive Adaptation](../responsive-adaptation.md) transforms the result and [Accessibility Audit](../accessibility-audit.md) verifies it.

### Frame and Shell

- Keep page, screen, and window regions usable from minimum through wide sizes. Headers, navigation, sidebars, footers, panels, and persistent tools use their [supported component sizes](../canonical/components.md); they do not grow merely because the viewport does.
- Let the main work region fill available space when the task benefits, while bounding reading areas, inspectors, and utility panels when excess width weakens use. [Grid and Layout](grid-layout.md) owns their placement and spans.
- Confirm that [supported expanded, focused, open, or selected states](../canonical/components.md) fit their assigned region. [Grid and Layout](grid-layout.md) owns placement, [Rhythm and Space](rhythm-space.md) owns clearance, and neither should be repaired by scaling neighboring controls.

### Content and Task Regions

- Size sections, heroes, articles, media, and product details around the confirmed subject. Focal content may be larger; explanation, evidence, and supporting media remain proportionate to their roles.
- Let forms, workflows, notices, errors, and completion states grow vertically with content. Choose a [supported field width](../canonical/components.md) that suggests the expected answer when available; do not make every short input fill its region.
- Bound reading, viewing, and editing areas when unrestricted size harms comprehension or operation. [Typography and Readability](typography-readability.md) owns text measure and sizes.

### Repeated and Data Regions

- Keep peer cards, list items, feed entries, results, comparisons, tiles, thumbnails, and previews comparable. Equal height is useful only for direct comparison and only when real content and states still fit.
- Preserve a minimum usable area for tables, charts, dashboards, maps, canvases, editors, and two-dimensional comparisons. When reflow would destroy meaning, [Responsive Adaptation](../responsive-adaptation.md) may keep scrolling local to that region.
- Do not enlarge a metric, chart, image, selected record, or live value unless its confirmed role changes. Loading placeholders should reserve the expected outer size without fixing variable content to that height.

### Layers, States, and Contexts

- Size dialogs, drawers, menus, popovers, tooltips, and feedback from their content, supported bounds, and available viewport. Long copy, errors, and translated actions expand or reflow instead of shrinking controls.
- Hover, focus, pressed, selected, disabled, open, dragged, loading, empty, success, warning, and error states may change outer size only through [supported canonical behavior](../canonical/components.md) or real content growth.
- Preserve image subjects, video controls, chart labels, map tools, and other essential details across ratios and modes. Do not depend on tiny details or text embedded in media.
- Recheck narrow and short containers, split windows, wide screens, zoom, text enlargement, dynamic data, localization, RTL, vertical writing, keyboard, pointer, touch, and responsive results through [Accessibility Audit](../accessibility-audit.md).

## Focused Audit

- Does each subject use the right sizing behavior and a scale matching its confirmed role?
- Do content, peers, states, and necessary work areas fit without clipping, distortion, or arbitrary fixed dimensions?
- Are [canonical components](../canonical/components.md) and [number mappings](../canonical/foundations.md) intact, with unsupported sizes or proportions reported?
- Do media ratios preserve subject and meaning without inconsistent peer treatment?
- Does the result survive real content, states, zoom, localization, input, and responsive transformation without shrinking essential UI?
