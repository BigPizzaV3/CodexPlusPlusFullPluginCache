## rics-dip-sample

**Cadence:** Monthly or quarterly ({{SAMPLE_CADENCE}}), e.g. first Monday, 08:00
**Surface:** Desktop
**Prerequisites:** routine-state history from other installed routines; a named reviewing surveyor ({{NAMED_SURVEYOR}}); see `docs/rics-ai-standard.md` in the plugin repo for the duty this discharges
**Priority:** Standard

**Instructions:**
```
RICS §4.2 dip sample of AI-assisted routine outputs (the standard's route for automated /
high-volume use — see the plugin's docs/rics-ai-standard.md).

List the routine outputs recorded under {{FOLDER}}/routine-state/*/last-run.md since the date
in {{FOLDER}}/routine-state/rics-dip-sample/last-run.md. Select {{SAMPLE_SIZE}} of them,
spread across different routines (state which were selected and why that spread).

For each sampled output, re-verify its load-bearing figures against the underlying records
now: re-run the source query for the same explicit period and compare. Record per sample:
what was checked, the assumptions the original stated, any concerns found (with the reason
for each), whether anything lessens each concern, and a conclusion on whether the output was
reliable for its intended purpose.

Write the results to {{FOLDER}}/rics-dip-samples/[run-date].md as the written record, headed:
"Reviewer: {{NAMED_SURVEYOR}} — this record supports, and does not substitute for, the named
surveyor's written reliability decision under RICS §4.2."
Lead the reply with any sample that failed re-verification; if all passed, say so in three
lines. Update routine-state/rics-dip-sample/last-run.md with the date and samples checked.
```

---
