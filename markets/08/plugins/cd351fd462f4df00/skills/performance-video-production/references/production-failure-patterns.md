# Production failure patterns and recovery

Use this reference only when a production artifact fails, a user reports a symptom, or a proposed fix risks changing approved Creative. It is a diagnosis catalog, not a recipe book. Preserve the approved handoff and choose the smallest recovery that removes the confirmed defect.

## Contents

- [Stage-first diagnosis](#stage-first-diagnosis)
- [Learning promotion](#learning-promotion)
- [Recurring failure patterns](#recurring-failure-patterns)
- [What does not belong in the global Skill](#what-does-not-belong-in-the-global-skill)

## Stage-first diagnosis

Trace the same event through this evidence chain:

```text
approved input
  -> provider or source Raw
  -> fitted/retimed asset
  -> deterministic composition
  -> isolated audio/video stems
  -> final mix and encode
  -> target player
```

Find the earliest stage where the symptom is visible or audible. Do not blame a model for a defect that first appears after ingest, retiming, composition, mixing, encoding, or playback. Do not "fix" an upstream asset that passes its own natural-speed review.

For every incident, record:

1. the viewer-observed symptom;
2. the earliest bad stage and the last known-good stage;
3. direct evidence from both stages;
4. whether the root cause is confirmed, inferred, or unknown;
5. the smallest recovery that preserves approved Creative;
6. a prevention gate stated independently of a specific provider or tool.

Use `assets/templates/production-learning.json`. The validator intentionally blocks unsupported root-cause certainty and premature global promotion.

## Learning promotion

Route learnings by stability, not by how frustrating the incident felt.

| Learning | Destination |
|---|---|
| One job, one provider response, exact timestamp, or personal Taste choice | job `production-learning.json` |
| Transferable symptom/evidence/cause/recovery pattern | this reference |
| Stable production invariant or authority boundary | `SKILL.md` |
| Deterministic check that should fail automatically | `scripts/` plus fixtures |
| Campaign response or business outcome | performance learning system, never this Skill |

Normal promotion requires confirmation in at least two independent jobs or a reproducible test. A single incident may be promoted when failure can materially waste paid requests, corrupt the deliverable, expose private information, or distribute/activate without authority. A provisional safety rule may fail closed while root cause is investigated, but must remain marked as provisional.

Prefer general gates such as "compare Raw with the first composed artifact" over fixed HOW such as "always use model X" or "always cut at 4.5 seconds." Model names, exact commands, gains, crop percentages, and timestamps remain job evidence unless the verified capability itself is the subject.

## Recurring failure patterns

### PF-01: Raw is stable but the composed video jitters or reverses

- **Symptom:** the final or previewed shot shakes, repeats frames, moves backward, or has uneven cadence while the downloaded Raw plays smoothly.
- **Required evidence:** natural-speed Raw; first composition without overlays or effects; frame rate, frame count, timestamps, duration, and aligned frame samples.
- **Likely fault domain:** ingest/decode, variable-to-constant frame conversion, timestamp handling, looping, retiming, duplicated/dropped frames, or render media component.
- **Do not assume:** that the generation model failed, or that stabilization can repair temporal reversal.
- **Recovery:** reproduce a treatment-free round trip; correct timestamp/frame mapping; preserve forward-only motion; then re-add deterministic layers. Regenerate only when the Raw itself fails.
- **Prevention gate:** approve Raw cadence and first-composition cadence separately at natural speed.

### PF-02: A generated shot does not connect to adjacent scenes

- **Symptom:** the action, camera, background, character pose, lighting, or material state jumps at the cut even when the generated shot looks good alone.
- **Required evidence:** actual accepted upstream last frame, generated first/last frames, actual downstream first frame, and a boundary contact sheet or short splice.
- **Likely fault domain:** planned rather than actual endpoints, over-broad single-shot generation, missing identity reference, or incompatible deterministic/generative boundaries.
- **Do not assume:** that a good standalone Raw is usable in the edit.
- **Recovery:** use the actual accepted boundary frame; regenerate or deterministically bridge only the failing boundary; keep exact UI and Japanese outside the generated motion.
- **Prevention gate:** approve a zero-cost boundary preview before a paid continuity shot and review the final splice before full assembly.

### PF-03: Too much exact advertising work is delegated to one generation

- **Symptom:** weak causal force, identity drift, malformed UI/Japanese, unstable logo/CTA, or an attractive shot that cannot satisfy frame-accurate timing.
- **Required evidence:** list of exact constraints requested from the generator and which failed.
- **Likely fault domain:** generation scope exceeds the tolerance for variation.
- **Do not assume:** that a longer prompt or a more expensive model removes conflicting exact constraints.
- **Recovery:** preserve the approved idea, split only at a named semantic, camera, continuity, or exact-surface boundary, then assign the minimum controls each resulting unit needs. Keep exact content deterministic without turning every visual Beat into a separate generated clip.
- **Prevention gate:** classify every element as deterministic, generative, or hybrid before paid execution.

### PF-04: Character or product identity drifts before motion

- **Symptom:** the subject is recognizable only in concept, has the wrong silhouette/details, or differs from the canonical reference.
- **Required evidence:** canonical reference, every proposed identity anchor, and a side-by-side identity review. Do not create extra peak or endpoint anchors unless a named continuity risk requires them.
- **Likely fault domain:** wrong reference, weak reference coverage, or keyframe generation drift.
- **Do not assume:** that motion generation will restore a wrong keyframe identity.
- **Recovery:** reject before paid motion; rebuild the keyframe from canonical views and named identity constraints.
- **Prevention gate:** identity PASS on all anchor frames before motion approval.

### PF-05: TTS fails, overruns its slot, or becomes unnatural after fitting

- **Symptom:** provider rejection, missing/foreign tail, muffled timbre, clipped copy, excessive speed, or narration that no longer aligns with the visual cause.
- **Required evidence:** exact requested text, provider response, saved Raw audio, expected slot, first/last audible time, tempo ratio, and human transcript/timbre review.
- **Likely fault domain:** provider acceptance edge, insufficient timeline headroom, unsafe silence trimming, excessive fitting, or late visual lock.
- **Do not assume:** a documented language option guarantees every short fragment is accepted, or a waveform proves correct Japanese.
- **Recovery:** preserve the paid result; trim verified outer silence; evaluate within the approved short-form tempo envelope; use a bounded timeline extension; request a new paid synthesis only with fresh approval.
- **Prevention gate:** test the highest-risk fragment first and plan provisional speech at 88–92% slot occupancy. Follow [audio-production-and-qc.md](audio-production-and-qc.md) for exact QC.

### PF-06: Source audio is valid but a required bus disappears from the final

- **Symptom:** an early Hook, CTA, SFX cluster, music window, or retained body audio is silent even though its source file plays and whole-file loudness passes.
- **Required evidence:** isolated full-length stems and measured expected-active windows in the final timeline, plus the encoded target-player file.
- **Likely fault domain:** final filter graph, bus routing, trim/offset, mapping, ducking, or encode.
- **Do not assume:** source validity or global loudness proves that each intended bus survived.
- **Recovery:** render and verify each bus on the full timeline; identify the first missing stage; repair routing; rebuild and fully decode the final.
- **Prevention gate:** per-window stem presence for every expected narration, SFX, music, and retained-body bus.

### PF-07: SFX exists but weakens comprehension

- **Symptom:** narration becomes hard to hear, accents feel random, the mix is tiring, or an intended silence loses tension.
- **Required evidence:** narration-only, SFX-only, full-mix, and mute-picture reviews at natural speed on phone speaker and headphones.
- **Likely fault domain:** decoration without sound intent, transient masking, too many unrelated families, or cues aligned to cuts rather than causes.
- **Do not assume:** more frequent SFX automatically creates short-form tempo.
- **Recovery:** keep causal and payoff cues; remove decorative competition; reuse a motif for repeated events; duck or spectrally soften overlap.
- **Prevention gate:** every cue maps to an approved intent and visible final-timeline trigger.

### PF-08: Proof looks plentiful but not credible or readable

- **Symptom:** documents appear as tiny mosaics, dummy content is presented as real, private information is visible, or the viewer cannot understand what is being delivered.
- **Required evidence:** source audit, permission/anonymization status, target-size frames, and mute review.
- **Likely fault domain:** quantity prioritized over a readable anchor, missing provenance, or unsafe proof substitution.
- **Do not assume:** blur or visual density creates credibility.
- **Recovery:** lead with one large source-audited page, use rapid quantity only as support, return to a readable payoff, and label mock/dummy material honestly.
- **Prevention gate:** provenance and privacy PASS plus at least one readable proof anchor at target 9:16 size.

### PF-09: The viewer cannot understand the Hook or copy without narration

- **Symptom:** text is too small, the incident disappears before it can be parsed, camera movement competes with reading, or the meaning exists only in audio.
- **Required evidence:** first-frame and key-frame captures at target mobile size, mute playback, and time-to-understand review.
- **Likely fault domain:** hierarchy, hold duration, over-dense UI, repeated micro-zooms, or narration carrying an essential fact alone.
- **Do not assume:** technically legible text is comprehensible at feed speed.
- **Recovery:** enlarge the decisive fact, remove administrative copy, hold the incident, use one intentional reframing, and keep essential meaning visible and spoken where required.
- **Prevention gate:** Hook and CTA pass mute comprehension; major payoff passes both picture and narration checks.

### PF-10: The encoded file stops, crashes, or differs in the target player

- **Symptom:** playback ends early, freezes after a scene, loses audio, or behaves differently from the editor preview.
- **Required evidence:** video-stream duration, container duration, full decode, timestamp monotonicity, and target-player playback.
- **Likely fault domain:** damaged stream, inconsistent duration, non-monotonic timestamps, unsupported pixel/audio format, or incomplete encode.
- **Do not assume:** a successful render command or editor preview proves delivery validity.
- **Recovery:** identify the first decode error or timestamp discontinuity, rebuild only the defective stage, encode to the declared compatibility profile, and review the complete file.
- **Prevention gate:** full-file decode plus target-player review before Creative approval.

### PF-11: A precise deterministic scene still looks like a prototype

- **Symptom:** copy, timing, and hierarchy are correct, but the hero scene feels like an interface demo, slide animation, or product prototype rather than a finished performance ad.
- **Required evidence:** approved viewer job, route plan, natural-speed deterministic preview, mute review, and named motion qualities the scene must carry.
- **Likely fault domain:** route selection. The primary picture was assigned to deterministic motion even though the viewer job depends on spatial depth, material interaction, organic camera motion, natural subject motion, or environmental parallax.
- **Do not assume:** that all Remotion or code-native motion is low quality, or that generation should own exact Japanese, UI, CTA, or brand surfaces.
- **Recovery:** preserve exact surfaces and timing, but move the cinematic picture job to `directed_generation` or `controlled_generation`. Lock the macro event and add only the identity, boundary, or endpoint anchors justified by a named risk; let the model direct the remaining camera and motion choreography. Realize exact copy and UI through the approved screen-native or world-binding mode.
- **Prevention gate:** validate `route-plan.json`; two or more organic/spatial motion needs require generated primary motion or an explicit natural-speed human Taste override. A world-bound exact surface also requires composite-feasibility PASS.

### PF-12: The generated Raw looks premium but the exact surface floats in a second world

- **Symptom:** the background has camera travel, perspective, depth, blur, or occlusion while the exact UI, mail, report, or copy remains fixed to screen coordinates or moves with unrelated CSS transforms.
- **Required evidence:** selected Visual Treatment, object ownership, binding mode, moving composite proof, background and surface tracks, boundary frames, and natural-speed composite review.
- **Likely fault domain:** the same semantic object has two geometry owners, a world-bound surface was implemented as screen-space overlay, or production bypassed the approved binding proof.
- **Do not assume:** that accurate Japanese, a technically valid render, or an attractive Raw makes the composite one visual world.
- **Recovery:** return to surface ownership and binding mode. Use the same tracked plane, corner pin, UV/3D geometry, deterministic motion scaffold, or declared readable-anchor repair; otherwise move the exact surface to a genuine screen-native scene. Do not keep polishing a detached overlay.
- **Prevention gate:** `visual-treatment-contract.json` assigns one geometry owner per semantic object, and `compositing-feasibility-gate.json` passes relative motion, perspective, occlusion, look match, readability, and applicable trackability before handoff v4.

## What does not belong in the global Skill

Keep these in the job learning unless promotion criteria are met:

- an exact cut point, speed multiplier, gain, crop, prompt, or model name;
- one user's creative preference unless it becomes approved brand guidance;
- a provider error without saved evidence and a transferable diagnosis;
- a workaround that changes the approved Hook, Body, Promise, CTA, or timing contract;
- an inference stated as confirmed root cause;
- any claim that a production choice improved campaign performance without campaign evidence.

The catalog should teach how to locate and recover from a class of failure. It should not force every future ad to look or move like the incident that taught the lesson.
