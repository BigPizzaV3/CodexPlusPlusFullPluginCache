# Body Contract and Hook fit

## Body Question Gate

After Hook hypotheses exist but before a controlled batch is locked, identify the downstream question each Hook promises the Body will resolve.

Create one Body Contract only when every Hook shares the same Promise family. A valid Body Contract must define:

- `body_family_id`
- `promise_family`
- `hook_question_to_resolve`
- `belief_to_break`
- `new_belief`
- `mechanism`
- `visible_transformation.before` and `.after`
- `concrete_payoff`
- `cta_deliverable`
- `max_concepts_per_beat`
- `matched_hook_ids`

When `hookBodyReuseVersion: 1` is active, also lock `hook_entry_contract` before producing the baseline. This is the semantic socket every later Hook must fit:

- `signature`: stable ID for this exact Body entry;
- `required_viewer_state`: the state the Hook or its handoff must create;
- `required_open_question`: the unresolved question carried into the Body;
- `expected_body_answer`: what the first common Body beat answers;
- `allowed_variation`: fields that may change without rebuilding the Body;
- `new_body_triggers`: changes that require a new Body family or a new Creative.

Each Hook records the same values under `bodyEntryCompatibility` and sets `decision: PASS`. Exact opening copy, work incident, UI surface, first sound, and framing may vary only when the Hook-specific handoff still lands on the locked entry. A Hook that changes the Promise, unresolved question, expected answer, proof level, CTA, or desired relief is not a reusable Hook variant.

The contract preserves the complete belief change, product mechanism, visible before/after, payoff, and CTA deliverable. The rendered Body is stage-aware rather than automatically showing all of them.

When `funnelRoleBodyVersion: 1` is active, set `stage_role_mode` from the Funnel Role Contract:

- `qualified_curiosity`: render tension, reframe, one product/intervention statement, and CTA; leave the full mechanism and payoff to the destination;
- `full_explainer`: render the reframe, mechanism, visible transformation, payoff, and CTA;
- `proof_explainer`: render only the proof sequence justified by the stage and evidence.

For a cold click-through ad leading to a full-persuasion LP, require `qualified_curiosity`. Do not attach a diagnostic demo merely because the canonical contract contains diagnostic details. In every mode, reject a sequence of service labels or noun lists.

## Split behavior

If Hooks promise different downstream answers:

1. Mark the planning portfolio `consultation_cohorts`.
2. Keep `test-batch.json` in `DRAFT`; do not call the portfolio a controlled Hook test.
3. Draft one Body Contract per Promise family and show all Hook-to-Body mappings.
4. Permit a shared CTA and End Card when the offer is identical.
5. After human approval, create a separate job for each Body family.
6. Inside each execution job, hold the Body, duration, Promise, proof, CTA, destination, and placement fixed.
7. Expand each `initial_hook_test` cohort to at least six Hooks and target eight before performance comparison.
8. Compare Hook results only within the same Body family. Never label one Body family the winner from a mixed test.

## Baseline reuse rule

Treat the approved baseline as `Hook Package -> locked Body entry -> common Body`, not as an indivisible finished ad.

- `hook_execution_test`: keep the incident angle and `hook_entry_contract.signature` fixed. Change presentation only.
- `angle_discovery`: the work incident may change, but reuse the Body only if the Hook-specific handoff produces the exact locked viewer state, open question, and expected Body answer.
- `new creative`: use when any `new_body_triggers` field changes. Do not force it into the existing Body to save production work.

Run the fit gate before Animatic work. `NEW_BODY_REQUIRED` is a routing decision, not a failed creative: remove it from the current controlled job, draft its own Body family, and do not compare it directly with the fixed-Body Hooks.

Run:

```bash
node scripts/validate-body-contract.mjs <body-contract.json>
node scripts/validate-hook-body-fit.mjs <hook-packages.json> <body-contract.json> [more...]
```
