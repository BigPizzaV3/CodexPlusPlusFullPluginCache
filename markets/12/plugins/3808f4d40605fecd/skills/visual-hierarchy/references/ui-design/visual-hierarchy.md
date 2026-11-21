# Visual Hierarchy

## Purpose

Make a page or screen communicate what needs attention now, what follows, and what must not be missed.

Visual Hierarchy owns intended perceptual rank and checks how combined cues affect it. It assigns primary, secondary, supporting, peer, and exception roles and identifies competing or false prominence. It receives task and content importance from [User Experience](../user-experience.md), spatial hierarchy and reading order from [Grid and Layout](grid-layout.md), and relationships from [Gestalt](gestalt.md).

It does not choose layout patterns, rewrite content priority, regroup content, set visual values, or define [component behavior](../canonical/components.md). [Scale and Proportion](scale-proportion.md), [Typography and Readability](typography-readability.md), [Color Discipline](color-discipline.md), [Rhythm and Space](rhythm-space.md), [Alignment](alignment.md), [Balance](balance.md), [Elevation](elevation.md), and [Motion and Transition](motion-transition.md) own the cues used to express the confirmed rank. A selected website style may change their character, never the rank itself. [Responsive Adaptation](../responsive-adaptation.md) owns transformations, and [Accessibility Audit](../accessibility-audit.md) verifies the result.

## Canonical Component Boundary

Treat every [canonical component](../canonical/components.md) as an indivisible unit. Compare or adjust its prominence only through [supported variants, states, and exposed properties](../canonical/components.md) and outer composition.

Never rebuild [component anatomy](../canonical/components.md), reorder [component internals](../canonical/components.md), wrap a [canonical component](../canonical/components.md) to force emphasis, or add local emphasis overrides. Report a missing priority treatment to the [canonical component system](../canonical/components.md) or the skill that owns the required cue.

## Core Rules

1. **Define attention order outside in.** Work frame → region → group → standalone content. Name the intended first read, next step, primary action, support, peers, and exceptions before requesting visual treatment.
2. **Give each active task scope one lead.** A page, region, or layer needs one clear entry point. Genuine alternatives and peer data may share rank; unrelated subjects and actions must not compete for first attention.
3. **Match prominence to importance, consequence, and state.** The current task, consequential action, or critical feedback may lead. Decorative media, optional utilities, passive metadata, and inactive controls may not outrank them.
4. **Resolve competition before adding emphasis.** First reduce the prominence of unrelated elements. Then request the fewest necessary cues from the owning [scale](scale-proportion.md), [type](typography-readability.md), [color](color-discipline.md), [spacing](rhythm-space.md), [alignment](alignment.md), [balance](balance.md), or [elevation](elevation.md) skill.
5. **Keep peers consistent and exceptions earned.** Repeated items with the same role receive equal prominence. Selection, recommendation, status, alert, or a changed task may create an exception; visual variety alone may not.
6. **Keep the current context legible.** Persistent shell, the active layer, state feedback, live updates, and [motion](motion-transition.md) must support the current task. Transient or moving UI interrupts it only for a consequential change.
7. **Preserve priority through real conditions.** Perceptual rank must not contradict task, source, reading, or focus order. Test real content, states, modes, containers, zoom, localization, writing direction, input, and responsive results.

## How to Apply

### Visual Hierarchy Pass

1. Receive confirmed importance, [structure and order](grid-layout.md), [relationships](gestalt.md), real content, states, and [canonical component support](../canonical/components.md).
2. Work outside in. Assign the lead, next step, primary action, support, peers, and justified exceptions at each active scope.
3. Inspect the intended path beside neighboring regions and persistent UI. Return unresolved importance to [User Experience](../user-experience.md) and unresolved structure to [Grid and Layout](grid-layout.md).
4. Reduce competition, preserve [canonical components](../canonical/components.md), and request only the necessary cue changes from their owning skills.
5. Test the composed result before routing transformations to [Responsive Adaptation](../responsive-adaptation.md) and verification to [Accessibility Audit](../accessibility-audit.md).

### Frame and Shell

- In websites, pages, screens, and windows, keep brand, global navigation, local navigation, current location, page subject, and the active task in a comprehensible order. The page subject or current task normally leads; navigation leads only when orientation is the task.
- Keep headers, sidebars, footers, panels, persistent tools, and utility actions available without letting them compete with main content. A fixed control should not reclaim attention on every scroll or state change.
- Let critical account, security, connectivity, or system status interrupt the shell only in proportion to urgency. Routine status remains supporting.

### Content and Task Regions

- In sections, heroes, articles, media, and product details, lead with the confirmed subject or outcome, then explanation, evidence, and action. Media leads only when it carries the subject; decoration remains supporting.
- In forms, checkout, onboarding, settings, editors, and other workflows, emphasize the current step or question, blocking feedback, and the action that advances or completes it. Progress, help, optional fields, and secondary actions remain subordinate.
- On long pages, preserve the role of repeated actions without turning every section into a focal point. Destructive or high-consequence actions become prominent only when they are relevant to the current decision.

### Repeated and Data Regions

- Keep peer cards, list items, feed entries, grid cells, results, comparison options, and collection items equal. Create an exception only for a real selection, recommendation, alert, status, or task change.
- In tables, dashboards, and charts, distinguish page summary, collection controls, panel or chart detail, row content, and local actions. A metric or status leads only when it answers the current task.
- Keep global, collection, selection, row, and item actions at their true level. Long labels, missing values, live data, and changed values must not accidentally reorder attention.

### Layers, States, and Contexts

- An active dialog, drawer, menu, popover, or disclosure leads while its purpose, trigger, and surrounding context remain understandable. Tooltips and toasts must not dominate unless they carry critical information.
- Hover, focus, pressed, selected, disabled, loading, empty, success, warning, and error states must remain distinguishable without scrambling rank. Loading, empty, and error states preserve the next useful or recovery action.
- Live updates and [motion](motion-transition.md) draw attention in proportion to consequence. Continuous activity must not keep stealing attention after it has communicated the change.
- Recheck real copy, wrapping, dynamic data, supported modes, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, keyboard, pointer, touch, and responsive results. [Responsive Adaptation](../responsive-adaptation.md) transforms the composition; [Accessibility Audit](../accessibility-audit.md) verifies semantic, reading, and focus order.

## Focused Audit

- Are importance, structure, relationships, and unsupported requirements routed to their owners?
- Is the intended first read, next step, and primary action clear without unjustified competition?
- Do peers remain consistent and do exceptions, layers, states, live updates, and motion reflect real consequence?
- Are [canonical components](../canonical/components.md) intact, with missing priority treatments reported rather than improvised?
- Does the same priority survive real content, states, modes, reflow, zoom, localization, writing direction, input, and semantic or focus order?
