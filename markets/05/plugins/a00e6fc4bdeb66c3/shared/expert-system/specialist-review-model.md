# Specialist review model

Critical artifacts require review by a role independent of their implementation. Independence means the reviewer did not own the implementation or the material decision being accepted. Prefer fresh bounded context for a material review, but never equate a new session with independence.

For each gate record:

- artifact or observable under review;
- implementer and decision owner;
- reviewer role and independence rationale;
- source target, requirements, and acceptance method;
- objective evidence and perceptual evidence where applicable;
- result: `PASS`, `PASS WITH RISKS`, `FAIL`, or `NOT VERIFIABLE`;
- defects, owner, rework, and re-review condition.

Also record reviewer capability class when it is relevant and evidenced, implementation participation, direct evidence inspection, fallback/reduced-capability status and required ratification. A fallback reviewer may provide bounded findings but cannot inherit the authority of a required full-capability reviewer by label alone. A fresh session is not proof of independence.

The reviewer should re-identify the exact candidate, inspect the evidence directly and exercise the real system when the outcome cannot be established from artifacts alone. Give the reviewer criteria and necessary sources without the builder's desired verdict.

If adversarial or destructive review actions could mutate the candidate, use a bounded isolated copy such as a temporary worktree, isolated clone or disposable test environment when the project's risk and tooling justify it. Bind the review to the exact candidate revision, dispose of the isolated state safely, and never make Docker or worktrees universal requirements.

Self-review may precede independent review but cannot replace it for critical security, architecture, release, or premium visual gates. A reviewer may reject a compliant result when the real outcome is defective. Correct compliance with a defective specification is not success.
