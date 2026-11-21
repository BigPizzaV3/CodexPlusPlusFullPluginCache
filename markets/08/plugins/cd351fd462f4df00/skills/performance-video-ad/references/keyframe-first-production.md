# Keyframe-first hybrid production

Use this workflow after Animatic approval and before any paid video call. Its purpose is to resolve taste, composition, identity, and shot continuity with still images rather than repeated full-motion generations.

## Production unit

Build the complete ad scene by scene, but do not split one physical cause-and-effect event into unrelated clips.

- Keep exact chat, dashboards, Japanese, captions, logos, CTA, prices, and legal copy in Remotion.
- Create or composite static character, environment, product, and cinematic action frames before motion.
- Animate only shots whose value depends on motion, atmosphere, transformation, or material reaction.
- Keep `impact -> rupture -> passage -> landing` in one short generated shot when the same body must cause every step.

## Required still gate

For every AI-motion shot, prepare:

1. `start_frame`: the exact composition that must connect from the previous deterministic scene;
2. `peak_action`: the single frame that proves the intended force, pose, or transformation;
3. `endpoint`: the composition that must connect to the next deterministic scene.

The frames may be made with image generation, deterministic compositing, or both. Exact UI should be built deterministically. When exact scene continuity and subject identity are both critical, compose them into the same approved start frame or select an endpoint that explicitly supports both controls. Do not assume loose reference images will lock the first generated frame.

Create a zero-cost transition preview from the stills and adjacent Remotion frames. Human approval must cover:

- visual identity;
- composition and screen occupancy;
- the peak action's force or emotional value;
- continuity from the previous scene;
- continuity into the next scene;
- acceptable crop and safe-zone space.

Static approval is not permission to generate a continuity-dependent downstream shot before its upstream actual output exists. Record shot order in `shot-dependency-graph.json`. For a continuous or match-cut edge, extract the approved upstream video's actual last frame, use that exact file as the downstream start input, and require matching SHA-256 values. A candidate endpoint still proves design intent only; it cannot stand in for model output. Read [actual-shot-continuity.md](actual-shot-continuity.md).

## Paid motion gate

Block paid video generation unless all of the following are true:

- the Animatic is approved;
- all three required keyframes are approved;
- the transition preview is approved;
- the target passes `validate-shot-dependency-graph.mjs` in actual-output dependency order;
- the motion shot has one coherent event and one camera setup;
- exact text and UI are assigned to Remotion;
- the provider input roles match the controls actually needed;
- one-attempt cost approval exists in the current task.

Keep the first paid motion attempt short, normally three to five seconds when the endpoint supports it. Do not lengthen a single-event shot merely because the provider supports a longer maximum. Front-load the event when the approved intent is impact or interruption.

## Failure handling

When a raw video fails taste, force, identity, or continuity:

1. mark it `FAIL` and preserve it as generation learning;
2. identify which still or transition contract was missing or misleading;
3. return to the keyframe board rather than rewriting the long motion prompt first;
4. do not make another paid request until the revised stills and transition preview pass human review.

Do not treat speed ramps, camera shake, debris overlays, or sound effects as proof that a weak raw motion shot passed. They may polish an approved shot; they may not rescue a failed central event.
