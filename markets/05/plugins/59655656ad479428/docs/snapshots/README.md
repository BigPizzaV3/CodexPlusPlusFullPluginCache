# Product and release snapshots

This directory keeps dated, reviewable snapshots of Empire LLM for Codex. A snapshot records what was shown, which version and commit it represents, and whether the image is a product illustration or a capture of live system state.

## Current snapshot

- [2026-09-03 — version 1.7.0 release-evidence snapshot](2026-09-03-v1.7.0.md)
- [2026-09-03 — version 1.6.0 release-evidence snapshot](2026-09-03-v1.6.0.md)
- [2026-08-01 — version 0.1.5 release-evidence snapshot](2026-08-01-v0.1.5.md)
- [2026-07-26 — version 0.1.2 submission snapshot](2026-07-26-v0.1.2.md)

## Snapshot rules

1. Never include API keys, organization identifiers, private prompts, raw provider responses, billing data, or personal account details.
2. Label each image as `product_illustration`, `local_validation`, or `live_portal_capture`.
3. Record the represented plugin version, source commit, capture date, and relevant test evidence.
4. Do not use a product illustration as proof that OpenAI approved or publicly listed the plugin.
5. Replace or annotate stale images when the released Codex interface or Empire behavior materially changes.

## Template

```markdown
# YYYY-MM-DD — snapshot title

- Plugin version:
- Source commit:
- Snapshot class:
- Validation evidence:
- Sensitive-data review:
- Notes and limitations:
```
