# Timing, ownership and relationships

All scene-owned DTO timings start at local 0 milliseconds: object animationStart/animationDuration, timing.startMs/endMs, track animationStartMs/animationDurationMs, keys.time, camera.timeMs, Draw Steps startMs/durationMs, kinetic/path-morph timing and scene audio. Runtime object animation stores seconds; apply converts it. Never add previous scenes' durations to DTO times. Global timeline.seek and scene-local frame preview are different live contracts.

Use `timing: {startMs, endMs, mode:"visible-range", endBehavior:"hide"}` for temporary content, and `endBehavior:"hold"` for content that should retain its final state. Legacy omitted endBehavior follows hold behavior. Current imports preserve explicit hide/hold. Inspect the exact boundary, then the settled hold.

Use a single intended authority per property: ordinary animation for entrance, a supported lane for precise change, Draw Step/draw.progress for reveal, camera for framing. If multiple representations control the same reveal, synchronize from one timing plan and check precedence in playback. Canonical lint checks nonnegative intervals within scene duration, sorted camera/track keys, positive camera zoom and duplicate key/step/scene IDs. Production imports may warn/clamp timing; a valid import does not prove the intended motion survived. Blocks lack a scene duration: check insertion against the destination scene at runtime.

| Relationship | Portable field and ownership |
|---|---|
| Smart connector | `connector.start/end.{targetObjectId,anchor}`; targets are existing local scene objects. Native resolver owns endpoint geometry. |
| Anchor | `anchorBinding.{sourceObjectId,sourceAnchor,targetAnchor,offsetX,offsetY}`; source supplies placement. x/y property lanes are skipped when anchor placement owns them. |
| Clip | `clipBinding.{sourceObjectId,mode:"inside"}`; runtime requires an eligible visible native shape source. A rectangle AABB diagnostic cannot certify curved clipping. |
| Path follow | `props.pathFollow` with enabled/boundPathId/rotateWithPath/rotationOffset/offsetX/offsetY/reverse. Timeline progress binding is `pathFollower.t`, not `pathFollow.progress`. |
| Camera follow | timeline.cameraMode follow-object and cameraFollowTargetId; use remapped runtime target after apply. |
| Morph | `pathMorph` contains source/target geometry snapshots; do not invent a live target-object dependency. |
| Kinetic text | `kineticText` version/mode/timing/easing/from/hash/runOverrides; text edits can suspend stale overrides. |
| Procedural | Asset/recipe parameters, semantic frames/attachments/motion/marks/fills belong to one procedural host; scene transforms remain ordinary object control. |

Keep local scene IDs/references unique and stable while authoring. The app remaps them on apply. Read back returned IDs before revision. Slots and object roles must target actual authored objects; declared lock intent must agree with runtime state. Graph cycles, type-ineligible Clip/Anchor targets and competing controllers need actual app validation and event-frame QA even when the structural schema passes.
