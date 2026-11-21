# Rhythm and Space

## Required Related Resources

- [Semantic Tokens](../canonical/semantic-tokens.md) — canonical Space roles and values.
- [Canonical Components](../canonical/components.md) — supported internal spacing, density, states, and behavior.

## Purpose

Create clear spacing relationships, usable density, and deliberate page pacing across a website or interface.

Rhythm and Space owns [canonical spacing](../canonical/semantic-tokens.md) between complete components and standalone content, outer and regional padding, page gutters, section intervals, density, and static visual cadence. It receives structure from [Grid and Layout](grid-layout.md), relationships from [Gestalt](gestalt.md), perceptual priority from [Visual Hierarchy](visual-hierarchy.md), component behavior from [User Experience](../user-experience.md) and the [canonical component system](../canonical/components.md), and text metrics from [Typography and Readability](typography-readability.md).

It does not choose layout, grouping, priority, [component anatomy or behavior](../canonical/components.md), line height, letter spacing, border treatment, motion, or responsive transformations. [Border and Divider](border-divider.md) owns separators, [Motion and Transition](motion-transition.md) owns movement and timing, [Responsive Adaptation](../responsive-adaptation.md) owns transformations, and [Accessibility Audit](../accessibility-audit.md) verifies target spacing, reflow, and text enlargement. A selected website style may influence static cadence and density only through supported [Space roles](../canonical/semantic-tokens.md).

## Canonical Component Boundary

Treat every [canonical component](../canonical/components.md) as an indivisible unit. [Canonical components](../canonical/components.md) own their internal padding, gaps, density, and control size. This skill may use [supported size or density variants and exposed properties](../canonical/components.md), outer gaps, regional padding, and viewport clearance.

Never alter [component internals](../canonical/components.md), add repair wrappers, or use negative margins to force overlap. Report missing spacing or density coverage to the [canonical component system](../canonical/components.md).

## Core Rules

1. **Work outside in.** Set frame clearance, region and section intervals, group gaps, then standalone-content spacing. Never begin inside a component.
2. **Make every distance express a relationship.** Related items stay closer than separate groups; the nearest shared parent owns the gap. [Gestalt](gestalt.md) decides the relationship, and this skill selects its distance.
3. **Use a small [canonical Space cadence](../canonical/semantic-tokens.md).** Implement only [canonical Space tokens](../canonical/semantic-tokens.md). Repeat the same token for equal relationships and change it only for a different relationship, density, priority, or state.
4. **Pace sections by purpose.** Use Section Rhythm for continuity and pauses; use Display Rhythm only for confirmed focal moments. Do not alternate spacing merely for variety.
5. **Choose density by task and region.** Compact density is for scan-heavy expert work, not an entire product or a substitute for responsive adaptation. Preserve readable content, [canonical controls](../canonical/components.md), and usable targets.
6. **Adapt large spacing before small relationships.** Keep tight relational gaps stable when possible, compress page and section space first, and protect safe areas, sticky UI, keyboards, wrapping, and reflow through Mobile Rhythm.
7. **Prove the rhythm with real conditions.** Test real copy, dynamic data, loading, empty and error states, modes, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, input methods, and responsive results.

### Spacing Relationships

Use these ranges only to select the nearest supported [canonical Space role](../canonical/semantic-tokens.md); implement the token, never the literal value.

| Relationship | Token selection guidance |
|---|---:|
| Icon to label or tightly related details | `4–8px` |
| Related text, controls, or compact outer gap | `12–16px` |
| Heading to introduction | `16–24px` |
| Standalone region or non-component surface padding | `16–24px` |
| Between related groups, cards, or features | `24–32px` |
| Introduction to primary content | `32–48px` |
| Between major blocks inside a section | `40–64px` |
| Content to a closing action | `24–40px` |

Use whitespace before requesting a [divider](border-divider.md). Avoid doubled distance where child margin, parent gap, section padding, and sticky clearance meet.

### Section Rhythm

| Section type | Desktop | Tablet | Mobile |
|---|---:|---:|---:|
| Compact supporting section | `48–64px` | `40–56px` | `32–48px` |
| Standard content section | `80–100px` | `64–80px` | `48–64px` |
| Editorial or marketing section | `96–120px` | `80–96px` | `64–80px` |
| Hero or statement section | `120–160px` | `96–120px` | `64–96px` |

Use the ranges to select supported section [Space tokens](../canonical/semantic-tokens.md). Do not add a second large margin between padded sections. Use less space where one section continues another and more after dense content or around a confirmed focal statement. Repeat a few purposeful rhythms instead of making every section identical or unique.

### Display Rhythm

Treat oversized display type as a major section moment, not an ordinary heading. Give it a supported pause above and below, follow it with calmer reading, proof, product, or task content, and reintroduce it only for a meaningful chapter or closing moment. [Typography and Readability](typography-readability.md) owns the text treatment; [Visual Hierarchy](visual-hierarchy.md) confirms its prominence.

Let the section grow when display text wraps. Never crush nearby gaps, add negative margins, or force a fixed-height composition to preserve the display effect.

### Density

| Density | Use | Token selection guidance |
|---|---|---|
| Compact | Repeated data, tables, lists, and expert tools | `8–12px` gaps; `12–16px` regional padding |
| Default | Most application and task regions | `12–16px` gaps; `20–24px` regional padding |
| Comfortable | Reading, explanation, touch, and important decisions | `16–24px` gaps; `24–32px` regional padding |

Default to normal or comfortable density. Use compact density only when seeing more information improves the task, and give dense regions a clear entry, exit, or surrounding pause. Mobile does not automatically mean compact.

### Mobile Rhythm

Small relationship spacing usually stays stable; large page spacing compresses. Use these ranges only to select [canonical Space roles](../canonical/semantic-tokens.md), and let [Responsive Adaptation](../responsive-adaptation.md) perform the transformation.

| Desktop guidance | Mobile token selection guidance |
|---:|---:|
| `4–16px` | Keep unchanged |
| `20–32px` | `16–24px` |
| `40–64px` | `24–40px` |
| `80–100px` | `48–64px` |
| `120–160px` | `64–96px` |

Select page-gutter roles near `16–24px` on mobile, `32–48px` on tablet, and `48–80px` on desktop. When side-by-side regions stack, start with a `24–32px` relationship. Add safe-area and keyboard clearance without duplicating visual padding; keep sticky actions clear of content. Never force ordinary sections to viewport height.

### Motion Rhythm

[Motion and Transition](motion-transition.md) owns motion purpose, transition behavior, timing, easing, cadence, sequencing, interruption, and reduced-motion design. Rhythm and Space supplies the static section, display, and density cadence that movement must respect; do not duplicate motion values here.

## How to Apply

### Rhythm and Space Pass

1. Receive confirmed [structure](grid-layout.md), [relationships](gestalt.md), [priority](visual-hierarchy.md), content, behavior, states, [canonical component support](../canonical/components.md), and [canonical Space roles](../canonical/semantic-tokens.md).
2. Work frame → region → group → standalone content. Mark [component-owned internals](../canonical/components.md) and unsupported needs before selecting spacing.
3. Choose the smallest set of [canonical Space roles](../canonical/semantic-tokens.md) that expresses the relationships, section rhythm, and local density without doubled gaps.
4. Test real conditions before routing motion to [Motion and Transition](motion-transition.md), transformations to [Responsive Adaptation](../responsive-adaptation.md), and verification to [Accessibility Audit](../accessibility-audit.md).

### Frame and Shell

- Use consistent page gutters and purposeful clearance among navigation, headers, sidebars, footers, panels, main content, and persistent tools. Do not scatter shell regions on wide screens merely to occupy space.
- Keep brand, navigation, account, search, and utility clusters internally close while separating them from the active page task. [Gestalt](gestalt.md) owns the grouping.
- Separate sticky and fixed UI from content, safe areas, browser chrome, and mobile keyboards without stacking multiple clearances or obscuring focus and actions.

### Content and Task Regions

- Apply Section Rhythm to heroes, sections, articles, media, product details, forms, and workflows. Keep headings, introductions, evidence, fields, help, errors, and actions at distances matching their real relationships.
- Use Display Rhythm only where [Visual Hierarchy](visual-hierarchy.md) confirms a focal moment. Let real copy and translation grow rather than compressing the surrounding task.
- In forms and multi-step work, keep label, control, help, and validation close; separate fields, field groups, steps, and completion actions progressively. Do not use space to hide weak task order.

### Repeated and Data Regions

- Keep peer cards, list items, feed entries, results, comparison options, and collection controls on a repeatable cadence. A selected, expanded, recommended, or error item changes spacing only when its content or state requires it.
- Use compact density locally for tables, dashboards, charts, maps, editors, and expert tools when comparison or simultaneous visibility benefits. Keep surrounding regions calmer and preserve usable targets.
- Let long labels, missing values, expanded rows, filters, pagination, loading, and live updates change height without breaking peer gaps or causing nearby regions to jump unnecessarily.

### Layers, States, and Contexts

- Separate overlay content padding from viewport, trigger, safe-area, and keyboard clearance. Keep dialogs, drawers, menus, popovers, tooltips, and feedback close to their owning context without modifying [component internals](../canonical/components.md).
- Loading, empty, success, warning, and error states preserve the region’s established spacing and next useful action; added messages expand the region rather than overlap or clip it.
- Preserve established gaps and clearance through state change, reveal, reordering, progress, and live updates; [Motion and Transition](motion-transition.md) owns how those changes move.
- Recheck modes, narrow containers, zoom, text enlargement, translation, RTL, vertical writing, keyboard, pointer, touch, and responsive results through [Accessibility Audit](../accessibility-audit.md).

## Focused Audit

- Does every gap, section interval, and density change express a confirmed relationship, priority, task, or state?
- Are [canonical Space tokens](../canonical/semantic-tokens.md) used, [component internals](../canonical/components.md) intact, and unsupported spacing or density reported?
- Are equal relationships consistent without doubled gaps, arbitrary pauses, or page-wide compactness?
- Do real content, states, layers, live updates, safe areas, reflow, localization, and input preserve the rhythm?
