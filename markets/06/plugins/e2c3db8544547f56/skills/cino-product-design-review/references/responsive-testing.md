# Responsive testing protocol

Use this protocol when layout behavior depends on viewport, application shell, panel, embed, or component width.

## Build the matrix

Start from documented target devices and product requirements. If none exist, select representative widths that cover:

- the widest supported working context;
- a common laptop or constrained desktop context;
- the narrowest supported desktop or tablet context;
- mobile contexts when the product claims mobile support; and
- breakpoints where the composition visibly changes.

Do not make one project's historical widths into a universal standard. Record the exact widths used and why they are representative.

For embedded, split-pane, sidebar, or resizable interfaces, measure both the browser viewport and the usable content container. A large viewport does not prove that the component had sufficient width.

## Test states, not empty templates

At each consequential width, exercise realistic content and state variation:

- short and long labels, names, addresses, or translated content;
- sparse and dense lists, tables, charts, or cards;
- zero, one, and many repeated items where supported;
- validation messages, warnings, errors, loading, and empty states;
- expanded menus, tooltips, dialogs, drawers, and sticky regions; and
- permission or role variations that change available actions.

Use product-appropriate data. Do not invent a state the system cannot actually represent.

## Inspect continuity

Check whether resizing or switching breakpoints preserves:

- reading and focus order;
- the primary task and action visibility;
- labels, units, totals, and warnings;
- selection, entered data, expansion, scroll position, and context when applicable;
- nonoverlapping touch or pointer targets; and
- usable dialogs, tables, charts, navigation, and sticky controls.

Look for clipping, accidental hiding, horizontal scroll, orphaned labels, unpredictable wrapping, overly narrow columns, off-screen actions, and fixed elements covering content.

## Include accessibility pressure

Where supported, inspect keyboard operation, visible focus, increased text size, 200% zoom, and reduced motion. Record which checks were actually performed. Do not claim assistive-technology compatibility from visual inspection alone.

## Record evidence

For every width-dependent P0 or P1, record:

- viewport dimensions;
- content-container dimensions when relevant;
- device or emulation mode;
- zoom and text-scaling conditions;
- route, state, role, and data conditions;
- the breakpoint behavior observed; and
- the exact expected behavior for verification.

Screenshots should include enough surrounding context to locate the issue. When a defect occurs across a range, identify the tested boundaries rather than claiming every intermediate pixel fails.

## Stop conditions

Return **INCOMPLETE EVIDENCE** when a required responsive context cannot be reached or authenticated and its absence prevents a reliable decision. Report verified issues separately. Never substitute source-code inspection for missing rendered coverage without labeling the conclusion as inference.
