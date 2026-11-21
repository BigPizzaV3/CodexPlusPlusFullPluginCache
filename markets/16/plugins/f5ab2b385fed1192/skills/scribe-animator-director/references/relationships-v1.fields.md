# Generated ObjectDTO structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

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
| shadow | no | Record7 |
| glow | no | Record8 |

## Record7

| Field | Required | Structural type |
|---|---|---|
| color | yes | string |
| blur | yes | number |
| offsetX | yes | number |
| offsetY | yes | number |
| opacity | yes | number |

## Record8

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
| runOverrides | no | array<Record11> |

## KineticTextTransform

| Field | Required | Structural type |
|---|---|---|
| offsetX | yes | number |
| offsetY | yes | number |
| scale | yes | number |
| rotation | yes | number |
| opacity | yes | number |

## Record11

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

Opaque contracts: ObjectDTO.props.*.
