# Generative hero-shot control

## Purpose

Use this contract when one AI-generated moment carries the ad's main physical or cinematic payoff. It prevents two recurring failures: splitting one causal event across incompatible tools, and overloading one model with unlabelled references and a long prompt.

## One coherent shot

A coherent shot has:

- one camera setup;
- one dominant cause-and-effect event;
- one subject objective;
- one readable endpoint;
- at most five causal steps.

Storyboard beats are not automatic generation boundaries. Keep `impact -> rupture -> emergence -> landing` together when the same character must visibly cause the whole event. Split before or after the shot where exact UI, Japanese text, proof pages, logo, CTA, or legal copy becomes deterministic.

## Control budget

Count the controls that must succeed simultaneously:

- exact character identity;
- exact UI or readable text;
- physical contact and material reaction;
- camera movement;
- multiple timed actions;
- exact start or end composition;
- multiple characters or props.

High control burden is not solved by adding prose. Use this order:

1. Remove exact text and UI from the generated shot.
2. Reduce the shot to one dominant event and one camera setup.
3. Assign two character directions; add a low-detail motion driver only when motion remains the named uncertainty and the user accepts it.
4. Choose a model whose current official capabilities match the approved roles.
5. Split only at a deterministic or semantic boundary if the burden still exceeds verified capability.

## Reference pack

Start with the smallest sufficient pack:

1. `identity_front`
2. `identity_three_quarter`

Add `motion_driver`, `first_frame`, `last_frame`, or `scene_style` only to solve a named control problem. Do not assume a larger pack improves fidelity.

When used, a motion driver is intentionally low-detail. It carries only timing, path, force, pose, relative scale, and screen occupancy. Use a neutral silhouette or simple 3D proxy with no brand texture, face detail, text, logo, or finished environment. Its manifest role and prompt must both say `motion_only`. It is never mandatory: if human review says the proxy creates the wrong emotional expectation, remove it from the active reference pack.

Keep the human Animatic separate. It proves that people can follow the story and pacing; it does not become a visual reference unless a deliberate conditioning experiment is approved.

## Capability refresh

Before provider lock, capture a dated snapshot from official sources:

- model and endpoint;
- input modes and reference roles;
- maximum number and duration of image/video references;
- first/last-frame support;
- aspect, duration, resolution, and audio limits;
- current price and commercial-use notes;
- language or prompt caveats;
- adapter schema and output path.

Treat named models as current candidates, not permanent defaults. General arena performance is not a brand-subject benchmark. A comparable paid benchmark uses the same reference pack and causal intent across candidates and requires explicit approval.

## Responsibility boundary

Use AI video for motion, material reaction, character action, atmosphere, and a coherent cinematic event. Use Remotion or FFmpeg for exact Japanese text, real UI, captions, logo, CTA, price, proof pages, safe zones, audio mix, duration, and final codec.

Do not divide one contact event between AI and Remotion. If a body causes a screen to bend and tear, the body interaction and screen reaction belong to the same generated shot. Deterministic UI can end immediately before the hit and resume after the raw shot passes review.

## Raw hero gate

Technical QC and Creative QC are separate. Before integration, inspect the raw shot at natural speed. All five intent-critical checks must pass:

1. central causal event;
2. impact energy;
3. identity fidelity;
4. natural-speed readability;
5. adjacent-surface continuity when the shot claims to break or transform the preceding deterministic screen.

Identity references and first-frame anchors solve different problems. A reference-to-video route may preserve the subject while replacing the adjacent UI or surface. An image-to-video route may lock the first frame while losing a hidden subject. When both are critical, approve a composite start keyframe containing the exact deterministic surface and enough correct subject information, or choose a verified route that accepts both controls. Do not infer first-frame continuity from loose image references.

Any failure means `FAIL`. Do not use `PASS_WITH_DEVIATIONS` when the deviation removes the approved hero intent. Record the failure as generation learning, keep automatic regeneration off, and return to the reference pack, model route, or shot simplification. Human raw-shot approval is mandatory before deterministic integration.

## Compact specification

Keep the provider-facing shot specification compact:

- one-sentence intent;
- duration and aspect ratio;
- camera setup;
- dominant event;
- three to five causal steps;
- role-labeled references;
- AI versus deterministic responsibilities;
- short prompt kernel and short avoid list;
- raw hero QC state;
- paid, distribution, and publication locks.

Validate it with:

```bash
node scripts/validate-coherent-shot.mjs <hero-shot-spec.json>
```
