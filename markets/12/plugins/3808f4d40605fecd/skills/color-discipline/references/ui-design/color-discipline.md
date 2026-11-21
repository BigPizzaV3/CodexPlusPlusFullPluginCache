# Color Discipline

## Mandatory Use

Use this skill whenever a task creates, changes, reviews, or audits interface color. The user chooses the direction; the agent completes the canonical Alpy color system without exploring alternatives.

## Required Related Resources

- Use [Components](../canonical/components.md) and [Component Tokens](../canonical/component-tokens.md) when a canonical component owns the colored UI.
- Use [Semantic Tokens](../canonical/semantic-tokens.md) to select color by intent for standalone content and to interpret component bindings.
- Use [Palette](../canonical/palette.md) only to resolve the mode-specific target selected by a semantic or component binding.

## Purpose

Apply the user-confirmed color direction through canonical palette, semantic, component, state, data, and mode roles.

Color Discipline owns color-system completion and role assignment. Prominence requirements come from [Visual Hierarchy](visual-hierarchy.md), structural role from [Grid and Layout](grid-layout.md), visual weight from [Balance](balance.md), grouping from [Gestalt](gestalt.md), text use from [Typography and Readability](typography-readability.md), boundaries from [Border and Divider](border-divider.md), layers from [Elevation](elevation.md), and responsive results from [Responsive Adaptation](../responsive-adaptation.md). The selected website style supplies character; it does not authorize raw or unconfirmed colors.

## Canonical Component Boundary

[Canonical Alpy components](../canonical/components.md) own their color roles, foreground pairs, and interaction states. Use only supported variants and [component-token bindings](../canonical/component-tokens.md).

- Never recolor component internals, hardcode values, or create local semantic aliases.
- Standalone content uses exact [canonical semantic roles](../canonical/semantic-tokens.md). Report missing component, state, mode, or token coverage.

## Core Rules

1. Start from user-confirmed colors. Preserve each as a palette anchor and never introduce another brand hue without approval.
2. Apply color by semantic role. One role keeps one meaning across pages, components, states, and modes.
3. Use 60–30–10 as a presence guide, not a quota. Keep one leading accent and never override semantics or accessibility.
4. Never use color as the only cue. Validate text, icons, boundaries, focus, and states against their actual adjacent backgrounds.
5. Keep surface levels few and use their paired foreground, border, control, focus, and state roles.
6. Treat charts as localized systems with stable meaning, perceptual order, and redundant cues.

## Canonical Color Workflow

Use the existing [canonical palette](../canonical/palette.md) unless the user requests a change.

1. Gather the user's brand or preferred colors and clarify dominant, secondary, and accent roles only when needed.
2. Generate or override the canonical palette from those anchors; one color may anchor its tonal scale and supporting neutrals.
3. Complete shades, foreground pairs, semantic roles, states, and explicit light and dark mappings. Another brand hue requires approval.
4. Validate and resolve the explicit mode. For component-owned UI, start with [Components](../canonical/components.md) and [Component Tokens](../canonical/component-tokens.md); for standalone content, start with [Semantic Tokens](../canonical/semantic-tokens.md). Follow the resulting semantic target to [Palette](../canonical/palette.md), then apply the exact role—never a raw value.

## Practical Color Baselines

### 60–30–10

| Share | Role | Typical use |
|---:|---|---|
| `60%` | Dominant foundation | Canvas, page backgrounds, large surfaces, quiet regions |
| `30%` | Secondary support | Navigation, panels, cards, section backgrounds, supporting brand areas |
| `10%` | Accent emphasis | Primary actions, important links, selections, and small high-impact details |

- Treat the shares as a starting relationship, not measured coverage. Count related shades as one family and judge presence by area, saturation, and contrast.
- Reduce secondary or accent presence when noisy; strengthen foundation-to-support distinction when flat. Never use color to repair another skill's problem.

### Contrast and Readability

These minimums apply against actual adjacent backgrounds in every mode and state.

| Content | Minimum contrast |
|---|---:|
| Body text and smaller labels | `4.5:1` |
| Large text: about `24px` regular or `19px` bold | `3:1` |
| Essential icons, input boundaries, focus indicators, and other meaningful UI | `3:1` against adjacent colors |

### Canonical Semantic Roles

Use the matching role from [Semantic Tokens](../canonical/semantic-tokens.md) for every interface color and state.

| Semantic color | Includes |
|---|---|
| Shades | Neutral and Brand Color One, Two, and Three |
| System | Black, white, and transparent |
| Surface | Canvas and interaction states |
| Shadow | Soft, medium, strong, and deep |
| Functional | Info, danger, success, and warning |
| Border | Input, functional, brand, neutral, and interaction |
| Text | Base, link, functional, and brand |
| Icon | Base, functional, interaction, and brand |

## How to Apply

### Color Discipline Pass

1. Complete the Canonical Color Workflow, then map every surface, foreground, component, state, and data relationship to an exact role and mode.
2. Validate meaning, foreground pairs, interaction states, contrast, and overall presence before applying tokens.
3. Repeat with real content, modes, states, responsive results, and accessibility settings; report unsupported coverage.

### Frame and Shell

- Let the dominant family establish canvas and large surfaces, secondary color support navigation and panels, and accent mark a few confirmed focal moments.
- Change shell or section surfaces only for real grouping, context, emphasis, or task boundaries. Reuse roles for equivalent regions and keep persistent controls restrained on rich backgrounds.

### Content and Task Regions

- Use a canonical semantic text color when the user wants a colorful headline. For standalone headlines, choose the heading, on-color, or user-confirmed brand text role by meaning in [Semantic Tokens](../canonical/semantic-tokens.md), then resolve its active-mode target in [Palette](../canonical/palette.md); never choose a palette shade directly. If a [canonical component](../canonical/components.md) owns the headline, preserve its [component-token binding](../canonical/component-tokens.md).
- Use [canonical text roles](../canonical/semantic-tokens.md) for copy, labels, links, and functional messages. Display text stays one semantic color unless a user-confirmed accent has a clear purpose and cannot be mistaken for a link or status.
- On strong surfaces, use the paired on-color text, icon, border, control, and focus roles. Functional colors appear only for real info, danger, success, or warning meaning.
- Apply [canonical component and state bindings](../canonical/component-tokens.md) to forms, actions, selection, validation, and task feedback. Color reinforces confirmed priority and never substitutes for labels, grouping, or action order.

### Repeated and Data Regions

- Give equivalent cards, rows, results, plans, and data regions the same roles. Stronger color requires a confirmed selection, recommendation, exception, status, or focus.
- Treat each chart as a localized system while its surrounding interface follows 60–30–10.

| Data relationship | Color approach |
|---|---|
| Unordered categories | Distinct colors with stable labels and mapping |
| Low to high | One perceptually ordered sequence |
| Values around a midpoint | Two ordered directions with a neutral center |
| Threshold or status | Explicit meaning, labels, and a redundant cue |

- Use the fewest colors, keep mappings stable, avoid misleading rainbow scales, and test marks at real size. Add labels, shape, pattern, or line style when needed.

### Layers, States, and Contexts

- Use canonical [overlay, scrim, shadow, and layered-surface roles](../canonical/semantic-tokens.md); [Elevation](elevation.md) owns the relationship. Never invent opacity to force separation.
- Apply [semantic interaction and feedback roles](../canonical/semantic-tokens.md) consistently, with another visible cue. Generate light and dark mappings independently; never mechanically invert them.
- Validate increased-contrast and forced-color contexts through [Accessibility Audit](../accessibility-audit.md). After [Responsive Adaptation](../responsive-adaptation.md), recheck presence, foreground pairs, small marks, imagery, transparency, localization, and cultural meaning.

## Focused Audit

- Is every color user-confirmed, canonical, semantic, and resolved for the explicit mode?
- Does presence reinforce hierarchy without becoming a quota or replacing another skill?
- Do foreground pairs and essential UI pass contrast in every state and context, with meaning available without color alone?
- Are equivalent roles and data mappings stable?
- Are canonical components intact and unsupported needs reported rather than patched?
