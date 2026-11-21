# Generated ProceduralRecipeV1 structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

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
| pivot | yes | Record3 |
| rotation | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| scale | yes | Record10 |

## Record3

| Field | Required | Structural type |
|---|---|---|
| x | yes | number |
| y | yes | number |

## Record4

| Field | Required | Structural type |
|---|---|---|
| op | yes | "parameter" |
| id | yes | string |

## Record5

| Field | Required | Structural type |
|---|---|---|
| op | yes | "random" |
| purpose | yes | string |
| min | yes | number |
| max | yes | number |

## Record6

| Field | Required | Structural type |
|---|---|---|
| op | yes | "motion" |
| id | yes | string |

## Record7

| Field | Required | Structural type |
|---|---|---|
| op | yes | "instance-index" |

## Record8

| Field | Required | Structural type |
|---|---|---|
| op | yes | "add" / "subtract" / "multiply" / "divide" |
| left | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| right | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## Record9

| Field | Required | Structural type |
|---|---|---|
| op | yes | "sin" / "cos" |
| value | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## Record10

| Field | Required | Structural type |
|---|---|---|
| x | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| y | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## BodyFrameV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| kind | yes | "body" |
| spine | yes | Record12 / Record16 |
| halfWidth | yes | array<Record18> |
| deformation | no | Record19 |

## Record12

| Field | Required | Structural type |
|---|---|---|
| op | yes | "polyline" |
| points | yes | array<WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1> |
| closed | yes | boolean |

## WorldCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "world" |
| x | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| y | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## LocalCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "local" |
| frame | yes | string |
| x | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| y | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## BodyCoordinateV1

| Field | Required | Structural type |
|---|---|---|
| space | yes | "body" |
| frame | yes | string |
| t | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| s | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| tangentOffset | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |
| normalOffset | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## Record16

| Field | Required | Structural type |
|---|---|---|
| op | yes | "cubic-bezier" |
| start | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| segments | yes | array<Record17> |
| samplesPerSegment | yes | number |
| closed | yes | boolean |

## Record17

| Field | Required | Structural type |
|---|---|---|
| control1 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| control2 | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |
| end | yes | WorldCoordinateV1 / LocalCoordinateV1 / BodyCoordinateV1 |

## Record18

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

## Record19

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "traveling-wave" |
| phaseChannel | yes | string |
| cyclesAlongSpine | yes | number |
| amplitude | yes | array<Record20> |

## Record20

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number / Record4 / Record5 / Record6 / Record7 / Record8 / Record9 |

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
| signal | yes | Record23 / Record24 |

## Record23

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "sine" / "phase" |
| cyclesPerLoop | yes | number |
| phase | yes | number |

## Record24

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
| geometry | yes | Record12 / Record16 / Record26 |
| direction | yes | "forward" / "reverse" |
| drawOrder | yes | number |
| paintOrder | yes | number |
| repeat | no | Record27 |
| style | no | Partial |

## Record26

| Field | Required | Structural type |
|---|---|---|
| op | yes | "body-outline" |
| body | yes | string |
| samples | yes | number |

## Record27

| Field | Required | Structural type |
|---|---|---|
| count | yes | number |

## Partial

| Field | Required | Structural type |
|---|---|---|
| width | no | number |
| pressure | no | array<Record29> |
| taper | no | Record30 |
| wobble | no | number |
| opacity | no | number |
| color | no | string |

## Record29

| Field | Required | Structural type |
|---|---|---|
| t | yes | number |
| value | yes | number |

## Record30

| Field | Required | Structural type |
|---|---|---|
| start | yes | number |
| end | yes | number |

## FillV1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| styleRole | no | "outlinePrimary" / "bodyBase" / "accentPrimary" / "accentSecondary" / "detail" / "construction" / "highlight" / "shadow" |
| boundary | yes | Record12 / Record16 / Record26 |
| paintOrder | yes | number |
| color | yes | string |
| opacity | yes | number |
| fillRule | yes | "nonzero" / "evenodd" |
| reveal | yes | Record32 / Record33 |

## Record32

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "after-drawing" |

## Record33

| Field | Required | Structural type |
|---|---|---|
| kind | yes | "after-mark" |
| mark | yes | string |

Opaque contracts: none.
