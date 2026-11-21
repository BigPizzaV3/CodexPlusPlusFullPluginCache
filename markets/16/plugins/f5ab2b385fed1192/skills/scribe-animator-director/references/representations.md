# Editable representation choices

| Unit | Choice and limits |
|---|---|
| Text | `text` with `props.text`, explicit font size, fill, width/height and fixed/auto-content box policy. A slot default must match authored text. |
| Simple panel/ellipse | `shape` DTO with `props.shapeType`, fill/stroke/strokeWidth. Current apply converts common shapes into inline SVG runtime leaves; do not promise a native shape runtime identity after AI import. |
| Photo/screenshot | `image` using a verified asset or intentional self-contained source. External assets need permissions, network and live resolution; offline validation never fetches them. |
| Vector visual | `svg` with `props.svg`; keep viewBox/bounds tight. No script/event handler, foreignObject or external resource. Runtime SVG geometry budgeting is not a sanitizer certification. |
| Precise drawing | `svgPath` / path-backed drawing with `props.paths`; paths carry authored IDs and path data. Use one independently editable logical unit per object. See opaque props limits in contract scope. |
| Clean connector | `smartLine`/`smartArrow` and verified smart-stroke props; attachment metadata is top-level `connector`. Prefer clean round-capped shafts with a proportionate head. No Unicode arrow as diagram geometry. |
| Repeatable drawing with motion | `procedural` with versioned asset/recipe/material/seed/parameters and optional playback/score/palette/component source. No cached/derived runtime state. |
| Group | Logical native grouping only when supported by the live tools/import route. Nested `props.children` is opaque DTO data; do not assume nesting equals shared identity. Verify selection and independent editing. |
| Video | AI JSON currently rejects `video` even though the DTO union includes it. Use the live user-mediated local-video capability. `videoEmbed` is a separate supported DTO type with opaque props; do not invent media persistence. |

Native text, object transforms and authored recipe parameters remain editable. A coherent SVG illustration can be one selectable/movable unit; split parts when independent replacement or motion matters. Do not flatten text/cards/connectors into an opaque full-scene image or SVG merely to reduce counts. Slots expose intentional replacements; ordinary objects remain editable without slots.

For catalog assets, verify actual IDs/paths with live discovery. `requiredAssets` records actual dependencies. Inline text/geometry examples here have no external assets. Never claim URL checks or asset resolution based solely on a schema/validator result.
