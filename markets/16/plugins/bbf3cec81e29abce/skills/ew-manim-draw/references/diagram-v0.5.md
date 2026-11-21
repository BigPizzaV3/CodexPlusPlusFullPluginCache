# EW Diagram 0.5 executable contract

Use `scripts/diagram.py`, which dispatches by schema version. The new implementation is `guided.py`. Root: schema_version="0.5", title, optional subtitle, locale en/zh-TW/zh-CN, graph, sources, optional theme, story, optional export. No unknown keys. Geometry uses a 1920×1080 canvas. Diagram bounds must lie inside x=60..1860, y=205..925. Reserve the title and bottom caption bar. Card label 30 px, subtitle/badge 23 px, group/caption 28 px, title 48 px. Do not shrink text.

## Graph
- groups: `{id,label,parent?,bounds?,columns?,color?}`. Bounds `[x,y,width,height]`. Parent IDs must resolve; no hierarchy cycles. Top-level groups default to equal horizontal sections; direct node children default to a grid of up to 4 columns. For mixed nested groups + cards use explicit bounds to avoid collisions. Group header reserves 58 px; minimum inner padding 12 px. Max 12 groups.
- nodes: `{id,label,subtitle?,badge?,group?,bounds?,shape?,color?}`. Shape card/diamond (default card); group optional for external actors/devices. Max 40 nodes. A group and all its node descendants must contain their geometries.
- edges: `{id,from,to?,from_port?,to_port?,points?,direction?,label?,color?,kind?}`. Endpoints can be nodes or groups. Ports left/right/top/bottom (defaults right/left). Direction forward/both. Kind data/feedback/reference/control; does not by itself confer control authority. Max 100 edges. With `to` omitted/null, supply points beginning at the actual origin port and ending at an open endpoint; put the original branch label in label. No fake terminal node. Points are complete orthogonal routes, including both ports. Automatic visibility-grid routing avoids node interiors; supply explicit ports/points for ambiguous bus/feedback geometry. Crossings do not represent junctions.
- Colors are literal #RRGGBB only. IDs are ASCII letters followed by letters/digits/_/-, max64; globally unique. Strings are literal text.

## Sources and story
Every group/node/edge requires provenance in `sources:[{id,text,targets,status}]`; status confirmed or synthetic. Unconfirmed facts must be resolved before rendering. Text describes the exact source page, containment and arrow direction; coverage is not proof of completeness.

`story:{mode:"guided",trail:true,steps:[{id,text,targets,duration:3}]}`. Targets can be groups/nodes/edges. Entire diagram remains visible, geometry never moves. Active step gets bright border/path + traveling particles; previous targets remain moderately bright; inactive labels remain readable. Bottom bar shows step number/caption/progress. Guided sequence resets intentionally. Loop mode permits exactly one step. Total duration max90 seconds, max30 steps, frame budget720. Do not truncate; lower fps or split. Relationship-only sources require explanatory, not operational, captions.

`theme:{preset:"reference-dark"}` is the only preset implemented in this version. `export:{width:1920,height:1080,formats:["json","png","svg","html","gif"],fps:8}` supplies optional defaults. MP4/native PPTX/light theme/dashed path overlay are not implemented in 0.5 renderer; the active path uses luminous moving points with tapered trails.

## Commands and outputs
`python scripts/diagram.py example.json --font /absolute/NotoSansCJKtc-Regular.otf --out output`

Always emits diagram.json/layout.json/capability-report.json, plus requested formats. JSON-only validation emits diagram.json/report without layout. PNG is the fully lit overview; SVG is the editable vector scene; HTML adds the same timeline and geometry. GIF/HTML share deterministic step selection and path phase; browser font metrics still need checking. Use `--embed-font` only with a permitted licensed font. Fonts are not distributed with this skill. `--gif-fps 6` can reduce output size. HTML browser test status defaults to false until an actual host test is performed.

## Neon renderer 0.5.1
Keep schema 0.5 compatibility. reference-dark now uses deep navy, lightly tinted cards, two-radius geometry bloom, saturated role accents and a bright-core particle with tapered trailing points. Raster and HTML both include tails; their glow is implemented by Pillow and SVG/CSS respectively. Do not promise pixel equality between browsers and Pillow. Keep text outside glow processing and card interiors static. Use a shared 248-color GIF palette and disposal=1 delta frames. Default generation is 10fps unless export.fps or CLI overrides it. Inspect active-step samples and route clearance at group headings. Preserve longer source facts in step captions or a separate detailed view rather than shrinking type.
