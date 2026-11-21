# Border and Divider

## Purpose

Use borders, dividers, and corner radius to clarify real boundaries, separation, and states without outlining everything.

Border and Divider receives grouping from [Gestalt](gestalt.md), spacing from [Rhythm and Space](rhythm-space.md), structure from [Grid and Layout](grid-layout.md), required prominence from [Visual Hierarchy](visual-hierarchy.md), alignment from [Alignment](alignment.md), semantic border color from [Color Discipline](color-discipline.md), layers from [Elevation](elevation.md), and responsive results from [Responsive Adaptation](../responsive-adaptation.md). The selected website style supplies character; this skill applies supported canonical boundary roles.

## Canonical Component Boundary

[Canonical Alpy components](../canonical/components.md) own their [borders, dividers, focus treatment, and radius](../canonical/component-tokens.md), plus internal geometry. Use only supported variants; never repair them with wrappers or local overrides.

For standalone regions, use canonical semantic [Border and Color / Border roles](../canonical/semantic-tokens.md), plus [Radius and Space tokens](../canonical/semantic-tokens.md). Never hardcode the baselines below. Active-package values override them; report missing canonical coverage.

## Core Rules

1. Start with grouping, space, or a surface change. Add a line only when the boundary, separation, or state remains unclear.
2. Use a perimeter for containment, a divider for separation, and a single edge for a real seam, status rail, or supported accent. One line should communicate one relationship.
3. Draw shared edges once. Round only a connected group's exterior corners, keep internal joins square, and make edge media follow the parent corners.
4. Use one canonical [width and radius](../canonical/semantic-tokens.md) for each role. Similar surfaces stay consistent; nested surfaces use supported concentric radii rather than becoming progressively rounder.
5. Border changes must not resize content or shift layout. State and focus treatments use their canonical [semantic roles](../canonical/semantic-tokens.md), never a stronger local substitute.
6. Anchor dividers to visible content edges, omit the final divider, and keep canonical [space](../canonical/semantic-tokens.md) around every line. A divider never replaces spacing or invents a group.
7. Re-evaluate boundaries after reflow. Remove or replace vertical dividers when regions stack, and change edge-to-edge corners only through supported responsive behavior.

## Practical Starting Baselines

### Stroke Width

| Alpy token | Current baseline | Best use |
|---|---:|---|
| `border.width.0` | `0px` | No line when space, surface, or an adjoining boundary already separates. |
| `border.width.hairline` | `0.5px` | Quiet decorative separation only; never an essential boundary, state, or focus indicator. |
| `border.width.1` | `1px` | Default containers, cards, fields, rows, menus, tables, and dividers. |
| `border.width.1.5` | `1.5px` | A slightly stronger non-state boundary; use sparingly. |
| `border.width.2` | `2px` | Canonical focused, selected, invalid, active, or emphasized states. |
| `border.width.4` | `4px` | Strong accents or status rails; never an ordinary perimeter or divider. |

Use one weight consistently for the same role. Do not create near-duplicate local widths. A change in border weight must not resize the element or shift nearby content.

### Radius Candidates

These candidates apply only when a canonical component does not already own the radius.

| Alpy token | Current baseline | Best use |
|---|---:|---|
| `radius.none` | `0px` | Tables, joined controls, shared seams, edge-to-edge regions, and rectilinear layouts. |
| `radius.xsmall` | `2px` | Tiny indicators, compact data regions, and technical surfaces. |
| `radius.small` | `4px` | Compact controls, thumbnails, tags, and small containers. |
| `radius.medium` | `8px` | General cards, inputs, menus, and interface surfaces. |
| `radius.large` | `12px` | Prominent cards, popovers, panels, and medium floating surfaces. |
| `radius.tile` | `12px` | Repeated tiles when the active system distinguishes the tile role from other surfaces. |
| `radius.xlarge` | `16px` | Dialogs, drawers, feature cards, and large floating surfaces. |
| `radius.xxlarge` | `24px` | Large sheets, focal media, and oversized surfaces; use sparingly. |
| `radius.full` | Full | Pills, capsules, and circles only; never ordinary rounded rectangles. |

Use a small radius vocabulary. Similar surfaces should share a radius, nested surfaces should not become progressively rounder, and adjoining edges should share one clean seam.

## How to Apply

### Border and Divider Pass

1. Receive confirmed components, regions, groups, spacing, surfaces, layers, states, and responsive results from their owners.
2. Decide whether the relationship needs no line, a perimeter, one edge, or a divider. Prefer no line when space or surface already communicates it.
3. Select the exact canonical width, color, radius, and space roles. Check shared seams, joined corners, nested radii, edge media, focus clearance, and layout stability.
4. Repeat with real content, states, modes, zoom, and every approved responsive result; route unsupported needs to their owner.

### Frame and Shell

- Use boundaries on headers, navigation, sidebars, footers, panels, and persistent regions only when space or surface changes are insufficient. Draw adjoining shell seams once.
- Keep section dividers inside their content region unless they separate true full-width regions. Place a section divider above its heading rather than underlining it.
- On edge-to-edge layouts, remove only corners that touch the viewport through supported behavior. [Responsive Adaptation](../responsive-adaptation.md) owns the transformation.

### Content and Task Regions

- Prefer canonical field boundaries in forms. Divide genuinely different task groups, not every input, and keep focus treatment separate from ordinary borders.
- Give standalone cards, panels, media, and independent regions one coherent perimeter and radius. Internal dividers follow the content keyline; use equal insets only in a symmetric region.
- For nested surfaces, use `outer radius − inset = inner radius` only as a geometry check, then choose a supported token pair. Edge media follows the parent's exterior corners.
- Use labeled, icon, dashed, or dotted dividers only when a canonical pattern or established domain meaning requires them; never as decoration.

### Repeated and Data Regions

- In lists and rows, use a leading inset only when it anchors to shared text, icon, or media; use full-bleed when each item occupies the complete region. Omit the final divider.
- Draw adjacent or joined item seams once and round only the group's exterior corners. Repeated peers use the same border and radius roles.
- Prefer canonical table and comparison treatments. Use quiet horizontal rules for scanning; add vertical rules only when columns remain unclear.
- Treat canonical cards, tables, lists, and controls only through supported outer treatments. Never add local borders to normalize different content.

### Layers, States, and Contexts

- Let [Elevation](elevation.md) establish layer relationships. Add an overlay border only when the canonical surface still needs a visible edge; do not duplicate the shadow's job.
- Use the matching semantic border role for focus, selected, invalid, active, disabled, and other states. Border changes must not shift layout.
- Essential control and state boundaries need at least `3:1` contrast against adjacent colors. Never remove, soften, crop, or disguise canonical focus treatment; [Accessibility Audit](../accessibility-audit.md) verifies it.
- Recheck light, dark, and high-contrast modes, zoom, enlarged text, translation, RTL, dynamic content, and states. When regions stack, replace obsolete vertical dividers and keep insets anchored to the logical content edge.

## Focused Audit

- Are canonical components intact and all values token-backed?
- Could spacing or a surface change replace an unnecessary line?
- Are widths, radii, shared seams, joined corners, nested surfaces, and edge media consistent?
- Do dividers follow real groups, visible anchors, and responsive results?
- Are essential boundaries and focus treatments visible across modes and states without shifting layout?

Remove unnecessary lines first. Report missing canonical coverage instead of creating a local rule.
