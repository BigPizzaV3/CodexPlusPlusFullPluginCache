# Cyberpunk

## Mandatory Brief Flow

Cyberpunk is one visual style and adds no art-direction selections.

Before building a homepage or landing page, read [Hero](../hero.md) and reproduce the complete Markdown table under **Choose the Structure** in the user-facing question, including both headers and every row with its full `Choose it when` guidance. Do not shorten, paraphrase, flatten it into a list, rename, filter, merge, preselect, or omit anything. Ask the user to choose exactly one structure or delegate the choice, then record it in the brief.

Use the selected [Hero](../hero.md) only for opening layout and content relationships. Cyberpunk owns its frame, media treatment, typography, color, cuts, signal light, and technical atmosphere.

## UI Skill Coordination

[User Experience](../user-experience.md) supplies purpose, content, and actions. [Hero](../hero.md) supplies only the selected opening content relationship. [Typography and Readability](../ui-design/typography-readability.md) resolves the chosen Cyberpunk typefaces into [complete canonical tuples](../canonical/type-scale.md) and verifies spacing, wrapping, and legibility. [Rhythm and Space](../ui-design/rhythm-space.md) supplies [canonical spacing](../canonical/foundations.md) for tighter section intervals, aligned route handoffs, and text clearance—not layouts, borders, or component shapes. [Responsive Adaptation](../responsive-adaptation.md), [Motion and Transition](../ui-design/motion-transition.md), and [Accessibility Audit](../accessibility-audit.md) adapt behavior and verify the result. Cyberpunk retains visual authority, including when these resources refer onward to other UI skills.

Required supporting resources:

- [Agent Instructions](../AGENTS.md) — `AGENTS.md`

Before using this file, complete the Mandatory Brief, present its final restatement, and obtain user confirmation as required by [Agent Instructions](../AGENTS.md).

## Canonical Alpy Resolution

Before art direction, resolve the active Alpy library, revision, and explicit `dark` mode through Alpy MCP. Cyberpunk defines the visible geometry and treatment of compositions and components. Alpy supplies [canonical semantic tokens](../canonical/semantic-tokens.md) plus [each component's purpose](../canonical/components.md), [required anatomy and content](../canonical/components.md), required states, behavior, and accessibility.

| Cyberpunk decision | Mandatory Alpy source |
|---|---|
| Black canvas, primary action fills, secondary structural borders, text, icons, and localized halo | `System`, `Surface`, `Text`, `Functional`, `Border`, `Icon`, `Shadow`, and `Shades` roles from [alpy/semantic-tokens.md](../canonical/semantic-tokens.md); apply the role assignments in Color and Signal Light below |
| Display, interface, and telemetry type | Complete supported tuples from [alpy/type-scale.md](../canonical/type-scale.md), including family, weight, size, line height, and letter spacing |
| Stroke weight, spacing, notches, and visible geometry | Canonical [Border.Width](../canonical/foundations.md) and [Space](../canonical/foundations.md) from [alpy/foundations.md](../canonical/foundations.md); Cyberpunk supplies chamfers, cuts, contours, connectors, and border-led state treatment across compositions and components |
| Buttons, tabs, navigation, fields, cards, and states | Semantic purpose, [required anatomy and content](../canonical/components.md), required states, behavior, and accessibility from [alpy/components.md](../canonical/components.md); visible geometry and treatment come from Cyberpunk and resolve through [canonical semantic tokens](../canonical/semantic-tokens.md) |
| Responsive and motion behavior | [Canonical component behavior](../canonical/components.md) plus [Responsive Adaptation](../responsive-adaptation.md) and [Motion and Transition](../ui-design/motion-transition.md) |

Never hardcode raw visual values, reach [alpy/palette.md](../canonical/palette.md) directly, invent component meaning, omit [required anatomy or states](../canonical/components.md), or change [expected behavior](../canonical/components.md). If a required semantic role, component contract, state, or mapping is unavailable, report the exact gap instead of creating a local substitute.

CSS colors, typography, spacing, strokes, and effects must reference resolved canonical Alpy tokens. For standalone HTML, embed the exact canonical names and resolved values once; selectors and local aliases reference those declarations. A custom property containing a guessed hex, pixel value, opacity, shadow, or fallback literal is still hardcoding. Compute SVG coordinates from actual container dimensions and token-resolved offsets; do not invent a second spacing or stroke scale.

## Required Art Direction

Build a hyper-technological interface that feels engineered into the screen. Establish this visual system in the opening viewport and carry its geometry across the landing page:

- **Cinematic field:** one [canonical deep black canvas](../canonical/semantic-tokens.md) and black-dominant imagery create a continuous field with generous negative space. The page must read as an engineered interface before any copy names the style.
- **Hero restraint:** preserve the selected [Hero](../hero.md) layout. Use a dominant product or character cut-out with a transparent background directly on the black canvas—no full-scene photograph, rectangular image panel, or enclosing image frame. Let the silhouette and typography dominate. Add only a few supporting graphics: a partial targeting arc, stepped outline, or short guide marks around the subject, clear of text. Keep the hero open and cinematic; dense framing and routing begin below it.
- **Framed capability:** contain data and technical information within one compact, asymmetric instrument panel. Use a thin, continuous [Alpy secondary](../canonical/semantic-tokens.md) outline with a stepped shoulder and fully stroked chamfers. Integrate the section label into a small header bay. Inside, group a relevant wireframe illustration, prominent values, compact units, and supporting labels into clearly organized data bays. Short internal separators connect to the enclosure without entering text-clearance zones. Avoid floating metrics on long staircase lines, oversized empty areas, or a detached heading beside scattered numbers. Keep the interior black and use [Rhythm and Space](../ui-design/rhythm-space.md) for compact padding and balanced group spacing.
- **Techno typography:** a squared, extended Google Fonts display face and visibly engineered interface face define the page; generic system sans is not an acceptable substitute.
- **Shared geometry:** compositions and components repeat one base contour stroke width, 45° chamfer angle, long/short cut-depth pair, stepped notch, connector primitives, and node system. Every chamfer must remain exactly 45° at all sizes: use equal horizontal and vertical offsets for each diagonal cut. Hero supporting graphics, corner-bracket accents, and outer-margin accents use their stated exceptions. Concentrate the shoulder, step, and deep return on different sides. Never mirror identical cuts around all four corners, clip every corner, or build symmetrical chamfered rectangles.
- **Welded perimeter:** enclosed panels, framed media, banners, controls, cards, and section shells have one seamless solid outer stroke, meeting through every corner, step, and chamfer. This rule does not require a frame around the hero or its cut-out. Draw each enclosure as one SVG path or polygon/mask paired with one continuous stroke. Never assemble it from independent CSS border sides, pseudo-elements, floating fragments, or a clipped rectangular border; every cut edge must remain stroked.
- **Interrupted route:** internal dividers, connectors, measurement rails, and circuit branches may contain deliberate blank gaps on long orthogonal runs. Enclosure silhouettes stay continuous; open hero graphics and detached corner brackets are separate accents, not missing perimeter edges. Never use dashed or dotted borders, repeating broken lines, or `stroke-dasharray`.
- **Signal light:** canonical [Alpy primary](../canonical/semantic-tokens.md) marks actions and selected signals; [Alpy secondary](../canonical/semantic-tokens.md) defines structural contours. State and hierarchy remain clear without glow.
- **Undistorted contours:** never use `preserveAspectRatio="none"` or non-uniform scaling on frame, control, or connector geometry. Match a fixed SVG's intrinsic ratio to its box, or regenerate a fluid path from the rendered width and height using the shared angle and token-resolved cut depths. Media clipping and its stroke share those coordinates. `vector-effect="non-scaling-stroke"` preserves thickness, not chamfer angles.
- **No-stroke zones:** reserve [canonical Space](../canonical/foundations.md) clearance around the full rendered bounds of headings, paragraphs, captions, labels, and units. Routes, nodes, chamfers, and halos stay outside that zone; reroute around text rather than crossing behind it or masking a line with a label background. Recalculate clearance after wrapping, font loading, and resizing without breaking the outer perimeter.
- **L-shaped corner brackets:** accent selected focal cards, images, media boxes, banners or callouts inside routed sections with four solid, inward-facing Ls outside a thin closed border. Use equal arm lengths, one consistent clear offset, a heavier canonical [Border.Width](../canonical/foundations.md), canonical [Space](../canonical/foundations.md), and [Alpy secondary](../canonical/semantic-tokens.md) border emphasis. The rectangular inner box and heavier bracket strokes are a local exception; main contours keep the shared chamfered language. Keep the interior black or media, preserve text clearance, and do not repeat it on every card or section. The width of L-shaped corner bracket should 1px thicker than the main shape.


Corner-bracket example: the heavy Ls sit outside the thin, uninterrupted inner border.

```text
┏━━━━                                         ━━━━┓
┃  ┌───────────────────────────────────────────┐  ┃
   │                                           │
   │           CARD / MEDIA / CALLOUT          │
   │                                           │
   │            Open black interior            │
   │                                           │
┃  └───────────────────────────────────────────┘  ┃
┗━━━━                                         ━━━━┛


Use this full composition for horizontal tabbed sections below the hero. Use the same language for vertical tabbed content.

- **Topology:** `image-top branch → integrated Cyberpunk tab rail → terminal right rail → open content field → stepped image shoulder → seamless media contour → continuous inset left notch → deep lower-left and lower-right returns`.


                                  ╱────────────────┐   ╱────────────────┐   ╱────────────────┐   ╱────────────────┐
                             ────╱     ACTIVE     │──╱     TAB 02     │──╱     TAB 03     │──╱     TAB 04     │
                            ╱    │              ╱    │              ╱    │              ╱    └────────────────┤
                           ╱     └─────────────╱     └─────────────╱     └─────────────╱                       │
                          ╱                                                                                  │
┌────────────────────────┴────────────────────────╲                                                         │
│                                                  ╲────────┐                    SECTION NAME               │
│                                                           │                                               │
│                                                           │          • Feature or capability              │
│                                                           │                                               │
│                 DOMINANT IMAGE                            │          • Feature or capability              │
│                                                           │                                               │
╲                                                           │          PRIMARY METRIC                       │
 ╲                                                          │                                               │
  │                                                         │                                               │
  │                                                                                                        │
  ╱                                                                                                        │
 ╱                                                                                                         │
│                                                                                                          │
│                                                                                                          │
│                                                                                                          │
╲                                                                                                          │
 ╲────────────────────────────────────────────────────────────────────────────────────────────────────────╱
```

## Typography

Use three visibly distinct roles:

| Role | Character | Application |
|---|---|---|
| Display | Wide or extended with squared terminals and engineered counters | Short hero statements, section names, major indices, and dramatic words |
| Interface | Squared techno sans with engineered counters | Navigation, controls, feature copy, pricing, and descriptions |
| Telemetry | Mechanically constructed techno sans | Metrics, units, IDs, coordinates, status, and edge labels |

Recommend the Google Fonts pairing **Michroma + Oxanium**: Michroma for display headings and monumental labels; Oxanium for navigation, controls, body copy, metrics, units, IDs, and telemetry. **Tektur** is the approved alternate display recommendation when Michroma does not fit the brand. Resolve the chosen faces through a user-confirmed [canonical Alpy mapping](../canonical/type-scale.md). If none is mapped, stop and report the typography gap; never silently substitute a generic system sans.

Set display copy in short uppercase lines and give it architectural weight through scale and placement. Apply [Typography and Readability](../ui-design/typography-readability.md) during implementation and review. Preserve word spaces and [canonical type tuples](../canonical/type-scale.md). Reject merged words, compressed tracking, and collisions at desktop and mobile sizes. Keep body and interface copy calm, readable, and subordinate.

## Color and Signal Light

Use color as circuitry, not decoration.

- **Field:** one [canonical deep black canvas](../canonical/semantic-tokens.md) spans the entire page.
- **Structural borders:** use the active library's [Alpy secondary](../canonical/semantic-tokens.md) through `color.border.brand.color-two.*` for composition frames, media contours, routed dividers, and non-action outlines. Resolve a readable dark-mode emphasis; do not substitute white, gray, or a guessed blue.
- **Primary buttons:** solid [Alpy primary](../canonical/semantic-tokens.md) fill through its canonical `color-one` fill role, with [canonical on-color text and icons](../canonical/semantic-tokens.md). Fill follows the same asymmetric chamfered silhouette and continuous border.
- **Secondary buttons:** transparent interior with [Alpy primary](../canonical/semantic-tokens.md) blue outline, text, and icons through the corresponding `color-one` semantic roles. “Secondary” means action hierarchy here, not a secondary-palette fill; this action outline is the exception to secondary-colored structural borders.
- **States and support:** canonical [selected, hover, pressed, focus, disabled, and functional roles](../canonical/semantic-tokens.md) retain their meaning. Tabs and other controls use border, text, icon, or node changes; metadata uses readable muted text tokens.

Use the resolved library colors, never a separately chosen neon palette. If its primary does not supply the requested blue or a required role is missing, report the mapping gap; do not hardcode a replacement.

No UI overlays. No filled cards, tabs, banners, sections, caption plates, or navigation panels. [Canonical halos](../canonical/semantic-tokens.md) may accent a few joints and endpoints; most strokes stay crisp. Keep photographic lighting inside imagery.

## Mandatory Page-Level Routing

Below the open hero, treat the landing page as one routed machine schematic, not a stack of self-contained sections. Before building, map one master path: `capability enclosure → title bay → media contour → section handoffs → closing CTA terminal`.

- **Composition variety:** vary scale, crop, placement, and enclosure arrangement—not the shared shape language. Avoid repeating shells and image-plus-text layouts. Integrate section titles into recessed title bays beside the route, respecting text clearance, instead of repeating a detached heading-and-intro row.
- **Connector variety:** vary zigzag direction, position, and step sequence using shared geometry and [canonical spacing](../canonical/foundations.md). Connect meaningful anchors; avoid decorative detours.
- **Rhythm:** use [Rhythm and Space](../ui-design/rhythm-space.md) to tighten section intervals and connector handoffs; one shared parent owns each gap. Remove doubled padding/margins and empty viewport-height sections. Keep focal breathing room inside compositions, not long blank scroll bands between them. Handoffs meet on shared anchors without a long empty rail or accidental gap.
- **Secondary marks:** coordinates, line-only grids, waveforms, and wireframes may appear sparingly inside routed regions. They remain subordinate to the master path and real content.
- **Outer-margin accents:** place sparse concentric targeting rings, partial arcs, crosshair reticles, registration crosses, L-shaped brackets, chamfered corner fragments, diamonds, hexagon clusters, chevrons, ruler ticks, dot matrices, diagonal hatch patches, and node-linked circuit traces in outer margins and section gaps. Select a few complementary motifs rather than using the entire set. Use canonical [Alpy secondary](../canonical/semantic-tokens.md) strokes, varied placement, and restrained scale. Keep them subordinate to content and clear of text and controls. Tick and hatch clusters are standalone accents—not dashed borders. Circular and polygonal accents are allowed; structural chamfers remain 45°.

Outer silhouettes remain seamless; only internal routes may contain deliberate blank gaps on long straight runs.

### Gallery Composition

Build one asymmetric image assembly: a dominant product crop.
Place the gallery title in a recessed contour bay and short captions in adjacent open black bays, outside the images with full clearance from every stroke. A chamfered index rail can select the dominant view with a synchronized caption and [keyboard support](../accessibility-audit.md); avoid adding a separate thumbnail-card sidebar. Use black-dominant images with coherent lighting and distinct wide/detail/action crops. [On narrow screens](../responsive-adaptation.md), reflow these windows along the same stepped route; preserve their visual hierarchy and stroked chamfers.

## Responsive and Motion

[On narrow screens](../responsive-adaptation.md), fold the same master route into a vertical or stepped path while preserving its stroke, chamfer angle, cut depths, gap rhythm, subject, and active control. Reduce secondary branches, grids, and micro-labels before essential content; never collapse the system into plain stacked rectangles.

When motion supports the experience, choose one or two behaviors that make the system feel powered and assembled:

- traces draw toward a real destination;
- nodes activate after their route arrives;
- tabs switch with a short edge sweep after state changes;
- metrics resolve in a brief mechanical sequence.

Keep the resolved interface complete without animation. [Reduced-motion states](../ui-design/motion-transition.md) show the final frames, content, and active states immediately.
