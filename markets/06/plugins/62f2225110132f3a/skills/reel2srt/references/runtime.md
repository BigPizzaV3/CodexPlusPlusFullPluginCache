# Runtime

Resolve paths relative to this skill folder. Python 3.12 is the tested runtime. Install `faster-whisper==1.2.1` and `av==18.1.0` in an isolated environment; their transitive dependencies and the large-v3-turbo model are separate from this bundle. PyAV includes decoding libraries; a separate ffmpeg executable is not required. This prototype uses local CPU compute, not an OpenAI API key.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install faster-whisper==1.2.1 av==18.1.0
.venv/bin/python scripts/reel2srt.py --video '/path/clip.mov' --out '/path/output/clip.srt' --language th --allow-model-download
```

Run this from the skill folder. The first model download can be large; subsequent runs omit `--allow-model-download`. With a predownloaded model, `--model /absolute/model/folder` works. Missing cached model fails closed by default. Outputs must use a fresh filename. No customer media is uploaded by this runner; a model download contacts the model repository. Hosting/platform behavior is separate.

Use `--language auto`, `th`, or `en`. Mixed language is transcribed as spoken, not translated. Predominantly Thai mixed clips should also be benchmarked with `th` to match the old engine configuration.

Replay a trusted alignment for deterministic regression testing:

```sh
python3 scripts/reel2srt.py --alignment '/path/alignment.json' --out '/path/output/replay.srt'
```

Schema: `{ "duration": 30.0, "words": [{ "word": "Hello", "start": 1.0, "end": 1.5, "probability": 0.9 }] }`. Seconds are relative to video start. The old `segments[].words[]` shape is also accepted. Replay does not listen to audio or verify provenance; never use invented word timing to pass validation.

Success writes SRT plus alignment/report JSON. No speech writes JSON only. Exit 2 and a blocked report mean no SRT is delivered. Diagnose the audio/alignment, not just the error. Single words over cue limits, standalone zero-duration cues, overlaps, and end times past the clip must be rechecked against audio. Inward millisecond rounding avoids exceeding word/clip boundaries.
