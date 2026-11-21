# Generated ProceduralAssetV1 structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

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
| provenance | yes | Record47 |

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
| pivot | yes | Record4 |
| rotation | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| scale | yes | Record11 |

## Record4

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## Record5

| Field | Required | Structural type |
|---|---|---|
| op | yes | "parameter" |
| id | yes | string |

## Record6

| Field | Required | Structural type |
|---|---|---|
| op | yes | "random" |
| purpose | yes | string |
| min | yes | number |
| max | yes | number |

## Record7

| Field | Required | Structural type |
|---|---|---|
| op | yes | "motion" |
| id | yes | string |

## Record8

| Field | Required | Structural type |
|---|---|---|
| op | yes | "instance-index" |

## Record9

| Field | Required | Structural type |
|---|---|---|
| op | yes | "add" / "subtract" / "multiply" / "divide" |
| left | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| right | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## Record10

| Field | Required | Structural type |
|---|---|---|
| op | yes | "sin" / "cos" |
| value | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## Record11

| Field | Required | Structural type |
|---|---|---|
| x | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| y | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## BodyFrameV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| kind | yes | "body" |
| spine | yes | Record13 / Record17 |
| halfWidth | yes | array<Record19> |
| deformation | no | Record20 |

## Record13

| Field | Required | Structural type |
|---|---|---|
| op | yes | "polyline" |
| points | yes | array<WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1> |
| closed | yes | boolean |

## WorldCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "world" |
| x | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| y | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## LocalCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "local" |
| frame | yes | string |
| x | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| y | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## BodyCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "body" |
| frame | yes | string |
| t | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| s | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| tangentOffset | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |
| normalOffset | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## Record17

| Field | Required | Structural type |
|---|---|---|
| op | yes | "cubic-bezier" |
| start | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| segments | yes | array<Record18> |
| samplesPerSegment | yes | number |
| closed | yes | boolean |

## Record18

| Field | Required | Structural type |
|---|---|---|
| control1 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| control2 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| end | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |

## Record19

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

## Record20

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "traveling-wave" |
| phaseChannel | yes | string |
| cyclesAlongSpine | yes | number |
| amplitude | yes | array<Record21> |

## Record21

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record5 / Record6 / Record7 / Record8 / Record9 / Record10 |

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
| signal | yes | Record24 / Record25 |

## Record24

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "sine" / "phase" |
| cyclesPerLoop | yes | number |
| phase | yes | number |

## Record25

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
| geometry | yes | Record13 / Record17 / Record27 |
| direction | yes | "forward" / "reverse" |
| drawOrder | yes | number |
| paintOrder | yes | number |
| repeat | no | Record28 |
| style | no | Partial |

## Record27

| Field | Required | Structural type |
|---|---|---|
| op | yes | "body-outline" |
| body | yes | string |
| samples | yes | number |

## Record28

| Field | Required | Structural type |
|---|---|---|
| count | yes | number |

## Partial

| Field | Required | Structural type |
|---|---|---|
| width | no | number |
| pressure | no | array<Record30> |
| taper | no | Record31 |
| wobble | no | number |
| opacity | no | number |
| color | no | string |

## Record30

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number |

## Record31

| Field | Required | Structural type |
|---|---|---|
| start | yes | number |
| end | yes | number |

## FillV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| styleRole | no | "outlinePrimary" / "bodyBase" / "accentPrimary" / "accentSecondary" / "detail" / "construction" / "highlight" / "shadow" |
| boundary | yes | Record13 / Record17 / Record27 |
| paintOrder | yes | number |
| color | yes | string |
| opacity | yes | number |
| fillRule | yes | "nonzero" / "evenodd" |
| reveal | yes | Record33 / Record34 |

## Record33

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "after-drawing" |

## Record34

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
| space | yes | Record37 / Record38 / Record39 |
| region | yes | Record40 / Record42 |
| hatch | yes | ProceduralHatchDescriptorV1 |
| drawOrder | yes | number |
| paintOrder | yes | number |

## Record37

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "world" |

## Record38

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "local" |
| frame | yes | string |

## Record39

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "body" |
| frame | yes | string |
| unitsPerT | yes | number |
| unitsPerS | yes | number |

## Record40

| Field | Required | Structural type |
|---|---|---|
| op | yes | "polygon" |
| points | yes | array<TonePointV1> |

## TonePointV1

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## Record42

| Field | Required | Structural type |
|---|---|---|
| op | yes | "subtract" / "union" / "intersect" |
| left | yes | Record40 / Record42 |
| right | yes | Record40 / Record42 |

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
| pressure | yes | array<Record30> |
| taper | yes | Record31 |
| wobble | yes | number |
| opacity | yes | number |
| color | yes | string |

## Record47

| Field | Required | Structural type |
|---|---|---|
| authoring | yes | "human" / "agent" / "system" |
| source | no | string |

Opaque contracts: ProceduralAssetV1.recipeRevision.
