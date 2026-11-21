# Generated ProceduralPaletteV1 structural contract

Read alongside [contract scope](contract-scope.md). JSON Schema descriptions carry field comments. This is the complete reachable structural type, including explicitly opaque data; it does not certify import support for every DTO member.

## ProceduralPaletteV1

| Field | Required | Structural type |
|---|---|---|
| schema | yes | "scribe.procedural-palette/1" |
| baseInk | no | ProceduralPaletteInkV1 |
| roles | yes | Readonly |

## ProceduralPaletteInkV1

| Field | Required | Structural type |
|---|---|---|
| color | no | string |
| width | no | number |
| opacity | no | number |
| wobble | no | number |

## Readonly

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
| fill | no | Record4 |

## Record4

| Field | Required | Structural type |
|---|---|---|
| color | no | string |
| opacity | no | number |

Opaque contracts: none.
