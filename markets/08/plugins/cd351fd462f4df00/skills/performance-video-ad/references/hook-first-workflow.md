# Hook-first controlled production

## State machine

```text
SOURCE_LOCKED
  -> CONTEXT_RESOLVED
  -> FUNNEL_ROLE_RESOLVED
  -> CONTEXT_CLASSIFIED
  -> EXPRESSION_POLICY_RESOLVED
  -> HOOK_PORTFOLIO_READY
  -> BODY_QUESTION_CLASSIFIED
  -> BODY_FAMILY_CONSULTATION | BATCH_CONTRACT_READY
  -> AWAITING_PORTFOLIO_APPROVAL
  -> BODY_FAMILY_LOCKED
  -> ANIMATIC_READY
  -> AWAITING_ANIMATIC_APPROVAL
  -> MANIFESTS_READY
  -> AWAITING_COST_APPROVAL
  -> GENERATED_PENDING_QC
  -> LOCAL_QC_ONLY
  -> PUBLISH_APPROVED
```

No state implies a later approval. An optional direction exploration is not a state gate and does not imply `HOOK_PORTFOLIO_AND_BODY_FAMILY`, paid execution, or publication approval.

## Nine-stage workflow

1. Lock who, moment, pain, offer, promise, proof, CTA, destination, and placement from offer-specific sources.
2. Retrieve the required funnel context from canonical sources, the live destination, MyMarketer, and attributable current memory. Ask one to three questions only for remaining blocking gaps.
3. Assign the ad's stage role, message budget, curiosity handoff, metric set, and duration strategy.
4. Classify Creative Context and resolve attention and expression policy from sources.
5. Write reusable Hook hypotheses, then combine them with explicit executions and optional wrappers.
6. Classify each Hook's downstream question and Promise family. Validate stage-sized Body Contract candidates and natural Japanese.
7. If Promise families split, keep the planning job in Body consultation and map every Hook to exactly one Body. Do not call it a controlled test.
8. After human approval, create one controlled job per Body family. During an initial Hook test, change only `hook_package` and expand the cohort to at least six Hooks.
9. After single-family portfolio approval, create static frames or a low-fidelity Animatic.
10. Require human Animatic approval before shot routing or generation.
11. Compile the reviewed batch into modular shot manifests and provider inputs.
12. Ask AI models for visual assets; add exact Japanese, logos, CTA, prices, legal copy, safe zones, and timing deterministically.
13. Store generation learning in production and performance learning in MyMarketer. Never infer ad performance from visual quality or compare mixed Body families.

## Artifact responsibilities

- `test-batch.json`: one controlled learning question, fixed and test variables, minimum and target Hook counts, and one Body ID. Keep it draft while Body families are split.
- `context-resolution.json`: authoritative resolution or a maximum-three-question user-input gate for blocking offer and funnel fields.
- `funnel-role-contract.json`: one stage job, message budget, curiosity handoff, destination responsibility, metrics, and duration strategy.
- `creative-context.json`: source-backed acquisition, trust, audience, evidence, and historical-signal classification.
- `expression-policy.json`: resolved attention sources, profile, intensity, cognitive-load, trend, and spectacle boundaries.
- `creative-hypotheses.json`: reusable business hypotheses independent of rendering technique.
- `hook-packages.json`: hypothesis plus execution plus optional wrapper; never a disposable shortlist.
- `body-contract.json` or `body-family-<id>.json`: belief change, new explanation, mechanism, visible transformation, payoff, CTA deliverable, and matched Hooks.
- `body-family.json`: the single locked execution Body after consultation; an unlocked placeholder while split consultation is active.
- `hook-portfolio-approval.json`: approved Hook IDs plus Body approval.
- `beat-sheet.json`: batch modules and per-Hook substitutions.
- `animatic-review.json`: human preproduction approval; required before executable routing.
- `shot-manifest.json`: shared Body shots plus Hook-specific opening shots.
- `route-plan.json`: provider candidates for already-approved shots.
- `cost-estimate.json` and `approval.json`: paid-call gate, separate from creative approval.
- `explorations/`: optional non-gating visual-territory studies. Legacy `structure-options.json` and `structure-approval.json` may be preserved here conceptually but never gate Hook creation.

## Initial test versus later revision

`initial_hook_test` defaults to eight and requires six or more Hook Packages inside one Body family, at least three mechanisms, and no majority mechanism above 50%. A consultation cohort below six is not a performance test. Use `single_revision` or `production_pick` only when both `sourcePortfolioId` and `sourceHookPackageId` point to an approved source portfolio.

## Consultation behavior

When the user wants to discuss structure, show the full Hook portfolio, Hook-to-Body mapping, and all Body Contract drafts together. Explain the video image, mechanism, Promise family, and why the matched Body resolves the Hook. Do not require a direction winner first. Do not extend any package into a full manifest until one single-family controlled job is approved.
