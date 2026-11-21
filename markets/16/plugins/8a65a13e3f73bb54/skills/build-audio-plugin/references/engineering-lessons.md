# Engineering lessons and evidence limits

Use only the entries relevant to the user's task. These are general descriptions
derived from a reviewed release-cycle handoff finalized 2026-10-02. They are not
product implementations, fresh regression results, or permission to redistribute
product, shared-template, SDK, signing, artwork or test-harness source. Keep the
source owner's evidence separately; never publish private runbooks or data.

Dispro's executable recipe remains the original mono LV2 gain example. None of
the UI, browser, entitlement or commerce systems below is implemented by Dispro.
Record applicability separately from result: a non-applicable gate is not a pass.

## visual-first

For a new plugin, present a visual mockup plus control/signal-flow brief before
new DSP implementation. Record which mockup the user approved and its scope;
approval of an unrelated design does not transfer. Keep an unchanged example run
separate from new design work. Preserve approved sound/UI during delivery repairs.
**Basis:** standing workflow requirement, not evidence that approval occurred.

## teardown-order

Map editor, peer, child-window, attachment, control and LookAndFeel ownership.
Fence late callbacks; stop timers/listeners and asynchronous prewarm/creation.
Destroy attachments before controls and dependent children before resources.
For applicable owned child windows, hide, clear owned content, then destroy the
owner while required parent state still exists. Respect message-thread and
SafePointer requirements; detach LookAndFeel references before its destruction.
**Basis:** historical repair chain plus isolated source/syntax/mock checks.
**Open:** exact native editor-close, child-window and DLL-unload acceptance.

## windows-renderer

Inspect actual renderer creation and resource lifetime in the pinned JUCE input.
Where an appropriate reviewed policy calls for GDI, select it by name and manage
software-backed images deliberately; never assume a numeric renderer index.
The exact `JUCE_DIRECT2D` token had no disabling consumer in the inspected pinned
modules. `JUCE_DIRECT2D=0` is therefore not an effective fix for those inputs;
similarly named `_METRICS` tokens do not establish otherwise. Verify each new
dependency version rather than transplanting the define. GDI peer selection
alone does not prove that no DirectX device or static cache was initialized.
**Basis:** historical D3D11/WARP DLL-unload diagnosis and current source inspection.
No original debugger dump or fresh Windows GUI/DLL-unload pass was supplied.
**Open:** exact-binary native lifecycle acceptance, including the affected
Windows ARM64/WARP/host condition when available. Headless x64 smoke is separate.

## webview-lifetime

Treat embedded-browser UI/STA, callbacks and resource backing as their own
lifetime graph. Retain resource backing through browser teardown, and follow
the selected browser SDK's thread requirements. Its GPU/COM lifetime is distinct
from the JUCE peer renderer; switching that renderer does not qualify the browser.
**Basis:** source/syntax/mock checks only; native Windows browser closure pending.

## preset-identity

Restore a preset label only when both the saved index is in bounds and the exact
name matches. Do not reload the preset or overwrite saved parameter values merely
to restore identity. Include stale index, renamed preset and edited-state cases.
**Basis:** historical recorded regression scope. Adapt to the actual state schema;
this checklist does not implement or newly test that product behavior.

## automation-state

Exercise legal parameter steps, balanced gestures, saved bypass states and
session recall. Bind the mapped binary path/hash and actual loaded instance;
bundle selection or a plausible UI is insufficient. Compare rendered PCM as well
as state. Keep named-host results attached to their exact artifact and environment.
**Basis:** retained host/audio/state passes with bounded scope; AU transition
acceptance remains a separate gate.

## bypass-latency

Compare warm wet-to-bypass, unchanged bypass and return-to-wet against
latency-aligned dry input. Distinguish API bypass from a host route that stops AU
rendering. Account for reported latency and the actual input boundary.
**Basis:** a targeted candidate repair/API fixture passed, while the actual
Logic AU transition case remained failing. This is unresolved, not a proven
shared fix. Do not transplant a DSP or wrapper workaround on that evidence.

## causal-controls

Declare the hypothesis and a falsifying control before another run. Compare
PCM, input boundary, instance identity and lossless trace completeness. Block
subdivision alone does not establish causation; repeated identical exports add
no useful evidence after that control is established. Qualify instrumentation
overhead separately from the effect being observed.
**Basis:** recorded unchanged-wet controls and complete trace scope; sanitizer
coverage and real-time performance were not established.

## pinned-provenance

Pin product, shared platform, JUCE/SDK and build inputs independently. An enclosing
snapshot HEAD is not a component revision. A mutable CMake cache path cannot prove
which historical dependency bytes built a binary. Preserve input locks and hashes.
**Basis:** frozen future-input manifests; historical reproducibility stays bounded.

## retained-artifact

Bind archives to source, CI run and attempt; retain the deliverable before expiry.
Check archive hash, extraction inventory and inner payload hashes. Limit any
line-ending/metadata compatibility rule to its declared fields without weakening
byte integrity. Build logs are not binaries, installers or installed-host proof.
**Basis:** retained diagnostic artifacts and scoped smoke receipts only.

## sign-notarize-staple

Track signing, notarization acceptance, stapling, Gatekeeper, installer execution,
rollback and installed host behavior separately for every declared format.
Preserve original bytes and record post-staple hashes as new artifacts; do not
silently reuse the old digest. Stapling/Gatekeeper acceptance does not prove
installation. Dispro never starts signing or publishing automatically.
**Basis:** exact retained macOS artifact receipts, not universal release readiness.

## product-specific-signing

Use the product's authorized PACE configuration and signer. Never substitute a
different product's GUID or infer remote absence from a local inventory gap.
Keep unsigned Windows candidates explicitly unqualified. Check applicable SDK
rights and publisher authorization before a separately requested signing action.
**Basis:** product-local inspection and pending gates; no keys/configuration copied.

## install-safety

Preserve installed originals and unsaved projects; agree a bounded rollback plan.
Close normally, bind the actual mapped binary path/hash and use owned-process
timeouts. Do not discard sessions or treat forced termination as a normal-close
pass. A diagnostic left installed is not a release candidate acceptance result.
**Basis:** particular controlled installations only; new installs require their
own authorization and receipts. Dispro's runner does not install anything.

## licence-policy

Keep free and grandfathered entitlements intact. Resolve registered-device,
concurrent-use, offline-duration and revocation policies before protocol changes.
An indefinitely valid offline receipt cannot guarantee a strict concurrent-use
cap after revocation. Another product's offline format is not transferable proof.
**Basis:** policy tradeoffs and separate product implementations; proposed permanent
receipts are not implemented by a time-limited lease adapter. No policy migration
or entitlement enforcement is included in Dispro.

## transactional-licensing

For an authorized future server implementation, use persisted authoritative
linkage, one lock order, commit-before-response and byte-identical idempotent
replay. Test real contention, commit failure and rollback in a disposable database
with external providers blocked. Do not run such fixtures against production.
**Basis:** local unwired adapter fixtures only; production migration, cryptographic
security and native-client compatibility remain distinct open gates.

## fulfilment-acceptance

Use authenticated provider identity, preserve one licence under retries and
monotonic accepted-mail state. Separate database issuance, provider acceptance,
inbox receipt and installed activation. Zero-value checkout does not demonstrate
positive-payment settlement. Never use customer data or contact real recipients
merely to make a routine fixture pass.
**Basis:** historical local and scoped transaction/mail receipts; no blanket paid
activation or positive-settlement claim. Dispro adds no commerce integration.

## measurement-definitions

Separate service requests, consented page events, redirects, trial starts and
purchases. Preserve QA exclusions and matching time windows. A redirect is not
a completed download; consented analytics does not cover all traffic. Keep the
measurement definition with its result and do not introduce identity stitching.
**Basis:** existing implementation/source evidence, not new collection or deployment.

## bounded-execution

Use one owner per mutable surface and record UTC state transitions: prior state,
input/artifact identity, authority, action, result, unresolved gate and next step.
Reuse passed evidence only for the same relevant bytes and environment. Use models
for design or exceptions; deterministic scripts handle routine checks. No new
workers, CI, paid services, repeated native builds or uncontrolled polling.
Distinguish accumulated storage charges from current artifact byte counts.
**Basis:** operational lessons, not a statement about current budget or tool access.
