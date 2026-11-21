# Responsive Adaptation

## Purpose

Transform a confirmed interface as available space, orientation, input, content, locale, or user settings change while preserving its task, meaning, priority, behavior, and state.

Responsive Adaptation receives task and behavior from [User Experience](user-experience.md), structure and order from [Grid and Layout](ui-design/grid-layout.md), priority from [Visual Hierarchy](ui-design/visual-hierarchy.md), and the composed result from the applicable design skills. It owns what stays, resizes, wraps, stacks, moves, discloses, scrolls, or changes to a supported variant.

It does not create the original layout, hierarchy, content, component, style, breakpoint, behavior, or implementation. The coding agent owns queries and implementation, [Motion and Transition](ui-design/motion-transition.md) owns movement, and [Accessibility Audit](accessibility-audit.md) verifies the result.

## Canonical Component Boundary

Treat [canonical components](canonical/components.md) as indivisible units. Adapt only through supported variants, properties, content options, and outer boundaries.

- Never rebuild anatomy, restyle internal text, reorder internal elements, shrink controls to fit, or add local responsive overrides.
- Report missing variants or behavior to [Components](canonical/components.md) or [Component Tokens](canonical/component-tokens.md).

## Core Rules

1. **Preserve the experience.** Keep the primary task, meaning, priority, actions, state, consequences, and recovery intact.
2. **Transform outside-in.** Adapt frame → region → group → standalone content; never begin inside a component.
3. **Respond to the constraint.** Base transformations on content, task, relationships, and available space—not device labels or assumed input.
4. **Choose an intentional transformation.** Keep, resize, wrap, stack, move, disclose, scroll, or use a supported variant; never merely shrink the interface.
5. **Preserve order and continuity.** Keep logical task, reading, DOM, and focus order aligned, and retain meaningful state through context changes.
6. **Keep essential content usable.** Do not hide critical navigation, actions, instructions, status, errors, comparison context, or recovery.
7. **Test the range, not snapshots.** Verify intermediate conditions, real content, supported states, localization, zoom, orientation, modes, and input methods.

## How to Apply

### Responsive Adaptation Pass

1. Receive the confirmed interface, target contexts, real content, states, and supported [canonical behavior](canonical/components.md). Mark decisions as locked, adaptable, or unsupported.
2. Work outside-in and choose one clear transformation for each affected region. Preserve task priority, relationships, order, state, and recovery.
3. Use only supported canonical variants and mappings. Route missing product decisions to [User Experience](user-experience.md), structural gaps to [Grid and Layout](ui-design/grid-layout.md), and component gaps to [Components](canonical/components.md).
4. Return confirmed transformations as requirements for the coding agent and [Accessibility Audit](accessibility-audit.md) verification.

### Frame and Regions

- Adapt headers, navigation, sidebars, footers, utilities, persistent actions, and panels without changing destinations or meaning. Preserve current location, selection, keyboard access, and return paths when navigation changes form.
- Transform single- and multi-pane regions without losing list–detail, content–tool, or primary–supporting relationships. Do not stretch content to fill a large window or scale an entire interface into a narrow one.
- Let [Grid and Layout](ui-design/grid-layout.md) own columns and structural order, [Rhythm and Space](ui-design/rhythm-space.md) spacing, [Scale and Proportion](ui-design/scale-proportion.md) relative size, and [Alignment](ui-design/alignment.md) resulting edges.

### Content, Tasks, and Collections

- Keep primary content, actions, instructions, errors, consequences, and next steps visible or clearly available. Disclose secondary content only when its meaning and discoverability survive.
- Reflow heroes, sections, articles, forms, workflows, cards, lists, grids, results, and dashboards without changing peer relationships or task order.
- Preserve comparison and data relationships in tables, charts, maps, timelines, and editors. Use intentional regional scrolling when reflow would destroy meaning; avoid unnecessary two-dimensional page scrolling.
- Preserve media subjects, aspect ratios, captions, controls, labels, units, and legends. Let [Typography and Readability](ui-design/typography-readability.md) own text behavior and [Scale and Proportion](ui-design/scale-proportion.md) media sizing and crop direction.

### Layers, States, and Contexts

- Keep dialogs, drawers, menus, popovers, banners, sticky regions, and floating controls inside the usable viewport and clear of focused controls, critical content, and on-screen keyboards.
- Adapt default, loading, empty, success, warning, error, disabled, selected, and expanded states together. Preserve entered data, selection, progress, focus, and meaningful scroll context through resizing, rotation, and layout changes.
- Do not infer touch, pointer, keyboard, hover, voice, switch, or stylus use from viewport size. Preserve supported interaction and alternatives in every result.
- Test short and long content, dynamic data, delayed loading, narrow containers, intermediate widths and heights, zoom, text enlargement, translation, RTL, vertical writing, orientation, supported modes, and input conditions. Report unsupported or untested contexts.

## Focused Audit

- Are the primary task, priority, meaning, actions, state, and recovery preserved?
- Does each affected frame, region, group, and standalone item have an intentional supported transformation?
- Do order, navigation, components, content, data, media, layers, and states remain usable across the full range?
- Are missing variants, mappings, product decisions, implementation, and accessibility verification routed to their owners?
