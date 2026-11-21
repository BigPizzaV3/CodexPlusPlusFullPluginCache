# Deferred local acceptance protocol

Status: NOT_RUN in this cloud phase. Run with the built ZIP on a supported local desktop; no source checkout, repository lookup, hidden helper scripts or preinstalled skill may be available to the agent. Record ZIP hash, package/app versions/build SHA, OS, ChatGPT app version, model, policy/rollout, tool list and timestamps. If GPT-6.1 Sol tools are absent, record the compatibility blocker; do not silently use a different model. The person running this phase operates their own desktop and approves browser confirmations.

| Case | Observable acceptance evidence |
|---|---|
| Fresh install/discovery | Extract/install package via local marketplace in a fresh profile/chat. Confirm version, skill/resources and top-level Scribe Site tools actually discovered. Capture installation and tool UI. |
| Create | From a new brief, discover/get/execute live capabilities, create an editable scene with native text and separate visuals. Read back IDs/state and inspect rendered frame. |
| Revise/Undo/Redo | Change text/geometry, inspect result, Undo once and verify original state, Redo and verify revision. Preserve focused text/history behavior. |
| Procedural import | Import the supplied self-contained procedural scene through real Import AI JSON or its discovered supported workflow. Edit seed/parameter/material/playback, inspect drawing motion and recipe persistence. Reject a bad digest without mutation. |
| Unavailable/denied tools | Disable or deny the appropriate tool through normal controls; verify stop/recovery, preserved state and truthful NOT_RUN. No script/store bypass. |
| Composition fallback | Open genuine >100-active-leaf scene (without flattening). Record actual diagnostic rejection/preflight and perform manual exact-frame review. Keep diagnostic and manual statuses distinct. |
| Native save/reopen | Save `.scribe` through the supported app flow, reopen it in a clean editor, verify object IDs/types/editability/references/timing/procedural props. Hash delivered file. |
| Visual/playback/export | Inspect settled frame and before/during/after event strips; play complete animation. Export representative MP4 output (SVG export is unavailable publicly), inspect actual file, record format/resolution/codec/duration and errors. |

Record each PASS/FAIL/NOT_RUN and attach frames, call ledger, native file and actual output. Automated package, mocked WebMCP and source-assisted importer tests are supporting engineering evidence only; they do not count as this acceptance. Resolve failures and rerun only affected cases before release.
