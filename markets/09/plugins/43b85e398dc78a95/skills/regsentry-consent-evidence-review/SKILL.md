---
name: regsentry-consent-evidence-review
description: "Inspect an authorized public website's tracking signals, compare observed consent phases, and prepare a practical evidence report and retest plan."
---

Use the connected RegSentry tools at https://regsentry.com/mcp. If unavailable, use https://regsentry.com/mcp-guide for connection guidance. The service is public and needs no account.



# Review consent evidence

Begin with a public URL the user is authorized to test. Keep static markup and runtime observations separate. Ask for the URL if absent; do not invent a site, permission or scan history. No account connection is required.

Use `inspect_site_tracking` for markup signals and `inspect_runtime_consent` when the user needs observed behavior. Runtime inspection uses separate fresh browser contexts for before consent, exact reject-all and exact accept-all phases. It observes attempted requests matching known trackers, not proof that a server received personal data. Preserve timestamps, observation windows, controls, errors and limitations. An incomplete phase or control_not_found is unresolved, never a passing rejection test.

The inspector restricts network activity, blocks non-GET requests, forms, frames, media, images, service workers and WebSockets. These restrictions can prevent a site or consent flow from operating normally. A tracker absent from the observation window is not proof of absence; unknown trackers and excluded traffic remain gaps.

Use `compare_consent_observations` only with actual supplied observations from the same domain, preserving phase completeness. No stored history is implied. Compare before/after evidence without treating missing phases or changed coverage as improvements. Use `interpret_consent_evidence` and `get_remediation_playbook` to prioritize a fix and an explicit retest step; do not infer jurisdictional compliance.

Use `export_consent_report` to produce file content from the observed evidence when requested. It does not publish a report or persist a monitoring project. On return visits, request the earlier snapshot when unavailable, run a newly authorized observation if needed, and compare like-for-like phases. Never promise ongoing scans or claim certification, legal compliance, successful data transmission or independent proof of consent from these bounded checks.
