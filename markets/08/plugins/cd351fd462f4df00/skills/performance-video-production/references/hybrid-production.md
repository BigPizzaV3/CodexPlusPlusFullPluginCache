# Adaptive hybrid production

## Principle

Match control to risk. Use broad cinematic direction when the model should author motion and camera; use keyframes and references only when identity, composition, continuity, or an endpoint must be exact. Keep exact surfaces deterministic in either case.

## Asset layers

Use four layers:

1. `deterministic`: exact UI, Japanese, logo, CTA, numbers, reports, layout, timing;
2. `static_generated`: character, product, environment, texture, or cinematic keyframes;
3. `motion_generated`: short movement between approved visual anchors;
4. `composition`: Remotion/FFmpeg cuts, overlays, crop, audio, safe zones, codec.

Do not flatten these into one giant prompt.

## Control gate

For every generative unit, approve the direction package and its control budget. Require only the anchors selected by the route:

- `none`: prompt-directed choreography; no keyframe approval;
- `first_only`: the opening composition must connect or remain exact;
- `first_last`: both boundary compositions are strict;
- `start_peak_end`: an exceptional controlled route where the middle event itself is fragile and a verified endpoint supports the control.

Every non-`none` policy needs a named risk. For continuous or match-cut units, a planned endpoint is not an upstream result. After the upstream Raw passes QC, extract its actual final frame and use its exact path and SHA-256 downstream.

## Choosing controls

Use only controls supported by the current official endpoint. Prefer first/last-frame interpolation when both compositions are strict. Add identity references when subject fidelity is the risk. Add a middle keyframe when camera travel or appearance drift is the named risk and the endpoint supports it. Use video-to-video when an existing motion structure is valuable and the permitted transformation strength is understood.

Do not hard-code a permanent winning model. Capabilities and schemas change. Record the official source, date, reference count, frame controls, duration, resolution, audio behavior, price, and caveats before approval.

## Generation-unit size

Keep one dominant viewer job and one coherent visual concept per generated unit. Do not generate a full ad simply because a model supports the duration. Do not micro-split one causal event, one material transformation, or one unified editorial installation when continuity and finish are the viewer value.

Typical production split:

- Hook: plausible work or social surface, with exact copy composited when required;
- cinematic problem or transformation: one coherent directed sequence when the model can carry it;
- identity- or endpoint-sensitive transition: one controlled unit with minimum anchors;
- proof or deliverable: readable real artifacts with optional generated spatial treatment;
- End Card: deterministic.

## Raw QC before polish

Review the unmodified provider output at natural speed and frame-by-frame. Reject it if:

- the approved causal event is absent or ambiguous;
- force or motion energy is wrong;
- subject identity or product shape drifts;
- hands, limbs, faces, props, or text are malformed;
- the first or final frame cannot connect;
- cadence judders at the intended final frame rate.

Camera shake, debris, SFX, speed ramps, and overlays may polish a passing Raw. They may not rescue a failed event.

## Final cadence

Prefer the final delivery frame rate to match the human-approved Raw's native rate. If deterministic sections use another frame rate, render them separately and splice the untouched native sequence into the final-rate master. Avoid interpolation unless separately reviewed. Decode the entire MP4 and test the actual target player, especially splice boundaries.
