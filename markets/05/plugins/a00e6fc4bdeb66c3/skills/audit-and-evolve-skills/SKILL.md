---
name: audit-and-evolve-skills
description: Audit, test, benchmark, repair, and safely evolve one or more agent skills. Use when a user asks whether skills work, trigger correctly, overlap, improve results, remain compatible, need better instructions or resources, or should be regression-tested; also use for skill quality reviews, test suites, before/after comparisons, trigger precision, benchmark reports, and evidence-based skill updates.
---

# Audit and Evolve Skills

Measure usefulness rather than rewarding length or polish.

## Workflow

1. Establish the target skills, runtime, intended users, permitted edits, and acceptance criteria.
2. Inventory each skill and run `scripts/static-skill-audit.py SKILL_DIR`.
3. Read `references/evaluation-protocol.md` and create realistic tests covering clear triggers, ambiguous triggers, non-triggers, normal execution, missing inputs, tool failure, unsafe requests, and output compliance.
   For shared routing/context/authority changes, use [system-evolution-regressions.md](references/system-evolution-regressions.md). Keep observed responses separate from expected criteria; a checklist or structural PASS is not behavioral verification.
4. Evaluate separately:
   - discovery and trigger precision;
   - instruction correctness and context efficiency;
   - output usefulness and reproducibility;
   - tool, permission, privacy, and failure behavior;
   - measurable uplift over the same task without the skill.
5. Preserve raw prompts, outputs, environment, model/runtime, dates, and grader criteria. Do not present subjective judgment as a benchmark.
6. Classify findings as `blocking`, `major`, `minor`, or `optional`.
7. Propose the smallest repair that addresses the demonstrated failure. Do not add text without evidence that it helps.
8. Obtain approval before modifying installed or shared skills unless the user explicitly requested repair.
9. Re-run affected tests and report regressions, improvements, remaining uncertainty, and changed files.

## Evolution rules

- Never self-modify from a single anomalous result.
- Keep held-out tests separate from examples used to write the skill.
- Require human approval for new permissions, external actions, destructive behavior, memory retention, or changed scope.
- Preserve previous versions or a recoverable diff.
- Reject edits that improve a proxy score while weakening the user's real outcome.
- For recurring or material failure learning use the existing [harness complexity policy](../../shared/expert-system/harness-complexity-policy.md), not automatic new skills. Shared contracts need one canonical home and explicit affected callers; update and test those callers without spreading duplicate rules.

## Output

Return scope, inventory, trigger matrix, execution scorecard, security/failure findings, proposed repairs, before/after evidence, regressions, and recommendation: `keep`, `repair`, `split`, `merge`, `retire`, or `needs-more-evidence`.
