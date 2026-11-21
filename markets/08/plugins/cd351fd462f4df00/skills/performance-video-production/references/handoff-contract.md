# Production handoff contract

## Purpose

Use `visual-treatment-contract.json` and `compositing-feasibility-gate.json` as the reversible preflight API, then use production-handoff v4 as the immutable API between creative planning and media production. This prevents provider, rendering, or audio work from silently changing the approved ad without freezing an unproven visual route too early.

## Authority

The planning Skill owns:

- offer and audience
- Sales Thesis ID, Single Sell Reason, stop reason, continue reason, and ordered viewer-question chain
- hero visual concept, must-feel and must-see outcomes, macro locks, delegated motion, exact-surface responsibilities, and acceptable unit-boundary reasons
- Visual Treatment risk, semantic carrier objects, content authority, geometry owner, motion owner, world relation, binding mode, and exactness windows
- Territory, Hook, Body, Promise, proof, and CTA
- exact rendered copy
- Beat meaning and final-delivery timing
- approved Animatic
- test semantics and destination continuity

The production Skill owns:

- how approved intent becomes assets and shots
- local, non-paid world-binding feasibility and its evidence report
- keyframes and transition controls
- current provider and model selection
- paid execution after approval
- deterministic composition, sound, and QC

## Immutable fields

Treat `immutableCreative`, `productionIntent`, approved Treatment, scene `surfaceOwnership`, and every `scene.lockedFields` entry as read-only. In a v2 handoff this includes `salesThesisId`, `singleSellReason`, `stopReason`, `continueReason`, and `salesQuestionChain`. In v3, production may improvise only fields listed in `delegatedMotion`; it must preserve `heroVisualConcept`, `mustFeel`, `mustSee`, `macroLocks`, and `exactSurfaceResponsibilities`. In v4, it must also preserve lineage and the approved content/geometry/motion ownership and binding mode. Production may shorten dead air inside a generated Raw or choose another technical route only when final Beat boundaries and meaning remain unchanged. It may change how a question is pictured, but it may not omit, reorder, replace, or detach the question's answer surface without returning a blocker.

The question chain is a comprehension contract, not a fixed editing recipe. It does not require PASONA, a specific number of cuts, or a particular motion style. The opening only needs to realize the locked reason to stop and begin the locked reason to continue; the rest of the edit must keep advancing the one sales thesis.

If the handoff requests contradictory controls, return:

```json
{
  "schemaVersion": 1,
  "status": "PRODUCTION_BLOCKED",
  "jobId": "example",
  "conflicts": [
    {
      "field": "scenes.s03.timeRange",
      "reason": "The required coherent physical event cannot fit the locked duration with the selected exact endpoint.",
      "smallestDecisionNeeded": "Approve a longer shot or a hard-cut endpoint."
    }
  ]
}
```

Do not use a blocker for ordinary provider choice, rendering, pacing within unlocked shot motion, or deterministic implementation details.

## Approval separation

Keep six independent states:

1. Creative Premise approval
2. Animatic approval
3. Visual Treatment plus composite-feasibility approval
4. production-handoff approval
5. paid request approval with request count and cost ceiling
6. distribution authority

No state implies another.

## Hashes

Record SHA-256 for the Animatic, selected Treatment, composite proof, feasibility report, and any locked identity, logo, document, or UI asset. Revalidate hashes before handoff approval, paid upload, and final render. Require `lineage.jobDirectoryId` to equal `jobId`; preserve parent and derived-job identifiers when a repair forks the job.
