# Motion and Transition

## Required Related Resources

- [Canonical Components](../canonical/components.md) — supported states, event transitions, variants, properties, and built-in motion.

## Purpose

Use motion to explain change, preserve context, confirm response, show progress, and guide attention without delaying work.

Motion and Transition owns whether movement is appropriate and how a confirmed state change is expressed: transition model, direction, properties, choreography, timing, easing, interruption, reversal, continuous or scroll-linked behavior, and static or reduced-motion alternatives. It receives task behavior and feedback meaning from [User Experience](../user-experience.md), structure and reading order from [Grid and Layout](grid-layout.md), relationships from [Gestalt](gestalt.md), attention requirements from [Visual Hierarchy](visual-hierarchy.md), section pacing from [Rhythm and Space](rhythm-space.md), and plane changes from [Elevation](elevation.md).

It does not invent product behavior, states, navigation, hierarchy, layout, [component anatomy](../canonical/components.md), responsive transformations, style direction, or implementation. A selected website style may supply motion character without changing behavior or accessibility. [Responsive Adaptation](../responsive-adaptation.md) owns context transformations, the coding agent owns implementation, and [Accessibility Audit](../accessibility-audit.md) verifies motion, timing, controls, flashing, and alternatives.

## Canonical Component Boundary

[Canonical components](../canonical/components.md) own their internal state transitions, motion, timing, focus behavior, and reduced-motion support. Use only [supported variants, properties, states, and events](../canonical/components.md).

- Never animate, delay, reorder, wrap, or override [component internals](../canonical/components.md); replace [built-in motion](../canonical/components.md); or add local keyframes to simulate an [unsupported state](../canonical/components.md).
- For standalone content, prefer approved project or platform motion primitives. The starting bands below guide supported custom motion only; they do not authorize a local motion system.
- Report missing component motion, transition, interruption, control, or reduced-motion coverage to the [canonical system](../canonical/components.md).

## Core Rules

1. **Define the state pair first.** Name the trigger, before state, after state, changed subject, final focus, and interruption result before selecting movement.
2. **Make motion earn its place.** Use it only to clarify feedback, continuity, relationship, progress, orientation, or a confirmed low-frequency focal moment. Otherwise change instantly.
3. **Preserve cause and spatial logic.** Movement begins from the action or subject that caused it, follows the real layer or navigation relationship, and returns consistently. Equivalent events use equivalent transitions.
4. **Keep response immediate and interruptible.** Never delay input, focus, errors, announcements, dismissal, or the next action until animation finishes. New input takes priority; motion retargets from its current rendered state without a jump and preserves meaningful velocity when supported.
5. **Keep supported manipulation continuous.** Preserve the grab point and direct input relationship while an item moves. On release, use supported direction and projected trajectory—not release position alone—to choose a valid destination; use progressive resistance rather than a hard stop only where the confirmed interaction and [canonical component](../canonical/components.md) support it.
6. **Coordinate one event, not every element.** Give each event one lead, move affected peers together, and sequence only a meaningful order. Stagger must not delay repeated content or create several competing focal points.
7. **Match the property to the change.** Use opacity for nonspatial replacement, translation for directional entry or exit, scale for a shared subject or bounded expansion, and minimal state-property changes for feedback. Combine few properties and avoid unnecessary travel.
8. **Match rhythm to frequency, scale, and distance.** Frequent actions stay near-instant; larger or less frequent transitions may take slightly longer; exits clear faster than entrances. Expression never makes routine work feel slow.
9. **Restrict continuous, automatic, and scroll-linked motion.** Use it only when time, progress, demonstration, depth, or direct manipulation is essential. Preserve native scrolling, provide required control, and stop motion from competing after it communicates.
10. **Design the static and reduced result with the motion.** Meaning, order, state, and action must remain complete when movement is reduced, removed, paused, unsupported, or unfinished.
11. **Protect stability and performance.** Prefer small affected areas and properties that can remain smooth. Do not animate layout merely for spectacle or let loading, resizing, live data, localization, or delayed assets leave content in an incorrect state.

### Transition Choices

| Choice | Use when | Avoid when |
|---|---|---|
| **Instant** | The change is expected, frequent, or already clear. | Spatial continuity or consequential feedback would be lost. |
| **Fade or crossfade** | Content replaces content in the same place without meaningful travel. | Direction or origin is essential to understanding. |
| **Translate or slide** | Entry, exit, navigation, or disclosure has a real direction. | The element has no spatial relationship to that direction. |
| **Scale or expand** | One subject opens, closes, or changes detail in place. | Scaling text, controls, or large viewport areas would impair reading or comfort. |
| **Shared-subject transition** | The same object persists between a source and destination. | The subjects only look similar or the relationship breaks under responsive results. |
| **Reorder or direct manipulation** | Dragging, sorting, inserting, or removing uses supported continuous tracking and valid destinations. | The grab relationship, source order, focus, bounds, or destination cannot remain valid. |
| **Progress or restrained loop** | Work is genuinely continuing and a static state could look stalled. | The state is complete, indeterminate motion adds no information, or the loop competes with content. |
| **Scroll-linked** | Scroll position directly controls a confirmed comparison, sequence, or depth relationship. | Ordinary reading, navigation, or task completion would become motion-dependent. |

### Motion Rhythm

Use approved motion values when available. Otherwise, use these bands only as starting guidance for supported custom motion.

| Event | Starting duration |
|---|---:|
| Press, hover, or small feedback | `100–150ms` |
| Menu, tooltip, or small reveal | `150–250ms` |
| Drawer, dialog, or larger transition | `250–400ms` |
| Page-level or expressive transition | `400–600ms`, sparingly |

Larger elements and longer travel may need slightly more time. Entrances may orient; exits should clear sooner. Use easing that arrives clearly, leaves efficiently, and does not bounce, overshoot, or dramatize routine work. Start immediately after the trigger and never postpone critical feedback, focus, or announcements.

## How to Apply

### Motion and Transition Pass

1. Receive confirmed behavior, states, structure, relationships, priority, layers, [component support](../canonical/components.md), and style character from their owners.
2. Work frame → region → group → standalone content. Mark [component-owned motion](../canonical/components.md) before considering custom movement.
3. For each event, define trigger, state pair, subject, spatial relationship, focus result, interruption behavior, gesture attachment and release result when applicable, and static or reduced alternative.
4. Choose instant change or one Transition Choice, then set the smallest useful rhythm and choreography.
5. Test real content, repeated input, unfinished motion, states, modes, responsive results, localization, input methods, reduced motion, and performance; route unsupported needs to their owner.

### Frame and Shell

- Keep headers, navigation, sidebars, panels, footers, and persistent tools stable unless movement explains a real open, close, resize, or navigation relationship. Preserve the current page or task as the stationary reference.
- For route and view changes, reveal the destination without delaying its title, focus, or primary task. Use direction only when it reflects deeper, previous, next, or peer navigation; otherwise prefer an instant change or restrained fade.
- Keep native scrolling and browser controls intact. Sticky, pinned, parallax, typing, viewport-reveal, and page-transition treatments require confirmed value, a complete resting state, and a static or reduced result.

### Content and Task Regions

- Make press, selection, validation, submission, success, error, disclosure, and step changes respond immediately. Motion may reinforce the result but never substitute for the visible state, message, or recovery path.
- Open details, media, product views, and progressive disclosure from their source when that relationship matters. Keep headlines, instructions, fields, and primary actions readable before, during, and after the transition.
- For supported direct manipulation, preserve the grab offset and one-to-one input relationship. Continue from the current rendered state and carry supported velocity through retargeting; choose among confirmed destinations using direction and projected trajectory rather than the release coordinate alone. Apply progressive boundary resistance only when the result ends at a valid [canonical final state](../canonical/components.md). Provide a non-drag or non-gesture route through [User Experience](../user-experience.md) and verify it through [Accessibility Audit](../accessibility-audit.md).

### Repeated and Data Regions

- In lists, cards, feeds, results, tables, dashboards, charts, and collections, animate only changed records or marks. Keep unaffected peers, headers, controls, and reading anchors stable.
- For insert, remove, sort, filter, expand, and reorder events, preserve identity and final order. Batch related changes; do not cascade long entrances across content people are waiting to scan.
- Match loading motion to real state: use determinate progress when known, restrained activity when unknown, and a stable skeleton or placeholder when content geometry matters. Stop or replace it as soon as the state resolves.
- Live updates and notifications move only enough to make consequential change discoverable. Do not repeatedly steal attention or shift an active target.

### Layers, States, and Contexts

- Open dialogs, sheets, drawers, menus, popovers, tooltips, banners, and toasts from a meaningful trigger, edge, or layer relationship. Place focus and announcements when the state changes, not after the entrance completes.
- Preserve [canonical hover, focus, pressed, selected, disabled, open, dragged, loading, and feedback transitions](../canonical/components.md). Motion must agree with [Elevation](elevation.md), [Color Discipline](color-discipline.md), and [Border and Divider](border-divider.md) in the final state.
- Automatic, looping, blinking, scrolling, auto-advancing, video, canvas, 3D, and ambient motion require confirmed purpose, supported controls, and a complete nonmoving result. Never use flashing, sustained oscillation, scroll hijacking, cursor-chasing, or peripheral movement as decoration.
- After [Responsive Adaptation](../responsive-adaptation.md), reconsider travel, origin, distance, pinning, and choreography for the resulting regions. Use logical direction for LTR, RTL, and vertical writing, and verify keyboard, pointer, touch, voice, switch, device-motion, narrow-container, zoom, translation, delayed-content, offline, and reduced-motion conditions through [Accessibility Audit](../accessibility-audit.md).

## Focused Audit

- Does every motion event explain a confirmed change, relationship, response, progress state, or focal moment?
- Are [canonical components](../canonical/components.md) intact and unsupported motion reported rather than recreated?
- Are trigger, state pair, spatial logic, final focus, interruption, reversal, release destination, velocity continuity, and supported manipulation correct?
- Is routine work immediate, with one coherent event rather than competing or delayed movement?
- Are static, paused, reduced, responsive, localized, and unfinished results complete and usable?
- Do continuous motion, controls, flashing, input alternatives, stability, and performance have material gaps?
