# Direction and evidence

Adapted from OOVideo/Recordly's directing guidance; source attribution and license are retained at the plugin root.

Start from the communication goal, audience, the strongest attributable evidence, and the tension or progression that belongs to the product. Compare genuinely different directions when useful, then choose a coherent visual grammar. A focused revision preserves that grammar unless the diagnosed defect requires a wider change.

Research assertions, implemented code, observed runtime behavior and user-provided facts are different evidence. Keep references to source versions, file/line locations, assets and recording times. Generated or illustrative graphics can explain a concept but cannot prove product behavior. A camera move over a screenshot does not demonstrate the product's animation.

Select cuts from meaningful state changes. Keep enough context before the action and enough visible response afterward to preserve causality. Waiting and repetition can be removed or compressed; meaningful processing may need to remain. Use actual frame inspection and speech timing when choosing ranges.

Compose for attention and legibility. Footage, contextual type, captions, pointers and graphics have different jobs. Protect controls and visible outcomes from overlays and cropping. Choose full-frame footage, paired copy, crops, magnification, spatial layouts and transitions when they serve the current evidence. Animation should have a designed progression and deliberate holds.

Treat motion, typography and sound as a coherent system. Coordinate position, scale, opacity and easing; maintain enough stillness to read. Preserve the source audio needed to understand a result. Keep music gains and narration intelligibility intentional.

Before a revision, write its affected objects/range, observed problem, concrete change and expected observable difference into director state. Preserve useful decisions across turns rather than repeating settled research or generating arbitrary alternatives.

## Choose a treatment for the actual goal

- Product promotion: lead with a useful outcome, establish the product identity, demonstrate the strongest benefits, then give a clear next step. Give the strongest proof more screen time than a repeated title card.
- Product demonstration: keep the initial state, action and visible result understandable. Show the relevant control at a readable size; frame the result when it changes. Do not describe a capability as demonstrated if only its menu or empty state was recorded.
- Tutorial: preserve order, labels and enough time to follow each operation. Keep intentional pauses for reading or processing. Establish location before moving into a detail.
- Science and how-it-works explanation: prefer [Anatomy explainer](../../anatomy-explainer/SKILL.md). Research the mechanism, build one coherent object and a shared state model, then establish the whole before following a cause into a readable detail. Reuse the same figure across shots; fade surrounding assemblies while preserving enough context to locate the subject. Derived readouts and movement come from the same state. Identify illustrative simplifications and distinguish them from verified measurements.

These are alternatives, not required structures. Follow the user's references and desired style. Decide where footage should fill the frame and where explanatory type is useful. Several adjacent shots with the same layout and entrance timing deserve inspection, but repetition may be a deliberate system.

## Shot plans in director-state.json

For new work, add plans for shots whose message needs recorded evidence. A title or abstract bridge can use an empty `requiredStages` list. Old projects without `shots` remain valid. A plan is not evidence until actual source frames have been inspected.

```json
{
  "goal": "Explain how the product turns a selected input into a result",
  "qualityProfile": {"viewingWidth":960,"minCaptionPixels":18,"maxUpscale":1.5},
  "shots": [{
    "sceneId":"real-proof",
    "intent":"Show that running the action changes the result",
    "viewerFocus":"Run button, then the completed result",
    "requiredStages":["action","result"],
    "evidence":[
      {"assetId":"IMPORTED_ASSET_ID","sourceRange":{"start":1,"end":1.4},"stage":"action","observation":"The control is clicked in these inspected frames","verified":true},
      {"assetId":"IMPORTED_ASSET_ID","sourceRange":{"start":1.8,"end":2.6},"stage":"result","observation":"The expected result is visible in these inspected frames","verified":true}
    ],
    "acceptance":["The button label is readable","The result change is shown after the click"]
  }]
}
```

Replace all example IDs, observations and times with actual evidence. Evidence times are source seconds, and must be included in that scene's selected clip. `verified` records the director's visual observation; the CLI checks references and coverage, not semantic truth. `project validate` reports missing required stages, uninspected evidence and evidence excluded by the edit.

Use `qualityProfile.viewingWidth` for the intended playback size; a phone-focused film may need a smaller value and larger type. `minCaptionPixels` and `maxUpscale` are adjustable warning thresholds, not delivery constraints. Change them only to fit the intended viewing conditions and inspected results.

## Plan an authored explanation

Save the chosen `workflow: "anatomy-explainer"` in director state with the communication goal. Record research sources and assumptions, the authored figure ID, its meaningful assemblies and connections, and the model quantities that drive motion and readouts. A short `figures` list and `shots` entries can hold this plan; these are director notes, not additional timeline schema fields.

For each explanation shot, name the target assembly, its relation to the whole, the action, the visible result and the exact visual acceptance check. Examples: the piston visibly displaces the fluid; a valve closes before reverse flow; the derived pressure readout changes with the same state as the piston. Do not use a plausible animation as evidence of a quantitatively correct simulation. Cite the model's assumptions and units.

Keep the figure's geometry and IDs stable across shots. Set each shot's `anatomy.view.timeOffsetSeconds` and `timeScale` deliberately so the object state continues across cuts or restarts only when the explanation calls for it. Label illustrative speed changes when the viewer could otherwise mistake them for real-time behaviour. Plan overview, focused detail and causal result from the actual explanation, without a fixed shot count.

Record inspected full frames, 4× crops of relevant joints and a 390 px-wide viewing frame before approving an authored object for the final edit. Recheck the exact crop after framing it in the film: enlarging a sparse sketch does not create a detailed object. Use purposeful construction detail such as supports, bushings, seals, fasteners and surfaces only when it belongs to that object.

## Focus a real interaction

`media interactions --asset <id>` exposes recorded control/result regions when available. `media focus --asset <id> --start <source-start> --end <source-end> --scene-start <film-start> --width <canvas-width> --height <canvas-height>` returns editable `visualLayer` candidates with source and scene ranges, a fitted viewport and camera keyframes. Optional `--duration` maps a source interval to a different scene duration. Preserve enough context around the action.

Inspect `reviewSourceTimes`. Select a useful candidate, use its `visualLayer` in the returned `sceneRange`, and preserve the source aspect ratio of its viewport. Camera keyframes are scene-relative; cursor sample timestamps are full-film times, so set `--scene-start` when placing a candidate later in the film. The candidate's control/result regions guide framing; they do not establish that the outcome succeeded. Check the actual preview. Missing result metadata or legacy pointer-only events require the director to identify the outcome from frames.

When the recording was made with `--no-cursor`, a candidate can include a separately rendered cursor. Recordings with a baked pointer do not receive a second one.

## Sound and reading rhythm

Base scene timing on real narration lengths and the action being explained. Where useful, divide long captions at phrase boundaries and preserve names from the verified script. Keep spoken words attached to the relevant visual event. Music and effects should support the important beats while preserving intelligibility. Do not infer missing speech from an intentional pause or require a soundtrack for every film.
