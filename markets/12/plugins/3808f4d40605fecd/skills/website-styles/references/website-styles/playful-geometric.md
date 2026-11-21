# Playful Geometric

## Mandatory Brief Flow

When the user selects Playful Geometric, present every option in **Required Playful Geometric Style** as one compact form. Ask the user to choose exactly one style or delegate the choice. Do not filter, rename, merge, preselect, or omit options.

Before building a homepage or landing page, read [Hero](../hero.md) and reproduce the complete Markdown table under **Choose the Structure** in the user-facing question, including both headers and every row with its full `Choose it when` guidance. Do not shorten, paraphrase, flatten it into a list, rename, filter, merge, preselect, or omit anything. Ask the user to choose exactly one structure or delegate the choice.

### Style Choice

**Which Playful Geometric style should lead? Choose one, or delegate the choice.**

| Select | What it looks like |
|---|---|
| SaaS  | Friendly product UI inside colorful varied cards, pills, and simple workflow shapes. |
| Dark  | A deep canvas with bright flat geometry, luminous media, and oversized type. |
| Organic Masked  | Photography inside soft organic masks, with spacious layouts and broad backplates. |
| Memphis | Cutout people or products, bold rounded type, layered colorful geometry, and subject-specific icons. |
| Editorial | Oversized type, assertive image crops, sparse geometric annotations, and large quiet fields. |
| Illustrated  | One consistent illustration world for characters, objects, and explanatory scenes. |
| Modular Bento  | A varied card grid with one dominant tile, mixed spans, and one repeated shape cue. |

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

- [Agent Instructions](../../AGENTS.md) — `AGENTS.md`

Before using this file, recursively resolve and disclose all declared dependencies under the Required Alpy Skill Disclosure And Approval rule in `AGENTS.md`.

This file cannot be used alone when related skills are declared.

If any required file is missing, unread, unregistered, or not approved by the user, stop the affected work.

### UI Skill Coordination

Related UI skills own layout mechanics, canonical components, interaction, accessibility, and responsive behavior. This profile owns the recognizable Playful Geometric signature: its media treatment, typography, shape construction, color rhythm, and repeated visual motifs. Resolve all actual values through the user's Alpy system.

## Creative Purpose

Make the page recognizable before it is merely polished. Apply the user's selected style's required signature to the hero, cards, media, and final CTA.

A valid direction must show its signature in the opening viewport and repeat it in at least two later sections. A collection of bright shapes without a repeated media, type, and composition system is not Playful Geometric.

## Classification

- **Kind:** Primary direction.
- **Best suited for:** Friendly technology, SaaS, media, education, culture, events, food, entertainment, community, portfolios, campaigns, and expressive consumer brands.
- **Use selectively for:** Finance, healthcare, legal, government, security, emergency, dense data, or other high-consequence tasks.
- **Foundation:** Canonical grid and components, one named style, one signature media treatment, one display-type treatment, one repeated shape vocabulary, and assigned color roles.
- **Mode:** Resolve an explicit canonical light or dark mode. Never infer a fallback mode.

## Required Playful Geometric Style

Use only the style named in the confirmed restatement. Apply its required signature, not a diluted mixture of several styles.

### Cutout Hero Reference

Use this recipe after the user confirms a split-column hero and completes the mandatory brief gate. Adapt it to the confirmed hero structure and selected Playful Geometric subtype. It records construction relationships from the YouPod prototype; resolve actual components, tokens, assets, and breakpoints through the active Alpy library.

Reference files:

- `apps/web/public/websites/Playful-geometric/index.html` — working HTML and CSS.
- `apps/web/public/websites/Playful-geometric/assets/hero-host-male.png` — transparent upper-person cutout.
- `apps/web/public/websites/Playful-geometric/assets/hero-host-female-v3.png` — transparent lower-person cutout.
- `apps/web/public/websites/Playful-geometric/design-qa.md` — wide, narrow, and focused comparison evidence.

```text
confirmed brief
  -> resolve canonical canvas, ink, accents, type, border, and breakpoints
  -> build one normalized collage coordinate system
  -> place backplates and motifs
  -> seat transparent people inside or over their backplates
  -> render-check wide and narrow states
```

**Composition contract**

- For a split-column hero, let the collage own about half the desktop hero. For other confirmed structures, preserve the collage proportions inside its media region.
- Use one relative container with a `600 / 680` aspect ratio and positions expressed as percentages.
- Keep copy, actions, and navigation outside the collage. The collage is decorative media, not layout structure.

| Element | Reference bounds | Construction and role |
|---|---|---|
| Wave badge | `left 18%; top 5%; width 25%; height 12%` | White capsule; five outlined sound bars. |
| Play | `left 18%; top 20%; width 14%` | Outlined circle with an outlined triangle. |
| Large star | `left 33%; top 25%; width 8%` | Layered clipped star for a visible ink outline. |
| Person arch | `left 42%; top 5%; width 29%; height 50%` | Rounded arch backplate; clips the upper person. |
| Speech | `left 52%; top 3%; width 21%` | Rotated capsule plus a two-layer outlined tail. |
| Organic blob | `right 4%; top 5%; width 23%` | One base form plus two rotated pseudo-elements. |
| Title slab | `right 2%; top 29%; width 33%` | Saturated rotated label; keep text readable and level enough. |
| Half-circle | `left 17%; top 34%; width 28%; height 14%` | `border-radius: 0 0 999px 999px; transform: rotate(59deg)`. Use the primary strong action role. |
| Support circle | `left 18%; top 58%; width 18%` | Secondary accent behind the lower portrait. |
| Small star | `right 6%; top 44%; width 6%` | Small secondary accent; never compete with faces. |
| Sound circle | `right 3%; top 48%; width 26%` | Warm circular backplate with four outlined sound bars. |
| Lower capsule | `left 18%; bottom 5%; width 66%; height 18%` | Deep anchor behind the lower person. |
| Vertical ring | `right 6%; bottom 5%; width 11%; height 20%` | Filled capsule with an inset canvas-colored cutout. |

**People and layering**

- Use clean RGBA cutouts. Verify transparent edges around hair, headphones, hands, and clothing; remove baked checkerboards before delivery.
- Put the upper person inside the arch: center horizontally, anchor below its base, scale slightly wider than the arch, and let `overflow: hidden` create the seated crop.
- Keep the lower person outside the capsule: reference placement is `left 23%; bottom 5%; width 55%; height 44%` with a top-aligned cover crop.
- Layer in this order: lower capsule; support shapes; arch and large backplates; controls-shaped motifs; people and stars; speech; title slab.
- Never cover faces, pointing hands, copy, actions, or focus indicators.

**Shape and color discipline**

- Apply one canonical ink boundary to every outer shape and internal glyph. On narrow screens, reduce the boundary one supported step rather than removing it.
- Assign recurring roles: subtle primary for the canvas and blob, primary strong for the half-circle and title slab, primary deepest for the lower capsule, secondary for play and green accents, tertiary for arch and sound motifs.
- The YouPod reference uses Primary 500 for the half-circle. Treat that as an example role assignment, not a portable raw value.
- Keep the system flat. A minimal cutout edge shadow is acceptable; do not add a second elevation language.

**Responsive and accessibility**

- Around the medium breakpoint, tighten the split grid before stacking it.
- At the narrow breakpoint, place the collage before the copy, cap its width, preserve its aspect ratio, and reduce border weight. Remove minor accents before shrinking people or essential motifs.
- Give the complete collage one descriptive `role="img"` label. Mark nested shapes and empty-alt cutouts decorative to prevent duplicate announcements.
- Test the primary action, horizontal overflow, image loading, transparent edges, and the rendered collage at wide and narrow viewports.

### Rhythmic Motif Continuation

Continue the selected signature beyond the hero without applying geometry to every section. In the sections after the opening, alternate between a signature-carrying region and a quieter reading region whenever the information architecture allows it.

- A signature-carrying region should repeat one or two of the selected domain motifs from the hero in the **section canvas**—the field, edge, backdrop, or boundary surrounding its content—at a smaller or supporting scale.
- A quiet region may omit decorative geometry, but must preserve the same visual grammar through typography, containment, media treatment, or color roles.
- Do not treat a card-level accent alone as section continuation. Cards remain content containers; use section-level motifs to carry the page rhythm between regions.
- Do not introduce a new shape vocabulary in later sections. Reuse the approved motif set to frame a section, reinforce a section label, create a backdrop, or emphasize a section-level action.
- Do not place the same number or placement of shapes in every region. Vary the cluster while keeping the motif family recognizable.

### SaaS Playful

**Required signature:** Real product UI presented inside large friendly frames, supported by colorful bento cards, pills, diagrams, and simple geometric signals.

- **Hero:** Pair concise copy with one dominant product screenshot or interactive product view. Frame it in a rounded tile and add two to four supporting chips, nodes, or mini-cards.
- **Typography:** Use a confident geometric or rounded display role for short headings and a neutral text role for product explanation.
- **Cards:** Use one large feature tile, two to four smaller tiles, and visibly different spans. Each tile communicates one benefit, workflow, integration, or proof point.
- **Shapes:** Use rounded tiles, circles, arcs, pills, connector lines, and small bursts. Shapes should explain grouping, flow, status, or emphasis.
- **Surface:** Prefer a clean canvas, flat or shallow depth, crisp product imagery, and two or three controlled brand accents.
- **Avoid:** Generic gradient blobs around an otherwise ordinary SaaS page, fake dashboards, decorative charts, or a card grid with identical spans and no visual hierarchy.

### Dark Playful

**Required signature:** Deep surfaces interrupted by saturated flat geometry, luminous media, oversized type, and a small number of high-impact playful marks.

- **Hero:** Use one bright product, portrait, or illustration focal point against a deep canvas. Surround it with one large colored backplate and two or three sharp accents.
- **Typography:** Use high-contrast display type with short lines. Keep supporting copy compact and never gray it below comfortable reading contrast.
- **Cards:** Use dark cards with one saturated shape or media crop per card. Separate cards through surface contrast or a consistent outline, not several shadow systems.
- **Shapes:** Favor crisp arcs, rings, capsules, bursts, and cropped slabs. Keep marks larger and fewer than in light Memphis work.
- **Surface:** Use one deep base, one readable foreground system, and two or three saturated accent roles. Keep glow optional and localized.
- **Avoid:** Neon-everything cyberpunk styling, transparent glass stacks, weak gray text, or constant floating animation.

### Organic Masked Playful

**Required signature:** Relevant photography repeatedly cropped through soft blob masks and placed over large organic backplates on a quiet, spacious canvas.

- **Hero:** Pair calm copy with one large masked photograph. Let the mask or backplate occupy roughly half the visual region.
- **Typography:** Use warm, open display type with a restrained text role. Keep the type quieter than the media silhouette.
- **Cards:** Use image-led stories, testimonials, team profiles, or outcomes with the same mask family. Repeat no more than two closely related silhouettes.
- **Shapes:** Use blobs, soft capsules, circles, broad waves, and rounded organic section boundaries.
- **Surface:** Use low-contrast backplates, generous negative space, minimal outlines, and flat or shallow depth.
- **Avoid:** A different blob for every image, tight text wrapped around irregular edges, facial crops near the mask boundary, or random organic decoration without media.

### Memphis

**Required signature:** Layered cutout photography, colorful portrait cards, oversized rounded display type, and recurring domain-specific iconography assembled with flat geometric forms.

- **Hero:** Use a split composition. Give oversized copy roughly half the width and build the other half as a cutout-photo collage. Use one or two people, one backplate per person, and three to six supporting shapes or icons.
- **Photography:** Use approved transparent-background or carefully cut out people and products. Anchor people to the bottom of a frame, preserve clean silhouettes, and allow controlled overlap with backplates—not text or actions.
- **Portrait cards:** Build a repeatable series of three or four cards on desktop. Use a tall rounded tile, one cutout person, a solid or arch-shaped backplate, a name or short metric in the top safe area, and up to two small accents. Target a consistent portrait proportion near 3:4 or 4:5.
- **Typography:** Use the strongest supported rounded or geometric display role. Set hero copy in two to four short lines, use heavy weight, tight rhythm, and large scale. Keep body copy plain and compact.
- **Iconography:** Extract three to five motifs from the actual subject and repeat the same set across the hero, cards, feature blocks, and CTA. For a podcast, use approved waveform, sound-bar, play, microphone, or headphone motifs. For another domain, replace them with equally specific product symbols.
- **Shapes:** Use circles, semicircles, rings, arches, capsules, rotated slabs, bursts, scallops, and one simple organic mark. Build balanced clusters, not evenly scattered confetti.
- **Color:** Use one light or dark canvas, one ink color, and three to five canonical brand accents. Assign each accent a recurring role across shapes, cards, icons, and actions.
- **Feature blocks:** Combine one cutout or product focal point with two to four supporting shapes. Keep text in a separate aligned column or solid text area.
- **Stats:** Use oversized display numerals with short plain labels. Let the numerals carry emphasis; do not place every metric in a decorative shape.
- **CTA:** Use a large rounded color block with a compact collage on one side and copy plus a pill action on the other.
- **Avoid:** Generic 1980s wallpaper, copied historic Memphis patterns, unrelated squiggles, stock portraits chosen only for color, or a different visual grammar in every section.

### Editorial Playful

**Required signature:** Oversized type and assertive image crops organized like an editorial spread, with sparse geometric annotations and large quiet fields.

- **Hero:** Let the headline or one media crop dominate 50–70% of the opening region. Use a visible grid and one deliberate offset.
- **Typography:** Use one expressive display role at extreme scale, one reading role, and strong contrast between them. Keep display lines short.
- **Cards:** Use article, project, issue, or case-study cards with strong image crops, clear metadata, and one repeated annotation shape.
- **Shapes:** Use rules, circles, underlines, brackets, crop windows, and one large edge-cropped form.
- **Surface:** Prefer flat fields, limited color, strong ink, and little or no shadow.
- **Avoid:** Decorating every paragraph, mixing magazine layouts with soft cards, or using expressive type for long reading.

### Illustrated Playful

**Required signature:** One coherent illustration world in which characters, objects, and explanatory scenes share the same geometry, stroke, palette, and level of detail.

- **Hero:** Use one primary scene or character group. Let shapes create the setting, frame, or motion path.
- **Typography:** Choose display type that matches the illustration's geometry without imitating hand lettering unless that lettering is an approved asset.
- **Cards:** Use spot illustrations for benefits, steps, categories, or stories. Keep viewpoint, stroke, shading, and character construction consistent.
- **Shapes:** Reuse the illustration's native primitives as containers and section anchors.
- **Surface:** Match illustration fills to canonical brand colors and keep UI controls visually simpler than the artwork.
- **Avoid:** Mixing 3D, line art, flat vector, and hand-drawn assets; using decorative characters with no content role; or turning controls into illustrations.

### Modular Bento Playful

**Required signature:** A visibly varied grid with one dominant tile, mixed card spans, strong content contrast, and a repeated shape cue connecting otherwise different modules.

- **Grid:** Use one dominant tile, two to four support tiles, two or three span sizes, and no more than two card heights in the same region.
- **Hero:** Use the grid as the opening only when each visible tile provides real value. Otherwise use a conventional hero followed by the bento system.
- **Typography:** Vary canonical type roles by module importance, not by decoration. Keep labels and repeated metadata consistent.
- **Cards:** Give every tile one job: product view, feature, metric, quote, process, media, or action. Use one focal element per tile.
- **Shapes:** Repeat one cue—such as an arch, circle, capsule, or corner treatment—across at least three modules.
- **Surface:** Keep gap, radius, boundary, and depth consistent while varying fill, span, media, and type scale.
- **Avoid:** A uniform card grid called bento, several unrelated card styles, empty decorative tiles, or arbitrary spans that break reading order.

The selected style must control media, typography, shape, color, and section rhythm. Borrow a functional shape from another style only when it does not weaken the selected style's required signature.

## Section Separation

Use section transitions to repeat the chosen signature:

- **SaaS:** alternate clean canvas and contained feature-card regions;
- **Dark:** alternate deep base and one saturated focal band;
- **Organic Masked:** use broad organic backplates or soft edge transitions;
- **Memphis:** alternate quiet light regions, colorful portrait/card fields, and one dark graphic CTA band;
- **Editorial:** use whitespace, rules, and hard crop changes;
- **Illustrated:** move between one hero scene and smaller spot-illustration regions;
- **Bento:** separate grids with calm narrative or proof sections.

Do not add a decorative transition between every section. Follow a dense signature region with a quieter reading region.

## Art Direction

Define these five decisions before layout:

1. required signature;
2. primary media treatment;
3. display-type treatment;
4. repeated shape and icon vocabulary;
5. canvas, ink, accent, boundary, and depth roles.

Reject a direction if its required signature depends on unavailable imagery, unsupported type, unapproved icons, or noncanonical values. Do not replace missing signature assets with generic decoration.

## Mandatory Pre-Build Signature Map

After the user confirms the complete brief and before generating assets, layout, or code, write a signature map for every major section in the confirmed information architecture. Share the map in the current conversation so the user can interrupt or correct the direction. Do not turn the map into a second approval gate unless it introduces a material choice outside the confirmed brief.

Use these exact columns:

| Section | Signature density | Media treatment | Card or containment construction | Geometric cluster | Repeated domain motifs | Accent roles |
|---|---|---|---|---|---|---|

Complete the map with construction-level decisions:

- **Signature density:** Mark the section `dense` or `quiet`. Use quiet regions deliberately; they must continue the same visual grammar through their transition, typography, containment, or one repeated cue.
- **Media treatment:** Name the approved asset type, crop or cutout behavior, backplate, and overlap relationship. Write `none — deliberate quiet region` only when media would not serve the content.
- **Card or containment construction:** State the span, proportion, surface role, and family relationship. Do not write only `cards`, `tiles`, or `standard section`.
- **Geometric cluster:** Name the two to six shapes or domain icons, their scale relationship, and what they frame, organize, crop, connect, or emphasize. Write `none — deliberate quiet region` only when another mapped section directly before or after it carries the signature.
- **Repeated domain motifs:** Reuse the same three to five approved motifs across the page. For a podcast, name the selected waveform, sound-bar, play, microphone, or headphone motifs instead of writing `podcast icons`.
- **Accent roles:** Assign each canonical accent a recurring job such as action, portrait backplate, play icon, label, statistic, or secondary shape. Do not list raw colors without roles.

Reject the map before implementation when any major section is missing, any cell is blank or says `TBD`, or the plan uses vague phrases such as `playful shapes`, `colorful cards`, or `Memphis accents` without naming the construction. Also reject it unless:

- the opening viewport contains the selected style's required signature;
- at least two later major sections visibly repeat that signature;
- the primary media treatment appears in at least three mapped placements;
- the main card or media system translates the selected signature instead of falling back to a generic uniform grid; and
- the final CTA carries the selected subtype's required collage, shape, surface, and action treatment.

If approved assets or canonical roles cannot satisfy the map, stop and report the exact gap. Do not dilute the map to fit what is easiest to build.

## Composition

Keep text and controls on the canonical grid. Let media and noninteractive geometry create the asymmetry.

- **Hero collage:** one focal media subject, one major backplate, and two to six supporting shapes or domain icons.
- **Portrait card:** one person or object, one backplate, one label area, and zero to two accents.
- **Feature block:** one media or product focal point, two to four supporting shapes, and a separate text column.
- **Bento region:** one dominant card plus two to four support cards.
- **CTA collage:** one anchor shape plus two to four accents beside the action.
- **Overlap:** use no more than two visible overlap layers around essential media. Never cover faces, product details, copy, actions, or focus indicators.
- **Rotation:** rotate only decorative slabs, labels, or approved media frames. Keep paragraphs, controls, forms, tables, and metrics level.

Repeat a composition pattern before inventing another. A portrait-card series should look like one family even when its background colors and accents vary.

## Hero and Opening Region

Make the required signature visible without scrolling.

- Keep the proposition, support copy, and primary action immediately readable.
- Give the signature media or type 45–60% of the desktop composition.
- Use a short display headline: usually 8–14 words across two to four lines.
- Place the primary action on a calm solid surface.
- Repeat at least one hero motif later in the card system and final CTA.

Do not build a conventional hero and add unrelated shapes around its perimeter.

## Typography

Use canonical type roles, then push scale, weight, measure, and rhythm far enough to support the selected signature.

- Use one display family or role and one text family or role.
- Use rounded or geometric display type for Memphis and SaaS only when canonical and brand-appropriate.
- Use heavy display weight and tight line rhythm for short Memphis or Editorial headlines.
- Use two to four headline lines; prefer two to five words per line over one long line.
- Keep body copy, navigation, forms, tables, and captions conventional.
- Highlight one phrase or one to three words—not arbitrary individual letters.
- Keep all essential text live and selectable.

If the canonical type system cannot produce the defining display treatment, report the gap instead of substituting a fashionable font.

## Media As Content

Choose the media treatment before choosing decorative shapes.

- **Cutout photography:** Use a clean subject silhouette, bottom anchoring, deliberate overlap, and a solid backplate. Preserve hair, hands, products, and accessories.
- **Masked photography:** Use one repeated blob, arch, capsule, or circle family. Keep faces and key objects away from the mask edge.
- **Product UI:** Show real approved states and content. Keep important interface details unmasked and readable.
- **Illustration:** Use one system with consistent stroke, geometry, shading, perspective, and palette.
- **Portrait series:** Keep crop height, face position, label zone, and card proportion consistent across the set.

Do not use stock media simply because its clothing matches the palette. The subject must support the product, audience, or story.

### Design the Atmosphere

Build atmosphere from recurring product-specific motifs, not generic decoration.

- Select three to five approved domain motifs.
- Repeat the same motifs at different scales across the hero, cards, and CTA.
- Place small marks in clusters of two to four near focal content.
- Use one large motif as a backplate or crop window.
- Keep motifs noninteractive unless implemented as canonical controls.

For media brands, use relevant sound, play, broadcast, camera, or editorial motifs. For education, use learning, making, or subject-specific motifs. For SaaS, use real workflow, connection, data, or collaboration motifs.

## Surface, Color, and Detail

Use color as a repeatable system:

- one canvas role;
- one primary ink role;
- one action role;
- two to four supporting brand-accent roles when the selected signature requires them;
- separate semantic roles for status and feedback.

Repeat accent roles consistently. For example, one color may own actions and play icons, another portrait backplates, another secondary geometric accents, and another statistics or labels.

Use one boundary system and one depth system per page. Memphis, Editorial, and most Bento work should remain flat or use one hard graphic treatment. SaaS and Organic Masked may use shallow depth. Dark Playful may use localized glow only when canonical.

Resolve every fill, contrast pair, radius, border, and shadow from Alpy tokens.

## Background Patterns

Use a pattern only when it strengthens the selected signature.

- Keep it inside one hero zone, transition, card field, or CTA.
- Use one repeated motif or elementary-form system.
- Keep body copy and controls on a solid surface.
- Crop patterns at section boundaries instead of filling the entire page.
- Prefer large spaced forms over dense confetti.
- Never reproduce recognizable Memphis artwork or proprietary patterns.

## Viewport Reveal and [Motion](../ui-design/motion-transition.md)

Make the static composition complete first.

- Reveal a cutout collage by bringing in the backplate, subject, then two to four accents.
- Reveal a portrait-card row as one short staggered group.
- Reveal bento modules in reading order.
- Use one signature motion: gentle float, short rotation settle, mask reveal, or shape scale-in.
- Stop decorative motion during reading and interaction.
- Remove travel, spin, float, and parallax under reduced motion.

Do not animate every icon or run several perpetual loops.

## CTA System

Keep actions canonical and let geometry frame them.

- Use one consistent primary-button treatment.
- Use a pill action only when the canonical button supports it.
- Use a large backplate, split color block, or compact collage for the final CTA.
- In Memphis, pair a dark or saturated rounded band with a small product-specific collage and one clear action.
- Keep bursts and scallops as badges or emphasis, never ambiguous buttons.

## Page Rhythm

Build a recognizable sequence:

1. required-signature hero;
2. quiet explanation or proof;
3. repeated signature card or media system;
4. feature story or process block;
5. calm detail, comparison, FAQ, or trust region;
6. required-signature final CTA.

Repeat the media treatment at least three times across the page: hero, one middle system, and CTA or closing media block. Change scale and composition while keeping the same visual language.

## Responsive and Preference Behavior

Preserve the signature while reducing density.

- Stack copy before supporting media unless content requires another order.
- Reduce hero collages to one subject, one backplate, and one or two accents.
- Show portrait cards in one or two columns while preserving crop and label zones.
- Convert bento spans into a clear linear order.
- Remove decorative overlaps before shrinking essential content.
- Keep touch targets, focus rings, zoom, localization, and RTL behavior intact.
- Preserve the selected explicit mode; never substitute another.
- Provide a static reduced-motion result with the same signature.

## Creative Workflow

1. Resolve the confirmed brief, content, explicit mode, approved assets, and active Alpy library.
2. Use the exact style selected by the user and write its required signature in one sentence.
3. Confirm the required media, display type, iconography, components, and canonical roles exist.
4. Write and disclose the Mandatory Pre-Build Signature Map for every major section.
5. Build the hero signature before adding later sections.
6. Repeat the same media treatment, shape vocabulary, and icon set in at least two later sections.
7. Adapt the signature for narrow screens and reduced motion.
8. Remove generic decoration and any second visual language.
9. Run the Mandatory Rendered Visual Compliance Check and revise until it passes.

## Mandatory Rendered Visual Compliance Check

Before delivery, render the implemented page at representative wide and narrow viewports and inspect the actual pixels. Do not infer visual compliance from source code, class names, token usage, or DOM presence.

Compare the render against every row of the approved signature map. Record a concise result with these exact columns:

| Section | Planned signature elements | Observed rendered elements | Result |
|---|---|---|---|

Mark each row `pass` or `fail`. A row passes only when its mapped media treatment, containment construction, geometric cluster, repeated motifs, and accent roles are visibly present at the intended hierarchy. A deliberate quiet region passes only when it preserves the mapped transition or repeated cue and does not introduce a new visual grammar.

The compliance check must include the opening viewport, the primary card or media system, every other major section, and the final CTA. Verify the narrow render separately; responsive simplification must not erase the selected signature.

Fail the check and revise before delivery when:

- the required signature is not immediately recognizable in the opening viewport;
- a required mapped element is absent, too small to carry its intended role, or visually subordinated by generic layout;
- the repeated media treatment, shape vocabulary, domain motifs, or accent roles do not remain visibly related across the page;
- a mapped varied card field has collapsed into a uniform generic card grid;
- the final CTA lacks the mapped closing signature; or
- the narrow layout removes the signature instead of reducing its density.

After any revision, re-render and repeat the failed rows. Do not call the page complete or present it for delivery while any required row is marked `fail`.

## Canonical Resolution

Resolve the user's active Alpy library, revision, and explicit mode before selecting values.

Use Alpy MCP and declared skills to obtain:

- canonical components, variants, and states;
- supported typography roles and font mappings;
- semantic and component tokens;
- spacing, radius, border, surface, color, and depth relationships;
- documented responsive and interaction behavior.

Use approved user media, illustrations, icons, and brand assets. References establish visual relationships only; do not copy their raw values, fonts, artwork, photos, or proprietary patterns.

Do not create local tokens, component variants, or fallback design-system values. If the selected style's required signature requires unsupported typography, components, tokens, or assets, report the exact gap.

## Mandatory Style Fidelity

Apply only the confirmed style, subtype, material, mode, brief, and related guidance. Do not reinterpret, mix, soften, substitute, or drift. If faithful execution is impossible, stop and report the gap.

The direction designated in this skill file must visibly govern composition, grid, hierarchy, spacing, typography, color, surfaces, material texture, background patterns, imagery, photography treatment, illustration, crops, masks, cutouts, collage, image effects, filters, blending, shapes, borders, edges, separators, section transitions, cards, buttons, navigation, forms, icons, decorative marks, depth, shadows, motion, interaction states, responsive behavior, density, and page rhythm.

The implementing agent may not self-approve. A separate visual reviewer or the user must approve the rendered opening before full implementation and the final wide and narrow renders before delivery. Generic, mixed, unclear, missing, or conflicting treatments fail and must be revised. Code, class names, and element presence are not evidence.

## Success Criteria

- The user selected one exact Playful Geometric style and the confirmed restatement names it.
- The Mandatory Pre-Build Signature Map covers every major section with concrete construction decisions.
- The named style is recognizable from the first viewport.
- Its required signature appears in the hero and at least two later sections.
- Media treatment, typography, shapes, iconography, and color roles form one system.
- Memphis uses layered cutout photography, colorful portrait cards, oversized rounded display type, and recurring domain motifs when those assets are approved and relevant.
- Cards and portrait series remain visibly related.
- Shapes frame, organize, crop, connect, or emphasize real content.
- Product UI, photography, illustration, and proof are real and relevant.
- Controls remain canonical, readable, and familiar.
- Narrow screens preserve the signature with fewer layers.
- Reduced motion preserves the complete static composition.
- The Mandatory Rendered Visual Compliance Check passes at wide and narrow viewports with no required failed row.
- All design-system values resolve through Alpy.
- No copied artwork, generic decoration, fake proof, or unsupported fallback appears.
