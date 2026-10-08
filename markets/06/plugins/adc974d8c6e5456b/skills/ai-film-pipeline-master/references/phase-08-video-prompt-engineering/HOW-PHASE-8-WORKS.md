# How Phase 8 Works: Video Prompt Engineering & Model-Agnostic Kinematics

Phase 8 is the kinetic culmination of the 8-phase AI film production pipeline. It takes the frozen keyframe stills generated in Phase 7 (photorealistic live-action plates or stylized 2D/3D animation frames, along with the animatic timing and blocking decisions from Phase 6 and the shot list from Phase 3) and injects mathematically grounded temporal motion, 3D camera trajectories, and physical momentum.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [0. The keyframe gate, before anything in this phase](#0-the-keyframe-gate-before-anything-in-this-phase)
- [1. The Golden Law of Model-Agnostic Creative Sovereignty](#1-the-golden-law-of-model-agnostic-creative-sovereignty)
- [2. The Nine Laws of Video Prompting](#2-the-nine-laws-of-video-prompting)
- [3. The 6-Axis Camera Kinetic Coordinate System](#3-the-6-axis-camera-kinetic-coordinate-system)
- [4. Temporal Continuity & Artifact Elimination](#4-temporal-continuity-artifact-elimination)
- [5. Master File Reference](#5-master-file-reference)
- [6. The closing check: what the brief asked for that nobody made](#6-the-closing-check-what-the-brief-asked-for-that-nobody-made)

<!-- /GENERATED:toc -->

## 0. The keyframe gate, before anything in this phase

Phase 8 starts only when `keyframes_approved_by` in `project.yaml` carries the owner's name and the
date. It is written by the owner at the keyframe approval gate, after they have looked at the still
deck from Phase 7 — or, in prompts-only mode, where no still is rendered, the keyframe *prompt* deck,
recorded as `<name>, prompts-only, <date>`; each clip prompt then carries `pending_keyframe_render`
until its still exists. While it is null, this phase writes nothing and says why. The closing check in
§6 is not part of this phase's writing: it runs whatever this gate says, on every route
(root `SKILL.md` §4, rule 7). An agent never fills
it, and never reads approval from silence, from an Express run or from `paid_generation_approved_by`
(`../PROJECT-STATE.md`, section 1).

## 1. The Golden Law of Model-Agnostic Creative Sovereignty

> [!IMPORTANT]
> **Creative Decisions Are 100% Free and Uncompromised**:
> 1. **Directed for the Most Capable Engine Available**: Every shot, camera vector, physical performance, and atmospheric interaction is directed at the highest cinematic standard, completely agnostic of any specific provider or AI model.
> 2. **Never Dumb Down a Shot**: Never reduce motion speed, omit a complex camera rotation, or compromise a narrative beat out of fear that a particular model cannot render it.
> 3. **The Universal Construction Standard**: Prompts are formulated using **[how-to-write-a-video-prompt.md](./how-to-write-a-video-prompt.md)** as the single master construction standard, directing motion kinematics, camera trajectories, and conditioning locks without vendor lock-in.
> 4. **Zero Vendor Lock-in**: Because the prompt is built with pure physical motion verbs, speed qualifiers, and camera coordinates, it executes with peak visual fidelity across ANY present or future state-of-the-art video model (whether commercial or open-source).
> 5. **Model Neutrality vs Provider Adapters**: Prompts are written for the shot itself in pure physical and cinematic language and remain strictly model-neutral; provider-specific syntax, token flags, or aspect parameters live in dated engine conditioning adapters, never hardcoded into the creative prompt.

---

## 2. The Nine Laws of Video Prompting

Unlike static image prompts that direct what is in a scene, video prompts direct **what changes over time**.

1. **Law of the Single Intention**: one clear intention per clip is a **craft default, not a model limit**. Name the move with a speed ("slow push in", not "push in"). **Where the shot genuinely wants a developing move — a push that becomes an orbit, a crane that settles into a track — write it as one continuous trajectory with one start and one end state, and declare it.** What is still avoided is the accidental stack: two unrelated intentions sharing one clip because neither was worth its own shot. Scoped to clips of roughly six seconds or less; above that [how-to-write-a-video-prompt.md](./how-to-write-a-video-prompt.md) section 4.2b governs. If a specific engine cannot hold the move, that is a note for engine selection, never a reason to write a smaller move.
2. **Law of Image-to-Video (I2V) Supremacy**: Never generate video from raw text when narrative consistency is required. Always condition motion upon an approved keyframe produced in Phase 7 (photorealistic live-action plate or stylized animation frame).
3. **Law of the Kinetic Verb**: Replace descriptive nouns and adjectives with active, physically descriptive verbs (e.g., instead of "a fast horse", write "the horse gallops violently forward, hooves pounding mud into the air").
4. **Law of Speed Qualifiers**: Every motion phrase must specify speed and acceleration (e.g., "slow constant-speed pan", "rapid whip pan with sudden deceleration to dead stop", "smooth gradual push-in").
5. **Law of Start-and-End Frame Locking (F2L)**: For complex transitions, character rotations, or camera arrivals, supply both Frame A (0.0s) and Frame B (at the clip's verified duration, the value the engine-selection step confirmed for this run — never a number carried from a previous project). Let the diffusion model synthesize the in-between physical interpolation.
6. **Law of Separation (Camera vs. Subject)**: Explicitly separate the camera's spatial trajectory from the subject's physical performance (e.g., `Camera: static low-angle tripod. Subject: warrior draws bronze blade from scabbard with deliberate tension`).
7. **Law of Banishment (Fluff Removal)**: Absolute ban on buzzwords ("photorealistic, 8k, cinematic, hyper-detailed, masterpiece"). In video models, token fluff induces temporal noise and limb flickering.
8. **Law of Temporal Inertia**: Obey the physics the piece is made in. Objects with mass require acceleration and deceleration; cloth, hair, and dust require secondary momentum and drag. *(Render Mode Rule, the motion half of law 5 in Phase 7: **this law is about consistent mass, not about photographic mass.** On photoreal and 3D work it means real-world physics as written. On flat 2D, cel-shaded and cartoon work it means **the physics of the school being drawn**, which is a deliberate, codified exaggeration of the same principles rather than an absence of them: squash and stretch on impact, anticipation before a move, overshoot and settle on arrival, drag on trailing parts, and held poses where a photographed body could not hold still. Written at drawn work unmodified, "obey real-world physics" asks an animator's frame to stop animating — it removes exactly the deformation the style is made of, and the result reads as stiff rather than as realistic. The requirement does not relax either way: the frame still declares how weight behaves, and a cartoon that ignores weight fails as badly as a live-action shot that does. Only the vocabulary changes, from measured momentum to named animation behaviours. **A `built` shot is outside this law too**: its motion is authored in the graphics layer from the data, and `dataviz.transition_is_the_argument` governs what that movement means. Note also that squash and stretch is a **timing and deformation** instruction, not a licence for a character's proportions to drift between shots — identity stays locked exactly as it does on photoreal work.)*
9. **Law of Audio-Visual Synchrony**: Ingest the acoustic beats and vocal rhythm established in Phase 4 (Narration) and Phase 5 (Song Generation) so cut points and camera peaks align to the sonic rhythm.

---

## 3. The 6-Axis Camera Kinetic Coordinate System

Phase 8 directs camera motion using the standardized 6-axis kinematic model:

| Axis | Linear Translation | Rotational Velocity | Cinematic Term |
| :--- | :--- | :--- | :--- |
| **X-Axis** | Truck Left / Truck Right | Tilt Up / Tilt Down | `move.truck`, `move.tilt_up`, `move.tilt_down` |
| **Y-Axis** | Pedestal Up / Pedestal Down | Pan Left / Pan Right | `move.pedestal_up`, `move.pedestal_down`, `move.pan` |
| **Z-Axis** | Dolly In (Push) / Dolly Out (Pull) | Roll Partial / 360 Roll | `move.dolly_in`, `move.dolly_out`, `move.roll_partial`, `move.roll_360` |

### Complex Compound Moves
- **Dolly Zoom (Vertigo Effect)**: `sig.dolly_zoom` — Camera dollies backward along Z-axis while optical lens zooms in, holding subject framing constant while background perspective stretches dramatically.
- **Orbital Arc**: `move.orbit_360` — Camera translates horizontally along X/Z while rotating Y-axis yaw to hold subject pinned at screen center.

---

## 4. Temporal Continuity & Artifact Elimination

Phase 8 provides dedicated checks in `temporal-continuity-checks.md` and failure cards in `video-failure-modes.md`:
1. **Eliminating Geometric Morphing (`fail.morphing`)**: condition the move rather than shrink it — First-Frame-to-Last-Frame interpolation, rigid geometry named explicitly, and the arc written as one continuous trajectory with a stated start and end bearing. See `fail.morphing` in [video-failure-modes.md](./video-failure-modes.md); no arc limit is written here, because the angle at which an engine starts to morph is a measured, dated, per-engine value.
2. **Preventing Limb Duplication & Phantom Hands (`fail.limb_drift`)**: Pre-render fingers clearly clenched or resting in Phase 7 start frame. Direct arms along established body vectors.
3. **Suppressing High-Frequency Camera Jitter (`fail.flicker_jitter`)**: Specify "smooth steady tracking on rigid dolly tracks". **Hold the rate the piece was designed in, and fix judder in the move.** This line used to say *lock frame rates to 24fps cinema standard*, which was wrong twice over: it prescribed cinema for every piece while `look.fps_25_30` owns broadcast and `look.hfr_48`, `look.fps_60` and `look.fps_120` own the rest — and it prescribed, as a cure for judder, the rate that judders most. `look.fps_24` says so itself: fast horizontal movement strobes badly at 24, and for sports and live broadcast it is simply not enough. The frame rate is a delivery decision made upstream; what this remedy owns is the steadiness of the move.
4. **Preventing Geometric Melting (`fail.geometric_melting`)**: Enforce rigid background geometry and sharp structural boundaries separated from subject motion vectors.

---

## 5. Master File Reference
- **Master Prompting Manual**: [how-to-write-a-video-prompt.md](./how-to-write-a-video-prompt.md) (Single master construction standard)
- **Core Camera Moves**: [camera-moves.md](./camera-moves.md) (114 cards)
- **Signature Cinema Moves**: [signature-moves.md](./signature-moves.md) (97 cards)
- **AI Directing Methods**: [ai-video-directing.md](./ai-video-directing.md) (47 cards)
- **Rigs & Mounts**: [rigs-and-platforms.md](./rigs-and-platforms.md) (52 cards)
- **Time & Speed**: [time-and-speed.md](./time-and-speed.md) (49 cards)
- **Temporal Continuity**: [temporal-continuity-checks.md](./temporal-continuity-checks.md) (19 cards)
- **Sound as Visual Motion**: [../phase-03-shooting-script/sound-as-visual.md](../phase-03-shooting-script/sound-as-visual.md) (26 cards)
- **Failure Modes**: [video-failure-modes.md](./video-failure-modes.md) (8 cards)
- **Catalog & Lookup**: [INDEX.md](./INDEX.md) & [LOOKUP.md](./LOOKUP.md) (394 cards (414 total headings))

---

## 6. The closing check: what the brief asked for that nobody made

**Run this once, at the end, against the brief — not against the phase you just finished.** Every
check before this one is a check on a deliverable that exists. This is the only one that looks for a
deliverable that does not, and it is the last chance to notice.

Take the original brief, sentence by sentence, and for each thing it asked for, name the file or the
section that answers it. The questions, in this order:

1. **What did the brief ask for that has no deliverable?** A cover image, a set of cutdowns, a
   second language, an end card, captions, a thumbnail, a poster, a version for a different aspect
   ratio, the third episode. Anything the brief named and no phase produced.
2. **What does the delivery need that the brief did not think to ask for?** The things a piece cannot
   ship without and nobody writes down: subtitles for a piece that will autoplay muted, a title and
   description, the credit for anything borrowed, the safe area for the surface it
   will actually live on, a still for wherever it gets posted.
3. **On a history piece the user wants realistic: what does the piece assert that nobody checked?**
   Every factual claim in the narration, the captions and the on-screen text (a date, a number, a
   name, a sequence of events) is read back against its source, and `info.fact_check_pass` is the
   card for it. The order is the root `SKILL.md` §0 order: found, keep it; not found, search; nothing
   found, take the closest thing, record it under `decisions`, and carry on. It is never a stop.
   The two things that slip through most are claims that were *true separately and are being said
   together* (three excavations described as simultaneous when their dates do not overlap) and a
   quoted line with no source beside it. **On any other piece this question is skipped**: facts and
   sources are not part of the job there.
4. **Does the piece tell anyone to do anything — and is it right?** Separate from the factual pass above, because this one is about *actions* rather than claims. Any instruction the piece depicts or implies — take this, go there, do this if it happens — is checked against the guidance that governs that subject **in that place**, and the wrong ones are written into `FORBIDDEN-GLOBAL.md` as prohibitions rather than simply avoided. A piece can be accurate in every statement and still show someone doing the wrong thing, and an audience copies what it sees before it remembers what it heard.
5. **Is anyone in this piece exposed by it?** Ask it separately from every question above, because
   nothing above can catch it: an exposure is factually true, has a deliverable, is internally
   consistent and carries no marker. Go through every contributor, every location and every person
   visible in borrowed material, and for anyone who was promised protection - or who never consented
   at all - name what in the finished piece could identify them. Not the face alone: **the uniform,
   the insignia, the build and the posture inside a silhouette, the view through a window, a
   doorway, a skyline, a street sign, a vehicle, a dialect word, a named date that narrows it to one
   person, a sound coming through a wall, and a voice that has been shifted rather than replaced.**
   **If the answer is yes for anybody, the package writes no concealment method** (see
   [`../../SKILL.md`](../../SKILL.md) §0), so the output of this question is a note in the handoff, not a
   fix and not a stop: name who is exposed and by what, for whoever delivers, and carry on with
   everything else. This is tier 0 in
   [`../PRECEDENCE.md`](../PRECEDENCE.md), it outranks everything including the factual pass, and the
   entries belong in `forbidden_global` at the start of the project rather than in a shot note at the
   end.

6. **What is still carrying a marker?** Search the whole package of work for every marker in the
   set below — the list is generated from `ENGINE-CHECK.md`, so a marker added there appears in this
   sweep without anyone editing this page, which is the failure this block replaces.

<!-- GENERATED:marker-set — do not edit by hand. Generated in the source package -->

**The marker set.** One marker per input the package needs and cannot produce for itself. This list is generated from the table in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which is the authority — a marker added there appears here without anyone retyping it. **Each one closes two ways:** *resolved*, or *`unobtainable — why, and what was done instead`*. The second is a finished answer, not an open one; what is never acceptable is deleting a marker because it could not be resolved.

- `pending_engine_check` — a resolution, a clip length, a take length, a voice limit
- `pending_forbidden_global` — the project's standing prohibitions
- `pending_measured_duration` — a runtime that is not yet measured — whether it is waiting on a render, or on a recording of speech nobody wrote
- `pending_quote_source` — the publication a quoted ancient line comes from, on a history piece the user wants realistic
- `pending_archive_source` — where a piece of found material came from, when a search has not found it
- `pending_figure_source` — the publication a figure stated as fact comes from, on a history piece the user wants realistic or a factual piece
- `pending_reference_image` — the visual reference a historical element is supposed to be built from
- `pending_language_check` — a line in a language nobody on the project reads — including one invented for the piece
- `pending_pronunciation_source` — the spoken form of a name that no named source or native speaker has yet supplied — a respelling that would otherwise be guessed
- `pending_permission` — a real person's consent before their voice or likeness is cloned — for a real child, the parent's (root `SKILL.md` §0)
- `pending_keyframe_render` — a clip prompt written, in prompts-only mode, against an approved keyframe *prompt* whose still has not been rendered yet
- `pending_measured_figure` — a number that has to be measured, sampled or counted *for this film*, because no published source holds it
- `pending_supplied_spec` — the official file for something the brief's owner holds — a brand identity, an attested figure, a required line
- `pending_photosensitivity_check` — whether a deliberate strobe or rapid flash sequence is safe to show — a measurement this package does not make. Ordinary light (fire, candles, lamps, a sunset, a flickering bulb in a scene) never takes it

<!-- /GENERATED:marker-set -->

   Each one is a
   note that travels with the handoff after the search-and-choose of the root
   [`../../SKILL.md`](../../SKILL.md) §0: what was chosen, and what may still want confirming by whoever
   delivers. It never held the work. A marker reaching delivery is the system working (it was meant
   to be visible), but only if somebody looks.

**Why it lives here and not in each phase.** A phase can only check itself, and every omission found
in testing was the kind no single phase owns: the piece that had eight beautiful shots and no end
card, the bilingual piece where only one language got a deliverable, the episode whose cover was
mentioned once in the brief and never again. Each phase was complete. The piece was not.

Write the answer down, even when it is empty — *"brief asked for nothing further; two markers still
open, both engine-record cells"* — because an unwritten check and a check that found nothing look
identical afterwards, which is the same reason `pending_` markers exist at all.
