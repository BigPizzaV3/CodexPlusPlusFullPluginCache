# Elevation

## Required Related Resources

- Use [Components](../canonical/components.md) and [Component Tokens](../canonical/component-tokens.md) when a canonical component owns the surface, variant, state, or effect.
- Use [Semantic Tokens](../canonical/semantic-tokens.md) to resolve the complete Shadow styles available for standalone surfaces in the explicit mode.

## Purpose

Use perceived depth to clarify when one interface surface is resting, raised, overlapping, moving above, or covering another surface.

Elevation owns whether a standalone surface needs perceived lift and, when supported, selects one complete canonical [Shadow style](../canonical/semantic-tokens.md). It receives structure from [Grid and Layout](grid-layout.md), required prominence from [Visual Hierarchy](visual-hierarchy.md), grouping from [Gestalt](gestalt.md), surface color and mode roles from [Color Discipline](color-discipline.md), required edges from [Border and Divider](border-divider.md), spacing from [Rhythm and Space](rhythm-space.md), moving plane behavior from [Motion and Transition](motion-transition.md), and transformed results from [Responsive Adaptation](../responsive-adaptation.md). [Accessibility Audit](../accessibility-audit.md) verifies the result without relying on shadow. The selected website style may supply character only through supported canonical treatments.

Elevation does not own stacking order, modality, focus, interaction behavior, surface color, boundaries, grouping, priority, or responsive transformation.

## Canonical Component Boundary

[Canonical components](../canonical/components.md) own their internal elevation, material, effects, variants, and states. Preserve the exact [component-token binding](../canonical/component-tokens.md); never rebuild anatomy, wrap a component to simulate lift, replace its effect, or add a local shadow.

For standalone surfaces, select one complete Shadow style available in [Semantic Tokens](../canonical/semantic-tokens.md) for the explicit `light` or `dark` mode. Never decompose, alter, or locally recreate it with raw values, direct `color.shadow.*` use, custom filters or glows, invented layers, or a local elevation scale.

Apply Shadow styles only to interface surfaces, never to text, icons, or transparent artwork unless a canonical component defines the effect. If the required component, variant, state, mode, effect binding, or standalone Shadow style is unavailable, report the canonical gap instead of approximating it.

## Core Rules

1. Name the actual surface relationship before selecting a Shadow style. Keep ordinary content flat and use the lowest supported style that makes real separation clear.
2. Keep resting planes few. Equivalent relationships use the same treatment; nesting alone never requires stronger elevation.
3. Apply one complete canonical style for the explicit mode. Never alter its offset, blur, spread, opacity, color, direction, or layers.
4. Remove elevation when overlap, movement, or separation remains clear through the confirmed surface, boundary, or composition. Never strengthen shadow to repair another skill's problem.
5. Change elevation only when a supported component state or confirmed interaction changes the surface relationship. Temporary lift returns to its canonical resting treatment after completion or cancellation.
6. Shadow is never the only cue for a boundary, focus, selection, validation, disabled state, hidden overflow, or modality. The interface must remain understandable when shadows are clipped, visually weak, or removed.

## How to Apply

### Elevation Pass

1. Receive confirmed components, structure, groups, priority, surfaces, boundaries, behavior, mode, and responsive results from their owners.
2. Work outside in: inspect the frame, major regions, groups, then standalone surfaces. For each candidate, name the receiving surface and whether the candidate rests on it, rises from it, overlaps it, or temporarily moves above it.
3. Keep the relationship flat when separation is already clear. When lift is required, resolve component-owned treatment first; otherwise select the lowest complete standalone Shadow style that communicates the relationship.
4. Compare equivalent relationships, reduce competing planes, preserve the complete active-mode style, and report unsupported coverage to the canonical or skill owner.

### Frame and Shell

- Keep page canvases, ordinary headers, navigation, sidebars, footers, adjacent panels, and persistent regions flat unless they genuinely overlap content.
- Elevate a sticky header, toolbar, rail, or floating shell control only while content passes beneath it and only through supported treatment. [Responsive Adaptation](../responsive-adaptation.md) owns whether the region becomes sticky, floating, edge-attached, or full-screen.
- Use surface change or a required edge for adjoining shell regions before adding depth. [Color Discipline](color-discipline.md) owns the surface relationship and [Border and Divider](border-divider.md) owns the edge.

### Content and Task Regions

- Keep articles, forms, workflows, product details, sections, and ordinary media on their containing plane. Do not elevate every region merely to create variety or emphasis.
- Use supported lift for a genuinely floating or overlapping standalone surface. Menus, popovers, dialogs, drawers, sheets, tooltips, and other component-owned layers keep their canonical treatment.
- Let the selected website style determine the character of hero or campaign imagery, then use a supported Shadow style only when the imagery is intentionally presented as a raised object. Never make decorative media look interactive.
- Loading, empty, error, success, warning, and validation content retain the current plane unless the confirmed state changes the surface relationship.

### Repeated and Data Regions

- Give peer cards, tiles, rows, results, plans, comparisons, and dashboard panels the same resting treatment. Elevate one only for a real movable, overlapping, or supported temporary state—not to imply rank, recommendation, selection, or status.
- Keep lists, feeds, tables, and dense data regions flat by default. Use a supported overflow or sticky-edge treatment only when content actually moves underneath and the relationship remains unclear after the owning boundary treatment.
- Restore dragged cards, rows, or tiles to their canonical resting treatment after drop or cancellation. Group related floating actions instead of creating several competing raised objects.

### Layers, States, and Contexts

- Use stronger perceived separation only for a real overlay relationship. Shadow does not establish document order, focus order, stacking order, dismissal, focus trapping, or modality; preserve canonical component behavior.
- Hover, pressed, focused, selected, open, dragged, and disabled states change elevation only when the supported state changes the plane relationship. [Motion and Transition](motion-transition.md) must agree with that change and settle into the correct resting state.
- Resolve the exact style independently for `light` and `dark`, then inspect the entire perimeter against its actual receiving surface, including colored regions, imagery, gradients, nested surfaces, and changing content. Never invert, tint, or strengthen a mode manually.
- After [Responsive Adaptation](../responsive-adaptation.md) changes a region to full-screen, edge-attached, stacked, or otherwise recomposed, re-evaluate whether lift still communicates a real relationship and choose only a supported resulting treatment.
- Test conditions that change a surface's size, edge, or direction: real copy and wrapping, dynamic data, loading, empty and error states, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, scrolling, and content growth. The result must not clip the shadow, focus treatment, or interactive content.
- Verify high-contrast and forced-color results through [Accessibility Audit](../accessibility-audit.md). Required boundaries, states, focus, and operation must remain clear when shadow is absent.

## Focused Audit

- Does every elevated surface have a real receiving surface and relationship, or can the shadow be removed?
- Are canonical components intact and every standalone treatment a complete supported Shadow style for the explicit mode?
- Do equivalent relationships use consistent treatment with few resting planes across real content and responsive results?
- Do temporary states return to rest without using elevation to imply priority, grouping, stacking, modality, focus, or status?
- Does the relationship remain clear when shadows are weak, clipped, or removed, with unsupported needs reported instead of patched?
