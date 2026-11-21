# Bento Grid

## Mandatory Brief Flow

Bento Grid adds no style-specific choice group beyond the shared [Mandatory Brief](../AGENTS.md). Record Bento Grid in the final restatement; do not invent a subtype.

Before building a homepage or landing page, read [Hero](../hero.md) and reproduce the complete Markdown table under **Choose the Structure** in the user-facing question, including both headers and every row with its full `Choose it when` guidance. Do not shorten, paraphrase, flatten it into a list, rename, filter, merge, preselect, or omit anything. Ask the user to choose exactly one structure or delegate the choice.

## Required Related Skills

This file must declare every directly related Alpy skill and supporting resource by exact name and Markdown path.

The declared list must match the dependencies returned by `get_alpy_skill`.

Required direct skills:

- [User Experience](../user-experience.md) — `skills/user-experience.md`
- [Balance](../ui-design/balance.md) — `skills/ui-design/balance.md`
- [Gestalt](../ui-design/gestalt.md) — `skills/ui-design/gestalt.md`
- [Hero](../hero.md) — `skills/hero.md`
- [Accessibility Audit](../accessibility-audit.md) — `skills/accessibility-audit.md`
- [Responsive Adaptation](../responsive-adaptation.md) — `skills/responsive-adaptation.md`
- [Grid and Layout](../ui-design/grid-layout.md) — `skills/ui-design/grid-layout.md`
- [Alignment](../ui-design/alignment.md) — `skills/ui-design/alignment.md`
- [Scale and Proportion](../ui-design/scale-proportion.md) — `skills/ui-design/scale-proportion.md`
- [Rhythm and Space](../ui-design/rhythm-space.md) — `skills/ui-design/rhythm-space.md`
- [Motion and Transition](../ui-design/motion-transition.md) — `skills/ui-design/motion-transition.md`
- [Visual Hierarchy](../ui-design/visual-hierarchy.md) — `skills/ui-design/visual-hierarchy.md`
- [Color Discipline](../ui-design/color-discipline.md) — `skills/ui-design/color-discipline.md`
- [Typography and Readability](../ui-design/typography-readability.md) — `skills/ui-design/typography-readability.md`
- [Border and Divider](../ui-design/border-divider.md) — `skills/ui-design/border-divider.md`
- [Elevation](../ui-design/elevation.md) — `skills/ui-design/elevation.md`

Required supporting resources:

- [Agent Instructions](../AGENTS.md) — `AGENTS.md`

Before using this file, recursively resolve and disclose all declared dependencies through [Skill Resolution](../AGENTS.md) and its approval flow.

This file cannot be used alone when related skills are declared. If any required file is missing, unread, unregistered, or not approved by the user, stop the affected work.

### UI Skill Coordination

Each Art Direction section names its UI-design owners. Bento Grid coordinates their visible result into one card-mosaic aesthetic without replacing or overriding them. [Hero](../hero.md), [User Experience](../user-experience.md), [Responsive Adaptation](../responsive-adaptation.md), and [Accessibility Audit](../accessibility-audit.md) own opening structure, semantics, reflow, and verification.

## Art Direction

Art Direction governs every Bento aesthetic below: asymmetric card composition, grid balance, balanced height, anchor hierarchy, media construction, shared seams, copy placement, atmosphere, rhythm, and finish. Preserve the complete practical system and resolve its values through the linked UI skills.

### Strongest Signature

[Grid and Layout](../ui-design/grid-layout.md) constructs the mosaic, [Alignment](../ui-design/alignment.md) creates shared seams, [Visual Hierarchy](../ui-design/visual-hierarchy.md) and [Scale and Proportion](../ui-design/scale-proportion.md) establish the anchor, and [Balance](../ui-design/balance.md) with [Gestalt](../ui-design/gestalt.md) organizes the unequal card group.

Build one asymmetric, edge-aligned card mosaic around a dominant media-rich anchor. Surround it with four to six unequal supporting cards that repeat the same media frame, copy placement, surface, gap, and corner treatment. Size and placement—not decoration—must create the reading order.

Show this signature in the hero or opening region and repeat it in at least one later feature or showcase section. If the page cannot support both with meaningful content, do not claim a Bento direction.

### Creative Purpose

[Visual Hierarchy](../ui-design/visual-hierarchy.md) owns the scannable emphasis; [User Experience](../user-experience.md) owns the meaning and priority of the content assigned to each card.

Use Bento to turn a product story into a scannable visual hierarchy. Every card must reveal one useful feature, product moment, proof point, outcome, or action.

### Named Ingredients

- **Anchor card:** the largest card; carries the strongest promise and best media.
- **Supporting card:** expands one feature or proof point with the same visual construction.
- **Compact card:** contains one metric, quote, status, integration, or action.
- **Media field:** the visual area occupying most of every large card.
- **Copy dock:** one consistent edge where label, heading, and short copy sit.
- **Shared seams:** aligned card edges, one gap, one radius family, and one boundary treatment.
- **Quiet release band:** an open proof, reading, logo, or transition section between mosaics.

### Required Bento System

Apply the related layout skills for supported grid mechanics and canonical values. Preserve these Bento proportions:

[Grid and Layout](../ui-design/grid-layout.md) owns columns and spans, [Alignment](../ui-design/alignment.md) shared edges, [Scale and Proportion](../ui-design/scale-proportion.md) card ratios, [Balance](../ui-design/balance.md) unequal masses, [Rhythm and Space](../ui-design/rhythm-space.md) gaps, and [Responsive Adaptation](../responsive-adaptation.md) reflow.

1. Use a shared column grid; use 12 columns on wide screens when supported.
2. Use five to seven cards per Bento group.
3. Use only three size roles: one anchor, supporting cards, and optional compact cards.
4. Make the anchor roughly 1.5–2 times the visible area of the largest supporting card.
5. Let the anchor span 7–8 columns and two rows; let supporting cards span 4–5 columns; let compact cards span 3–4 columns.
6. Use no more than three card widths and two row heights in one group.
7. Align every edge to the grid. Do not use masonry, loose offsets, or overlapping cards.
8. Give each card one job. Remove any card that exists only to fill the rectangle.
9. Reflow in narrative order: anchor first, supporting cards next, compact proof or action last. Collapse to one column on narrow screens without empty gaps.

### Grid Balance

Use the canonical [Modular grid](../ui-design/grid-layout.md#types-of-grids) with the [Grid or Card-Based layout](../ui-design/grid-layout.md#layout-families). Use the [Practical Column Scaffold](../ui-design/grid-layout.md#practical-column-scaffold) and [Practical Spans](../ui-design/grid-layout.md#practical-spans) as supported starting references; do not substitute Masonry.

[Balance](../ui-design/balance.md) owns visual-weight distribution, [Grid and Layout](../ui-design/grid-layout.md) shared rows and spans, [Alignment](../ui-design/alignment.md) seams and baselines, [Scale and Proportion](../ui-design/scale-proportion.md) card ratios, [Rhythm and Space](../ui-design/rhythm-space.md) gutters, and [Gestalt](../ui-design/gestalt.md) the mosaic as one whole.

- Close every Bento group into one stable outer silhouette: adjacent columns and stacks must terminate on shared top and bottom edges.
- When an anchor spans multiple rows, the combined height of the supporting stack plus its internal gaps must equal the anchor height.
- Cards sharing one row must share its height and baseline. Do not let text length, media aspect ratio, or local padding create ragged bottoms.
- Keep one gutter value across rows and columns so internal seams remain continuous and stacked-height relationships stay exact.
- Balance optical weight as well as area. Saturated color, dense copy, large media, and heavy type increase weight; adjust span, crop, density, or negative space so the supporting cluster counterbalances the anchor without competing with it.
- Check the group at thumbnail scale: the anchor should read first, while the complete mosaic remains visually stable rather than tipping toward one side.
- During [Responsive Adaptation](../responsive-adaptation.md), rebuild complete row bands or a gap-free stack. Reset desktop equal-height tracks when cards become sequential; never preserve empty cells or force unrelated cards to matching mobile heights.

### Repeatable Media Construction

[Visual Hierarchy](../ui-design/visual-hierarchy.md) owns media emphasis, [Scale and Proportion](../ui-design/scale-proportion.md) the media field, [Alignment](../ui-design/alignment.md) the copy dock, [Gestalt](../ui-design/gestalt.md) media-copy attachment, [Color Discipline](../ui-design/color-discipline.md) treatment, and [Typography and Readability](../ui-design/typography-readability.md) the copy roles.

Use one **media field + copy dock** construction across every anchor and large supporting card:

- Give the media field 55–70% of the card.
- Let it touch or deliberately crop against one or more card edges.
- Pin the copy dock to the same edge throughout the group.
- Keep the subject, product action, crop, perspective, lighting, and finish consistent.
- Enlarge the construction in the anchor; use tighter crops of the same visual system in supporting cards.
- Keep compact cards media-free unless one small approved mark is the content.

Choose one leading media family from the confirmed assets and use it throughout the Bento groups. Do not mix full-bleed photography, floating devices, tactile illustration, charts, abstract diagrams, and unrelated product UI as separate card treatments.

### Practical Section Recipes

#### Hero mosaic

Use a 7/5 split: one message-led anchor beside one substantial product or story card. Complete the next row with three compact 4-column proof, capability, or action cards. Keep the primary action inside the anchor.

#### Feature mosaic

Use one 7-column anchor spanning two rows. Stack two 5-column supporting cards beside it, then use a 5/4/3 supporting row. The anchor shows the complete product moment; supporting cards show specific details or outcomes.

#### Product-frame card

Give the product frame 55–70% of the card and keep the important interaction legible. Crop toward the action, not generic chrome. Place one short label, a two-line heading, and no more than two lines of explanation in the copy dock.

#### Proof strip

Place a quiet full-width logo, metric, or testimonial band between Bento groups. If proof requires cards, use three equal compact cards; do not turn the strip into another competing mosaic.

#### Showcase block

Use one wide 8-column product card with a 4-column stack containing one outcome and one proof point. Reuse the same product frame, copy dock, surface, and crop behavior established earlier.

### Section Separation

[Rhythm and Space](../ui-design/rhythm-space.md) owns dense–quiet pacing, [Gestalt](../ui-design/gestalt.md) continuity between groups, and [Motion and Transition](../ui-design/motion-transition.md) the transition between mosaic and release band.

Never place two dense mosaics back to back. Separate them with open copy, logos, a testimonial, a simple metric band, or another calm section. Keep navigation, long reading, pricing, forms, comparison, and the footer outside the Bento treatment unless unequal card emphasis is essential to their content.

### Visual World

Bento Art Direction owns the shared lighting model. [Color Discipline](../ui-design/color-discipline.md) resolves canvas, surface, accent, and lighting colors; [Alignment](../ui-design/alignment.md) the copy-dock position; [Border and Divider](../ui-design/border-divider.md) boundaries and radii; and [Elevation](../ui-design/elevation.md) depth and shadow.

Use one visual world across both required Bento groups:

- One canvas and related card-surface family.
- One leading media family.
- One crop, perspective, and edge behavior.
- One content alignment and copy-dock position.
- One accent family and one lighting model.
- One boundary, radius, and shadow treatment.

Make cards feel related through construction, not through identical content.

#### Design the Atmosphere

[Color Discipline](../ui-design/color-discipline.md) resolves the restrained gradient or light field, while [Elevation](../ui-design/elevation.md) resolves the single depth language.

Keep the canvas quieter than the cards. Use one restrained gradient or soft light field only when it supports the full composition. Use one subtle elevation language or none; multiple glows and shadow styles make the page look like a component gallery.

### Composition

[Grid and Layout](../ui-design/grid-layout.md) owns the mosaic structure, [Visual Hierarchy](../ui-design/visual-hierarchy.md) the anchor, [Scale and Proportion](../ui-design/scale-proportion.md) card spans, [Balance](../ui-design/balance.md) unequal weight, [Gestalt](../ui-design/gestalt.md) grouping, and [Rhythm and Space](../ui-design/rhythm-space.md) card pacing.

Read the group at thumbnail scale. The anchor must be the first shape and first idea noticed. Supporting cards should change pace through width, height, or crop while remaining subordinate. Preserve a clear path from promise, to product, to proof, to action.

### Hero and Opening Region

[Hero](../hero.md) owns the opening structure, [User Experience](../user-experience.md) its message and action semantics, and [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Scale and Proportion](../ui-design/scale-proportion.md), and [Balance](../ui-design/balance.md) create its Bento composition.

Put the Bento signature above the fold. Keep the main promise, short explanation, and primary action together in the anchor card. Use the adjacent large card for the strongest real product or story media. Do not scatter hero copy across several cards or fabricate compact cards to complete the grid.

### Typography

[Typography and Readability](../ui-design/typography-readability.md) owns the complete type system; [Alignment](../ui-design/alignment.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), and [Scale and Proportion](../ui-design/scale-proportion.md) coordinate copy docks, card hierarchy, and display emphasis.

Resolve typography through the related canonical skill. Keep card headings to two lines, supporting copy to two or three lines, and labels to one line. Use one alignment across the group. Reserve the largest display role for the hero anchor; do not turn every metric into oversized type.

### Media As Content

[Visual Hierarchy](../ui-design/visual-hierarchy.md) owns media emphasis, [Scale and Proportion](../ui-design/scale-proportion.md) legible size, [Color Discipline](../ui-design/color-discipline.md) treatment, and [User Experience](../user-experience.md) truth and relevance.

Use approved, meaningful assets that show the product, subject, evidence, or outcome. Keep product UI legible and crop toward the relevant interaction. Do not fabricate interfaces, charts, dashboards, or device scenes. Do not use icons or CSS shapes as substitutes for missing art direction.

### Surface, Color, and Detail

[Rhythm and Space](../ui-design/rhythm-space.md) owns gaps and padding, [Border and Divider](../ui-design/border-divider.md) radii and boundaries, [Color Discipline](../ui-design/color-discipline.md) surface contrast, and [Elevation](../ui-design/elevation.md) shadow and depth.

Use one gap, one padding logic, one radius family, and one boundary treatment throughout each group. Let surface contrast and media create hierarchy; borders, shadow, glow, and gradients are supporting details, not the Bento identity.

### Page Rhythm

[Rhythm and Space](../ui-design/rhythm-space.md) owns page pacing, [Gestalt](../ui-design/gestalt.md) continuity, and [Motion and Transition](../ui-design/motion-transition.md) mosaic reveal and section transitions.

1. Bento hero or opening mosaic.
2. Quiet proof or logo band.
3. Bento feature or showcase mosaic.
4. Open reading, testimonial, comparison, or action section.
5. Additional modular content only when the story requires it.

Reveal the mosaic as one related composition or in anchor-to-supporting order. Avoid unrelated card floating, stagger noise, and motion that breaks shared seams.

### Creative Workflow

1. Inventory the strongest real content and media.
2. Assign one anchor payload and four to six supporting jobs.
3. Choose the single media family and define the media field + copy dock.
4. Sketch the card masses before styling card interiors.
5. Apply one grid, gap, radius, surface, crop, and typography system.
6. Check hierarchy at thumbnail size and legibility at full size.
7. Remove filler cards and any media treatment that breaks the visual family.

## Canonical Resolution

Resolve an explicit canonical `light` or `dark` mode, then resolve the confirmed Bento direction through the linked UI skills and canonical Alpy components, component tokens, semantic tokens, type scale, foundations, palette bindings, and assets. Resolve [Modular](../ui-design/grid-layout.md#types-of-grids) for Bento; preserve the confirmed hierarchy, density, source order, responsive priorities, and permissioned project media.

If canonical capability cannot support the required opening and later Bento groups, spans, reflow, media, or behavior, report the exact gap. Never invent values, components, interfaces, evidence, data, assets, or product behavior, and never simulate missing imagery with CSS shapes or layout primitives.

## Mandatory Style Fidelity

The confirmed Bento direction, Required Bento System, and Grid Balance must visibly govern the result. Do not reinterpret, mix, soften, substitute, or drift; report unsupported fidelity gaps.

The implementing agent may not self-approve. A separate visual reviewer or the user must approve the rendered opening and the final wide and narrow results. Generic, mixed, unclear, or conflicting treatments fail; code and element presence are not evidence.

## Success Criteria

Validate with the applicable UI skills and [Accessibility Audit](../accessibility-audit.md). Approve Bento only when all rules pass:

1. The opening and one later section visibly use the same asymmetric anchor-and-support mosaic.
2. One anchor is unmistakably dominant and every card has one necessary job.
3. Every large card repeats the media field + copy dock construction with coordinated crop, perspective, lighting, and finish.
4. Grid lines, gaps, corners, boundaries, insets, alignment, surfaces, and responsive source order remain consistent.
5. Typography, color, components, and foundational values resolve through their canonical Alpy sources.
6. [Balance](../ui-design/balance.md), [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), and [Rhythm and Space](../ui-design/rhythm-space.md) keep adjacent columns on shared outer heights, each combined supporting stack equal in total height to its spanning anchor, and responsive recomposition free of ragged edges or empty gaps.
