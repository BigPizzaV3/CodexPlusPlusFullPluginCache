# Generated ProceduralDrawingScoreV1 structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

## ProceduralDrawingScoreV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-drawing-score/1" |
| parts | yes | array<Record1> |
| layers | yes | array<Record2> |
| steps | yes | array<Record6> |
| marks | yes | array<Record7> |

## Record1

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| label | no | string |
| dependsOn | no | array<string> |

## Record2

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| lifecycle | yes | Record3 / Record4 / Record5 |

## Record3

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "keep" |

## Record4

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "ghost" |
| retireAfterStepId | yes | string |
| finalOpacity | yes | number |
| fadeFraction | yes | number |

## Record5

| Field | Required | Structural type |
|---|---|---|
| finalBehavior | yes | "hide" |
| retireAfterStepId | yes | string |
| fadeFraction | yes | number |

## Record6

| Field | Required | Structural type |
|---|---|---|
| id | yes | string |
| phase | yes | "construction" / "placement" / "contours" / "details" / "accents" |
| markIds | yes | array<string> |

## Record7

| Field | Required | Structural type |
|---|---|---|
| markId | yes | string |
| partId | yes | string |
| layerId | yes | string |
| kind | yes | "detail" / "guide" / "contour" / "accent" |
| timingCost | no | number |
| after | no | array<string> |

Opaque contracts: none.
