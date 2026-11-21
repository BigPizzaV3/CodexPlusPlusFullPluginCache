# Gestalt

## Required Related Resources

- [Agent Instructions](../AGENTS.md) — required workflow, skill ownership, and canonical rules.
- [Canonical Components](../canonical/components.md) — supported component anatomy, properties, states, relationships, and behavior.

## Purpose

Make relationships immediately understandable in a website or interface: what belongs together, what is separate, which label, action, status, or feedback belongs to which subject, and where a sequence continues.

Gestalt owns perceived grouping and separation. It receives task and content relationships from [User Experience](../user-experience.md), structural placement and reading order from [Grid and Layout](grid-layout.md), perceptual priority from [Visual Hierarchy](visual-hierarchy.md), shared edges from [Alignment](alignment.md), exact spacing from [Rhythm and Space](rhythm-space.md), coordinated movement from [Motion and Transition](motion-transition.md), visual roles from [Color Discipline](color-discipline.md), boundary treatment from [Border and Divider](border-divider.md), and layer treatment from [Elevation](elevation.md). [Responsive Adaptation](../responsive-adaptation.md) owns transformations, and [Accessibility Audit](../accessibility-audit.md) verifies that visible relationships also exist in structure, labels, and behavior. A selected website style may shape character but must not change relationship meaning.

## Canonical Component Boundary

Treat every [canonical component](../canonical/components.md) as an indivisible unit. Apply Gestalt to the composition between components, their supported relationships, outer boundaries, and standalone content.

Do not rebuild anatomy, reorder internals, wrap a component to simulate a group, or add local relationship cues. Use exposed properties and supported variants or states; report missing coverage to the canonical system.

## Core Rules

Use the Gestalt principles as practical relationship rules, not as effects to apply everywhere. Most relationships need only one or two principles.

### Gestalt Relationships

| Principle | Practical rule |
|---|---|
| **Proximity** | Place related items closer together than unrelated groups. Keep each label, action, status, help message, and error with its subject; [Rhythm and Space](rhythm-space.md) owns the distances. |
| **Similarity** | Give elements with the same role or behavior a consistent appearance. Do not make navigation, destructive actions, passive metadata, selectable rows, and ordinary text look interchangeable. |
| **Common region** | Use a shared [surface](color-discipline.md) or [boundary](border-divider.md) when [spacing](rhythm-space.md) and a label cannot explain a durable group such as a card, panel, grouped form question, or bounded tool. Do not contain every section, row, or metric. |
| **Connectedness** | Use a [line or connector](border-divider.md) only for a real hierarchy, dependency, sequence, or explicit relationship. Decorative connections must not imply workflow, ownership, or causality. |
| **Continuity** | Use [shared edges](alignment.md) and directional flow to support a real reading path, navigation route, sequence, or task progression. Do not create a visual path that conflicts with [content or task order](grid-layout.md). |
| **Closure** | Partial or cropped forms may suggest continuation when the whole remains obvious. Never make essential content, direction, meaning, or action depend on inference. |
| **Figure and ground** | Keep active content, controls, selected objects, overlays, and layered surfaces distinguishable from their surroundings. Route treatment to [Color Discipline](color-discipline.md), [Border and Divider](border-divider.md), and [Elevation](elevation.md). |
| **Common fate** | Coordinate state or [motion](motion-transition.md) only when items form one selected set, dragged group, reordered collection, or shared system outcome. Keep unrelated items perceptually stable. |

Apply the principles to a real content, task, state, sequence, or ownership relationship first. Use the fewest cues that make it clear: proximity and a shared label, then stronger [separation](rhythm-space.md), a [boundary or connector](border-divider.md) only when the relationship still fails. Gestalt selects the cue; the owning skills select its values and treatment.

Preserve the relationship through content, state, localization, zoom, and [responsive changes](../responsive-adaptation.md). Visual grouping never replaces [semantic structure, labels, or behavior](../accessibility-audit.md).

## How to Apply

### Gestalt Pass

Work outside in: frame, region, group, then standalone content.

1. Identify each subject and what belongs to it.
2. Choose the smallest principle cue that makes the relationship clear. Do not use Gestalt to repair unresolved [structure](grid-layout.md), [perceptual priority](visual-hierarchy.md), or missing [canonical component](../canonical/components.md) coverage.
3. Stop when the relationship reads correctly. Route [spacing](rhythm-space.md), [motion](motion-transition.md), [alignment](alignment.md), [color](color-discipline.md), [boundaries](border-divider.md), [elevation](elevation.md), [responsive transformation](../responsive-adaptation.md), and [accessibility verification](../accessibility-audit.md) to their owners.

### Frame and Shell

- **Proximity + common region:** Cluster brand, primary navigation, search, account, and utility actions in a site header; separate persistent shell controls from page filters. [Grid and Layout](grid-layout.md) places the clusters, and [Rhythm and Space](rhythm-space.md) sets their gaps.
- **Similarity:** Style peer destinations alike while keeping workspace switching, help, and sign-out distinct. [Color Discipline](color-discipline.md) and [Border and Divider](border-divider.md) own the treatment.
- **Continuity:** Keep current location, breadcrumbs, expanded branches, and footer heading-to-link paths clear after stacking. [Grid and Layout](grid-layout.md) owns reading order.

### Content and Task Regions

- **Proximity:** Keep hero heading, copy, action, and qualifier together; keep article headings with content, captions with media, and price, options, and purchase actions with the correct product.
- **Proximity + common region:** Keep label, input, help, validation, and recovery together. Give choice sets and repeated shipping or billing fields a visible group label; [Accessibility Audit](../accessibility-audit.md) verifies the semantic group.
- **Continuity + connectedness:** Use paths or connectors in checkout, onboarding, and progressive forms only for actual step order.
- **Closure:** Crop media or reveal a partial next item only when the complete content, action, and direction remain explicit.

### Repeated and Data Regions

- **Similarity + common region:** Give cards, list items, feeds, grids, and results consistent peer anatomy. Contain an item only when it acts as one unit; preserve [canonical component](../canonical/components.md) anatomy.
- **Proximity:** Keep search, filters, sort, count, selection actions, results, and pagination with their collection; keep chart title, range, unit, legend, and status with the chart.
- **Continuity + connectedness:** Keep table headers, records, totals, comparison attributes, timelines, and dependencies on their real path. [Alignment](alignment.md) owns shared edges.
- **Common fate:** Coordinate selection, drag, reorder, or batch-edit state only across affected records. [Motion and Transition](motion-transition.md) owns movement and timing.

### Layers, States, and Contexts

- **Proximity:** Anchor tooltips, popovers, menus, disclosures, and validation to their trigger or subject.
- **Figure and ground:** Keep dialogs, drawers, and active work areas distinct from the layer behind them. [Color Discipline](color-discipline.md), [Border and Divider](border-divider.md), and [Elevation](elevation.md) own the treatment.
- **Similarity:** Keep states attached to the same canonical component without making focus, selection, disabled, loading, success, warning, and error appear equivalent.
- **All principles:** Recheck real copy, wrapping, dynamic data, loading, empty and error states, modes, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, keyboard focus, pointer input, and responsive results. [Responsive Adaptation](../responsive-adaptation.md) transforms the composition; [Accessibility Audit](../accessibility-audit.md) verifies programmatic relationships.

## Focused Audit

- Can every label, action, status, message, and layer be assigned without guessing?
- Does each principle express a real relationship with no redundant or false cue?
- Are [canonical components](../canonical/components.md) intact and unsupported gaps reported?
- Do real content, states, modes, reflow, zoom, localization, and input preserve the same visible and [semantic grouping](../accessibility-audit.md)?
