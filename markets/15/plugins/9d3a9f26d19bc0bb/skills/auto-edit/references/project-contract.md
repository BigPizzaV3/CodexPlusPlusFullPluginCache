# Project and CLI contract

Resolve `wandeo` to the bundled platform launcher. `--project` always names the editable working directory. It contains a manifest with assets and sources, `project.json`, `director-state.json`, immutable timeline revisions, evidence and outputs. Keep these files together for portability.

Run `project init`, then `media import --input <path>`. Use returned `asset.id` values in the timeline. Do not invent IDs or write absolute `assetPath` fields. The compiler verifies media hashes and resolves asset IDs internally. A timeline's `projectId` must match the manifest's ID.

The renderer preserves OOVideo's VideoProject 1.1.0 contract. Every scene has an absolute output `range`. `sourceRange` refers to the source asset's seconds; source rate can change the playback speed. Captions use absolute film seconds and normalized bounding boxes. Motion layer timeline times are layer-relative unless `timeBase: "film"` is explicit.

A scene may add a `spatial` object without changing the 1.1.0 schema. Use `backend: "three"` for imported `model3d` asset IDs or `backend: "anatomy"` for deterministic explanatory parts and groups. Three.js models use exactly one of `assetId`, procedural preset or `instanceOf` per model. Model ranges default to the scene range; camera and anatomy keyframes are seconds relative to the scene start. Keep imported model dependencies inside the project and record their source URL, version and license in the manifest. For a reusable authored Anatomy object, run `anatomy import --input <figure.anatomy.json>`, add `anatomyFigures: {"object": {"assetId": "IMPORTED_ASSET_ID"}}` at project level, and set each relevant scene's `spatial.anatomy.figureId` to `"object"`. The binder loads and verifies that asset; do not write `authoredFigure` or an absolute file path into the timeline. Use the [authored figure contract](../../anatomy-explainer/references/authored-figure.md) for model time, view keyframes and part focus. `nativeExample: "turning-dial"` remains a particular upstream reference example; it is not a substitute for a subject-specific object. Timeline progress is disabled by default; set `presentation.showTimelineProgress` only when an explicit progress indicator is part of the brief.

The following procedural example demonstrates the legacy spatial syntax for an abstract assembly. For a science explainer, use the reusable authored figure route above.

```json
"spatial": {
  "camera": {"projection":"perspective","position":[3,2,5],"target":[0,0,0],"near":0.01,"far":100},
  "lights":[{"id":"key","type":"directional","color":"#ffffff","intensity":2,"position":[3,4,5]}],
  "models":[
    {"id":"assembly","procedural":{"preset":"product-assembly","parameters":{"count":4}},"position":[0,0,0],"material":{"color":"#5eead4"},"animations":[{"id":"explode","track":"transform","preset":"explode","range":{"start":1,"end":3},"from":{"position":[0,0,0]},"to":{"position":[0,0,1]}}]}
  ],
  "annotations":[{"id":"label","text":"可观察的内部关系","anchor":[0,1,0],"range":{"start":0,"end":4},"color":"#ffffff"}]
}
```

```json
{
  "schemaVersion":"1.1.0",
  "projectId":"MANIFEST_ID",
  "width":1920,"height":1080,"fps":30,"durationSeconds":4,
  "scenes":[{
    "id":"proof","range":{"start":0,"end":4},
    "purpose":"Show the real product result","message":"",
    "visualLayers":[{
      "id":"recording","assetId":"IMPORTED_ASSET_ID","source":"asset",
      "sourceRange":{"start":1,"end":5},
      "zIndex":10,"opacity":1,"semanticTags":["product-evidence"]
    }],
    "captions":[{
      "id":"caption","range":{"start":0.3,"end":3.8},"text":"清晰呈现真实操作结果",
      "bbox":{"x":0.1,"y":0.85,"width":0.8,"height":0.1},
      "maxCharsPerLine":24,
      "style":{"fontFamily":"Noto Sans SC","fontSize":"56px","color":"white","background":"rgba(0,0,0,.8)"}
    }],
    "motionLayers":[{
      "id":"title","range":{"start":0,"end":4},"zIndex":20,
      "nodes":[{"id":"label","tag":"div","text":"真实产品演示","style":{"position":"absolute","top":"48px","left":"64px","fontFamily":"Noto Sans SC","fontSize":"48px","color":"white"}}],
      "timeline":[{"id":"title-in","method":"fromTo","targetIds":["label"],"atSeconds":0.1,"durationSeconds":0.6,"easing":"power2.out","from":{"style":{"opacity":0,"y":24}},"to":{"style":{"opacity":1,"y":0}}}]
    }],
    "protectedRegions":[],"claimIds":[]
  }]
}
```

Replace example IDs, source ranges, dimensions, duration and copy with observed values. This is a structural example, not a required treatment. `project validate` is authoritative for supported fields. `project capabilities` describes motion, source media, cameras and transitions. `project recipes --query <intent>` returns bounded matching vocabulary and parameters.

Optional per-scene audio: `voiceover` has `id`, `assetId`, `range`, `text`, `semanticTags`, optional `sourceStartSeconds/gainDb`; `music` has `id`, `assetId`, `range`, `gainDb`, optional `sourceStartSeconds/duckUnderVoiceDb`; sound effects also require their purpose and synchronization fields. Source video audio is preserved unless its `audioGainDb` mutes it.

For automatic captions, transcribe an audio-bearing asset and set top-level `autoCaptions` with a normalized `bbox` and optional style. Scenes with no authored captions use the bound voiceover transcript or first transcribed visual asset, adjusted to source trim/rate. Check synchronization in the render.

```text
wandeo project validate --project <work>
wandeo render preview --project <work> --start 0 --end 4
wandeo review --project <work> --times 0.1,1,2,3.8
wandeo render final --project <work>
```

Visual/backend upgrade requests use the scoped `director-state.json.revisionRequest` baseline described in [render review](render-review.md). Export results and frozen contexts contain `sourceUsage` and `spatialRuntime.observed`; these distinguish real runtime use from pre-rendered source footage.
