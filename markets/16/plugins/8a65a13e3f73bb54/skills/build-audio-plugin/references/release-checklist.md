# Candidate review worksheet

Copy this worksheet per exact artifact/format/OS/architecture/host combination.
This is a review aid, not a new executable validator or a signing authorization.
Do not populate it with example passes. Read existing receipts before rerunning.

Record owner, UTC, source commit, independent dependency locks, compiler/build
configuration, artifact SHA-256, package SHA-256, declared formats, named host and
version, OS/version and architecture. Record the mapped binary identity for host
tests. Redact secrets and private paths in any public handoff.

For each applicable row use `passed`, `failed` or `unrun`, its receipt reference,
evidence class (historical/source/mock/offline/native-host), exact scope and next
gate. Start at `unrun`. Record non-applicability with a reason separately; do not
count it as a pass. Record cancelled/timed-out outcomes without promoting stages.

| Gate | Evidence required before a pass claim |
|---|---|
| New design approval | Approved mockup identity, brief and approval scope before new DSP |
| Source and redistribution | Product/dependency locks and rights for every included source/asset |
| Native compile | Exact binary hash, inputs, toolchain and build result |
| Offline behavior | Exact binary and declared signal/state checks; simulated processes labelled mock |
| Package integrity | Retained archive/run/attempt and extraction plus payload hash agreement |
| Asset staging | Matching binary/asset configuration, required relative destinations and extracted payload inventory; diagnostic fallback is separate |
| Per-architecture platform floor | Binary/dependency slice requirements, installer preflight and published support reconciled; old-OS/hardware proof separate |
| Host discovery/audio | Actual mapped binary, named host, normal playback and rendered PCM |
| Presets/automation/recall | Index/name identity, edited parameter state, legal steps/gestures, reopened session |
| Bypass/latency | Warm transition, unchanged bypass and return-to-wet vs aligned dry; host route identified |
| Native UI/unload | Open/reopen, owned child windows, remove instance, close project, normal unload/exit |
| Browser UI lifetime | Separate browser-thread, callback, resource and closure acceptance when present |
| Signing | Correct product-specific identity/configuration and exact signed artifact |
| Windows publisher signature | Authenticode policy, expected publisher and timestamp; separate from AAX/PACE verification |
| Notarization | Recorded acceptance for that artifact; not inferred from signature validity |
| Stapling/Gatekeeper | Original and post-staple hashes and independent system acceptance |
| Installation/rollback | Preserved originals, normal close, approved install and actual loaded identity |
| Entitlement policy | Explicit free/grandfathered/device/offline/revocation policy and implementation scope |
| Licensing persistence | Disposable-database contention, commit failure/rollback and idempotent replay |
| Fulfilment | Issuance, provider mail acceptance, inbox receipt and installed activation separately |
| Positive settlement | Actual authorized nonzero settlement; a zero-value test cannot satisfy it |
| Measurement | Defined event, consent/QA exclusions and matching window; redirects not downloads |
| Publication | Exact approved payload, appropriate platform acceptance and separate publisher action |

Dispro's fixed runner automates only its input check, tiny build, offline contract
checks and bundle packaging/output-notice checks. It never fills the other rows
automatically. General lessons do not establish Linux, Windows, AU, VST3 or AAX
support for Dispro. Its example has no GUI, browser, preset/state extension,
latency reporting or entitlement server.

Keep the Windows GUI/DLL-unload and known Logic AU bypass-transition gaps open.
Source/syntax/mock checks do not close them. An unconsumed `JUCE_DIRECT2D` define
does not implement a renderer policy. Preserve unsuccessful receipts even if a
later test passes; record exactly which claim that later evidence addresses.

End with the next useful gate and why existing evidence cannot satisfy it. For a
new run, state one falsifiable hypothesis, the smallest control and a bounded
timeout. If nothing material changed, reuse evidence instead of adding a run.
