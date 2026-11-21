# Composition, motion QA and honest fallback

Before extra decoration/motion and before a completion claim, render the exact settled scene frame at project resolution. Identify hero, primaryVisual, proof and supporting IDs only when the roles exist. Use live context/object queries to estimate active bounded leaves at the same time. Groups, suppressed relationships, hidden/zero-opacity items and ineligible bounds are excluded by the runtime; clipped objects use a source-AABB intersection. Raw object count is only a conservative preflight, not the exact diagnostic count.

`layout.composition_inspect` accepts a nonnegative finite scene-local time within scene duration and current scene IDs. It rejects more than **100 active bounded objects**, accepts at most **8 unique role references total**, and uses at most 8 alignment objects. See [limits](limits.json). Its AABB rectangle-union mass, quadrants, distances, alignments and thresholds are review prompts, not painted pixels, glyph ink, effects extent, exact curved Clip edges, aesthetics or a design score.

| Situation | Required evidence route |
|---|---|
| Available and within limit (or count uncertain) | Query the diagnostic once; record exact input/result/limitations and compare with the exact rendered frame. |
| Known over 100 active bounded leaves | Record `DIAGNOSTIC_NOT_RUN: LIMIT_PREFLIGHT`; perform manual exact-frame review. |
| Query rejects, denies or is unavailable | Record `DIAGNOSTIC_REJECTED` with exact error, or `DIAGNOSTIC_NOT_RUN` with availability reason; perform manual exact-frame review if a frame can be obtained through an authorized route. |
| Exact frame unavailable | Record visual QA NOT_RUN and deliver a draft. Offline schemas/counts cannot yield a composition PASS. |

Manual review records scene/time/resolution, frame artifact, role IDs, checks and reviewer rationale. Check hierarchy, proof-to-message connection, whole-frame visual mass, intentional whitespace, readable type/data, margins, baselines, accidental overlap/clipping and connector endpoints. Record `MANUAL_REVIEW_PASS` or `NEEDS_COMPOSITION_REPAIR`; **never label this diagnostic PASS**. Do not alter, delete, hide, flatten or split authored content solely to make a bounded diagnostic pass. You may create a smaller *genuine* deliverable if the brief needs it, not as evidence substitution.

For each diagnostic review signal, repair a concrete communication defect or justify the measured condition using that frame's hierarchy and relationships. Reinforcing signals merit one bounded alternative arrangement: checkpoint/Undo boundary, adjust native geometry/text/layout, preview/reinspect, keep the stronger result. Do not optimize the metric in isolation.

For each present event, inspect before/during/after at its exact owner/time: entrance, travel/arrival, containment crossing, proof reveal, indication, camera, draw/morph, hide boundary and final hold. Use a short adjacent-frame strip when a transition looks suspicious, then play the complete result for tempo and legibility. Resolve conflicting controllers through the canonical owner; preview again after repair. Inspect editability, slot replacement and asset availability. Save/reopen `.scribe` and inspect a representative actual export separately.

Delivery evidence fields: package/app build identity, project/scene/time, input schema compatibility, offline import/canonical lint result, warnings addressed, diagnostic status, manual visual status, motion/playback, native save/reopen and export status. PASS/FAIL/NOT_RUN are per check. No offline or mocked test establishes fresh plugin installation, browser discovery or end-to-end WebMCP acceptance.
