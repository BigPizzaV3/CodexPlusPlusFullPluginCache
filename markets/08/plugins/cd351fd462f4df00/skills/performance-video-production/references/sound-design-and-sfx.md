# Short-form sound design and SFX

## Contents

1. What the research supports
2. Production pipeline
3. Asset rights and registry
4. Automatic selection
5. Sync and layering
6. Narration-first mixing
7. QC and learning

## What the research supports

Sound-on creative matters, but “more sounds” is not a universal performance rule. TikTok says SFX can bring surprise and reports widespread audio use in high-performing content. Meta reports better Reels outcomes for a combined 9:16, audio, and safe-zone treatment. Treat these as platform-format evidence, not proof that any individual SFX raises conversion.

Use temporal and semantic congruence as the core mechanism. Research shows that synchronous sound can facilitate visual processing and congruent sound can strengthen memory for audiovisual scenes. Therefore put the attack on the visible cause and choose a sound family that matches the event.

HIKAKIN's practice demonstrates deliberate density and fine-grained editing. His own interview emphasizes satisfying sound, speed, and framing; a Japanese analysis reports frequent short accents and longer emphasis sounds that create modulation. A creator-editor interview also warns that repeated high-pitched accents can collide with speech frequency and should be kept away from voice. Adopt meaningful micro-accents and contrast, not a blind “one SFX every N seconds” rule.

Sources:

- [TikTok Creative Codes](https://ads.tiktok.com/business/en/creative-codes)
- [TikTok Audio Library and commercial-use guidance](https://ads.tiktok.com/business/creativecenter/quicktok/online/tiktok_creative_accelerator/pc/en)
- [Meta Reels ads guidance](https://www.facebook.com/business/ads/facebook-instagram-reels-ads)
- [HIKAKIN on sound effects, action speed, and detailed editing](https://en.dragon-ball-official.com/news/01_888.html)
- [HIKAKIN content analysis](https://rikkyo.repo.nii.ac.jp/record/22711/files/AA12607699_10_06.pdf)
- [Creator-editor note on high SFX and voice masking](https://realsound.jp/tech/2024/08/post-1750647_3.html)
- [Audio-visual synchrony study](https://pubmed.ncbi.nlm.nih.gov/28802870/)
- [Semantic congruency and audiovisual memory study](https://pubmed.ncbi.nlm.nih.gov/26620810/)
- [FFmpeg audio filters](https://ffmpeg.org/ffmpeg-filters.html)

## Production pipeline

1. Validate the approved `sound-intent-map.json`.
2. Audit any provider-native audio for unapproved speech before treating it as SFX or ambience.
3. Build or load `sfx-asset-registry.json`.
4. Reject assets without verified commercial-use rights and platform scope or with unresolved voice contamination.
5. Run `select-sfx-assets.mjs` for a deterministic first pass.
6. Audition the selected assets in isolation and against narration.
7. Replace only failed assets; keep the intent and trigger locked.
8. Align cues to the final retimed picture.
9. Mix narration, SFX, ambience, music, and CTA motif as separate buses.
10. Render narration-only, SFX-only, music/ambience-only, provider-audio-only when retained, full-mix, and mute-picture review files.
11. Validate `audio-cue-sheet.json` and perform phone-speaker, headphones, and target-player review.

## Asset rights and registry

Use these source classes only:

- `owned`: commissioned or company-owned asset;
- `original_recording`: recorded for the project with recorded rights;
- `procedural`: generated locally without borrowed samples;
- `licensed_library`: third-party library with explicit commercial terms;
- `platform_library`: platform-provided asset whose scope includes the target platform and ad use.

Store for every asset:

- stable asset ID and local path;
- SHA-256 and duration;
- source class, license reference, commercial-use status, attribution requirement, and platform scopes;
- sound families and descriptive tags;
- whether the sound imitates a trademarked or recognizable app notification.

YouTube says only its Audio Library items are known by YouTube to be copyright-safe and warns that it cannot guarantee third-party “royalty-free” sources or off-platform uses. TikTok describes its Audio Library as pre-cleared for commercial purposes on TikTok. Never promote either statement into cross-platform permission.

Do not copy HIKAKIN's identifiable SFX, a television/anime sound, a Slack/Apple/Windows notification, or another creator's sonic tag. Learn the function and use an original or licensed sound.

## Automatic selection

Score only license-eligible assets:

1. exact `soundFamily` match;
2. target-platform scope;
3. desired character/tag overlap;
4. usable duration and clean attack;
5. lowest-risk deterministic tie-breaker by asset ID.

Reuse the same asset family for repeated events. Derive A/B/C variants with subtle pitch, EQ, transient, or tail changes only after checking that the variants still sound like one motif. Do not use extreme pitch shifts that make professional B2B footage comedic unless comedy is approved.

If no licensed match exists:

- fail a required cue;
- omit a recommended or optional cue with a reason;
- never search random download sites and silently import the first result.

## Sync and layering

Align the first meaningful transient, not the start of file silence, to the final visual frame.

- UI or notification: normally within 1–2 frames.
- Impact attack: exact contact frame.
- Rupture/material tail: begins on or immediately after contact.
- Passage/whoosh: follows the direction and duration of movement.
- Landing: exact deceleration/contact frame.
- Structural accent: exact semantic cut, not merely near it.

Recompute after every trim, speed change, or shot replacement.

Compare each selected asset's full cue span with the approved narration windows. A transient that begins before speech but rings into speech still counts as overlap and requires narration-safe EQ plus ducking. If the approved intent prohibited overlap, reject the asset or shorten/re-time the event; do not merely label it safe.

For major impacts, allow one layer group:

- `attack`: short high/mid transient for timing;
- `body`: lower-frequency weight;
- `material_or_tail`: crack, debris, paper, air, or room response.

Cap the layer group at three. Under narration, use fewer layers or duck them. Avoid stacking several full-spectrum “cinematic hits.”

## Narration-first mixing

Narration communicates claims and remains the priority bus.

- Duck music and sustained SFX under speech using automation or sidechain compression.
- Reduce or move high-frequency accents that compete with Japanese consonants.
- Keep micro-cues short and dry when they overlap speech.
- Let a major transient briefly lead only when the approved visual event is the message.
- Preserve intentional silence and room tone; do not normalize every gap into constant loudness.

Use FFmpeg's `sidechaincompress` or explicit volume envelopes for ducking and `loudnorm` for measured final normalization. Measure with an ITU-R BS.1770-compatible method. Keep the target loudness configurable because platform processing changes; always record integrated loudness, loudness range, and true peak. Never claim that a metadata target proves intelligibility.

## QC and learning

PASS requires:

- every required intent realized and every omission explained;
- every cue mapped to an approved intent;
- no SFX in an absolute silence window;
- causal attack within the allowed frame offset;
- no unlicensed or wrong-platform asset;
- no clipping or true-peak breach;
- narration intelligible on phone speaker and headphones;
- no tiring high-frequency pattern, pumping, or full-mix mud;
- CTA and brand motif clear but not louder than the offer;
- no unapproved speech, residual source narrator, or double voice in the provider, SFX, ambience, or music buses;
- target-player review at natural speed.

Render and inspect:

1. narration only;
2. SFX only;
3. music/ambience only;
4. full mix;
5. mute picture.

Record SFX density and mix notes as generation/production learning. Only a controlled sound-only test or real retention/performance data can establish that one sound design outperforms another.
