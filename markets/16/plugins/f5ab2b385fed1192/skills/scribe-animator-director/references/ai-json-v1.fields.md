# Generated TemplateEnvelopeV1 structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

## TemplateEnvelopeV1

| Field | Required | Structural type |
|---|---|---|
| schemaVersion | yes | 1 |
| meta | yes | TemplateMetaV1 |
| payload | yes | SceneDTO / BlockDTO / ProjectDTO |
| requiredAssets | no | array<AssetRef> |
| authoring | no | TemplateAuthoringV1 |

## TemplateMetaV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| type | yes | "project" / "scene" / "block" |
| name | yes | string |
| description | no | string |
| timingSemantics | no | "scene-local-v1" |
| tags | yes | array<string> |
| createdAt | yes | string |
| updatedAt | no | string |
| preview | no | Record2 |
| aspectRatio | no | string |
| durationMs | no | number |
| author | no | string |
| packId | no | string |
| useCaseTags | no | array<"education" / "coaching" / "business" / "marketing" / "storytelling" / "social" / "shorts"> |
| formatTags | no | array<"title" / "agenda" / "definition" / "steps" / "comparison" / "timeline" / "flowchart" / "stats" / "quote" / "outro" / "cta" / "intro" / "bullet-list" / "callout"> |
| styleTags | no | array<"clean-sketch" / "chalk" / "blueprint" / "minimal" / "colorful" / "professional"> |

## Record2

| Field | Required | Structural type |
|---|---|---|
| path | no | string |
| blobKey | no | string |
| dataUrl | no | string |

## SceneDTO

| Field | Required | Structural type |
|---|---|---|
| width | yes | number |
| height | yes | number |
| durationMs | yes | number |
| name | no | string |
| tags | no | array<string> |
| goal | no | string |
| notes | no | string |
| thumbnailLabel | no | string |
| thumbnailColor | no | string |
| transition | no | SceneTransition |
| cameraTransition | no | SceneCameraTransition |
| drawOverrides | no | HandDrawOverrides |
| background | no | BackgroundDTO |
| objects | yes | array<ObjectDTO> |
| timeline | no | TimelineSnippetDTO |

## SceneTransition

| Field | Required | Structural type |
|---|---|---|
| type | yes | "none" / "fade" / "crossfade" / "wipe-left" / "wipe-right" / "wipe-up" / "wipe-down" / "slide-left" / "slide-right" / "slide-up" / "slide-down" / "zoom-in" / "zoom-out" / "iris-in" / "iris-out" |
| durationMs | yes | number |
| easing | yes | "linear" / "ease-in" / "ease-out" / "ease-in-out" / "ease-in-cubic" / "ease-out-cubic" / "ease-in-out-cubic" |
| fadeColor | no | string |
| wipeAngle | no | number |
| irisCenter | no | Record5 |

## Record5

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## SceneCameraTransition

| Field | Required | Structural type |
|---|---|---|
| durationMs | yes | number |
| easing | yes | "linear" / "ease-in" / "ease-out" / "ease-in-out" / "ease-in-cubic" / "ease-out-cubic" / "ease-in-out-cubic" |
| enabled | yes | boolean |

## HandDrawOverrides

| Field | Required | Structural type |
|---|---|---|
| presetId | no | string |
| toolId | no | string |
| scale | no | number |
| mirror | no | false / true |
| drawSpeed | no | number |
| travelSpeed | no | number |
| jitter | no | number |
| smoothing | no | number |
| revealMode | no | "dash" / "mask" / "clip" |
| strokeMaterial | no | "chalk" / "solid" / "marker" / "pencil" / "crayon" / "dry-marker" / "ink-brush" / "highlighter" |
| strokeMaterialFollowsBoard | no | false / true |
| strokeColor | no | string |

## BackgroundDTO

| Field | Required | Structural type |
|---|---|---|
| type | yes | "solid" / "gradient" / "image" / "preset" |
| color | no | string |
| gradientStops | no | array<Record9> |
| imageUrl | no | string |
| presetId | no | string |

## Record9

| Field | Required | Structural type |
|---|---|---|
| offset | yes | number |
| color | yes | string |

## ObjectDTO

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| type | yes | "image" / "text" / "svg" / "shape" / "group" / "drawing" / "video" / "videoEmbed" / "svgPath" / "smartLine" / "smartArrow" / "procedural" |
| x | yes | number |
| y | yes | number |
| width | no | number |
| height | no | number |
| textBoxSizing | no | "auto-content" / "fixed" |
| rotation | no | number |
| props | yes | Record |
| connector | no | SmartConnectorMetadata |
| anchorBinding | no | AnchorBinding |
| clipBinding | no | ClipBinding |
| visualEffects | no | VisualEffectsV1 |
| kineticText | no | KineticTextBinding |
| pathMorph | no | PathMorphBinding |
| locked | no | false / true |
| visible | no | false / true |
| zIndex | no | number |
| styleRefs | no | ObjectStyleRefs |
| animationStart | no | number |
| animationDuration | no | number |
| timing | no | SceneObjectVisibleRangeTiming |
| animationType | no | "none" / "fadeIn" / "slideIn" / "scaleIn" / "drawIn" / "pathFollow" / "typewriter" |
| animationEasing | no | "linear" / "easeIn" / "easeOut" / "easeInOut" |

## Record

| Field | Required | Structural type |
|---|---|---|


## SmartConnectorMetadata

| Field | Required | Structural type |
|---|---|---|
| start | no | SmartConnectorEndpointAttachment |
| end | no | SmartConnectorEndpointAttachment |

## SmartConnectorEndpointAttachment

| Field | Required | Structural type |
|---|---|---|
| targetObjectId | yes | string |
| anchor | yes | "auto" / "top" / "right" / "bottom" / "left" / "center" |

## AnchorBinding

| Field | Required | Structural type |
|---|---|---|
| sourceObjectId | yes | string |
| sourceAnchor | yes | "center" / "top-left" / "top-center" / "top-right" / "center-left" / "center-right" / "bottom-left" / "bottom-center" / "bottom-right" |
| targetAnchor | yes | "center" / "top-left" / "top-center" / "top-right" / "center-left" / "center-right" / "bottom-left" / "bottom-center" / "bottom-right" |
| offsetX | yes | number |
| offsetY | yes | number |

## ClipBinding

| Field | Required | Structural type |
|---|---|---|
| sourceObjectId | yes | string |
| mode | yes | "inside" |

## VisualEffectsV1

| Field | Required | Structural type |
|---|---|---|
| blur | no | number |
| brightness | no | number |
| contrast | no | number |
| saturation | no | number |
| shadow | no | Record17 |
| glow | no | Record18 |

## Record17

| Field | Required | Structural type |
|---|---|---|
| color | yes | string |
| blur | yes | number |
| offsetX | yes | number |
| offsetY | yes | number |
| opacity | yes | number |

## Record18

| Field | Required | Structural type |
|---|---|---|
| color | yes | string |
| blur | yes | number |
| opacity | yes | number |

## KineticTextBinding

| Field | Required | Structural type |
|---|---|---|
| version | yes | 1 |
| mode | yes | "word" |
| startMs | yes | number |
| durationMs | yes | number |
| staggerMs | yes | number |
| easing | yes | "linear" / "ease-in" / "ease-out" / "ease-in-out" |
| from | yes | KineticTextTransform |
| overrideTextHash | yes | string |
| runOverrides | no | array<Record21> |

## KineticTextTransform

| Field | Required | Structural type |
|---|---|---|
| offsetX | yes | number |
| offsetY | yes | number |
| scale | yes | number |
| rotation | yes | number |
| opacity | yes | number |

## Record21

| Field | Required | Structural type |
|---|---|---|
| runIndex | yes | number |
| rotationFrom | no | number |
| delayMs | no | number |

## PathMorphBinding

| Field | Required | Structural type |
|---|---|---|
| version | yes | 1 |
| startMs | yes | number |
| durationMs | yes | number |
| easing | yes | "linear" / "ease-in" / "ease-out" / "ease-in-out" |
| source | yes | array<array<MorphCommand>> |
| target | yes | array<array<MorphCommand>> |

## MorphCommand

| Field | Required | Structural type |
|---|---|---|
| op | yes | "M" / "L" / "C" / "Q" / "Z" |
| values | yes | array<number> |

## ObjectStyleRefs

| Field | Required | Structural type |
|---|---|---|
| typographyId | no | string |
| handPresetId | no | string |

## SceneObjectVisibleRangeTiming

| Field | Required | Structural type |
|---|---|---|
| startMs | yes | number |
| endMs | yes | number |
| mode | no | "visible-range" |
| endBehavior | no | "hold" / "hide" |

## TimelineSnippetDTO

| Field | Required | Structural type |
|---|---|---|
| storyBeats | no | array<StoryBeat> |
| tracks | no | array<TemplateTimelineTrackDTO> |
| keys | no | array<TemplateTimelineKeyDTO> |
| drawSteps | no | array<DrawStepDTO> |
| cameraMode | no | "static" / "track" / "follow-hand" / "follow-object" |
| cameraFollowTargetId | no | null / string |
| camera | no | array<CameraKeyframeDTO> |
| audio | no | array<AudioClipDTO> |

## StoryBeat

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| sceneId | yes | string |
| name | yes | string |
| semanticId | no | string |
| startMs | yes | number |
| endMs | yes | number |
| timingAuthority | yes | "audio" / "visual" / "locked" |
| syncPolicy | yes | "preserve-relative" |
| narrationSegmentId | no | null / string |
| createdAt | no | number |
| updatedAt | no | number |
| objectRefs | yes | array<StoryBeatObjectRef> |
| drawStepIds | yes | array<string> |
| keyframeRefs | yes | array<StoryBeatKeyframeRef> |
| cameraKeyframeIds | yes | array<string> |

## StoryBeatObjectRef

| Field | Required | Structural type |
|---|---|---|
| objectId | yes | string |
| timingOwned | no | false / true |
| role | no | string |

## StoryBeatKeyframeRef

| Field | Required | Structural type |
|---|---|---|
| trackId | yes | string |
| keyIds | yes | array<string> |

## TemplateTimelineTrackDTO

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| ownerId | yes | string |
| binding | yes | string |
| type | yes | string |
| label | no | string |
| category | no | "audio" / "property" / "camera" / "draw" |
| order | no | number |
| hidden | no | false / true |
| locked | no | false / true |
| easing | no | string |
| animationStartMs | no | number |
| animationDurationMs | no | number |
| bounds | no | TemplateTimelineBoundsDTO |
| defaultValue | no | number |
| defaultEndValue | no | number |
| defaultInterp | no | string |
| meta | no | Record |

## TemplateTimelineBoundsDTO

| Field | Required | Structural type |
|---|---|---|
| min | no | number |
| max | no | number |

## TemplateTimelineKeyDTO

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| trackId | yes | string |
| time | yes | number |
| value | yes | number |
| interp | no | string |
| easing | no | string |
| tangentMode | no | "linear" / "auto" / "flat" / "broken" |
| inTangent | no | null / TemplateTimelineTangentDTO |
| outTangent | no | null / TemplateTimelineTangentDTO |
| group | no | string |
| meta | no | Record |

## TemplateTimelineTangentDTO

| Field | Required | Structural type |
|---|---|---|
| dx | yes | number |
| dy | yes | number |

## DrawStepDTO

| Field | Required | Structural type |
|---|---|---|
| id | no | string |
| objectId | yes | string |
| startMs | yes | number |
| durationMs | yes | number |
| from | no | number |
| to | no | number |
| targetPathId | no | string |
| strokeColor | no | string |
| strokeMaterial | no | "chalk" / "solid" / "marker" / "pencil" / "crayon" / "dry-marker" / "ink-brush" / "highlighter" |
| overrides | no | HandDrawOverrides |
| camera | no | DrawStepCameraSettings |
| easing | no | string |

## DrawStepCameraSettings

| Field | Required | Structural type |
|---|---|---|
| mode | yes | "none" / "hero" / "wide" / "lock" |
| transition | yes | number / "quick" / "smooth" |
| after | yes | "continue" / "revert" |
| paddingPct | no | number |
| framing | no | "wide" / "tight" / "medium" |
| startOffsetSec | no | number |
| holdSec | no | number |

## CameraKeyframeDTO

| Field | Required | Structural type |
|---|---|---|
| id | no | string |
| rotation | no | number |
| timeMs | yes | number |
| x | yes | number |
| y | yes | number |
| zoom | yes | number |
| easing | no | string |

## AudioClipDTO

| Field | Required | Structural type |
|---|---|---|
| assetRef | yes | string |
| startMs | yes | number |
| durationMs | yes | number |
| volume | no | number |

## BlockDTO

| Field | Required | Structural type |
|---|---|---|
| objects | yes | array<ObjectDTO> |
| anchor | no | BlockAnchor |
| timeline | no | TimelineSnippetDTO |

## BlockAnchor

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## ProjectDTO

| Field | Required | Structural type |
|---|---|---|
| name | yes | string |
| width | yes | number |
| height | yes | number |
| fps | yes | number |
| scenes | yes | array<ProjectSceneDTO> |
| stylePresets | no | Record42 |

## ProjectSceneDTO

| Field | Required | Structural type |
|---|---|---|
| sceneId | yes | string |
| order | yes | number |
| width | yes | number |
| height | yes | number |
| durationMs | yes | number |
| name | no | string |
| tags | no | array<string> |
| goal | no | string |
| notes | no | string |
| thumbnailLabel | no | string |
| thumbnailColor | no | string |
| transition | no | SceneTransition |
| cameraTransition | no | SceneCameraTransition |
| drawOverrides | no | HandDrawOverrides |
| background | no | BackgroundDTO |
| objects | yes | array<ObjectDTO> |
| timeline | no | TimelineSnippetDTO |

## Record42

| Field | Required | Structural type |
|---|---|---|
| typographyThemeId | no | string |
| handPresetId | no | string |
| backgroundPresetId | no | string |
| strokeMaterialId | no | "chalk" / "solid" / "marker" / "pencil" / "crayon" / "dry-marker" / "ink-brush" / "highlighter" |

## AssetRef

| Field | Required | Structural type |
|---|---|---|
| type | yes | "builtin" / "imported" / "url" |
| assetId | no | string |
| packId | no | string |
| filename | no | string |
| url | no | string |
| mime | no | string |

## TemplateAuthoringV1

| Field | Required | Structural type |
|---|---|---|
| editableSlots | yes | array<EditableSlot> |
| objectRoles | yes | array<ObjectRoleEntry> |
| assetChoices | no | array<TemplateAssetChoice> |
| primarySlotCount | no | number |

## EditableSlot

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| kind | yes | "image" / "text" / "audio" / "color" / "icon" |
| label | yes | string |
| objectIds | yes | array<string> |
| propKey | no | string |
| constraints | no | SlotConstraints |
| defaultValue | no | string |
| group | no | string |
| order | no | number |

## SlotConstraints

| Field | Required | Structural type |
|---|---|---|
| maxChars | no | number |
| minChars | no | number |
| aspectRatio | no | string |
| allowedCategories | no | array<string> |
| allowedColors | no | array<string> |
| placeholder | no | string |
| multiline | no | false / true |
| required | no | false / true |

## ObjectRoleEntry

| Field | Required | Structural type |
|---|---|---|
| objectId | yes | string |
| role | yes | "content" / "decoration" / "structure" / "background" |
| lockedByDefault | no | false / true |
| description | no | string |

## TemplateAssetChoice

| Field | Required | Structural type |
|---|---|---|
| role | yes | string |
| assetId | yes | string |
| objectId | no | string |

Opaque contracts: TemplateEnvelopeV1.payload.objects[].props.*.
