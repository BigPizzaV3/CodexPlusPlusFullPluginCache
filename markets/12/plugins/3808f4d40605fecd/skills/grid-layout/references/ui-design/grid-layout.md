# Grid and Layout

## Required Related Resources

- [Canonical Components](../canonical/components.md) — supported anatomy, variants, states, and behavior.
- [Semantic Tokens](../canonical/semantic-tokens.md) — Space roles for margins and gutters.

## Purpose

Turn confirmed content, tasks, and priority into the frame, container, regions, tracks, spans, layout pattern, and structural reading path.

Grid and Layout owns spatial structure and layout hierarchy: which regions are primary, supporting, peer, or sequential and how their order is expressed structurally. It receives page purpose, task order, and information priority from [User Experience](../user-experience.md), groups from [Gestalt](gestalt.md), distances from [Rhythm and Space](rhythm-space.md), edges from [Alignment](alignment.md), and size needs from [Scale and Proportion](scale-proportion.md). [Visual Hierarchy](visual-hierarchy.md) owns perceptual priority; Grid and Layout does not create it with local [type](typography-readability.md), [color](color-discipline.md), or [elevation](elevation.md). [Responsive Adaptation](../responsive-adaptation.md) owns transformations; [Accessibility Audit](../accessibility-audit.md) verifies the result.

## Canonical Component Boundary

Place complete canonical components by their outer boundaries only. Never rearrange internals, add repair wrappers or offsets, or invent variants. Use canonical [Space roles](../canonical/semantic-tokens.md) for margins and gutters; report unsupported components, grids, spans, breakpoints, or behavior.

## Core Rules

1. **Grid type follows the region’s job.** Keep linear tasks in normal flow; use the Types of Grids guidance for structured regions.
2. **Grid behavior follows sizing need.** Default to fluid, constrained, or content-led; fixed and hybrid require stable content or tools.
3. **Layout pattern follows the task relationship.** Choose one pattern from the appropriate Layout Family; combine only for distinct regions.
4. **Layout hierarchy follows confirmed priority.** Give the page subject and primary task the main region, keep support nearby without placing it ahead, and give genuine peers equal structure.
5. **Structure is outside-in.** Work frame → container → region → group → standalone content, with constraints owned by the nearest parent.
6. **Scaffold and spans follow content fit and role.** Use the smallest supported structure; do not add columns to fill space or exaggerate a secondary region.
7. **Repeated structure stays predictable.** Keep equal sections and items consistent, item actions with their item, and collection actions with the collection.
8. **Order and essential dimensions survive.** Preserve source, reading, and focus order; keep necessary two-dimensional content locally scrollable.
9. **Canonical boundaries hold.** Place complete components by outer boundaries and send transformations to [Responsive Adaptation](../responsive-adaptation.md).
10. **Real conditions prove the grid.** Test content, states, modes, containers, zoom, localization, direction, and responsive results through [Accessibility Audit](../accessibility-audit.md).

### Types of Grids

| Grid type | Best use | Guidance |
|---|---|---|
| **Manuscript** | Articles, documentation, forms, settings, checkout | One dominant area with readable measure |
| **Column** | Websites, landing pages, applications, dashboards | Use shared vertical tracks for flexible spans and repeated structure |
| **Modular** | Galleries, products, plans, calendars, dashboards | Repeated columns and rows for comparable items |
| **Hierarchical** | Editorial, portfolio, and marketing regions | Priority-led regions sharing enough structure |
| **Square** | Equal-cell selectors, launchers, swatches, tile collections | Equal width and height for scanning or selection |

Types may coexist, such as a column page grid containing a modular collection.

### Grid Behavior

| Behavior | Use when |
|---|---|
| **Fluid** | Tracks should grow and shrink with available space |
| **Constrained** | Content needs a maximum readable or usable width while outer margins grow |
| **Fixed** | Stable item size matters more than filling the region |
| **Hybrid** | Stable navigation or tools sit beside flexible content |
| **Content-led** | Labels, controls, media, or data should determine track size within limits |

Default to fluid, constrained, or content-led behavior. Fixed tracks require stable content and states.

### Layout Families

| Family | 30 UI Layout patterns | Choose when |
|---|---|---|
| **Flow and staged tasks** | 02 Stacked, 03 Tabbed, 18 Timeline, 24 Stepped / Nested, 29 Form-Based, 30 Chat-Based | Sequences, stages, or peer views |
| **Collections and comparison** | 01 Grid, 04 Card-Based, 09 Masonry, 16 Infinite Scroll, 23 Cover Flow, 25 Catalog, 28 Comparison | Scanning, browsing, or comparison |
| **Focused and multi-region work** | 06 Split-Screen, 08 Full-Screen, 12 Canvas, 13 Multi-Panel, 14 Hierarchical, 27 Map-Based | Focus or coupled work regions |
| **Shell and responsive structure** | 07 Liquid / Responsive, 17 Ribbon, 20 Fixed Sidebar, 21 Sticky Header / Footer, 22 Off-Canvas | Persistent or adapting regions |
| **Layers, focal actions, and states** | 05 Floating Action Button, 10 Overlay, 26 Empty State | Contextual tasks, actions, or replacement states |
| **Spatial and expressive structure** | 11 Circular, 15 Scattered / Freeform, 19 Parallax | Spatial relationships or storytelling |

### Structural Hierarchy Patterns

| Relationship | Starting structure |
|---|---|
| One reading or task path | Manuscript with Stacked, Full-Screen, Form-Based, or Chat-Based layout |
| Primary content with support | Split-Screen, Fixed Sidebar, or Multi-Panel with the primary region first |
| List with selected detail | Split-Screen or Multi-Panel with a clear list-to-detail relationship |
| Equal choices or content | Modular Grid, Card-Based, Catalog, or Comparison with equal spans |
| Ordered progression | Stacked, Timeline, or Stepped / Nested in source order |

Use a structural exception only for a real priority, selection, status, or task change.

### Practical Column Scaffold

Use the canonical grid when available; otherwise this scaffold is exploratory.

| Available space | Starting scaffold | Practical use |
|---|---:|---|
| Narrow | 4 columns | Usually one content column; two-up only for short, equal items that remain comfortable |
| Intermediate | 8 columns | Two peers or a main region with compact secondary support |
| Wide | 12 columns | Halves, thirds, quarters, primary–secondary layouts, and mixed dashboards |

Use fewer columns when the structure is simple.

### Practical Spans

| Pattern | Strong starting span on a 12-column grid |
|---|---|
| Two equal regions | 6 + 6 |
| Main content with sidebar | 8 + 4 or 9 + 3 |
| Three equal items | 4 + 4 + 4 |
| Four equal items | 3 + 3 + 3 + 3 |
| Text with supporting media | 7 + 5 or 6 + 6 |
| Full-width table, chart, hero, or media | 12 |

These are exploratory. Adjust for measure, component minimums, comparison, and priority.

## How to Apply

### Grid and Layout Pass

1. Receive the page purpose, task order, information priority, [groups](gestalt.md), content, and canonical support.
2. Choose the grid type, behavior, layout family, and one primary pattern in that order.
3. Map the subject, primary task, support, peers, and section sequence before choosing the scaffold, tracks, gutters, and spans.
4. Build frame → container → region → group; nest only for a distinct regional task and preserve canonical component boundaries.
5. Test real content and states before routing transformations to [Responsive Adaptation](../responsive-adaptation.md) and verification to [Accessibility Audit](../accessibility-audit.md).

### 30 UI Layouts

Choose the pattern that matches the confirmed task and content. Combine patterns only for distinct regions; the catalog does not authorize new component behavior or motion.

```text
01 GRID                  02 STACKED               03 TABBED
repeated regions         linear task flow         peer content groups
┌──────┬──────┐          ┌─────────────┐          ┌───┬───┬───┐
│      │      │          │ Section     │          │ 1 │ 2 │ 3 │
├──────┼──────┤          ├─────────────┤          ├───┴───┴───┤
│      │      │          │ Section     │          │ Content   │
└──────┴──────┘          └─────────────┘          └───────────┘
```

```text
04 CARD-BASED              05 FLOATING ACTION BUTTON    06 SPLIT-SCREEN
scannable content units    one frequent action          parallel tasks
┌──────┬──────┐            ┌─────────────┐              ┌──────┬──────┐
│ Card │ Card │            │             │              │      │      │
├──────┼──────┤            │          ●  │              │      │      │
│ Card │ Card │            │             │              │      │      │
└──────┴──────┘            └─────────────┘              └──────┴──────┘
```

```text
07 LIQUID / RESPONSIVE   08 FULL-SCREEN           09 MASONRY
fluid across widths      one focused task         uneven visual assets
    ← flexible →         ┌─────────────┐          ┌──────┬──────┐
┌─────────────────┐      │             │          │      │      │
│ Fluid regions   │      │ Focus       │          │      ├──────┤
└─────────────────┘      │             │          ├──────┤      │
                         └─────────────┘          └──────┴──────┘
```

```text
10 OVERLAY               11 CIRCULAR              12 CANVAS
brief contextual task    radial relationships     freeform creation
┌─────────────┐               ○   ○               ┌───┬─────────┐
│  ┌───────┐  │           ○     ●     ○           │ T │         │
│  │ Modal │  │               ○   ○               │ o │ Canvas  │
│  └───────┘  │                                   │ o │         │
└─────────────┘                                   └───┴─────────┘
```

```text
13 MULTI-PANEL           14 HIERARCHICAL          15 SCATTERED / FREEFORM
simultaneous work areas  parent-child structure   expressive composition
┌────┬────┬────┐         ┌─────────────┐             ┌─────┐
│ A  │ B  │ C  │         │ Primary     │         ┌───┘     │
├────┴────┼────┤         ├──────┬──────┤         │     ┌───┘
│ Main    │ D  │         │ Sub  │ Sub  │         └─────┘
└─────────┴────┘         └──────┴──────┘              └─────┘
```

```text
16 INFINITE SCROLL       17 RIBBON                18 TIMELINE
open-ended discovery     many grouped commands    chronological events
┌─────────────┐          ┌───┬───┬───┬───┐       ● Event
│ Item        │          │ A │ B │ C │ D │       │
├─────────────┤          ├───┴───┴───┴───┤       ● Event
│ Item        │          │ Workspace     │       │
└──────↓──────┘          └───────────────┘       ● Event
```

```text
19 PARALLAX              20 FIXED SIDEBAR         21 STICKY HEADER / FOOTER
layered storytelling     persistent navigation    persistent key controls
  ┌────────────┐         ┌────┬──────────┐        ┌──── FIXED ────┐
    ┌────────────┐       │Nav │          │        │ Content       │
      ┌────────────┐     │    │ Content  │        │               │
      layered motion     │    │          │        └──── FIXED ────┘
                         └────┴──────────┘
```

```text
22 OFF-CANVAS            23 COVER FLOW            24 STEPPED / NESTED
hidden secondary region  visual browsing          dependent steps
┌─────┐  ┌─────────┐       ┌───┐┌─────┐┌───┐     ┌───────────────┐
│ Nav │← │ Page    │       │ A ││  B  ││ C │     │ 1 ── 2 ── 3  │
│     │  │         │       └───┘└─────┘└───┘     ├───────────────┤
└─────┘  └─────────┘                              │ Current step  │
                                                  └───────────────┘
```

```text
25 CATALOG               26 EMPTY STATE           27 MAP-BASED
product inventory        guide the first action   locations and routes
┌──────┬──────┐          ┌─────────────┐          ┌─────────────┐
│ Img  │ Img  │          │      ○      │          │ ╲    ●    ╱ │
│ Name │ Name │          │   Message   │          │  ╲╱╲  ╱╲   │
├──────┼──────┤          │   [Action]  │          │ ╱   ╲╱  ╲  │
│ Img  │ Img  │          └─────────────┘          └─────────────┘
└──────┴──────┘
```

```text
28 COMPARISON            29 FORM-BASED            30 CHAT-BASED
side-by-side decisions   structured data entry    conversation
┌────┬────┬────┐         ┌─────────────┐          ┌─────────────┐
│ A  │ B  │ C  │         │ [ Field ]   │          │ Messages    │
├────┼────┼────┤         │ [ Field ]   │          │             │
│ •  │ •  │ •  │         │ [ Submit ]  │          ├─────────────┤
└────┴────┴────┘         └─────────────┘          │ Composer    │
                                                  └─────────────┘
```

### Frame and Shell

- Align header, navigation, main, and footer to one outer structure; [Alignment](alignment.md) owns the edges. Give the page subject and task the main region, and keep utility or secondary shell regions from interrupting that path.
- Use Liquid / Responsive, Ribbon, Fixed Sidebar, Sticky Header / Footer, or Off-Canvas only for genuinely persistent or adapting regions.

### Content and Task Regions

- Use manuscript grids for reading and focused tasks. Use Stacked, Tabbed, Split-Screen, Full-Screen, Canvas, Multi-Panel, Hierarchical, Stepped / Nested, Form-Based, or Chat-Based only when the task relationship matches.
- Order sections by the confirmed task or content sequence. Keep each heading with its region, support beside or after what it explains, and the completion action at the natural end of the task.
- Use stable sequences: marketing or feature—message → explanation → proof or media → action; editorial—heading → summary → body → related material; choice—context → options → comparison or evidence → decision; form—context → fields → guidance or errors → completion.
- Default forms to a vertical flow. Place fields side by side only when they form one familiar unit and remain usable under real content and supported transformations.
- [Typography and Readability](typography-readability.md) owns measure. Let real headings, labels, help, errors, media, and actions determine fit; do not alternate regions only for visual variety.

### Repeated and Data Regions

- Use Grid, Card-Based, Masonry, Infinite Scroll, Timeline, Cover Flow, Catalog, Comparison, or Map-Based for the matching scan, browse, sequence, or comparison task; content and supported minimums determine columns.
- Give peers equal spans and predictable outer structure. Use a structural exception only for a real selection, recommendation, alert, or status; never rearrange canonical internals to create it.
- Keep item actions with their item and collection controls with the collection. In tables and dashboards, separate page-wide controls from panel, row, or selection actions.
- Keep collection order as context → controls → items → continuation, and dashboard order as context and status → summary → trends or detail → local actions.
- Preserve essential two-dimensional relationships; [Scale and Proportion](scale-proportion.md) supplies the usable floor, and masonry preserves source order.

### Layers, States, and Contexts

- Use Floating Action Button, Overlay, or Empty State for a focal action, contextual task, or replacement state. Use Circular, Scattered / Freeform, or Parallax only when spatial meaning or storytelling justifies non-linear structure.
- Keep layers and loading, empty, success, warning, and error states with their owning region; keep sticky UI clear of content and focus.
- Start from a source order that works in a narrow container. Preserve the primary path, peer order, section ownership, and necessary comparison relationships through [Responsive Adaptation](../responsive-adaptation.md).
- Test real content, states, modes, narrow containers, zoom, text enlargement, localization, RTL, vertical writing, and responsive results through [Accessibility Audit](../accessibility-audit.md).

## Focused Audit

- Do the grid type, layout family, and pattern match the region’s job?
- Do the subject, primary task, support, peers, and sequence have the right structural relationship?
- Do behavior, scaffold, constraints, and spans follow real content and role?
- Are repeated regions predictable and are actions kept with their owners?
- Are parent structure, nesting, source order, reading order, and focus order sound?
- Are canonical components intact and unsupported needs reported?
- Does the structure survive real content, states, zoom, localization, and responsive results?
