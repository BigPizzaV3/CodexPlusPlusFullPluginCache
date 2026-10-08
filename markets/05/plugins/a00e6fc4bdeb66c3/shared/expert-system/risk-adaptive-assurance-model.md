# Risk-adaptive assurance model

Version 1.1. Provider-neutral policy for selecting the smallest reliable verification system for the risk of the current task. It does not create implementation, review, owner, deployment or publication authority.

## Assurance selection

Select assurance from failure impact, reversibility, affected data/permissions, user exposure, perceptual importance, uncertainty and evidence quality. Do not force every task through every layer.

| Mode | Typical use | Minimum pattern |
|---|---|---|
| `NORMAL` | Small, reversible, well-bounded engineering | implementation → proportionate tests/build → appropriate review |
| `MATERIAL` | A meaningful checkpoint or cross-component change | exact checkpoint → deterministic verification → targeted independent review |
| `HIGH_RISK` | Security, permissions, finance, destructive data, migrations or hard-to-reverse effects | deterministic verification → failure/abuse testing → rollback/recovery evidence → independent specialist review → required approval |
| `PERCEPTUAL_OWNER_CRITICAL` | Premium visual, brand, experience or other owner-judgement gate | technical verification → real preview/output → fresh perceptual review → owner gate where the contract requires it |

Modes may be combined when the task has multiple risk dimensions. Record the chosen mode and rationale in the existing task contract. Mark an irrelevant layer `NOT_APPLICABLE` with a reason; do not create empty ceremony. Escalate or reduce assurance when evidence changes the assessed risk.

## Builder, evaluator and report boundary

The builder may implement, run self-tests, produce evidence, report completion and disclose known risk. At a material gate the builder and the material decision owner cannot be the final evaluator of their own work. Builder self-review is useful evidence but not independent acceptance.

An implementer report is attributed evidence input, not authority. Statements such as “all tests pass”, “production-ready”, “security complete” or “visual quality passed” default to `UNVERIFIED` for the material acceptance decision until the required evidence and reviewer provenance are established. Trivial low-risk work does not require a ceremonial second reviewer when its contract justifies `NORMAL` assurance.

## Oracle-first and non-circular evidence

Prefer the closest authorized source of actual truth for the claim: real runtime, database, API response, browser behavior, filesystem, Git state, pixels/renderer, system of record, known-good authority or independently computed result. Agent-authored claims and summaries rank below directly inspected state.

For every material gate ask:

1. What real state would make this claim true or false?
2. Who controls the observation and expected truth?
3. Can the candidate or producer alter both sides of the comparison?
4. Is a simpler direct oracle available?

Do not validate producer-authored observed truth primarily against producer-authored expected truth. When the failure impact justifies it, use verifier-controlled acceptance: the verifier controls or independently observes the runtime, reads the relevant state, computes the result and issues the verdict. This is risk-based, not a universal infrastructure requirement.

## Authority checkpoint versus candidate checkpoint

Keep owner-ratified or otherwise authoritative baselines separate from the candidate under review. A candidate cannot silently change its expected truth and then use that change to prove itself. Changing the authority checkpoint requires the approval or ratification named by the governing contract. Use hashes or signatures only when the actual integrity risk justifies them.

## Outcome-first verification

Tests and reviews primarily verify the required observable outcome, failure behavior and protected invariants. Avoid brittle assertions about an internal implementation path merely because the prompt author expected it. Implementation-detail checks are justified only for explicit security boundaries, protected architecture, regulated behavior, deterministic contracts or owner-approved invariants.

## Acceptance environment and measurement identity

Use fast development runtimes for iteration. For material runtime, visual or release gates, decide whether acceptance needs an exact clean commit or approved snapshot, controlled build, fresh runtime/preview, test or capture, and shutdown. A persistent development server is not automatically acceptance authority.

Record only environment factors that can materially affect the measurement, such as runtime and dependency state, browser/renderer, viewport, DPR, resource tier, external-service state, clock/randomness, timeouts and configuration. Do not pin or inventory irrelevant details. Evidence from another material environment remains `SUPPORTED` or `UNVERIFIED` until compatibility is established.

## Real-use verification

For material user-facing behavior, prefer an actual journey through the running product when code inspection or unit tests cannot establish the outcome: navigate, interact, trigger state, inspect output, exercise failure/recovery and inspect errors. This supplements rather than replaces applicable deterministic, accessibility, security, performance and perceptual gates.

## Stable verification boundary

Keep reusable verifier logic stable when only the task, revision, target values, thresholds, source identities or evidence references change. Put those variable values in the current task or acceptance contract and bind the result to the inspected candidate. Create or revise a verifier only when the observable, verification method, risk boundary or supported environment materially changes; record the reason and regression evidence. Do not accumulate revision-named verifier copies, and do not force one verifier across genuinely incompatible oracles merely to preserve reuse.

## Verified-state rule

The default state of a required but unverified material gate is `NOT VERIFIED`, not PASS. Advance only when the task contract's required objective, runtime, specialist, perceptual and owner dimensions have the necessary evidence and authority. Failure in one required dimension cannot be overruled by success in another.
