# Narration production and QC

## Order of operations

1. Lock narrator role, emotional arc, exact copy, pronunciation, target duration, and cue trigger.
2. Select a voice using a short audition that includes concern, upward transition, proof, and CTA energy.
3. Estimate every request and wait for paid approval.
4. For a fixed-cue batch, submit the highest-risk calibration clip first: the shortest semantic fragment, tightest duration slot, or longest exact-Japanese clause. Stop the batch if it is rejected or cannot fit within the approved short-form tempo envelope.
5. Generate lossless output when supported.
6. Verify language and copy before trimming, fitting, EQ, or mixing.
7. Trim verified leading and trailing silence only.
8. Fit duration conservatively.
9. Verify the processed clip again at natural speed.
10. Mix to the final delivery timeline.
11. Render narration-only, SFX-only, music/ambience-only, and retained-body stems before the final mix.
12. Verify that every expected active window contains the intended bus and that its first audible event matches the final trigger.
13. Review the encoded target-player file for language, tone, sync, and CTA completeness.

## Final stem-presence gate

A source file containing a valid waveform does not prove that it survived the final filter graph. Before declaring a local Master complete:

- render each bus to a full-duration, timeline-aligned lossless stem;
- give the stem an explicit full-duration silent base and mix with `duration=first` or another deterministic duration rule;
- measure the expected active windows separately, not only the full-file mean or integrated loudness;
- verify the first audible phoneme or transient against the visual trigger after the final AAC encode;
- fail the mix if an expected narration window is effectively silent even when the source clip and whole-file loudness both pass;
- keep the broken Master and the corrected stem evidence so the regression is reproducible.

For short-form review, treat a narration source that measures normally but becomes silent in the final timeline as a mix-graph failure, not a voice-generation failure. Do not spend another paid TTS request until the stem-presence gate proves that the source itself is unusable.

## Exact Japanese gate

For each clip store:

- `expectedText`
- `observedTranscript`
- `transcriptMethod`: `human`, `asr`, or `human_plus_asr`
- `languageMatch`
- `copyComplete`
- `foreignOrHallucinatedTail`
- `pronunciationStatus`
- `intelligibilityStatus`

If a clip changes language, invents a tail, drops a clause, or becomes unclear after processing, set the clip and overall voice QC to `FAIL`. The original prompt is not proof of what the audio contains.

For exact-copy TTS, explicitly set Japanese, prefer low generation variance, and avoid unnecessary expressive tags. When a multi-clause line has failed once, split it at an approved semantic pause and concatenate losslessly with a deterministic pause. Count every clause request in the paid approval.

Splitting is not automatically safer. Some providers can reject a very short semantic fragment even when the schema lists no minimum. Treat provider acceptance and duration compliance as measured output, not as properties implied by the prompt. If a split fragment is the riskiest item, run it first inside the approved request budget. Record submitted requests separately from completed outputs. A provider error consumes the attempt for audit purposes even when billing is unknown, and it must not trigger an automatic retry.

Natural-language instructions such as “read in about 1.3 seconds” are direction, not a duration contract. For locked picture, measure the leading/trailing-trimmed calibration result before generating the rest of the voice batch. Use the staged tempo policy below; stop instead of spending the remaining batch when a clip exceeds the allowed envelope or needs an unapproved exception.

At Animatic time, use a provisional voice at the intended delivery pace and target roughly 88–92% speech occupancy per slot. Reserve the remaining 8–12% as editing headroom, not as mandatory silence. Fill it with ongoing motion, proof readability, room tone, or SFX and preserve the ad's forward cadence.

## Provider-native voice contamination gate

Before mixing external narration over model-native audio:

1. Render and review the untouched provider-audio-only stem at natural speed.
2. Record `providerSpeechPresent`, `approvedSpeakerMatch`, `reviewMethod`, and any speech windows. Do not infer these values from the prompt, model settings, or expected soundscape.
3. If unapproved speech or vocalization exists, set full-track retention to `FAIL`. Do not merely duck it under the approved narrator.
4. Treat center cancellation, phase subtraction, dialogue EQ, and stem labels as audition candidates only. They are not proof of removal because residual consonants, reverberation, or side-channel speech can remain.
5. Recover sound in this order: provider-exported isolated SFX stems that pass human review; independently reviewed clean time windows; owned/procedural/licensed voice-free replacement SFX; complete provider-audio discard.
6. Render provider-audio-only or replacement-SFX-only and the final full mix. Review specifically for double voice between words, under pauses, and during CTA tails.

If human review detects residual unapproved voice after attempted isolation, stop repairing the contaminated track. Preserve the picture, discard provider-native audio completely, and rebuild only the required sound functions. Record the unexpected provider voice as `prompt_model_learning`; record any decision to retain it without a valid gate as `finishing_learning`.

## Format and processing

Prefer provider WAV/PCM when available. A 24 kHz WAV remains 24 kHz quality after a 48 kHz mix; resampling does not restore missing high frequencies. Resample only once at final mix using a high-quality resampler.

Preserve internal pauses. An automatic silence-removal filter configured to remove every silence may change rhythm and intelligibility. Detect file-leading silence separately from silence after speech begins.

Use these tempo thresholds:

- `<= 1.05x`: transparent fit may proceed to final review;
- `> 1.05x and <= 1.12x`: require matched-loudness A/B against the raw clip;
- `> 1.12x and <= 1.20x`: short-form pace candidate; require matched-loudness A/B and explicit human pace approval;
- `> 1.20x and <= 1.25x`: named editorial-exception candidate; require explicit human approval of the processed clip, exact Japanese, timbre, and absence of rushed artifacts;
- `> 1.25x`: FAIL by default; re-synthesize, revise the provisional timeline, or request a new planning decision.

A faster processed read may be preferable when it improves short-form momentum without harming meaning. Do not optimize for the lowest ratio in isolation. Choose the approved pace that best balances comprehension, energy, and synchronization.

Do not use aggressive formant preservation, repeated lossy encodes, or per-clip loudness normalization as an automatic repair for a rejected timbre. Normalize the final narration bus and final mix; retain raw and fitted files separately.

## Replacement-only mode

Extract the accepted picture and cue contract before generation:

- source placeholder
- exact copy
- speaker role
- start frame and final-delivery timestamp
- slot duration and allowed tail
- visual phrase emphasis

Replace one-for-one. Do not move scenes, typography, or adjacent cues to accommodate an unsuitable generated clip without explicit editorial approval.

## Final voice QC

Technical checks:

- audio stream exists and fully decodes;
- no clipping or broken timestamps;
- final loudness is suitable for the placement;
- first-audible phoneme is within the cue tolerance;
- narration does not mask required SFX or CTA.

Creative checks:

- correct narrator, not accidental character speech;
- desired brightness, warmth, energy, and credibility;
- every Japanese phrase is understandable;
- no muffling, metallic artifacts, pumping, or rushed clauses;
- emotional lift occurs at the approved transition;
- CTA is complete and remains forward through its ending.
- provider-native, music, ambience, and SFX buses contain no unapproved speech or residual competing narrator.

Keep `humanTasteStatus: PENDING` until the actual final target-player file is reviewed. Technical metadata cannot promote it to PASS.
