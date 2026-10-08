# Helper contract

Python 3.9+, standard library only. Resolve the script relative to this skill. Replace these example paths with actual task paths:

```sh
python3 /actual/skill/scripts/srt_tool.py inspect /task/source.srt --output /task/manifest.json
python3 /actual/skill/scripts/srt_tool.py build /task/source.srt /task/translations.json --output /task/source.ar.srt --report /task/validation.json
```

Add `--bilingual` to build for original text then translation. Add an explicit `--encoding cp1256` or another confirmed codec to both commands for legacy files. Inputs are never overwritten; existing output files are also rejected, so choose new filenames on retries.

Output is UTF-8; a UTF-8 source BOM and predominant newline style are preserved. UTF-16 is converted to UTF-8. Inspection returns `cues` with `position`, `number`, `timestamp`, and `text` for each cue. Translate the text and write a JSON array:

```json
[
  {"position": 0, "text": "مرحبًا!"},
  {"position": 1, "text": "<i>لا تغادر الآن.</i>"}
]
```

Cover every position exactly once. Positions are order, not cue numbers. Build validates tags/control tokens, nonempty text, coverage, cue count, number lines, and timestamp lines. Failed validation exits nonzero without writing the SRT. Success prints a report and optionally saves it to `--report`.

The report includes source/output hashes, cue count, mode, encoding, structural checks, and source overlap warnings. Overlaps are reported but not repaired. The helper does not perform language translation.
