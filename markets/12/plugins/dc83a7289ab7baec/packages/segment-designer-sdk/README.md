# segment-designer-sdk

TypeScript SDK for deterministic authoring of eSNG dynamic-segment **UI-mode** JSON. The agent surface is limited to eight methods: `getModel`, `find`, `addCard`, `updateCard`, `addCondition`, `updateCondition`, `remove`, and `finish`.

The complete agent execution contract, method signatures, intent unions, aggregate-family behavior, update semantics, examples, end-to-end MCP catalog and runner procedure, validation errors, recovery guidance, and finish boundary are documented in [`SDK_API_REFERENCE.md`](../../skills/segment-designer/references/client/SDK_API_REFERENCE.md). That skill reference is authoritative for generated agent code; this README is only a package overview.

The SDK owns card-formula compilation and copy behavior, all eight aggregate families, automatic system criteria/defaults, contextual event properties, period and value normalization, selection-dependent resets, frontend coexistence/feature rules, and parameter-list derivation. The production runner supplies the complete raw definition endpoint response, signed authoritative UI context, and `segment-output.schema.json`; generated mutation code supplies none of those inputs.

```ts
import {createSegmentSdk} from "segment-designer-sdk";

const sdk = createSegmentSdk({definitions, outputSchema, uiContext: {timeZone: "Europe/London"}});
const cardResult = sdk.addCard("include", {
  firstCondition: {
    kind: "field",
    definition: {columnId: "EMAIL"},
    operator: "CONTAINS",
    value: "@example.com",
  },
});
if (!cardResult.ok) throw new Error(cardResult.issues[0].message);

const result = await sdk.finish();
```

`addCondition` has the same public signature for aggregate and non-aggregate conditions. A `CardRef` accepts a `ConditionIntent`; an `AggregateRef` accepts a `CriterionIntent`. `updateCondition` also handles aggregate selection/period/occurrence changes and simple↔aggregate replacement. Card copying is `addCard(branch, {mode: "copy", copyFrom})`, not a ninth method.

`finish()` is the mandatory frontend gate: it derives used parameters, validates the output schema, complete definitions, UI-reachable aggregate states, value/control shapes, and eSNG frontend rules, then seals the session. Mutations are atomic, and `getModel()`/`find()` return clones. In particular, occurrence shorthand becomes the UI's count criterion (`> 0` / `= 0`) and never silently changes aggregate negation.

Pass `uiContext.groupType: "PARAMETRIC"` only for parametric groups. Parameters are creation-only and limited to the frontend's text, text-area, integer, float, and date controls; their emitted parameter types are those frontend control types. `uiContext.enabledFeatures` contains resolved UI decisions, and `requireResolvedFeatures: true` makes relevant missing decisions a finish error.

The mutation API deliberately does **not** create DB-mode `aggregate.rule` or `originOperator`, call backend validation, or persist a segment. The package exposes `hydrateBackendSegmentModel()` solely for the trusted update runner to convert supported readback fields into UI mode before creating a mutation session; generated code must not call it. Persistence and UI-to-DB conversion remain service/MCP responsibilities after the SDK returns approved UI-mode JSON. Runtime autocomplete IDs not enumerated by the definition payload remain an external lookup/backend-validation boundary.
