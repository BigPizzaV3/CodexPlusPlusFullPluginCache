# Representation strategy contract

For an important visible or technically constrained element, ask first what the user must perceive, which part must actually respond in realtime, and where the required visual truth can be produced most reliably. Do not begin with the coding method.

This is the canonical **perceptual equivalence / representation economy** gate for design, media, experience planning and implementation. Choose the simplest sufficient and validated representation within the applicable solution class that preserves approved perception, Project Truth, interaction, necessary spatial truth, performance and maintainability. Simpler is preferable only when those requirements survive; technical sophistication is not evidence of quality. Use the existing [decision authority and method-closure policy](decision-authority-model.md): a recommendation does not authorize a medium, tool, architecture or design change, and a closed method is not reopened for speculative simplification. Bounded builder calibration may not change the target or resolve missing art direction.

## Decision record

Create this record only when representation choice is material; ordinary DOM/CSS/image work does not need ceremonial fields.

For a trivial CTA hover, an already-proven unchanged recipe or an applicable `METHOD_CLOSED` decision, keep the normal task and its applicable tests; do not compare every medium, produce an empty record, invoke another skill or demand a new approval. Reopen only under the canonical evidenced triggers. Load only the relevant target, current authority, method decision, candidate/proof and constraints—not all project history.

```text
TARGET
IMPORTANCE
QUALITY_LEVEL
PERCEPTUAL_OBSERVABLES
TARGET_PERCEPTION: SEE / FEEL / UNDERSTAND
REQUIRED_DEGREES_OF_FREEDOM
TRUTH_REQUIREMENT
REQUIRED_VIEWPOINTS
SCREEN_SPACE / STATES
CHANGE_TYPE: STATIC | DEFINED_MOTION | USER_CONTROLLED | DYNAMIC_DATA
REALTIME_NECESSITY
CANDIDATE_REPRESENTATIONS
METHOD_LOCK: applicable scoped view from the decision-authority model, or OPEN decision reference
AUTHORING_SOURCE
PUBLISHING_OR_DELIVERY_TARGET
RUNTIME_REPRESENTATION
RECOMMENDED_REPRESENTATION / WHY
REALTIME_VS_PRECOMPUTED
DOM_RESPONSIBILITY
MATERIAL_REPRESENTATION
MOTION_PURPOSE
STATE_OR_PROGRESS_ARCHITECTURE
TECHNICAL_LIMITATIONS
ACCESSIBILITY_AND_SEMANTICS
PERFORMANCE_COST
AUTHORING_COST / MAINTENANCE_COST / RUNTIME_COMPLEXITY / ASSET_WEIGHT
FALLBACK
EXPERIMENTAL_DEPENDENCIES
PROOF_METHOD
ACCEPTANCE
LEAD_ROLE
DECISION_CLASS
STOP_CONDITION
ESCALATION_TRIGGER
```

Treat `AUTHORING → PUBLISHING / DELIVERY → RUNTIME → PERCEPTUAL OUTPUT` as distinct layers. A high-resolution Source Master may produce optimized geometry, baked detail, compressed textures, responsive images, prerenders or other delivery assets; the Source Master is not automatically a runtime asset. Document this lineage only when it materially affects implementation, reproducibility or quality.

The record is a concise view of existing project decisions, not a second specification or compulsory file. Omit genuinely irrelevant fields with a short reason; preserve material unknowns as unknowns, not N/A. Return status, recommendation and rationale, scoped proof/acceptance and exact stop or escalation condition. Reuse source IDs rather than duplicating authority.

## Target, freedom and truth before technique

Define what the viewer must see, feel and understand: for example depth, weight, transparency, thickness, spatial continuity, product presence, atmosphere, living movement or distortion. Do not invent the intended perception from a tool preference.

For each material element identify which degrees of freedom are fixed, predefined, data-dependent or user-controlled: camera position/angle, object position/deformation, lighting, material response, occlusion, spatial depth, pointer, scroll, time, viewport and content state. Compute only what the user can perceive or control, while retaining semantic, accessibility and other project requirements. Fixed camera motion can be precomputed; responsive views or new content may invalidate that equivalence. A two-state day/night hero does not alone justify realtime lighting.

Classify truth per observable, not for the entire scene:

- **REAL / AUTHORITATIVE:** actual product geometry, identity, dimensions, important spatial relationships or other approved physical/data truth. Approximation may not misrepresent these.
- **PERCEPTUAL APPROXIMATION ALLOWED:** a cue may be simulated only within authorized views/states and approved equivalence bounds, without changing authoritative facts.
- **PURELY ATMOSPHERIC:** no authoritative physical claim; still preserve intended perception, rights, safety, accessibility and approved direction.

Semantic truth—copy, pricing, navigation, forms, products and actions—remains authoritative regardless of the visual class. A glass distortion may be simulated; an authoritative product silhouette cannot be replaced by a plausible invention. Missing or conflicting truth/target authority blocks dependent production; it is not permission for the builder to choose.

## Causal abstraction and backstage structure

`MECHANISM != MOTIF`. Understanding how a natural, physical, structural or procedural system forms or behaves does not require exposing its generator as literal visual language. When research informs an actual design translation, identify which geometry, relationship, hierarchy, timing, response, constraint, distribution or behavior must be preserved and what may be abstracted away. Use `MECHANISM → ESSENTIAL RELATIONSHIP → DESIGN ABSTRACTION → REPRESENTATION`, not automatic literal imitation. Prefer the useful visible consequence over the visible generator unless understanding the generator is itself an approved educational, explanatory or interaction purpose.

Distinguish the user-observable frontstage from backstage structure that materially produces or supports it. Hidden authoring, semantic, state, diagnostic or production structure may exceed the delivery representation when it measurably improves approved quality, behavior, reliability, performance, maintainability, editability, reproducibility, accessibility or plausible capacity. Invisible complexity must earn its existence: if removing it makes no material outcome worse, simplify. Do not expose backstage complexity unnecessarily or convert plausible future capacity into speculative features.

These are abstract representation rules, not domain science or permission to redesign. They do not globalize physical formulas, biology, anatomy, materials, shaders, topology or project-specific formation knowledge. A causal insight affecting an applicable `METHOD_CLOSED` target remains a proposal for the authorized decision owner unless it fits the existing scoped method and calibration authority.

## Representation choice

When the method is `OPEN`, compare only credible procedural or authored geometry, baked maps, normal or height information, sprites, planes or impostors, prerenders, video, DOM, SVG, CSS, realtime deformation or hybrid representations that could materially change the decision. Choose the smallest reliable representation that meets the approved observable, interaction, fidelity, runtime, accessibility, asset, maintenance and performance bounds. When an applicable method is `METHOD_CLOSED`, treat alternatives as historical unless a canonical reopen trigger is evidenced; execute and calibrate within the closed method instead of proving again that a weaker or merely different representation might work.

Use this option map, not an escalation ladder or ten-option checklist. Compare only credible alternatives that could change the decision; if authoritative authored 3D is clearly required, go directly there and explain the requirement.

| Family | Consider when / limiting question |
|---|---|
| A — DOM / CSS / SVG | Native layout, semantic UI, vectors or local effects; can these preserve the cue and interaction? |
| B — Layered 2D / masks / blend / filters | Composited depth or surface cues in bounded views; will occlusion remain credible? |
| C — GPU 2D / Canvas / Pixi / shader plane | Media displacement and layered effects needing GPU work; GPU rendering does not imply a 3D scene. |
| D — Video / image sequence / prerender | Fixed cinematic views/states; check scrub/input latency, decoding, bandwidth and responsive crop. |
| E — Depth / normal map / 2.5D | Limited parallax or material response; what happens when a new side or disoccluded region becomes visible? |
| F — Simple realtime 3D | Genuine spatial interaction, occlusion or variable views with simple forms. |
| G — Blender-authored 3D / GLB or approved equivalent | Specific true shape, authored surface structure, rigging or deformation-ready topology; authoring format and runtime export differ. |
| H — Procedural shader / WebGL / TSL / WebGPU | Required procedural or rendering behavior genuinely benefits; verify actual target support, APIs and fallback before commitment. |
| I — Gaussian splat / captured spatial media | Captured spatial appearance is appropriate; verify permitted capture, fidelity, new-view limits, editing, weight and runtime support. |
| J — Hybrid | Allocate each observable to a justified medium with explicit state, occlusion and semantic ownership. |

- Author physical or visual truth offline when offline work produces the approved result more reliably or cheaply.
- Realtime must earn its cost through user interaction, continuous state variation, viewpoint dependence, materially useful live lighting or reflection, responsive spatial composition, dynamic data/state or another evidenced perceptual need.
- Defined cinematic motion may be authored, baked, curve-driven or deterministic. User-controlled motion must respond to current user state in runtime.
- Detail cost follows screen-space value. Do not build expensive geometry or textures for detail that contributes only a few pixels when a cheaper representation is perceptually equivalent within approved views.
- An invisible perceptual cheat is legitimate when product behavior, accessibility, content truth and approved quality remain intact and the simplification does not misrepresent business or data claims.
- In web experiences, keep text, typography, forms, links, semantic structure, accessible interaction, dynamic information and selectable content browser-native unless a proven requirement outweighs those properties. Use realtime layers for spatial effects or interaction that materially benefits from them.

Static complexity should be precomputed when realtime calculation adds no perceptual value and precomputation meets the other bounds. Consider prepared lighting, shadows, AO, caustics, reflection information, fog/atmosphere, surface detail, depth/normals and fixed cinematic transitions. Evaluate invalidation when view, light, geometry or content changes; baked information must not contradict dynamic state. A smaller runtime may carry a larger asset/download cost—compare the whole delivery, not just shader cost.

Complex world does not require complex UI. A signature object, prepared atmosphere, guided journey and direct navigation can coexist without duplicating navigation inside GPU layers. Do not introduce proprietary infrastructure unless repeated real limitations justify its authoring and maintenance cost. These are general principles, not claims about any reference site's implementation or instructions to copy its aesthetics.

Do not infer a Blender-, GLB-, WebGL-, shader-, offline-, realtime- or framework-first rule. These are possible implementations, not policy.

## Conditional material and surface analysis

For a material-critical observable, treat **material as behavior, not color**. Describe relevant luminance, roughness/microfacet response, reflection/Fresnel/edges, thickness, transmission/absorption/refraction, normals/microstructure/texture scale, environment/light response, internal depth, anisotropy, density and diffusion. Not every material needs every field or a physically based renderer. Bind each required cue to authoritative physical behavior or permitted perceptual approximation; do not invent calibrated parameter values.

Separate the perceptual problem before choosing the technique:

| Signal | Question / responsibility |
|---|---|
| Outer form | Which silhouette/geometry is real truth? |
| Surface | Which roughness, reflection and microfacet cues carry the appearance? |
| Thickness | Which edge, absorption or transmission cues reveal thickness? |
| Internal structure | Which occlusion, depth, contrast, focus and parallax cues reveal interior structure? |
| Light | Which environmental response must change with view/state? |
| Motion | What changing or view-dependent information is revealed? |
| Atmosphere | What context supports—not substitutes for—the object/material? |

Assign a plausible representation and a focused proof to the unresolved signal. Do not solve every failure by changing one shader parameter. Use the existing causal failure route; preserve MIXED/INCONCLUSIVE when evidence is insufficient. Material-response quality cannot be certified from a list of physical parameters.

## Conditional motion, shared state and transitions

For material motion define trigger, object, direction, amplitude, duration, physics/easing, purpose and end state from approved targets/bounds or controlled calibration. Ask what information it reveals: space, hierarchy, material, state or narrative continuity. No random cinematic camera or effect just because it is technically possible. Flag purposeless motion for removal within authority; do not silently remove approved identity.

If camera, object, typography, media, material, transition and lighting must stay synchronized, evaluate one scoped shared state/progress owner and explicit mappings rather than independent effects. Define relevant seeking/reverse/interrupt, viewport/content change, reduced-motion and reset behavior. Use existing state machinery where adequate; a coordinated scene is not justification for a new global framework.

Treat a transition as its own representation choice: DOM View Transition, mask, clip-path, SVG, displacement, video/sequence, fog, occlusion, shader, camera or physical crossing may preserve continuity. Choose the simplest suitable option and verify current support before implementation. Do not force a camera move or shader when a mask or authored sequence preserves the same required result.

## Cost, fallback and escalation

Before material production rate performance risk, authoring cost, maintenance cost, runtime complexity and asset weight LOW / MEDIUM / HIGH with rationale, context and unknowns. These are planning judgments, not measured benchmarks; do not invent exact budgets. Use project-approved targets and measure the proof.

Consider only relevant controls: adaptive DPR, lazy loading, visibility-based playback, texture compression, baked information, LOD, culling, mobile fallback, reduced motion and streaming. Performance begins at representation selection, not late optimization. Preserve continuity and primary interaction when suspending offscreen media.

Where advanced visual layers may be unavailable, the fallback must preserve content, primary action and the approved core perception. Specify applicable GPU/context-loss, motion-disabled, media-failure and mobile states. If a simpler fallback cannot preserve required truth/perception, expose the trade-off and obtain authority; do not declare a degraded substitute equivalent or make important content reachable only through the failed layer.

Escalate complexity only when a required freedom, approved perceptual observable or Project Truth cannot be retained by the simpler candidate; cost/performance violations may instead require simplification or a reviewed trade-off. Limited meaningful parallax can justify 2.5D; new side surfaces, free camera, dynamic occlusion or spatial interaction can justify realtime 3D; specific form or deformation/surface architecture can justify authored assets. WebGPU requires an evidenced compute/material/rendering benefit and verified constraints, not novelty. Newer is not better; more complex is not more premium.

## Proof and failure routing

For an open method decision, build the smallest proof that can honestly falsify the chosen representation in the required view, screen size, state, motion and target-device conditions. Approve a production strategy only from real evidence; otherwise mark it `PROPOSED` or `CALIBRATION_REQUIRED`. For `METHOD_CLOSED`, use proofs only for remaining project-specific implementation, integration or calibration unknowns inside that method; do not use them to restart cross-method exploration without a valid reopen trigger.

Name the single unresolved design question and the cheapest valid proof: Figma, still composition, authored image, HTML/CSS, SVG, GPU 2D, simple shader, browser prototype, Blender blockout/render, GLB or full runtime proof as justified. Prove silhouette before costly material production; prove material without building the whole site. A still can answer composition, not dynamic interaction or runtime cost. Proof the question, not the entire product. Reuse the existing [visual checkpoints](visual-checkpoint-policy.md) and [perceptual gates](perceptual-quality-gates.md) for actual-scale, real-medium evidence and independent acceptance; do not create a second review process.

Real output outranks an implementation report. Technical PASS is not design PASS, and the builder cannot independently ratify their own required material visual gate. Preserve anti-generic authorship criteria: composition, proportion, hierarchy, material/surface/light, type, object scale, space, purposeful motion and content relationships—not technical spectacle or decorative defaults. Unavailable proof/reviewer evidence remains unverified, not implied approval.

When output fails, classify the causal layer before tuning the most salient parameter. Allow `MIXED` and `INCONCLUSIVE`; never invent causality. Apply the [faithful-implementation and failure-attribution gate](decision-authority-model.md) before rejecting a closed method. Repeated calibration failure or exhausted bounds routes to diagnosis/review; it does not itself prove method failure. Use `REPRESENTATION_FAIL` only when evidence establishes that the representation cannot meet required acceptance; its next safe action is `REPRESENTATION_REVIEW`. That review preserves the lock until a valid scoped reopen trigger and required authority are established before comparing media or production locations. `REPRESENTATION_REVIEW` is an action/gate, not a competing outcome.

Experimental browser or renderer paths may be researched, prototyped and kept architecture-compatible under `EXPERIMENTAL_FUTURE_PATH`. They are not Production Authority until current support, API stability, runtime behavior and fallback are verified.

Temporary diagnostic changes must be isolated, reversible, restored and restore-verified before their evidence is accepted.
