---
name: plan-release
description: "Build a dated release checklist counted back from a release date using the Artispreneur plan_release tool when it is connected, or the release-music-with-dsp skill when it is not. Use when the user gives a release date or asks to check a date."
metadata:
  author: Artispreneur
  version: "2.0.0"
  website: https://www.artispreneur.com
---

# Plan a Release by Date

1. Ask for `release_date` (YYYY-MM-DD) and, if known, today's date.
2. If the `plan_release` tool is available, call it with only those dates. Do not send track titles, files, or credentials. Present the milestones in order: asset lock, metadata and splits, distributor upload, editorial pitch, pre-save, content, outreach, royalties registration, release day, and the first 30 days. Surface `tight` or `at_risk` warnings for a late distributor upload or a pitch inside the 7-day window.
3. If the tool is not available, run `release-music-with-dsp`, which produces the same plan.
4. For any milestone with a linked skill, offer to run it.
5. State clearly that nothing was scheduled or submitted.

## Quality checks (run before handing over)

- [ ] Only `release_date` (and optional `today` date) was sent to `plan_release`.
- [ ] Milestones are ordered chronologically and flag `tight` or `at_risk` windows accurately.
- [ ] The response explicitly states that nothing was scheduled, uploaded, or submitted.

## Guardrails

- Send only minimal date inputs (`release_date` and optional `today`) to `plan_release`. Never send track audio, personal data, credentials, full chat history, or location data.
- `plan_release` is strictly read-only (`readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`) and operates independently without invoking external plugins.
- Never collect, solicit, or process Restricted Data (PCI DSS payment cards, PHI, government IDs such as SSN/ITIN/EIN, or passwords/API keys/MFA codes) or precise location data (street addresses or GPS coordinates).
- Draft first. Never claim a release was scheduled, uploaded, or submitted to a distributor or DSP.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
