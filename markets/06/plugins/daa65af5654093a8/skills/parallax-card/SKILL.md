---
name: parallax-card
description: Generate or adapt interactive collectible parallax cards with separate background and character artwork, 3D tilt, foil lighting, and optional flip and layer views. Use for trading-card experiences like Parallax; not generic scrolling parallax or desktop pets.
---

# Parallax Card

Build a collectible whose world, subject, and printed details move independently. This skill captures the Parallax/Aetherion implementation as an adaptable reference, not a mandatory character or page design.

## Choose the deliverable

Follow the user's subject, art direction, framework, and requested scope. For a new card with no stack specified, a React component with CSS 3D transforms is a useful default. For existing apps, integrate with their conventions. A request for a static card image needs artwork and composition, not an unsolicited application. Do not include the source project's companion pet, video pipeline, accounts, or deployment unless requested.

When the user requests an **interactive parallax card**, make a working interactive preview the primary deliverable. A transparent subject cutout, composed still image, screenshot, or source archive can support it but cannot satisfy the interaction request on its own. Use an in-conversation interactive surface when available; a full website or deployment is unnecessary just to demonstrate the card. Otherwise provide a directly usable preview link that opens the running card.

Use supplied artwork when suitable. Otherwise generate a background and transparent subject as separate assets using the available image-generation tool and its instructions. Read [artwork prompts](references/artwork.md) for exact source examples; adapt subject, palette, composition, and lighting together. Aetherion and its stats are example content.

## Artwork and composition

- Generate environment-only portrait art and a separate full-silhouette subject with true alpha, generous margins, and no baked-in frame or text. Match light direction and palette. Keep header and lower text zones visually quiet.
- Inspect the images and alpha before integration: a checkerboard painted into an opaque image is not transparency. Preserve alpha when copying. Place translucent environment art over an opaque base.
- Keep names, stats, rules, and edition marks as live text. Art generation should not produce these labels. Favor readable contrast over a strong foil effect.
- Overscan the background to cover its maximum displacement. Let the foreground break the inner artwork frame where intended, while keeping its silhouette within the stage at extreme tilt.
- Retain the actual prompts and final asset paths with the output. Never reuse the example's generation/provenance claims for newly generated art.

## Implementation

For React, read [integration notes](references/react.md) and adapt the files in `assets/react/`. They preserve the source card's motion and visual treatment without requiring its original repository. Artwork binaries are intentionally not bundled: supply or generate them.

Keep separate elements for perspective, interactive tilt, flip, front/back faces, and layers. Preserve 3D transforms through the relevant ancestors; clipping, filters, opacity, and blending can flatten a 3D context, so apply them locally and inspect the result. Clip the background within its own plane rather than clipping the entire foreground silhouette.

Useful source defaults (adjust to the design): 332 × 464 card, 1100px perspective, ±14° maximum input tilt, and layer Z positions of 8px for scenery, 22px for particles, 45px for the subject, 58px for print, and 62–63px for rim/light. Background displacement runs opposite to the subject. Keep text displacement modest.

Drive the light position from the same pointer coordinates as tilt. Use restrained gradient foil and radial glare with decorative layers ignoring pointer input. Finish variations should alter rim, foil, and selected art grading coherently. Provide foil, depth, finish, flip, and exploded-layer controls only where they fit the requested experience.

## Motion and interaction invariants

- Normalize and clamp input; smooth with elapsed time. Apply depth strength once, so a 50% setting does not unintentionally become 25%. Zero depth must neutralize input-driven rotation, displacement, lift, and light movement; a fixed presentation angle may remain.
- Update CSS variables through refs instead of rerendering React each frame. Stop requestAnimationFrame when settled or hidden; clean up listeners, pointer capture, and frames on unmount.
- Keep tilt and flip on separate wrappers. Suppress accidental flips after a drag; pointer cancellation must clear interaction state. Preserve vertical touch scrolling.
- Support keyboard tilt and reset, and Enter/Space for flip when present. Provide visible focus, useful accessible names, and announced toggle states. Hide the inactive face from assistive technology.
- Honor reduced motion at startup and when the preference changes: stop ambient/pointer motion and remove animated transitions while retaining usable controls and immediate state changes.
- If expanded view is included, implement dialog focus management, Escape, focus restoration, and scroll-lock cleanup.

## Verify and deliver

Run the target project's relevant build/lint checks. For an interactive request, open the actual preview in a browser and move a pointer or touch across the card. Confirm visibly distinct motion of the background, character, print, and foil layers; CSS variables changing or a successful build alone are insufficient. Check flipping if included, plus desktop and narrow mobile layouts. Also inspect pointer extremes, depth 0/50/100, finish and foil changes, drag versus tap, keyboard controls, and reduced motion. Inspect layer separation only if implemented. Check missing images, text contrast, horizontal overflow, clipping, and mirrored or leaking back-face content. Confirm animation settles and hidden-tab/unmount cleanup works when motion logic changes.

For an interactive request, present the directly usable preview link or embedded interactive surface **first**, then any source files or supporting stills. Label every still as **“static preview”**; never imply that an image demonstrates motion. If no interactive preview can be made available, state that limitation plainly and provide the working source files with instructions to run them. Do not substitute a generated card image without explaining the difference. Report any browser or generation checks that could not be performed; do not claim visual verification from source inspection alone.

Final handoff check: **“Can the user experience the parallax effect from the primary result I’m about to show?”** If the answer is no, the interactive-card task is not complete unless the preview truly cannot be made available and the limitation and working source are supplied as above.
