# Workflow routing

Discover each capability before use; names below are task hints from the baseline, not permission or proof of availability. Read current input schema, target surface, confirmation and transaction behavior. Returned IDs are the editor identities; template-local IDs are remapped during apply.

| Intent | Search/current capability owner | Verification |
|---|---|---|
| Context, current project and scene | editor context, project get, scene list/get | Confirm identity, dimensions, duration and revision. |
| Reusable full scene/project/block | template JSON import/apply; otherwise manual Import AI JSON | Validate, choose intended type/action, inspect warnings. Replacing a scene requires scoped authorization. |
| Native title/labels/panels | text create/update, object create/update/transform | Read back text, bounds and history. |
| Connected request journey | `motion.request_flow` | Native endpoints, actual path ownership, before/during/arrival frame. |
| Proportional categorical comparison | `motion.comparison_bars` | Exact values, baseline, ratios and readable hold. |
| Hero metric | `motion.metric_reveal` | Shell/label timing, copy and proof relationship. |
| Editable product in a device | `motion.device_showcase` | Original content IDs, native Clip source, containment and layer order. |
| Word title entrance | `motion.kinetic_title` / text kinetic owner | Word timing, type readability, no duplicated entrance owner. |
| Precise motion | timeline track/keyframe, animation preset, draw-step, camera, path-follow owners | Binding eligibility, ownership, scene-local timings and playback. |
| Procedural geometry/components | procedural validate/create/update, component discovery | Discover current recipe/component contract; retain recipe/parameters, native text and host editability. |
| Spatial review/placement | `layout.composition_inspect`, object get, layout flow/grid | Diagnostic is read-only; repair through a placement/text owner. See QA fallback. |
| Revise and recover | canonical owner, history Undo/Redo | Check a single intended revision and inspect before/after. |
| Native save/export | discovered project save, MP4 video or `.scribe` download/export; supported app UI when browser-mediated. SVG export is unavailable publicly. | Inspect returned completion/output, reopen native package, compare actual export. |

One intent can require several owners. Prefer useful semantic recipes to repeated construction calls without forcing every animation into a recipe. Do not force camera, keys, Draw Steps or effects to hit a quota. Preserve editability and the communication goal.
