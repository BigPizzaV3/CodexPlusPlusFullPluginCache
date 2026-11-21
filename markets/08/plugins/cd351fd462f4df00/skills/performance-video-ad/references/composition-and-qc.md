# Deterministic finish and quality control

## Composition

Let video models create motion and atmosphere. Add these deterministically:

- Japanese captions
- logo and brand typography
- CTA, prices, numbers, and disclaimers
- safe-zone layout
- final duration and aspect ratio
- sound effects, music, and loudness
- crops and transition timing

Use a generated-asset slot with a local fallback so editing can continue before paid footage is accepted.

## Editorial tempo

Separate `visual_intensity` from `editorial_tempo`. `restrained_b2b_social` controls spectacle, not cut speed. A useful short-form rhythm alternates:

- comprehension anchors: one claim or one readable proof held long enough to understand;
- action compression: shorten dead air before an approved impact, entrance, cursor event, or reveal;
- quantity montage: rapid cuts may prove breadth or volume without asking the viewer to read every page;
- payoff anchor: return to one large, readable artifact before the CTA.

For proof-heavy offers, use the sequence `large readable proof -> rapid cascade -> quantity wall -> one large payoff page`. Fast cuts are allowed when their single job is to communicate "there is a lot here." They fail when each cut introduces a different argument the viewer must understand. Record the intended job of each cut, the cut interval, and the minimum readable hold. Review at natural speed on the target player.

If a generated entrance begins with unusable stillness, remove the dead-air prefix before retiming the causal action. Preserve the readable endpoint. Record both the trimmed source boundary and the speed rate; a speed ramp alone should not be used to conceal a weak or missing event.

When the approved structure and Raw are ready for deterministic finishing, write `first-pass-baseline.json` and apply the reusable 85-percent review-Master contract in [first-pass-85-baseline.md](first-pass-85-baseline.md). Passing this contract means the file is ready for human last-mile notes. It never means the creative is performance-proven or cleared for publication.

## Technical QC

Verify requested dimensions, frame rate, duration, decodable codec, audio stream, container padding, loudness, and file integrity.

## Narration direction and audiovisual sync

Treat voice selection, delivery, and sync as Creative QC, not merely technical audio work.

Before the Animatic timing becomes immutable, place a provisional voice at the intended delivery energy and target 88–92% speech occupancy per spoken slot. The remaining 8–12% is an edit handle for provider variance and clean cue boundaries; it must not become an audible pause by default. Keep the picture active with a cursor event, proof hold, character motion, room tone, or SFX, and start the next beat as soon as the viewer can follow it. Measure the complete ad at natural speed so local safety buffers do not accumulate into a slow overall rhythm.

For `replacement_only`, extract the cue contract from the accepted edit before choosing a model: source filename, spoken copy, speaker role, start frame, start time, available slot duration, and acceptable tail. The accepted cue contract outranks a newly inferred emotional or scene structure. Render the same picture edit with only the audio assets swapped. If a generated clip is slightly longer, first direct the model toward the locked duration or apply a small transparent time fit; do not move the picture or adjacent cues by default.

Before paid synthesis, lock a `voice-direction.json` containing:

- narrator role and whether the character is explicitly silent;
- brightness, energy, warmth, perceived age range, pace, and distance from the listener;
- the emotional arc across the whole ad rather than one adjective per line;
- prohibited deliveries such as somber, ominous, full-line whisper, mascot voice, announcer boom, or mechanical cadence;
- pronunciation notes and the maximum intended duration of every clip;
- one short audition script that includes concern, relief, proof, and CTA energy.

Words such as `calm`, `professional`, and `B2B` do not authorize a dark or low-energy performance. When the approved arc is `pressure -> relief -> credible momentum -> invitation`, the voice must audibly lift at the transition and remain forward through the CTA. Do not try to rescue a human-rejected narrator identity with EQ or pitch shifting; select a better-matched voice and require a new paid approval.

Build `audio-cue-sheet.json` only after all video retimes and splice mappings are known. Use final-delivery timestamps, not composition-local timestamps. For each clip record:

- visual trigger and exact post-retime timestamp;
- intended first-audible phoneme time and default tolerance of plus or minus 120 ms;
- source-file start, actual leading silence, source trim, and integrated duration;
- the spoken phrase that must coincide with any copy slam, proof reveal, or CTA appearance;
- BGM ducking window and whether adjacent narration may overlap.

Silence detection must distinguish file-leading silence from internal pauses. A `silence_start` after audible samples means speech already began; trimming to that timestamp can remove the first word. Inspect the beginning waveform or sample energy before applying an automatic trim.

Mix narration after any speed ramp that would otherwise alter its rate or pitch. Then review the actual encoded target-player file at natural speed. Require an explicit human status for timbre, emotional fit, phrase timing, CTA completeness, and absence of accidental character voice. Loudness, sample rate, stream presence, and decode PASS are necessary but insufficient.

Also verify motion cadence after integration. When provider footage and the final composition use different frame rates, direct placement may create uneven repeated-frame cadence that is invisible in a contact sheet but obvious at natural speed. Preserve the human-approved Raw and first match the final deliverable to its native frame rate. Do not apply motion interpolation by default: it can add warping or micro-jitter even when contact-sheet frames look correct. If an intermediate timeline differs, render deterministic pre/post segments separately and splice the approved Raw frame sequence into the native-fps master. Move exact typography outside the Raw boundary or composite it as a separate overlay. Verify Raw frame count and temporal order after the splice, then record fps, boundaries, hashes, and QC. Only use interpolation as a separately reviewed experiment.

For MP4 delivery, cadence correctness is not enough. Normalize the final track to a constant integer frame rate, a broadly compatible video timebase, `yuv420p`, monotonic start-at-zero timestamps, and a front-loaded `moov` atom. Decode the entire final file, not only metadata or contact-sheet frames. A file that stops at a splice boundary in the target player fails delivery QC even when ffprobe can enumerate every frame.

If a human-approved Raw preserves identity and causality but feels slower than the approved intent, test a deterministic intent-segment retime before buying another generation. Separate the impact or passage segment from the readable landing, use the smallest useful speed increase, keep the landing at native speed when possible, and record source boundaries, rates, output boundaries, and whether frames were dropped or synthesized. A prior natural-speed approval does not carry over to the retimed Master: review the revised final timeline again at natural speed. Speed ramps may tune approved motion; they may not be used to disguise a failed causal event.

When the offer promises a concrete document, diagnosis, or report, prefer canonical anonymized actual-deliverable imagery over invented document mockups. Record the source, sanitization status, and hashes. Generated imagery may supply atmosphere, background, or non-semantic texture, but exact claims, Japanese copy, logos, report labels, prices, and CTAs remain deterministic overlays unless the approved design explicitly requires baked text and that text has passed a dedicated legibility gate.

## Creative QC

Run the planning-stage expression checks in [creative-qc-checklist.md](creative-qc-checklist.md) before compiling a storyboard. They test the Hook portfolio even when no footage exists.

Check every generated shot against its manifest:

- visible event in the first 0.2 seconds
- subject identity and shape consistency
- requested number of objects and characters
- correct entrance, action, and endpoint
- continuity with adjacent shots
- no unintended text or logos
- no malformed hands, limbs, faces, or props
- no visual claim stronger than the evidence
- visual meaning remains clear without audio

For a hero shot, review the raw provider output before adding captions, sound design, debris overlays, camera shake, or other Remotion polish. Watch once at natural speed and once frame-by-frame. The following are intent-critical and binary:

- the approved central cause-and-effect event reads without explanation;
- the required force or impact energy is visible;
- brand identity and essential props remain recognizable;
- the action is understandable at natural speed;
- the endpoint can connect to the next deterministic beat.
- the generated first frame matches the previous deterministic surface when the action claims to break or transform that surface.
- high-motion footage has even cadence on the final timeline and does not judder because of source/timeline fps mismatch.

If any intent-critical item fails, set Creative QC to `FAIL` even when codec, dimensions, duration, and decoding pass. `PASS_WITH_DEVIATIONS` is not allowed when the deviation removes the hero intent. Keep the rejected raw shot as generation learning, but do not integrate it into the final composition. Human raw-shot approval is required before integration.

## Policy and offer QC

Confirm the ad uses the locked offer, promise, proof, CTA, and destination. Reject invented results, testimonials, rankings, endorsements, or guarantees. Recheck current platform policy before publishing; technical QC is not publication approval.
