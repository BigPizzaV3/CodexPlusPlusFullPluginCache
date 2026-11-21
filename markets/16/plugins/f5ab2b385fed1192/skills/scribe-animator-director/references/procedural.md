# Procedural authoring without source inspection

Use discovered procedural/component tools for semantic reusable subjects when available. Get the current schema/catalog and immutable pins before creating; never guess component use/version/revision or convert internal mark IDs into scene object IDs. Otherwise author a bounded **data recipe** with the bundled contracts and offline workflow.

Portable object: `{id,type:"procedural",x,y,width,height,props:{proceduralVersion:1,asset,playback?,drawingScore?,proceduralPalette?,proceduralComponentSource?}}`. Host transform/bounds are finite and bounded. The app's project ingress caps procedural objects at 64 and canonical aggregate assets/score/palette/component-source at 4 MiB, including retained workspace objects during apply. Offline validates only input; it cannot know the destination's retained budget.

Host scaling uses semantic geometry bounds at time zero for the entire playback. An axis with zero span is floored to one logical unit; later deformation is not clipped to the reference box. Avoid an initially flat axis that later expands dramatically. Author a meaningful reference pose covering the motion range, allow room for material ink beyond centerlines, and inspect opening/quarter/three-quarter phases and extrema. The ribbon example starts at maximum rise and remaps its sine signal to [0, 1]; this repairs its authored geometry without changing renderer behavior.

| Contract | Resource |
|---|---|
| Host props: version/asset/playback/score/palette/component source, with explicit flexible host bag | [schema](../schemas/procedural-host-props-v1.schema.json), [fields](procedural-host-props-v1.fields.md) |
| Asset: version/schema/content digest, recipe, optional toneRegions, uint32 seed, RNG, parameter values, runtime revision, material/provenance | [schema](../schemas/procedural-asset-v1.schema.json), [fields](procedural-asset-v1.fields.md) |
| Recipe: number parameters, affine/body frames, attachments, motion channels, marks/fills; recursive scalar/coordinate/geometry vocabulary | [schema](../schemas/procedural-recipe-v1.schema.json), [fields](procedural-recipe-v1.fields.md) |
| Drawing Score: parts/layers/steps/mark memberships and lifecycle | [schema](../schemas/procedural-score-v1.schema.json), [fields](procedural-score-v1.fields.md) |
| Palette: semantic roles and styles | [schema](../schemas/procedural-palette-v1.schema.json), [fields](procedural-palette-v1.fields.md) |
| Component source: inert provenance pin and effective params, not a shared managed identity | [schema](../schemas/procedural-component-source-v1.schema.json), [fields](procedural-component-source-v1.fields.md) |
| Exact input/runtime/material budgets | [limits](limits.json) |

Scalar operations are the closed vocabulary parameter/random/motion/instance-index, add/subtract/multiply/divide and sin/cos. Geometry is polyline, cubic-bezier or body-outline. Recipe validation checks IDs, frame/attachment/parameter/channel/fill-mark references, bounds and budgets; runtime uses its fixed evaluator, never arbitrary code. `source` provenance is inert attribution and is not fetched. RecipeRevision is an actual SHA-256 of canonical validated recipe JSON, not an ID you invent.

To hash a changed recipe offline, run `node <installed-skill>/scripts/recipe-revision.mjs <recipe.json>`. It uses the bundled production `createProceduralContracts().recipeRevision`; update asset.recipeRevision only when authoring a genuinely changed recipe. Never repin frozen historical evidence. Then run the full envelope validator. A supplied asset's digest mismatch, unknown operation/code field, unsupported runtime revision, unknown/oversized parameters, invalid playback, unresolved score marks or persisted derived state must fail.

Do not persist paths/guides/LUT/runtime/cache/instance/compiledScore/resolved palette or generated detail outputs. Native object transforms and playback/drawing score remain separate editable controls. The package checks the current production ingress, which validates recipe and score references; successful validation alone does not certify every evaluated motion frame, host rendering or performance. Run the later browser acceptance checklist.
