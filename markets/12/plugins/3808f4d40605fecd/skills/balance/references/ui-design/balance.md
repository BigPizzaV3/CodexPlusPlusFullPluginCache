# Balance

## Required Related Resources

- [Agent Instructions](../AGENTS.md) — `AGENTS.md`

## Purpose

Distribute visual weight across already-established regions so the confirmed hierarchy feels stable, intentional, and appropriate to the selected website style.

Balance owns dominant, supporting, and equal weight relationships between complete regions. It receives perceptual priority from [Visual Hierarchy](visual-hierarchy.md), regions and structural hierarchy from [Grid and Layout](grid-layout.md), groups from [Gestalt](gestalt.md), spacing from [Rhythm and Space](rhythm-space.md), and moving behavior from [Motion and Transition](motion-transition.md). Size, color, alignment, responsive behavior, and character remain with their owning skills and the selected website style.

## Canonical Component Boundary

Treat every [canonical Alpy component](../canonical/components.md) as one indivisible unit. Judge only its outer visual weight within the surrounding composition.

- Never alter component anatomy, [styling](../canonical/component-tokens.md), order, grouping, alignment, or size to repair balance.
- Do not add wrappers, fillers, fixed heights, decorative counterweights, or local variants. Report missing canonical coverage.

## Core Rules

1. Reinforce the focal, supporting, and peer roles confirmed by [Visual Hierarchy](visual-hierarchy.md) and placed by [Grid and Layout](grid-layout.md). Equal roles need comparable weight; supporting regions must not compete with the focal region.
2. Judge regions by perceived weight, not object count. Footprint, contrast, saturation, imagery, detail, combined mass, density, isolation, motion, and edge position all matter.
3. Use one clear balance model per section or task region. Treat open space as part of the composition; never fill it with decoration or stretched content.
4. Preserve canonical components and familiar task patterns. Expressive balance must not disrupt navigation, forms, toolbars, tables, dialogs, or repeated controls.
5. Recheck real content, states, modes, and approved responsive results. Never preserve a desktop silhouette at the cost of content or usability.
6. Diagnose the cause of imbalance and send the correction to its owner. Balance does not change structure, grouping, spacing, scale, color, alignment, hierarchy, or responsive behavior.

## Choose the Balance Model

| Model | Real UI use | Balance test |
|---|---|---|
| **Symmetrical** | Centered tasks or true peer comparisons | Comparable regions feel equally present around a shared axis. |
| **Asymmetrical** | Heroes, media pairings, or primary and supporting panes | One confirmed focal region leads; the rest counter it without taking the first read. |
| **Mosaic** | Card feeds, galleries, marketplaces, or peer dashboards | Weight is distributed across the field. A featured tile creates local asymmetry and requires confirmed hierarchy. |
| **Radial** | A real center-based control, relationship, or data view | Supporting regions orbit a meaningful center. Never use it for ordinary reading, navigation, forms, or task flows. |

## How to Apply

### Balance Pass

1. Receive confirmed roles, regions, groups, spacing, components, and website style from their owners.
2. Weigh each complete region or perceptual group as one unit at normal and thumbnail size. Identify the first read, competitors, and purposeful open space.
3. Name the cause of any mismatch and route it to the owning skill; never counterbalance unrelated children or component internals.
4. Repeat with real content, states, modes, and every approved responsive result.

### Frame and Shell

- Balance main content against the complete header, navigation, sidebars, footer, panels, and persistent UI. Banners, cookie notices, sticky actions, and support tools must not overpower the task.
- Across long pages, keep repeated calls to action and alternating sections from competing. Let the footer close the page without becoming an unintended focal region.
- On wide screens, preserve the established composition instead of scattering regions or adding empty counter-columns. [Grid and Layout](grid-layout.md), [Alignment](alignment.md), and [Rhythm and Space](rhythm-space.md) own placement, references, and separation.

### Content and Task Regions

- Reflect each region's confirmed focal point or equal peers. In heroes, articles, documentation, product details, forms, onboarding, and checkout, keep primary content or tasks ahead of supporting media, sidebars, summaries, and trust content.
- Judge text, media, and canonical components as complete regions. Route weight caused by relative size, type, color, spacing, or hero treatment to [Scale and Proportion](scale-proportion.md), [Typography and Readability](typography-readability.md), [Color Discipline](color-discipline.md), [Rhythm and Space](rhythm-space.md), or [Hero](../hero.md).
- Preserve task order from [User Experience](../user-experience.md). Do not use decorative symmetry, filler, fixed heights, or hidden content to repair balance.

### Repeated and Data Regions

- Keep peer cards, lists, feeds, results, products, plans, comparisons, gallery items, and rows comparable. A featured item may be heavier only when confirmed by hierarchy.
- Judge mosaics, dashboards, tables, and charts as complete fields. Filters, legends, pagination, annotations, and actions must not compete with the content they support.
- Balance canonical collections only by outer boundaries. Do not alter anatomy, clip content, assign random spans, or make every item distinctive.

### Layers, States, and Contexts

- Judge dialogs, sheets, drawers, menus, popovers, banners, and toasts as complete regions. [Elevation](elevation.md), [Grid and Layout](grid-layout.md), and canonical components own their layering and placement.
- Keep loading, empty, error, success, permission, focus, hover, disabled, selected, and expanded states proportional to the region they explain. State graphics must not outweigh the next useful action.
- Treat autoplay, animation, live data, and notifications as added weight. Route competing movement to [Motion and Transition](motion-transition.md) and behavior or emphasis to its owner.
- After [Responsive Adaptation](../responsive-adaptation.md), judge each result independently. Verify narrow containers, reflow, zoom, 200% text enlargement, long copy, translation, RTL and vertical writing, dynamic data, modes, and states through [Accessibility Audit](../accessibility-audit.md).

## Focused Audit

- Does weight match the confirmed focal, supporting, and peer roles?
- Are equal regions comparable without forced uniformity or clipped content?
- Is any region dominant because of unintended contrast, density, imagery, motion, isolation, or position?
- Are open space, task patterns, and canonical components intact?
- Does every state and responsive result remain balanced, with corrections assigned to their owners?
