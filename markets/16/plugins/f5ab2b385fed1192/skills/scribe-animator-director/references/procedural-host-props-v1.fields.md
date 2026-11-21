# Generated ProceduralSceneObject structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

## Record0

| Field | Required | Structural type |
|---|---|---|
| proceduralVersion | yes | 1 |
| asset | yes | ProceduralAssetV1 |
| playback | no | ProceduralPlaybackV1 |
| drawingScore | no | ProceduralDrawingScoreV1 |
| proceduralPalette | no | ProceduralPaletteV1 |
| proceduralComponentSource | no | ProceduralComponentSourceV1 |

## ProceduralAssetV1

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "procedural" |
| assetVersion | yes | 1 |
| recipeSchema | yes | "scribe.procedural/1" |
| recipeRevision | yes | string |
| recipe | yes | ProceduralRecipeV1 |
| toneRegions | no | ProceduralToneRegionSetV1 |
| seed | yes | number |
| rngRevision | yes | 1 |
| parameters | yes | Readonly |
| runtimeRevision | yes | "recipe-runtime/1" |
| material | yes | BallpointMaterialV1 |
| provenance | yes | Record48 |

## ProceduralRecipeV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural/1" |
| parameters | yes | array<NumberParameterV1> |
| frames | yes | array<AffineFrameV1 / BodyFrameV1> |
| attachments | yes | array<AttachmentV1> |
| motionChannels | yes | array<MotionChannelV1> |
| marks | yes | array<MarkV1> |
| fills | yes | array<FillV1> |

## NumberParameterV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| type | yes | "number" |
| unit | yes | "ratio" / "logical-unit" / "radian" / "count" |
| min | yes | number |
| max | yes | number |
| default | yes | number |

## AffineFrameV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| kind | yes | "affine" |
| attachment | yes | string |
| pivot | yes | Record5 |
| rotation | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| scale | yes | Record12 |

## Record5

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## Record6

| Field | Required | Structural type |
|---|---|---|
| op | yes | "parameter" |
| id | yes | string |

## Record7

| Field | Required | Structural type |
|---|---|---|
| op | yes | "random" |
| purpose | yes | string |
| min | yes | number |
| max | yes | number |

## Record8

| Field | Required | Structural type |
|---|---|---|
| op | yes | "motion" |
| id | yes | string |

## Record9

| Field | Required | Structural type |
|---|---|---|
| op | yes | "instance-index" |

## Record10

| Field | Required | Structural type |
|---|---|---|
| op | yes | "add" / "subtract" / "multiply" / "divide" |
| left | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| right | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## Record11

| Field | Required | Structural type |
|---|---|---|
| op | yes | "sin" / "cos" |
| value | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## Record12

| Field | Required | Structural type |
|---|---|---|
| x | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| y | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## BodyFrameV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| kind | yes | "body" |
| spine | yes | Record14 / Record18 |
| halfWidth | yes | array<Record20> |
| deformation | no | Record21 |

## Record14

| Field | Required | Structural type |
|---|---|---|
| op | yes | "polyline" |
| points | yes | array<WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1> |
| closed | yes | boolean |

## WorldCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "world" |
| x | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| y | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## LocalCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "local" |
| frame | yes | string |
| x | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| y | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## BodyCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "body" |
| frame | yes | string |
| t | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| s | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| tangentOffset | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |
| normalOffset | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## Record18

| Field | Required | Structural type |
|---|---|---|
| op | yes | "cubic-bezier" |
| start | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| segments | yes | array<Record19> |
| samplesPerSegment | yes | number |
| closed | yes | boolean |

## Record19

| Field | Required | Structural type |
|---|---|---|
| control1 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| control2 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| end | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |

## Record20

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## Record21

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "traveling-wave" |
| phaseChannel | yes | string |
| cyclesAlongSpine | yes | number |
| amplitude | yes | array<Record22> |

## Record22

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record6 / Record7 / Record8 / Record9 / Record10 / Record11 |

## AttachmentV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| point | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| orientation | yes | "parent" / "tangent" |

## MotionChannelV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| unit | yes | "ratio" / "logical-unit" / "radian" / "cycle" |
| min | yes | number |
| max | yes | number |
| signal | yes | Record25 / Record26 |

## Record25

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "sine" / "phase" |
| cyclesPerLoop | yes | number |
| phase | yes | number |

## Record26

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "pulse" |
| cyclesPerLoop | yes | number |
| phase | yes | number |
| duty | yes | number |

## MarkV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| styleRole | no | "outlinePrimary" / "bodyBase" / "accentPrimary" / "accentSecondary" / "detail" / "construction" / "highlight" / "shadow" |
| geometry | yes | Record14 / Record18 / Record28 |
| direction | yes | "forward" / "reverse" |
| drawOrder | yes | number |
| paintOrder | yes | number |
| repeat | no | Record29 |
| style | no | Partial |

## Record28

| Field | Required | Structural type |
|---|---|---|
| op | yes | "body-outline" |
| body | yes | string |
| samples | yes | number |

## Record29

| Field | Required | Structural type |
|---|---|---|
| count | yes | number |

## Partial

| Field | Required | Structural type |
|---|---|---|
| width | no | number |
| pressure | no | array<Record31> |
| taper | no | Record32 |
| wobble | no | number |
| opacity | no | number |
| color | no | string |

## Record31

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number |

## Record32

| Field | Required | Structural type |
|---|---|---|
| start | yes | number |
| end | yes | number |

## FillV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| styleRole | no | "outlinePrimary" / "bodyBase" / "accentPrimary" / "accentSecondary" / "detail" / "construction" / "highlight" / "shadow" |
| boundary | yes | Record14 / Record18 / Record28 |
| paintOrder | yes | number |
| color | yes | string |
| opacity | yes | number |
| fillRule | yes | "nonzero" / "evenodd" |
| reveal | yes | Record34 / Record35 |

## Record34

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "after-drawing" |

## Record35

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "after-mark" |
| mark | yes | string |

## ProceduralToneRegionSetV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-tone-regions/1" |
| regions | yes | array<ProceduralToneRegionV1> |

## ProceduralToneRegionV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| space | yes | Record38 / Record39 / Record40 |
| region | yes | Record41 / Record43 |
| hatch | yes | ProceduralHatchDescriptorV1 |
| drawOrder | yes | number |
| paintOrder | yes | number |

## Record38

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "world" |

## Record39

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "local" |
| frame | yes | string |

## Record40

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "body" |
| frame | yes | string |
| unitsPerT | yes | number |
| unitsPerS | yes | number |

## Record41

| Field | Required | Structural type |
|---|---|---|
| op | yes | "polygon" |
| points | yes | array<TonePointV1> |

## TonePointV1

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## Record43

| Field | Required | Structural type |
|---|---|---|
| op | yes | "subtract" / "union" / "intersect" |
| left | yes | Record41 / Record43 |
| right | yes | Record41 / Record43 |

## ProceduralHatchDescriptorV1

| Field | Required | Structural type |
|---|---|---|
| angle | yes | number |
| spacing | yes | number |
| maxSegmentLength | yes | number |
| jitter | no | number |

## Readonly

| Field | Required | Structural type |
|---|---|---|


## BallpointMaterialV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | "ballpoint" |
| revision | yes | 1 |
| style | yes | BallpointStyleV1 |

## BallpointStyleV1

| Field | Required | Structural type |
|---|---|---|
| width | yes | number |
| pressure | yes | array<Record31> |
| taper | yes | Record32 |
| wobble | yes | number |
| opacity | yes | number |
| color | yes | string |

## Record48

| Field | Required | Structural type |
|---|---|---|
| authoring | yes | "human" / "agent" / "system" |
| source | no | string |

## ProceduralPlaybackV1

| Field | Required | Structural type |
|---|---|---|
| enabled | yes | boolean |
| periodMs | yes | number |
| phaseOffset | no | number |

## ProceduralDrawingScoreV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-drawing-score/1" |
| parts | yes | array<Record51> |
| layers | yes | array<Record52> |
| steps | yes | array<Record56> |
| marks | yes | array<Record57> |

## Record51

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| label | no | string |
| dependsOn | no | array<string> |

## Record52

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| lifecycle | yes | Record53 / Record54 / Record55 |

## Record53

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "keep" |

## Record54

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "ghost" |
| retireAfterStepId | yes | string |
| finalOpacity | yes | number |
| fadeFraction | yes | number |

## Record55

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "hide" |
| retireAfterStepId | yes | string |
| fadeFraction | yes | number |

## Record56

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| phase | yes | "construction" / "placement" / "contours" / "details" / "accents" |
| markIds | yes | array<string> |

## Record57

| Field | Required | Structural type |
|---|---|---|
| markId | yes | string |
| partId | yes | string |
| layerId | yes | string |
| kind | yes | "detail" / "guide" / "contour" / "accent" |
| timingCost | no | number |
| after | no | array<string> |

## ProceduralPaletteV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-palette/1" |
| baseInk | no | ProceduralPaletteInkV1 |
| roles | yes | Readonly_60 |

## ProceduralPaletteInkV1

| Field | Required | Structural type |
|---|---|---|
| color | no | string |
| width | no | number |
| opacity | no | number |
| wobble | no | number |

## Readonly_60

| Field | Required | Structural type |
|---|---|---|
| outlinePrimary | no | ProceduralPaletteRoleV1 |
| bodyBase | no | ProceduralPaletteRoleV1 |
| accentPrimary | no | ProceduralPaletteRoleV1 |
| accentSecondary | no | ProceduralPaletteRoleV1 |
| detail | no | ProceduralPaletteRoleV1 |
| construction | no | ProceduralPaletteRoleV1 |
| highlight | no | ProceduralPaletteRoleV1 |
| shadow | no | ProceduralPaletteRoleV1 |

## ProceduralPaletteRoleV1

| Field | Required | Structural type |
|---|---|---|
| markStyle | no | ProceduralPaletteInkV1 |
| fill | no | Record62 |

## Record62

| Field | Required | Structural type |
|---|---|---|
| color | no | string |
| opacity | no | number |

## ProceduralComponentSourceV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-component-source/1" |
| compilerRevision | yes | "component-compiler/1" |
| invocationId | yes | string |
| use | yes | string |
| version | yes | number |
| revision | yes | string |
| seed | yes | number |
| params | yes | Readonly |

Opaque contracts: ProceduralSceneObject.properties.*, ProceduralSceneObject.properties.asset.recipeRevision, ProceduralSceneObject.properties.proceduralComponentSource.revision.
