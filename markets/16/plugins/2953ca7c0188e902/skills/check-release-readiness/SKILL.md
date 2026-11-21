---
name: check-release-readiness
description: "Evaluate six artist-supplied release checkpoints (master, artwork, metadata, rights, distribution, promotion) using the Artispreneur check_release_readiness tool when connected, or the distribution-readiness skill when not. Use when an artist asks 'is my release ready'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  website: https://www.artispreneur.com
---

# Check Release Readiness

1. Collect a status for each checkpoint: master, artwork, metadata, rights, distribution, promotion. Allowed values: ready, missing, unknown. Prefer `unknown` over guessing.
2. If the `check_release_readiness` tool is available, call it with only those statuses. Do not send audio, contracts, or credentials. Otherwise run `distribution-readiness`.
3. Report the score, overall status, and next actions. Emphasize that statuses are self-reported and not independently verified.
4. Never claim legal clearances passed, that a distributor accepted a release, or that anything was verified outside the checklist.
5. To close a gap, route to the matching skill (`extract-metadata-from-track`, `create-split-sheet-agreement`, `release-music-with-dsp`, and so on).

## Quality checks (run before handing over)

- [ ] All six checkpoint statuses (`master`, `artwork`, `metadata`, `rights`, `distribution`, `promotion`) use only `ready`, `missing`, or `unknown`.
- [ ] Unverified checkpoints default to `unknown` rather than guessing.
- [ ] The output explicitly states that statuses are self-reported and not independently verified.

## Guardrails

- Send only the six enum checkpoint statuses to `check_release_readiness`. Never send audio files, contracts, personal data, credentials, full chat history, or location data.
- `check_release_readiness` is strictly read-only (`readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`) and operates independently without invoking external plugins.
- Never claim legal clearances passed, that a distributor accepted a release, or that any external account was checked.
- Never collect, solicit, or process Restricted Data (PCI DSS payment cards, PHI, government IDs such as SSN/ITIN/EIN, or passwords/API keys/MFA codes) or precise location data (street addresses or GPS coordinates).

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
