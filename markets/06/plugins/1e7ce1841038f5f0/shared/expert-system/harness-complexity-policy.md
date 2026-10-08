# Harness complexity policy

Version 1.0. Provider-neutral policy for keeping a coding-agent harness no larger than the assurance problem it must solve.

## Finite purpose

Every harness or material harness change must name:

- the assurance objective and bounded scope;
- the concrete failure modes it prevents or detects;
- the direct oracle or simpler control considered;
- the evidence that will show the control works;
- the owner and maintenance burden;
- the closure condition.

When the stated objective is met, freeze or stabilize the harness and return effort to the product. A newly evidenced failure may reopen the design; the theoretical possibility of another failure does not justify unlimited new layers.

## Complexity budget

Before adding a manifest, claim model, provenance layer, validator, hook, agent, contract, state model, evidence layer or registry, answer:

1. Which concrete failure mode does it address?
2. Why do existing controls or a direct real-system oracle not cover it?
3. Is there a simpler equivalent solution?
4. What new failure, maintenance and context cost does it introduce?
5. How will its value and removal condition be tested?

Reject or demote a component whose assurance benefit is not greater than its complexity and maintenance cost.

## Overengineering stop

Record `HARNESS_OVERENGINEERING_RISK` when one or more are evidenced:

- the harness creates material new failures;
- the same truth is modelled in multiple authoritative places;
- producer and verifier evidence are circular;
- new layers primarily validate other harness layers rather than product truth;
- the test/control system is harder to trust than the product observable;
- harness work blocks product work beyond the justified risk;
- maintenance cost exceeds the assurance gain.

Do not respond by automatically adding another layer. Route by evidence to `SIMPLIFY`, `DELETE`, `DEMOTE_TO_NON_AUTHORITATIVE`, `MERGE` or `USE_DIRECT_ORACLE`. Preserve required security, authority, rollback and evidence controls while simplifying.

## Ablation and load-bearing review

For a complex or long-lived harness, periodically test which components are load-bearing. Identify redundant, historical, circular or proxy-only controls and compare them with a direct runtime, E2E or system-of-record check. Remove or merge only with authority, rollback and evidence that required coverage remains.

Success is the smallest reliable harness for the current task and project, not the most sophisticated harness.

## Failure learning without rule accumulation

For a recurring or material observed failure, retain a small case in the existing audit/change record: actual failure, source/evidence, impact, recurrence, suspected cause versus verified cause, smallest proposed control, regression case, owner, cost and removal condition. Diagnose whether authority, context selection, acceptance, test/linter, permission/hook, skill, tool, provider choice or task contract is the actual missing control. Prefer the existing canonical home or a direct deterministic check. Do not add a hook or skill when a corrected source or task is sufficient.

An isolated low-impact anomaly warrants a local correction, not durable self-modification. A single material failure may justify a proposed repair, but durable mutation still needs the authorized change workflow and review. Version Added/Changed/Removed/Superseded, Reason, Tests and Known Limitations; preserve rollback and re-run affected dependencies. No automatic memory write, agent dispatch, new permission or installation follows from learning.
