# Alignment

## Purpose

Use shared edges, axes, and baselines to improve scanning and comparison across already-related standalone elements and whole canonical components.

Alignment receives structure and region priority from [Grid and Layout](grid-layout.md), prominence from [Visual Hierarchy](visual-hierarchy.md), groups from [Gestalt](gestalt.md), size from [Scale and Proportion](scale-proportion.md), text metrics from [Typography and Readability](typography-readability.md), and responsive results from [Responsive Adaptation](../responsive-adaptation.md).

[Rhythm and Space](rhythm-space.md) owns distance; [Balance](balance.md) owns visual-weight distribution; the selected website style owns character. Preserve these decisions, the confirmed [Hero](../hero.md) composition, and task order from [User Experience](../user-experience.md).

## Canonical Component Boundary

Treat each [canonical Alpy component](../canonical/components.md) as one indivisible unit. Align only its outer boundary.

- Never align, move, wrap, or override component internals.
- Do not add offsets, spacers, wrappers, fixed heights, or local variants to force alignment. Report missing canonical alignment coverage.

All guidance below respects this boundary; internal alignment guidance applies only to standalone content.

## Universal Rules

1. **Edges establish scanning references.** Choose edges for the reading or comparison relationship. Use the fewest meaningful guides, each belonging to a container, whole component, or standalone content. One shared edge can be enough; do not force every edge to match.
2. **Axes establish a common center.** Center compact focal groups only when their axis survives content changes. A centered container can contain start-aligned text. Start-align variable or multiline copy; never fully justify UI text.
3. **Baselines align text; edges align boxes.** Share a baseline when adjacent text reads as one line, including mixed sizes. A first baseline can preserve that relationship across multiline text; top-align independent blocks when their starts matter. Do not baseline-align an icon merely because it sits beside text.
4. **Optical alignment checks visible shape.** Aligned boxes can look uneven. Inspect contours, built-in whitespace, and text metrics at the rendered size. Use canonical asset geometry and supported placement; report persistent mismatches instead of cropping asset padding or nudging instances.
5. **Nesting establishes local references.** Work frame → region → group → standalone content. Align top-level containers globally and contents to their nearest meaningful local guide. A nested group can have its own edge while its outer boundary follows its parent.
6. **Equivalent roles remain comparable.** Give repeated text, media, controls, and data stable lanes. Start-align ordinary text and identifiers; choose numeric alignment for the comparison. Distinct roles may use distinct references.
7. **Intentional exceptions retain their purpose.** Preserve meaningful indentation, asymmetry, masonry, and confirmed style breaks. Exceptions need a clear relationship or compositional role. Route structural, spacing, and balance problems to their owners instead of patching them with alignment overrides.
8. **Distribution and alignment solve different problems.** Equal gaps do not establish shared edges, axes, or baselines. Align references, then resolve distances through the spacing system. Never imitate alignment with spaces, dividers, or empty elements.

## Application Coverage

Cover every relevant region, including custom compositions. These contexts are not a prescribed page structure.

| Context | Alignment guidance |
|---|---|
| **Page and screen structure** | Share guides across shell and content regions, including full-width backgrounds. Keep essential content inside safe areas; only approved backgrounds and media go full bleed. |
| **Navigation and tools** | Maintain clear edges for navigation, sidebars, panels, and nested levels. Align tabs to their panel and toolbars to the content they affect. |
| **Content and actions** | Apply the confirmed reading edge or focal axis to related headings, copy, and actions. Align complete controls by their appropriate center or starting edge. |
| **Media and annotations** | Align outer media frames; attach captions, credits, counters, controls, and overlay copy to their media or readable edge. Place standalone icons and avatars by a supported center beside one-line text, or a top or first-line reference beside longer blocks. Keep scanning paths stable across decorative media. |
| **Forms and task flows** | Share field edges; align standalone labels, help, errors, and actions to their field or group. Check wrapped rows against the baseline and top-alignment rules. |
| **Collections and repeated content** | Give cards, lists, feeds, messages, and timelines stable lanes. Top-align independent peers; accept uneven tops in masonry. In already equal-height standalone cards, align media/title starts and action ends while descriptions grow. |
| **Tables and comparisons** | Match headers and cells; use supported, locale-appropriate right or decimal alignment for comparable quantities. Top-align wrapping cells. Align summaries, metrics, pricing, pagination, chart controls, and notes to their full region. |
| **Overlays and anchored surfaces** | Preserve applicable trigger anchors and outer placement for dialogs, sheets, drawers, menus, popovers, banners, and toasts. Standalone overlays use a consistent inner reading edge and action edge. |
| **Changing states** | Align skeletons and replacement states to their content region. Center brief focal states; start-align longer or actionable messages. Keep feedback aligned with its affected content. |

## Resilience

- **Wrapping and variable content:** Compare short and long copy, multiline labels, unequal heights, and missing or expanding content. Keep references stable without forcing heights, clipping, or adding spacer content or offsets.
- **Responsive changes:** After responsive adaptation, replace failed desktop guides within the resulting regions and safe areas. Wrapped or stacked rows use a shared local start edge; growing independent blocks use a top reference.
- **Localization and writing direction:** Resolve inline and block start/end from the actual writing mode. Treat top/bottom examples as horizontal-writing cases. Recheck translated labels, mixed text and numbers, and script-dependent baselines; do not blindly mirror numeric columns or change text direction just to align a box.
- **Overflow and scrolling:** If centering hides the beginning, use a supported start-aligned fallback and verify reachability. Keep two-dimensional data locally scrollable while surrounding content reflows. Verify registration of sticky headers, frozen columns, and anchored surfaces during scrolling.
- **States and dynamic updates:** Recheck loading, empty, success, warning, error, expanded, selected, and live-updating content in supported modes. Content and height may change without introducing unrelated guides or detaching feedback.
- **Accessibility conditions:** Verify narrow containers, zoom, text enlargement, and text-spacing changes through [Accessibility Audit](../accessibility-audit.md). Preserve reading and focus order; visual alignment must not require reordered content or inaccessible overflow.

## How to Apply

1. Receive confirmed decisions from the owning skills and name the useful edges, axes, and baselines.
2. Apply the rules outside-in across relevant application contexts.
3. Check resilience with real content and states. Replace failed references, remove one-off corrections, and report missing component support or unresolved owner decisions.

## Focused Audit

- Do regions use the fewest meaningful references, with consistent peers and deliberate exceptions?
- Are all relevant content, controls, media, data, layers, and states aligned to the context they belong to?
- Do those relationships survive content growth, reflow, direction, scrolling, and accessibility conditions?
- Are canonical components intact, with structural, spacing, or balance problems routed to their owners?

Flag shared-reference problems only.
