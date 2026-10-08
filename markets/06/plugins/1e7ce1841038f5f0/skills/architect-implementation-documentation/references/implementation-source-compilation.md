# Implementation source compilation

Use only when a controlled suite is too large, redundant or diffuse for reliable gate execution. Compilation creates derived consumption artifacts; it never creates new authority.

## Required metadata

For each artifact record ID/path, version/hash, generation rule/tool, generation time/timezone, upstream source IDs/versions/sections, upstream authority and precedence, intended task/gate, permitted use, conflict handling, regeneration trigger, owner and validation evidence.

Minimum useful outputs may include an active-source manifest, decision slice, acceptance slice, protected invariants and task contract. Add machine-readable token, geometry, animation, content, asset or equivalent manifests only when the project has an evidenced machine-consumption need and an authoritative upstream model.

For a material creative or asset pipeline, a derived asset manifest may distinguish `SOURCE_MASTER`, `PUBLISHING_OR_DELIVERY_TARGET`, `RUNTIME_REPRESENTATION`, transformation/export rule, quality tier, accepted calibration checkpoint and regeneration trigger. It preserves lineage and does not make the derivative more authoritative than its approved source or perceptual target. Omit this layer when authoring and delivery are simple or identical.

## Controls

- A derivative cannot override, fill gaps in or silently reinterpret its upstream source.
- On conflict, the authorized source-of-truth and precedence matrix win; mark the derivative stale/invalid and regenerate after approved correction.
- Regenerate when an upstream source, precedence rule, gate scope or generation rule changes.
- Validate schema, source coverage, exact critical values, exclusions and round-trip traceability.
- Keep historical sources inactive unless explicitly required for a live conflict or coverage audit.
- The first-read must identify which derivative is usable and where authoritative detail remains upstream.

Run the clean-room test with only the declared first-read and slices. A complete suite still fails operational readiness when the agent must read unnecessary history, cannot discover a critical value or cannot deterministically re-enter after reset.
