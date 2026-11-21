# Parallax

## Mandatory Brief Flow

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

This file cannot be used alone when related skills are declared.

If any required file is missing, unread, unregistered, or not approved by the user, stop the affected work.

### UI Skill Coordination

Use the related skills for layout mechanics, interaction, accessibility, responsive adaptation, and canonical implementation. Do not repeat their instructions here.

Use this profile only for Parallax-specific decisions: narrative method, scene count, depth planes, scroll distance, pinning, media staging, and scene handoffs.

Parallax sets the visible narrative targets for scroll distance, pinning, and handoff character. [Motion and Transition](../ui-design/motion-transition.md) owns whether those targets are supported and resolves scroll-linked behavior, choreography, properties, timing, easing, interruption, reversal, and reduced-motion alternatives.

Correlate every Parallax decision to its UI owner:

| Parallax concern | UI owner |
|---|---|
| Scene regions, structural order, containers, and spans | [Grid and Layout](../ui-design/grid-layout.md) |
| Persistent scene edges, axes, and overlay-copy zones | [Alignment](../ui-design/alignment.md) |
| Focal-subject size, media proportions, and supported scale | [Scale and Proportion](../ui-design/scale-proportion.md) |
| Section intervals, release space, density, and static cadence | [Rhythm and Space](../ui-design/rhythm-space.md) |
| Scroll-linked behavior, pinning, transforms, timing, easing, interruption, and reduced motion | [Motion and Transition](../ui-design/motion-transition.md) |
| First read, attention order, and competing emphasis | [Visual Hierarchy](../ui-design/visual-hierarchy.md) |
| Visual-weight distribution between focal and supporting regions | [Balance](../ui-design/balance.md) |
| Plane grouping, continuity, and perceived scene relationships | [Gestalt](../ui-design/gestalt.md) |
| Canvas, palette roles, gradients, color grade, and contrast | [Color Discipline](../ui-design/color-discipline.md) |
| Text roles, metrics, measure, wrapping, and readability | [Typography and Readability](../ui-design/typography-readability.md) |
| Media-frame boundaries, seams, dividers, edges, and radius | [Border and Divider](../ui-design/border-divider.md) |
| Interface-layer relationships and supported shadows | [Elevation](../ui-design/elevation.md) |

## Mandatory Scroll-Storytelling Question

During the [Mandatory Brief](../AGENTS.md), ask this with the other brief questions when the current conversation does not already answer it:

**Which scroll-storytelling method should lead? Choose one, or combine no more than two.**

- Layered-world narrative
- Persistent-object narrative
- Moviescroller: video, image sequence, or 3D timeline
- Sticky chapter narrative
- Graphic-sequence narrative
- State-transformation narrative
- Pan-and-zoom narrative
- Horizontal chapter narrative
- Typography-led narrative
- Show-and-play narrative
- Hybrid: name no more than two methods

Include the selected method in the shared restatement. Do not infer it from the word “Parallax.” If the confirmed restatement omits it, stop before design and return to the [Mandatory Brief](../AGENTS.md).

## Creative Purpose

Use the confirmed direction to resolve purpose, audience, and character; use [Grid and Layout](../ui-design/grid-layout.md) for structure and [Visual Hierarchy](../ui-design/visual-hierarchy.md) for perceptual priority.

Use [Gestalt](../ui-design/gestalt.md) to preserve perceived continuity between scenes and [Balance](../ui-design/balance.md) to distribute weight between the focal subject and supporting regions.

Use native scrolling to reveal depth, continuity, or transformation through a finite sequence of meaningful scenes. Keep the product, story, message, and action understandable without motion.

A long page, reveal animation, sticky image, or animated hero alone is not Parallax.

## Required Parallax System

Apply [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Scale and Proportion](../ui-design/scale-proportion.md), [Rhythm and Space](../ui-design/rhythm-space.md), and [Responsive Adaptation](../responsive-adaptation.md) for supported structure and reflow.

Apply [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Balance](../ui-design/balance.md), and [Gestalt](../ui-design/gestalt.md) to keep each scene's subject dominant, its supporting planes subordinate, and its moving groups perceptually coherent. Resolve every scroll-linked mechanic and value through [Motion and Transition](../ui-design/motion-transition.md).

1. Use one primary method and no more than one supporting method.
2. Build `3–7` focal scenes. Give each scene one subject, one message, and one dominant transition.
3. Use no more than three depth planes: background, subject, and foreground.
4. Use no more than one active pinned region at a time. Never nest pinned regions, horizontal sequences, or internal scroll areas.
5. Divide every motion scene into entry, hold, and exit. Target `20% / 60% / 20%`; keep the message fully readable during the hold.
6. Use one motion vocabulary, one media finish, one light model, and one handoff language across the page.
7. Use no more than two dense motion sequences. Place a static section between them.
8. Keep navigation, forms, pricing, comparison, specifications, FAQ, and primary actions independent of page scroll.
9. Preserve native vertical scroll, scrollbar behavior, keyboard scrolling, touch panning, reverse movement, refresh, and mid-page entry.
10. Preserve the complete story and source order without transforms, pinning, horizontal movement, or autoplay.

Reference measurements in this profile are art-direction targets. Resolve the nearest supported values through the linked canonical Alpy skills; never hard-code unsupported values.

## Method Specifications

Use the confirmed method exactly:

| Method | Required structure |
|---|---|
| Layered world | Use `2–3` planes. Limit total travel to roughly `4vh` for the far plane, `8vh` for the subject, and `12vh` for the near plane. |
| Persistent object | Pin one object across `3–5` beats and `250–500vh` of scroll. Keep it at roughly `40–70%` of the stage; limit scale to about `0.8–1.2` and rotation to `15°`. |
| Moviescroller | Scrub one video, image sequence, or 3D camera across `3–6` chapter stops and `300–600vh`. Provide poster, captions, and complete static states. |
| Sticky chapters | Pair one fixed visual with `3–5` text steps of roughly `80–120vh` each. Give the visual `55–65%` of a wide layout. |
| Graphic sequence | Show `3–6` explicit visual states. Keep each stable for at least half its step; use cuts or one consistent fade, wipe, or mask. |
| State transformation | Use `3–5` named states. Change one primary property or relationship per beat and show the intermediate state clearly. |
| Pan and zoom | Move through `3–5` destinations. Keep the focal marker visible and limit ordinary scale change to roughly `1–2.25×`. |
| Horizontal chapters | Use one sequence of `3–6` panels driven by `250–450vh` of vertical travel. Provide visible progress, direct controls, and a vertical fallback. |
| Typography led | Use `2–4` display phrases of no more than `10` words each. Keep every phrase stable for at least half its step. |
| Show and play | Trigger one muted media event per chapter. Pause it when absent, expose replay, and keep the message available outside the media. |

For a hybrid, assign one method to the primary sequence and the other to one bounded supporting sequence. Do not merge both methods into every section.

## Grid and Composition

Apply [Grid and Layout](../ui-design/grid-layout.md), [Alignment](../ui-design/alignment.md), [Scale and Proportion](../ui-design/scale-proportion.md), [Visual Hierarchy](../ui-design/visual-hierarchy.md), [Balance](../ui-design/balance.md), [Gestalt](../ui-design/gestalt.md), and [Rhythm and Space](../ui-design/rhythm-space.md).

- Target a `12`-column desktop, `8`-column tablet, and `4`-column mobile relationship; resolve the nearest canonical grid.
- Keep every scene on one shared container and grid. Let full-bleed media leave the container only inside a deliberate stage.
- Use `7/5` or `8/4` media-to-copy splits on wide screens. Alternate sides only when it clarifies sequence.
- Give a pinned stage at least `100svh`. Keep text, controls, and focal media inside safe viewport bounds at every state.
- Use one dominant media mass and one compact copy block per focal scene. Avoid dashboard grids and decorative card stacks.
- Follow each dense stage with visible release space before the next pinned or animated region.

## Hero and Opening Region

Apply [Hero](../hero.md) for the confirmed structure, [User Experience](../user-experience.md) for message and action semantics, and [Responsive Adaptation](../responsive-adaptation.md) for source order and reflow.

Use [Visual Hierarchy](../ui-design/visual-hierarchy.md) and [Balance](../ui-design/balance.md) to keep the opening subject dominant without competing with the proposition or action. Use [Alignment](../ui-design/alignment.md) for persistent scene axes and [Scale and Proportion](../ui-design/scale-proportion.md) for the focal subject's supported size.

Use the hero structure and optional treatments confirmed through [Agent Instructions](../AGENTS.md). Parallax is a motion treatment, not permission to replace that choice.

1. Show the H1, helper, and primary action within the first `100svh`, before scroll is required.
2. Use one focal subject at roughly `45–70%` of the stage and no more than two supporting depth planes.
3. Keep the H1 and primary action stable. Move the subject or surrounding field, not the complete interface.
4. Complete any opening scrub or object-settle sequence within `200vh`, then hand off to a normal section.
5. Show the next section edge, continuation cue, or subject trajectory before the first viewport ends.
6. Do not use a preloader narrative, forced intro, hidden CTA, generic dashboard mockup, or unapproved product object.

## Typography

Apply [Typography and Readability](../ui-design/typography-readability.md) for every complete canonical tuple, including family, role, size, weight, line height, letter spacing, measure, wrapping, scaling, and readable text flow.

Use one display statement per focal scene, normally `2–4` lines, and keep body copy within roughly `45–70` characters per line. Keep overlay copy inside one consistent alignment zone.

Text may cross behind a subject only when every word remains available as live text and the complete message is readable in a stable state. Limit word or character progression to the confirmed typography-led method. Never animate body copy, navigation, controls, pricing, specifications, policy, or feedback.

## Media, Color, and Depth

This profile defines its Parallax shape language. Apply the confirmed direction, [User Experience](../user-experience.md), [Scale and Proportion](../ui-design/scale-proportion.md), [Color Discipline](../ui-design/color-discipline.md), [Border and Divider](../ui-design/border-divider.md), and [Elevation](../ui-design/elevation.md).

Parallax depth planes describe narrative media position; they do not authorize invented interface layers or shadows. Resolve media-frame edges and radius through [Border and Divider](../ui-design/border-divider.md), interface-layer relationships and shadows through [Elevation](../ui-design/elevation.md), and canvas, light, gradient, grade, and contrast roles through [Color Discipline](../ui-design/color-discipline.md).

- Use real, permissioned product, object, interface, human, environmental, diagrammatic, or editorial media in every focal scene.
- Keep the focal subject at least `8%` from unsafe crop edges during its stable state.
- Coordinate crop, perspective, lighting, edge treatment, shadow, grain, and color grade across all scenes.
- Use scale for proximity, translation for direction, and rotation only for a real viewpoint change.
- Use one accent family, one base canvas, and no more than one alternate canvas. Change canvas only at a chapter boundary.
- Keep gradients and shadows attached to the shared light model; do not add independent glow to each scene.
- Do not fabricate products, people, interfaces, metrics, testimonials, environments, or frames. Do not substitute CSS shapes for missing narrative media.

## Scroll, [Animation, and Transitions](../ui-design/motion-transition.md)

Apply [User Experience](../user-experience.md), [Motion and Transition](../ui-design/motion-transition.md), and [Accessibility Audit](../accessibility-audit.md).

1. Never capture, delay, accelerate, queue, or reshape page scrolling. Smooth only the visual response and keep visual lag below roughly `120ms`.
2. Map scrubbed motion directly and reversibly to scroll position. No state may depend on a previous animation finishing.
3. Use linear progress for scrubbing, ease-out for entry, and ease-in-out for scene handoffs.
4. Use opacity plus one transform for ordinary reveals. Target `24–48px` travel and `400–700ms`; reveal once and leave content stable.
5. Keep general plane movement within `12vh`, scale within roughly `0.9–1.1`, and rotation within `8°`. Use the wider method-specific limit only for the confirmed focal object.
6. Use one handoff family: crossfade, crop or mask, spatial pass, or canvas inversion. Do not combine all four.
7. Complete the outgoing message before replacing, covering, or reducing its contrast.
8. Never pin focusable controls beneath moving layers. Keep hover, focus, pressed, media, carousel, accordion, and CTA behavior independent of page scroll.
9. Give video a poster and controls when user playback matters. Never autoplay audio.
10. Verify slow, rapid, reverse, skipped, resized, refreshed, and mid-page entry states.

## Responsive and [Reduced Motion](../ui-design/motion-transition.md)

Apply [Responsive Adaptation](../responsive-adaptation.md), [User Experience](../user-experience.md), and [Accessibility Audit](../accessibility-audit.md).

On narrow viewports, use one column in media-then-copy source order, no more than two depth planes, and no more than `6vh` of movement. Convert horizontal sequences to vertical panels.

Remove pinning when it clips content, covers focus, creates internal scrolling, or leaves less than half the viewport for readable content. Use the same fallback for short viewports, zoom, large text, localization, limited performance, or unsupported behavior.

For reduced motion, remove pinning, frame and video scrubbing, character effects, automatic movement, large scale changes, and camera travel. Render every scene as a complete static composition in the same source order; do not merely shorten duration.

## Page Rhythm

Apply [Rhythm and Space](../ui-design/rhythm-space.md).

Use this default sequence when the confirmed content supports it:

1. Confirmed hero with one opening motion event.
2. Static proposition, proof, or orientation.
3. Primary `3–5`-beat scroll narrative.
4. Static product detail, evidence, process, or comparison.
5. Optional supporting scroll sequence using the second confirmed method.
6. Static pricing, FAQ, specifications, trust, or decision support.
7. Stable final CTA that recalls the opening subject or transition.

Skip unsupported sections. Do not add scroll distance, empty scenes, or decorative pauses to make the page feel longer.

## Creative Workflow

1. Inventory approved copy, media, evidence, and actions.
2. Confirm one primary method, optional secondary method, explicit mode, and hero structure.
3. Storyboard every scene as a complete static composition.
4. Assign each scene one subject, message, transition, depth plan, scroll distance, and fallback.
5. Establish the shared [grid](../ui-design/grid-layout.md), [typography](../ui-design/typography-readability.md), media finish, light model, [color roles](../ui-design/color-discipline.md), and [handoff family](../ui-design/motion-transition.md).
6. Add motion only where it clarifies depth, continuity, comparison, or transformation.
7. Test every intermediate frame, reverse path, action, breakpoint, and preference state; remove failed effects.

## Canonical Resolution

Resolve every decision in this order:

1. After the shared chat confirmation, resolve an explicit canonical `light` or `dark` mode before rendered work or component selection.
2. Preserve the confirmed narrative method, hero structure, information architecture, hierarchy, density, source order, interactions, and responsive priorities.
3. Confirm authoritative content, media, rights, captions, alternatives, evidence, states, actions, and destinations; report missing truth instead of fabricating it.
4. Resolve supported components and behavior through `alpy/components.md`, then component styling through `alpy/component-tokens.md`.
5. Resolve color roles through [Color Discipline](../ui-design/color-discipline.md) and `alpy/semantic-tokens.md`.
6. Resolve complete typography roles and tuples through [Typography and Readability](../ui-design/typography-readability.md) and `alpy/type-scale.md`.
7. Resolve [spacing](../ui-design/rhythm-space.md), [grid](../ui-design/grid-layout.md), [alignment](../ui-design/alignment.md), [radius and border](../ui-design/border-divider.md), icon, [size and proportion](../ui-design/scale-proportion.md), [surface and color](../ui-design/color-discipline.md), [depth and shadow](../ui-design/elevation.md), breakpoint, and supported [motion values](../ui-design/motion-transition.md) through their applicable UI skills and `alpy/foundations.md`.
8. Reach `alpy/palette.md` only through semantic or component bindings. Use canonical assets for system meaning and only approved project media for narrative content.

Across these resolutions, use [Visual Hierarchy](../ui-design/visual-hierarchy.md) for perceptual rank, [Balance](../ui-design/balance.md) for visual-weight distribution, and [Gestalt](../ui-design/gestalt.md) for plane and scene relationships.

If native scrolling, meaningful static order, reduced-motion behavior, responsive reflow, or the required motion relationship cannot be supported, report Parallax as unsupported rather than inventing local behavior.

## Mandatory Style Fidelity

Apply only the confirmed style, subtype, material, mode, brief, and related guidance. Do not reinterpret, mix, soften, substitute, or drift. If faithful execution is impossible, stop and report the gap.

Parallax must remain visibly recognizable across the concerns below, while the correlated UI skills and canonical component system remain the primary owners of their mechanics and values.

The direction designated in this skill file must visibly govern composition, grid, hierarchy, spacing, typography, color, surfaces, material texture, background patterns, imagery, photography treatment, illustration, crops, masks, cutouts, collage, image effects, filters, blending, shapes, borders, edges, separators, section transitions, cards, buttons, navigation, forms, icons, decorative marks, depth, shadows, motion, interaction states, responsive behavior, density, and page rhythm.

The implementing agent may not self-approve. A separate visual reviewer or the user must approve the rendered opening before full implementation and the final wide and narrow renders before delivery. Generic, mixed, unclear, missing, or conflicting treatments fail and must be revised. Code, class names, and element presence are not evidence.

## Success Criteria

Approve Parallax only when every condition is true:

1. The confirmed brief names one primary method and no more than one supporting method.
2. The page uses `3–7` purposeful scenes, one subject and message per scene, no more than three depth planes, and no nested pinned regions.
3. Every motion scene has a readable entry, majority hold, and exit; the page uses no more than two dense motion sequences and one horizontal sequence.
4. Native scrolling, reverse movement, keyboard input, touch panning, refresh, resize, and mid-page entry remain immediate and correct.
5. Resolve complete canonical typography through [Typography and Readability](../ui-design/typography-readability.md) and color through [Color Discipline](../ui-design/color-discipline.md). Never invent typography tuples, colors, tints, alpha values, gradients, motion values, depth values, or alignment treatments.
6. Every focal scene uses authentic, permissioned media with one coordinated crop, perspective, lighting, [edge](../ui-design/border-divider.md), [shadow](../ui-design/elevation.md), and [color](../ui-design/color-discipline.md) finish.
7. The H1, primary action, navigation, controls, forms, pricing, specifications, and decision content remain readable and operable without scroll animation.
8. Mobile, short-viewport, zoom, large-text, localization, reduced-motion, and static fallbacks preserve the complete story and source order.
9. Video and frame sequences provide posters and static states; horizontal sequences provide progress, direct controls, and a vertical fallback.
10. The page contains no scroll hijacking, filler scenes, decorative empty travel, fabricated media, fake product UI, constant motion, overlapping focusable layers, or effects without narrative purpose.

If any condition fails, revise the composition or do not use Parallax for that region.
