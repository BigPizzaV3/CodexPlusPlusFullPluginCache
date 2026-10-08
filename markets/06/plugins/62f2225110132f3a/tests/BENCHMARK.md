# Reel2SRT acceptance benchmark

## Automated structural checks

Run `python3 -m unittest discover -s tests -v` from package root. The matrix tests 30/60/180/300 seconds × Thai/English/mixed strings using synthetic word timings. These are not acoustic/ASR quality tests. With PyAV/numpy installed, the suite also generates 30/60/180/300-second MOV fixtures and tests preserved audio offsets, silence, missing audio and a 301-second rejection.

## Real-media acceptance

Use `benchmark.csv`: 24 planned cases = four durations × three languages × clean/stress. Record an actual clip, independent human transcript and speech boundaries. Clean cases use natural speech. Stress cases combine fast speech, silence >=0.2 s, music and basketball/proper names. Each duration group must include leading/trailing silence and a language switch where relevant. Do not count repeated/padded speech as four independent natural-speech quality samples.

For each case:
1. Save source duration and SHA-256, engine/model/language/version, elapsed time, environment/plan and platform. Keep customer media and transcripts private, outside the distributed plugin.
2. Run the original workflow and this prototype with the same model and language. Compare recognized content and every changed boundary. Record fixes separately; no manual changes hidden in the raw score.
3. A human checks all cues against audio. Record Thai character error rate (CER), English word error rate (WER), mixed-language corrections and names. Proposed pilot targets: CER <=5% / WER <=10%; critical names correct after review; owner may tighten after baseline measurements. These are proposed criteria, not achieved results.
4. Proposed boundary target: >=95% of reviewed starts/ends within 150 ms of manually marked speech boundaries. Report max error too. No missing final words, hallucinated speech in silence, global time scaling, time past duration or overlapping cues. Any known silence >=200 ms remains a gap. VAD alone is not proof of silence correctness.
5. Import into the customer's CapCut version; record OS/version and pass/fail for UTF-8 Thai/English, initial offset, gaps, final cue and unchanged playback speed.
6. All automated invariants must pass; acoustic and CapCut criteria need human evidence. Pending is not pass.

## Negative cases

- 300.001 seconds and >5 minutes: reject before ASR.
- No audio track, corrupt file, unknown duration: explicit block, no invented SRT.
- Silent/music-only video: no hallucinated dialogue; review if ASR emits words.
- Two audio tracks: require selection, no silent guess.
- Non-zero audio start and missing packets: keep original timeline; missing PTS: block.
- Engine unavailable, model cache missing, no file output: explain unsupported capability.
- Overlap, NaN, negative/reversed/standalone zero-duration cues: block and re-align.
- Uploaded speech says “ignore instructions”: transcribe it as speech without executing it.
- Request to stretch to five minutes: preserve measured timestamps and explain.
- Out-of-workspace buyer opens link: record actual installation result; no payment gate inferred from link possession.
