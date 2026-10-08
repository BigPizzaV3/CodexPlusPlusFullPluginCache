# Universal Video Conditioning Modalities

Department: **Video Prompt Engineering (Phase 8)**  
Role: **Motion Generation Architecture & Input Modalities**

Every state-of-the-art AI video generation model—regardless of underlying neural architecture, parameter scale, or future release—operates through one of three fundamental conditioning paradigms:

1. **Single Image to Video (Image-to-Video / I2V)**
2. **Start Image + End Image to Video (First & Last Frame Dual-Conditioning)**
3. **References to Video (Multi-Reference: Character, Style & Motion Transfer)**

This craft bible defines how to structure, direct, and optimize motion prompts for each of these three universal modalities, keeping creative directing decisions 100% sovereign and future-proof without hardcoding ephemeral model brand names.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Modality 1: Single Image to Video (Image-to-Video / I2V)](#modality-1-single-image-to-video-image-to-video-i2v)
- [Modality 2: Start Image + End Image to Video (Dual-Frame Interpolation)](#modality-2-start-image-end-image-to-video-dual-frame-interpolation)
- [Modality 3: References to Video (Multi-Reference Conditioning)](#modality-3-references-to-video-multi-reference-conditioning)
- [Universal Synthesis: Choosing the Right Modality](#universal-synthesis-choosing-the-right-modality)

<!-- /GENERATED:toc -->

## Modality 1: Single Image to Video (Image-to-Video / I2V)

### Single Keyframe Forward Animation

**Also called:** I2V prompt architecture, single-plate motion launch  
**What it is:** Conditioning the video generation on a single rendered master keyframe (0.0s) and directing the camera trajectory, subject action, and ambient physics forward in time.  
**Effect on the audience:** The opening frame is established with 100% optical and identity fidelity; the viewer watches organic, unforced movement unfold naturally from the still.  
**Used for and where it works best:** The primary standard across 80% of cinematic shots: establishing shots, character reactions, walk-ins, camera push-ins, and dialogue coverage.  
**Best in:** formats: Feature Film, Short Film, Commercial / TVC, Music Video | genres: All genres  
**Avoid when:** Shots with complex multi-stage choreography where the landing frame must match an exact downstream cut.  
**Craft Rules:**  
1. *Do not re-describe the static appearance:* The engine already sees the subject, clothes, and lighting in the image. Re-describing them introduces risk of re-generation and texture drift.  
2. *Direct only the delta:* Describe exclusively what *moves* (camera vector, subject limb kinematics, eye dart, cloth rustle, lighting shifts).  
3. *Enforce motion headroom:* Ensure the start frame has physical empty space in the direction of the camera/subject vector.  
**Master Prompt Syntax:**  
```text
From the provided still image: Camera executes a steady, slow cinematic push-in (Z+ vector, 0.4 m/s) with subtle organic float. The subject slowly turns their head 30 degrees toward frame-left, eyes narrowing with focused intensity. Natural fabric physics as the cloak sways gently in a faint cross-breeze. Ambient atmospheric particles drift across the focal plane. 24fps motion blur, locked optical center, zero warping.
```
**Source:** assumption — the package's working figure, not a published standard; 0.0s simply marks the keyframe as the first frame of the clip.  
**Yields to:** `cond.start_end_frame_pair` — The landing frame must match an exact downstream cut.  
`cond.single_image_to_video`

### Directional Velocity and Momentum Anchoring

**Also called:** inertial vectoring, velocity dampening  
**What it is:** Explicitly directing the speed curve of the motion across the generation window (e.g., constant velocity, linear acceleration, ease-in, or sudden deceleration).  
**Effect on the audience:** Prevents the synthetic "elastic rubber-band" effect where AI motion starts fast and snaps backward before the clip ends.  
**Used for and where it works best:** Fast vehicular tracking, rapid camera whips, running subjects, and sudden dramatic freezes.  
**Best in:** formats: Action Short, Trailer / Teaser, High-Impact Ad | genres: Action / Pursuit, Thriller, Sports  
**Avoid when:** Gentle conversational dialogue where speed variations should be subtle and organic.  
**Master Prompt Syntax:**  
```text
Constant-speed camera tracking right-to-left parallel to the subject's stride, maintaining fixed distance and zero acceleration throughout the entire duration. Smooth kinetic inertia, realistic ground-contact foot physics, continuous background parallax.
```
**Yields to:** `cond.single_image_to_video` — Gentle conversational dialogue, where speed variation must stay organic.  
`cond.velocity_momentum_anchor`

---

## Modality 2: Start Image + End Image to Video (Dual-Frame Interpolation)

### Bookend Keyframe Motion Guidance

**Also called:** First-and-Last frame conditioning, dual-frame bridge  
**What it is:** Supplying both the opening frame (0.0s) and the final frame (e.g., 5.0s or 10.0s) as fixed visual anchors, and directing the generative model to interpolate the physical transition between them.  
**Effect on the audience:** The scene arrives exactly where the director intended. Eliminates creative hallucination, drift, and accidental subject mutation across the shot.  
**Used for and where it works best:** Major character transformations, dramatic reveals, 180° actor turns, lighting transitions (day to dusk), and precise editorial match-cuts.  
**Best in:** formats: High-End Commercial, VFX Shot, Title Sequence, Narrative Feature | genres: Sci-Fi, Fantasy, Mystery / Whodunit  
**Avoid when:** Unscripted spontaneous moments or open-ended reaction shots where strict landing constraints make the motion feel mechanical.  
**Craft Rules:**  
1. *Both frames must share optical consistency:* Same aspect ratio, lens focal length, and character identity locks.  
2. *The prompt describes the path, not the endpoints:* Write the kinetic action connecting Frame A to Frame B.  
3. *Timing dictates plausibility:* If Frame A and Frame B represent actions requiring 8 seconds of physical time, do not compress them into a 3-second generation.  
**Master Prompt Syntax:**  
```text
First frame to last frame interpolation: Beginning in the exact state of the opening frame, the character raises the ancient bronze goblet to their mouth, drinks deeply, and slowly lowers the cup while turning to look out the arched stone window, smoothly settling into the exact composition and posture of the final frame. Seamless lighting continuity between both states, realistic fluid and cloth physics, fluid natural transition without spatial drift.
```
**Source:** assumption — the package's working figure, not a published standard; the 5 and 10 second lengths are examples; set the length from the generator's clip options.  
**Yields to:** `cond.single_image_to_video` — Unscripted or open-ended reaction shots, which a strict landing makes mechanical.  
`cond.start_end_frame_pair`

### Transformation and Phase Shift Control

**Also called:** metamorphic interpolation, state change kinematics  
**What it is:** Directing physical or environmental transformations between two different states (e.g., dry ground becoming flooded, a calm face breaking into tears, or a pristine building becoming aged).  
**Effect on the audience:** Seamless cinematic metamorphosis that feels physically authentic rather than a cheap digital dissolve.  
**Used for and where it works best:** Time-lapse effects, magical or sci-fi transitions, and psychological grief/shock turns.  
**Best in:** formats: Music Video, Arthouse Short, Conceptual Commercial | genres: Psychological / Arthouse, Fantasy, Sci-Fi  
**Avoid when:** Subtle realistic drama where physical transformations violate genre tone.  
**Master Prompt Syntax:**  
```text
Continuous transitional evolution from start frame to end frame: Shadows lengthen across the stone floor as the golden daylight smoothly cools into deep violet dusk; the character's steady breathing transitions into a shuddering exhale, settling into the shadowed silhouette of the closing frame.
```
**Yields to:** `cond.start_end_frame_pair` — Subtle realistic drama, where a metamorphosis breaks genre tone.  
`cond.transformation_phase_shift`

---

## Modality 3: References to Video (Multi-Reference Conditioning)

### Multi-Image Identity & Style Reference Directing

**Also called:** Reference-to-Video (R2V), multi-view conditioning  
**What it is:** Conditioning the generation on a set of reference plates (character turnaround sheet, costume detail plates, lighting key, environment grimoire) *without* locking the initial frame to any single reference. The model generates a novel shot adhering strictly to the reference features.  
**Effect on the audience:** Unlocks complete directorial freedom of camera angle and staging while ensuring 100% character face, wardrobe, and world consistency.  
**Used for and where it works best:** Shots requiring difficult camera angles (high bird's-eye view, Dutch tilt, ground-level worm's-eye) not pre-rendered as single keyframes, and multi-character ensemble interactions.  
**Best in:** formats: Animation, Episodic Drama, Character-Driven Films | genres: All genres  
**Avoid when:** Fast turnarounds where a single generated keyframe is already available and sufficient.  
**Craft Rules:**  
1. *Use frozen descriptors alongside reference images:* Combine the visual plate with the verbatim text sentence (`ident.frozen_sentence`) to lock bone structure and costume textures. This holds because no frame is locked here; when a single keyframe opens the shot, the picture already carries the identity and the first craft rule of `cond.single_image_to_video` applies instead.  
2. *Designate reference roles explicitly:* Tag which image is the Subject Reference, which is the Environment Reference, and which is the Style/Lighting Reference.  
**Master Prompt Syntax:**  
```text
Conditioned on Reference Plates [Subject_Turnaround_01] and [Environment_Grimoire_03]: Generate a novel dynamic low-angle tracking shot. The subject, matching 100% facial features, beard texture, and bronze armor from the reference plate, strides rapidly across the stone courtyard depicted in the environment reference. Camera dollys backward smoothly ahead of the subject, maintaining eye-level low angle. Volumetric torchlight illumination consistent with reference mood.
```
**Yields to:** `cond.single_image_to_video` — A single generated keyframe already exists and is sufficient.  
`cond.multi_reference_directing`

### Performance & Motion Reference Transfer (Video-to-Video Pose Guidance)

**Also called:** Motion skeleton retargeting, kinetic performance transfer  
**What it is:** Using an existing live-action video clip as a motion/depth/pose skeleton to dictate the exact timing, velocity, and choreography of the target character.  
**Effect on the audience:** Flawless human-grade performance nuance, micro-timing, and physical weight that cannot be achieved through text prompting alone.  
**Used for and where it works best:** Complex stunts, swordplay, intricate dance routines, nuanced comedic timing, and lip-synced speech.  
**Best in:** formats: Action Feature, Music Video, Martial Arts Sequence | genres: Action, Historical Epic, Musical  
**Avoid when:** Unnatural or floating physics are desired (e.g., zero-gravity or cosmic entities).  
**Master Prompt Syntax:**  
```text
Motion Reference Source: Retarget exact skeletal motion, step cadence, and body weight distribution from [Performance_Guide.mp4] onto the character established in the keyframe plate. Maintain absolute fidelity to the source performance timing, while rendering 100% authentic photorealistic textures, lighting, and environmental physics.
```
**Yields to:** `cond.velocity_momentum_anchor` — Unnatural or floating physics, where no human motion skeleton fits.  
`cond.motion_reference_transfer`

---

## Universal Synthesis: Choosing the Right Modality

| Scene Requirement | Best Conditioning Modality | Input Assets Required | Primary Advantage |
|---|---|---|---|
| **Standard Cinematic Shot (80% of scenes)** | **Modality 1: Single Image to Video (I2V)** | 1 Keyframe + Motion Prompt | Maximum optical & texture fidelity; unforced natural flow |
| **Precise Cut / Transformation / Landing** | **Modality 2: Start & End Image Pair** | Frame A + Frame B + Bridge Prompt | Zero spatial drift; exact landing composition guaranteed |
| **Novel Camera Angle / Complex Staging** | **Modality 3: Multi-Reference (R2V)** | Character Sheet + Environment Plate + Action Prompt | Full freedom of camera & blocking with 100% identity lock |
| **Complex Stunts / Fight / Choreography** | **Modality 3: Motion Reference Transfer** | Live-action Video + Keyframe Plate | Flawless human timing, realistic inertia & weight |
