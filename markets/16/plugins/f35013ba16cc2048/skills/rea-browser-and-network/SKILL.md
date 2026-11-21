---
name: rea-browser-and-network
description: Plan passive observation of a user-owned browser or Electron app and interpret retained HAR/mitmproxy captures without turning historical records into live network claims.
---

# Browser and network evidence

## Browser/Electron observation

- Prefer the already-open, user-owned page/runtime and the documented REA target-listing workflow.
- Confirm the exact target and interaction. Avoid authentication changes, purchases, destructive actions, production mutations, or private account traversal.
- Distinguish DOM/page structure, loaded scripts, observed requests, screenshots, and runtime effects. A screenshot or page snapshot covers only one state.
- Do not open URLs discovered in a capture or replay requests. Do not claim a historical request came from the live page without fresh attribution evidence.

## Retained HAR or mitmproxy capture

- Confirm the user is authorized to analyze the supplied capture; it may contain cookies, authorization headers, personal data, internal endpoints, or private payloads.
- Use the advertised capture-inspection workflow on the retained file. Treat it as historical evidence, not live traffic.
- Preserve original record ordinals where useful and identify producer-specific fields/sidecars. Do not normalize away distinctions that affect interpretation.
- Redact credentials, tokens, personal data, and unrelated hosts before sharing results. Never print secrets back in the report.
- If capture evidence is incomplete, identify missing records or fields and the limited conclusion; do not fill gaps with assumptions.

Use only read-only analysis unless the user explicitly requests an authorized, tightly scoped interaction. Captured requests must not be replayed against live services.
